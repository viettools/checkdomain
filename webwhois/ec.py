# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re
from bs4 import BeautifulSoup

def parse_ec_data(regex_input, raw_data):
    result = False
    if raw_data:
        regex_data = re.findall(regex_input, raw_data, re.DOTALL|re.M)
        if regex_data:
            pre_clean_data = regex_data[0]
            pre_clean_data = pre_clean_data.replace('<br>\t\t', '\n')
            clean_data = BeautifulSoup(pre_clean_data, features='html.parser').get_text()
            if clean_data:
                result = clean_data.strip()
                del clean_data
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
    req_post = False
    
    try:
        req_get = req.get('https://nic.ec/who-is.php', headers=headers, verify=False)
    except:
        pass
    
    token = ''
    if req_get and req_get.status_code == 200 and req_get.text:
        token = parse_ec_data('<input type="hidden" name="token" value="(.*?)"', req_get.text)
    
    req_cookie = req.cookies.get_dict()
    payload = {
        'domain': domain,
        'token': token
    }
    
    headers.update({
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://nic.ec/who-is.php'
    })
    
    try:
        req_post = requests.post('https://nic.ec/busqueda.php', data=payload, headers=headers, cookies=req_cookie, verify=False)
    except:
        pass
    
    result = []
    if req_post and req_post.status_code == 200 and req_post.text:
        json_data = req_post.json()
        if json_data:
            whois_data = json_data.get('whois', '')
            if whois_data:
                whois_data = whois_data.replace('<br />', '')
                result.append(whois_data)
    
    if result:
        result.append('Full WHOIS: https://nic.ec')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result