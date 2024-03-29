# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re, json
from bs4 import BeautifulSoup

def whois_via_web(USER_AGENT, domain, domain_type):
    domain = domain.replace('.lk', '')
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
        req_get = req.get('https://www.domains.lk/wp-content/themes/bridge-child/getDomainData.php?domainname={0}'.format(domain),
                          headers=headers,
                          verify=False)
    except:
        pass
    
    result = []
    raw_data = ''
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        json_data = json.loads(raw_data or '{}')
        
        if json_data.get('Message', False):
            result.append('Message: {0}'.format(json_data.get('Message')))
        if json_data.get('ExpireDate', False):
            expiry_date = json_data.get('ExpireDate')
            if expiry_date:
                expiry_date = expiry_date.replace('Expiration Date -', '')
                expiry_date = expiry_date.strip()
                result.append('Registry Expiry Date: {0}'.format(expiry_date))
            
    if result:
        result.append('Full WHOIS: https://www.domains.lk')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result