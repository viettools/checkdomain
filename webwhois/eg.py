# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re, json
from bs4 import BeautifulSoup

def whois_via_web(USER_AGENT, domain, domain_type):
    headers = {
        'User-Agent': USER_AGENT,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest'
    }
    
    if domain and domain_type:
        domain = domain.replace('.' + domain_type, '')
    
    payload = {
        'action': 'whois_query',
        'domain': domain,
        'tld': domain_type,
        'recaptcha': ''
    }    
    
    final_result = {
        'status': False,
        'result': False
    }
    
    req = requests.Session()
    req_post = False
    try:
        req_post = req.post('https://domain.eg/wp-admin/admin-ajax.php', headers=headers, data=payload, verify=False)
    except:
        pass
    
    result = []
    if req_post and req_post.status_code == 200 and req_post.json():
        json_data = req_post.json()
        if json_data:
            if json_data.get('status', False):
                status = ''
                if json_data.get('status') == 'registered':
                    status = 'Already registered!'
                elif json_data.get('status') == 'available_probably':
                    status = 'This domain is probably available'
                
                result.append('Domain Status: {0}'.format(status))
            
    if result:
        result.append('Full WHOIS: https://domain.eg')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result