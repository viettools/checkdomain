# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re, json
from bs4 import BeautifulSoup

def parse_dj_data(regex_input, raw_data):
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
        req_get = req.get('http://www.dj/cgi-bin/quiest.cgi?dn={0}'.format(domain), headers=headers, verify=False)
    except:
        pass
    
    result = []
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        if raw_data:
            expiry_date = parse_dj_data('Expiration date:(.*?)</TD>', raw_data)
            if expiry_date:
                result.append('Registry Expiry Date: {0}'.format(expiry_date))
            
    if result:
        result.append('Full WHOIS: http://www.dj')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result