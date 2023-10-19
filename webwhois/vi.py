# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re, json
from bs4 import BeautifulSoup

def parse_vi_data(regex_input, raw_data):
    result = False
    if raw_data:
        regex_data = re.findall(regex_input, raw_data, re.DOTALL|re.M)
        if regex_data:
            pre_clean_data = regex_data[0]
            clean_data = BeautifulSoup(pre_clean_data, features='html.parser').get_text()
            if clean_data:
                result = clean_data.strip()
                del clean_data
    return result

def get_hidden_value(req, headers):
    result = {}
    req_get = False
    try:
        req_get = req.get('https://whmcs.nic.vi/index.php?m=whois', headers=headers, verify=False)
    except:
        pass
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        token_value = re.search('<input type="hidden" name="token" value="(.*?)" />', raw_data, re.DOTALL|re.M)
        if token_value:
            result = {
                'token': token_value.group(1),
            }
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
    post_data = get_hidden_value(req, headers)
    if post_data:
        post_data.update({
            'domainName': domain,
        })
    else:
        return final_result
    
    req_cookie = req.cookies.get_dict()
    headers.update({
        'Referer': 'https://whmcs.nic.vi/index.php?m=whois',
        'Origin': 'https://whmcs.nic.vi'
    })

    req_post = False
    try:
        req_post = requests.post('https://whmcs.nic.vi/index.php?m=whois', data=post_data, headers=headers, cookies=req_cookie, verify=False)
    except:
        pass
    
    result = []
    if req_post and req_post.status_code == 200 and req_post.text:
        raw_data = req_post.text
        if raw_data:
            whois_details = parse_vi_data('<div class="panel-body">(.*?)</section>', raw_data)
            if whois_details:
                result.append(whois_details)
            
    if result:
        result.append('Full WHOIS: https://whmcs.nic.vi')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result