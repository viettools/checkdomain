# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re, json
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
        req_get = req.get('https://whois.inet.vn', headers=headers)
    except:
        pass
    
    req_cookie = req.cookies.get_dict()
    
    headers.update({
        'X-Requested-With': 'XMLHttpRequest',
        'X-Whois-Token': req_cookie.get('wtok', False),
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin'
    })
    try:
        req_get = req.get('https://whois.inet.vn/api/whois/domainspecify/{0}'.format(domain), headers=headers, cookies=req_cookie)
    except:
        pass
    
    result = []
    if req_get and req_get.status_code == 200 and req_get.text:
        json_data = req_get.json()
        
        if json_data.get('registrantName', False):
            result.append('Registrant Name: {0}'.format(json_data.get('registrantName')))
        if json_data.get('registrar', False):
            result.append('Registrar: {0}'.format(json_data.get('registrar')))
        if json_data.get('creationDate', False):
            result.append('Creation Date: {0}'.format(json_data.get('creationDate')))
        if json_data.get('expirationDate', False):
            result.append('Registry Expiry Date: {0}'.format(json_data.get('expirationDate')))
        
        for item in json_data.get('nameServer', []):
            result.append('Name Server: {0}'.format(item))
        for item in json_data.get('status', []):
            result.append('Domain Status: {0} https://icann.org/epp'.format(item))
            
    # Check "Reserved Domain"
    if not result:
        req_post = False
        try:
            req_post = req.post('https://whois.inet.vn/api/domain/checkavailable', json={'name': domain}, headers=headers, verify=False)
        except:
            pass
        
        if req_post and req_post.status_code == 200 and req_post.text:
            json_check_data = req_post.json()
            data_message = json_check_data.get('message', '')
            if data_message.find('Domain is reserved') > -1:
                result.append('Domain Status: Reserved Domain https://icann.org/epp')
            
    if result:
        result.append('Full WHOIS: https://tracuutenmien.gov.vn/ or https://vnnic.vn/en/whois-information?lang=en')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result