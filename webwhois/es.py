# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re
from bs4 import BeautifulSoup

def parse_es_data(regex_input, raw_data):
    result = False
    if raw_data:
        regex_data = re.findall(regex_input, raw_data, re.DOTALL|re.M)
        if regex_data:
            pre_clean_data = regex_data[0]
            arr_rep = ['<br />', '<br/>', '<br>']
            for rep in arr_rep:
                pre_clean_data = pre_clean_data.replace(rep, '\n')
            clean_data = BeautifulSoup(pre_clean_data, features='html.parser').get_text()
            if clean_data:
                clean_data = re.sub(r'\s+', '', clean_data)
                result = clean_data
                del clean_data
    return result

def whois_via_web(USER_AGENT, domain, domain_type):
    headers = {
        'User-Agent': USER_AGENT
    }
    # if domain and domain_type:
    #     domain = domain.replace('.{0}'.format(domain_type), '')
    
    final_result = {
        'status': False,
        'result': False
    }
    
    req = requests.Session()
    req_get = False
    try:
        req_get = req.get('https://www.loading.es/whois/info/{0}'.format(domain), headers=headers, verify=False)
    except:
        pass
    
    result = []
    raw_data = ''
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        if raw_data:
            
            creation = parse_es_data('Creation Date:(.*?)Expiration Date', raw_data)
            if creation:
                result.append('Creation Date: {0}'.format(creation))
                
            expiry = parse_es_data('Expiration Date:(.*?)<br />', raw_data)
            if expiry:
                result.append('Registry Expiry Date: {0}'.format(expiry))
            
            ns_server = parse_es_data('Name Server\s+\d:(.*?)<br', raw_data)
            if ns_server:
                arr_ns_server = ns_server.split('\n')
                for item_ns in arr_ns_server:
                    item_ns = item_ns.strip()
                    if item_ns:
                        result.append('Name Server: {0}'.format(item_ns))
            
    if result:
        result.append('\n*** ---> Data Could Be Inaccurate!!!\nFull WHOIS: https://www.dominios.es/en')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result