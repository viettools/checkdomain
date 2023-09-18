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
        req_get = req.get('https://account.alpha.net.bd/bd_domain_check.php?mode=whois&domain={0}'.format(domain, domain_type), headers=headers, verify=False)
    except:
        pass
    
    result = []
    if req_get and req_get.status_code == 200 and req_get.text:
        json_data = req_get.json()
        if json_data:
            if json_data.get('message', False):
                result.append(json_data.get('message'))
            if json_data.get('domain', False):
                result.append('Domain Name: {0}'.format(json_data.get('domain')))
            if  json_data.get('status', False):
                result.append('Domain Status: {0}'.format(json_data.get('status')))
            if json_data.get('ns1', False):
                result.append('Name Server: {0}'.format(json_data.get('ns1')))
            if json_data.get('ns2', False):
                result.append('Name Server: {0}'.format(json_data.get('ns2')))
            
    if result:
        result.append('Full WHOIS: https://bdia.btcl.com.bd/')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result