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
        req_get = req.get('https://api.nic.dz/v1/domains/{0}'.format(domain), headers=headers, verify=False)
    except:
        pass
    
    result = []
    if req_get and req_get.status_code >= 200 and req_get.status_code < 400 and req_get.json():
        raw_data = req_get.json()
        if raw_data:
            result.append('Registrant Organization: {0}'.format(raw_data.get('orgName', '')))
            result.append('Registrant Address: {0}'.format(raw_data.get('addressOrg', '')))

            result.append('Admin Organization: {0}'.format(raw_data.get('orgNameAdm', '')))
            result.append('Admin Address: {0}'.format(raw_data.get('addressAdm', '')))
            result.append('Admin Email: {0}'.format(raw_data.get('emailAdm', '')))
            result.append('Admin Phone: {0}'.format(raw_data.get('phoneAdm', '')))
            result.append('Admin Fax: {0}'.format(raw_data.get('faxAdm', '')))

            result.append('Tech Organization: {0}'.format(raw_data.get('orgNameTech', '')))
            result.append('Tech Address: {0}'.format(raw_data.get('addressTech', '')))
            result.append('Tech Email: {0}'.format(raw_data.get('emailTech', '')))
            result.append('Tech Phone: {0}'.format(raw_data.get('phoneTech', '')))
            result.append('Tech Fax: {0}'.format(raw_data.get('faxTech', '')))
            
            result.append('Registrar: {0}'.format(raw_data.get('registrar', '')))
            result.append('Creation Date: {0}'.format(raw_data.get('creationDate', '')))
    
    if result:
        result.append('Full WHOIS: https://www.nic.dz')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result