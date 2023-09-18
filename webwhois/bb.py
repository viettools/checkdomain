# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re
from bs4 import BeautifulSoup

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
        req_get = req.get('https://whois.telecoms.gov.bb/status/{0}'.format(domain, domain_type), headers=headers, verify=False)
    except:
        pass
    
    result = []
    raw_data = ''
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        if raw_data:
            filter_raw_data = re.findall('<pre>(.*?)</pre>', raw_data, re.DOTALL|re.M)
            if filter_raw_data:
                result.extend(filter_raw_data)
            
    if result:
        result.append('Full WHOIS: https://whois.telecoms.gov.bb/search/')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result