# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re, json
from bs4 import BeautifulSoup

def parse_np_data(regex_input, raw_data):
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
        req_get = req.get('https://register.com.np/whois-lookup', headers=headers, verify=False)
    except:
        pass
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        token_value = parse_np_data('<input type="hidden" name="_token" value="(.*?)">', raw_data)
        if token_value:
            result = {
                '_token': (None, token_value),
            }
    return result

def whois_via_web(USER_AGENT, domain, domain_type):
    headers = {
        'User-Agent': USER_AGENT
    }

    if domain and domain_type:
        domain_type = '.{0}'.format(domain_type)
        domain = domain.replace(domain_type, '')
    
    final_result = {
        'status': False,
        'result': False
    }
    
    req = requests.Session()
    post_data = get_hidden_value(req, headers)
    if post_data:
        post_data.update({
            'domainName': (None, domain),
            'domainExtension': (None, domain_type)
        })
    else:
        return final_result
    
    req_cookie = req.cookies.get_dict()
    headers.update({
        'Referer': 'https://register.com.np/whois-lookup',
        'Origin': 'https://register.com.np'
    })

    req_post = False
    try:
        req_post = requests.post('https://register.com.np/checkdomain_whois', files=post_data, headers=headers, cookies=req_cookie, verify=False)
    except:
        pass
    
    result = []
    if req_post and req_post.status_code == 200 and req_post.text:
        raw_data = req_post.text
        if raw_data:
            creation_date_details = parse_np_data('First registered date:(.*?)Last updated date:', raw_data)
            updated_date_details = parse_np_data('Last updated date:(.*?)Primary name server:', raw_data)
            ns1_details = parse_np_data('Primary name server:(.*?)Secondary name server:', raw_data)
            ns2_details = parse_np_data('Secondary name server:(.*?)Registrant Email:', raw_data)
            
            if creation_date_details:
                result.append('Creation Date: {0}'.format(creation_date_details))
            if updated_date_details:
                result.append('Updated Date: {0}'.format(updated_date_details))
            if ns1_details:
                result.append('Name Server: {0}'.format(ns1_details))
            if ns2_details:
                result.append('Name Server: {0}'.format(ns2_details))
    if result:
        result.append('Full WHOIS: https://register.com.np')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result