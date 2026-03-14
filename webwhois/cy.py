# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re
from bs4 import BeautifulSoup

def get_cy_id(req, headers, domain, domain_type):
    query_domain = ''
    if domain and domain_type:
        query_domain = domain.replace('.{0}'.format(domain_type), '')
    payload = {
        'domainEndingName': domain_type,
        'domainName': query_domain
    }
    
    result = {
    }
    req_post = False
    try:
        req_post = req.post('https://registry.nic.cy/api/domains/_search', json=payload, headers=headers, verify=False)
    except:
        pass
    
    if req_post and req_post.status_code == 200 and req_post.json():
        arr_json_data = req_post.json()
        if arr_json_data:
            json_data = arr_json_data[0]
            if json_data.get('id', False):
                result.update({
                    'domain_id': json_data.get('id')
                })
            if json_data.get('status', False):
                domain_status = json_data.get('status')
                result.update({
                    'domain_status': domain_status
                })
    return result

def whois_via_web(USER_AGENT, domain, domain_type):    
    return {'status': True, 'result': 'Full WHOIS: https://www.nic.cy'}