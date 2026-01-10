# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re, json
from bs4 import BeautifulSoup

def parse_gm_data(regex_input, raw_data):
    result = False
    if raw_data:
        regex_data = re.findall(regex_input, raw_data, re.DOTALL|re.M)
        if regex_data:
            pre_clean_data = regex_data[0]
            clean_data = BeautifulSoup(pre_clean_data, features='html.parser').get_text()
            if clean_data:
                result = clean_data.strip()
                del clean_data
    
    if result:
        result = re.sub(r'\n(?=\n)', '', result)
        result = re.sub('\s{2,}', ' ', result)
    return result

def whois_via_web(USER_AGENT, domain, domain_type):
    headers = {
        'User-Agent': USER_AGENT
    }
    
    if domain and domain_type:
        domain_type = '.{0}'.format(domain_type)
        domain = domain.replace(domain_type, '')
    
    final_result = {
        'status': False,
        'result': False
    }
    
    req = requests.Session()
    req_get = False
    try:
        req_get = req.get('https://www.nic.gm/NIC2/REG/Login.aspx?whois={0}'.format(domain), headers=headers, verify=False)
    except:
        pass
    
    result = []
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        if raw_data:
            spl_data = raw_data.split(';')
            if len(spl_data) == 13:
                result.append('Registrar: {0}'.format(spl_data[2]))
                result.append('Registrant Contact: {0}'.format(spl_data[1]))
                
                admin_contact = ''
                if spl_data[3]:
                    admin_contact = spl_data[3]
                if spl_data[4]:
                    if not admin_contact:
                        admin_contact = spl_data[4]
                    else:
                        admin_contact += ' ({0})'.format(spl_data[4])
                result.append('Admin Contact: {0}'.format(admin_contact))
                
                tech_contact = ''
                if spl_data[5]:
                    tech_contact = spl_data[5]
                if spl_data[6]:
                    if not tech_contact:
                        tech_contact = spl_data[6]
                    else:
                        tech_contact += ' ({0})'.format(spl_data[6])
                result.append('Tech Contact: {0}'.format(tech_contact))
                
                result.append('Creation Date: {0}'.format(spl_data[11]))
                
                # NS Server
                for i in range(7, 11):
                    if spl_data[i]:
                        result.append('Name Server: {0}'.format(spl_data[i]))
            
    if result:
        result.append('Full WHOIS: https://www.nic.gm/NIC2/search.html')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result