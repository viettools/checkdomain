# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re, json
from bs4 import BeautifulSoup

def parse_dz_data(regex_input, raw_data):
    result = False
    if raw_data:
        regex_data = re.findall(regex_input, raw_data, re.DOTALL|re.M)
        if regex_data:
            pre_clean_data = regex_data[0]
            #
            pre_clean_data = pre_clean_data.replace('</span>\n', '\t')
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
    
    final_result = {
        'status': False,
        'result': False
    }
    
    req = requests.Session()
    req_get = False
    try:
        req_get = req.get('http://www.nic.dz/index.php?domain_name={0}&Submit=Rechercher&option=com_whois'.format(domain), headers=headers, verify=False)
    except:
        pass
    
    result = []
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        if raw_data:
            raw_data = raw_data.replace('\r', '')
            raw_data = raw_data.replace('\n', '')
            arr_multi_data = re.findall('<table cellspacing="0" cellpadding="0" width="55%">(.*?)</tbody></table>', raw_data, re.DOTALL|re.M)
            for arr in arr_multi_data:
                registrant_address = parse_dz_data('Description :(.*?)Contact Administratif :', arr)
                admin_address = parse_dz_data('Contact Administratif :(.*?)Contact Technique :', arr)
                tech_address = parse_dz_data('Contact Technique :(.*?)Registrar :', arr)
                registrar = parse_dz_data('Registrar :(.*?)</td>', arr)
                creation_date = parse_dz_data('<strong>Date de cr&eacute;ation  : </strong>(.*?)</td>', arr)
                
                if registrant_address:
                    result.append('Registrant Address:\n\t{0}'.format(registrant_address))
                if admin_address:
                    result.append('Admin Address:\n\t{0}'.format(admin_address))
                if tech_address:
                    result.append('Tech Address:\n\t{0}'.format(tech_address))
                if registrar:
                    result.append('Registrar: {0}'.format(registrar))
                if creation_date:
                    result.append('Creation Date: {0}'.format(creation_date))
            
    if result:
        result.append('Full WHOIS: http://www.nic.dz')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result