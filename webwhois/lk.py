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
        req_get = req.get('https://register.domains.lk/proxy/domains/single-search?keyword={0}'.format(domain),
                          headers=headers,
                          verify=False)
    except:
        pass
    
    result = []
    raw_data = ''
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        json_data = json.loads(raw_data or '{}')
        
        json_msg = json_data.get('Message', '')
        if raw_data.find('Domain name you searched is restricted') > -1:
            result.append('Domain Status: Reserved Domain https://icann.org/epp')
        if json_data.get('result', {}):
            domainAvailability = json_data['result'].get('domainAvailability', {})
            if domainAvailability.get('message', False):
                result.append('Message: {0}'.format(domainAvailability['message']))

            if 'isAvailable' in domainAvailability and not domainAvailability['isAvailable']:
                domainInfo = domainAvailability.get('domainInfo', {})
                if domainInfo is not None and domainInfo.get('expireDate', False):
                    result.append('Registry Expiry Date: {0}'.format(domainInfo['expireDate']))
            
    if result:
        result.append('Full WHOIS: https://www.domains.lk')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result