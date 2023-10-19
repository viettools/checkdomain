# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re, json
from bs4 import BeautifulSoup

def parse_tt_data(regex_input, raw_data):
    result = False
    if raw_data:
        regex_data = re.findall(regex_input, raw_data, re.DOTALL|re.M)
        if regex_data:
            pre_clean_data = regex_data[0]
            pre_clean_data = pre_clean_data.replace('\xa0', '')
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
    post_data = {
        'name': (None, domain), 
        'Search': (None, 'Search')
    }
    
    req_cookie = req.cookies.get_dict()
    headers.update({
        'Referer': 'https://www.nic.tt/cgi-bin/search.pl',
        'Origin': 'https://www.nic.tt'
    })

    req_post = False
    try:
        req_post = requests.post('https://nic.tt/cgi-bin/search.pl', files=post_data, headers=headers, cookies=req_cookie, verify=False)
    except:
        pass
    
    result = []
    if req_post and req_post.status_code == 200 and req_post.text:
        raw_data = req_post.text
        if raw_data:
            creation_date_details = parse_tt_data('Registration Date(.*?)Expiration Date', raw_data)
            expiration_date_details = parse_tt_data('Expiration Date(.*?)Administrative Contact', raw_data)
            ns_details = parse_tt_data('DNS Hostnames(.*?)DNS IP Addresses', raw_data)
            
            if creation_date_details:
                result.append('Creation Date: {0}'.format(creation_date_details))
            if expiration_date_details:
                result.append('Registry Expiry Date: {0}'.format(expiration_date_details))
            if ns_details:
                spl_ns = ns_details.split(',')
                for ns in spl_ns:
                    result.append('Name Server: {0}'.format(ns.strip()))
    if result:
        result.append('Full WHOIS: https://nic.tt/cgi-bin/search.pl')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result