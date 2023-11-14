# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re, json
from bs4 import BeautifulSoup

def replace_ph_data(raw_data):
    create_date = ''
    re_create_date = re.search('createDate = moment\(\'(.*?)\'\)\.format', raw_data, re.DOTALL|re.M)
    if re_create_date:
        create_date = re_create_date.group(1)
    
    expiry_date = ''
    re_expiry_date = re.search('expiryDate = moment\(\'(.*?)\'\)\.format', raw_data, re.DOTALL|re.M)
    if re_expiry_date:
        expiry_date = re_expiry_date.group(1)
    
    update_date = ''
    re_update_date = re.search('updateDate = moment\(\'(.*?)\'\)\.format', raw_data, re.DOTALL|re.M)
    if re_update_date:
        update_date = re_update_date.group(1)
        
    return create_date, update_date, expiry_date

def parse_ph_data(regex_input, raw_data):
    result = False
    if raw_data:
        regex_data = re.findall(regex_input, raw_data, re.DOTALL|re.M)
        if regex_data:
            pre_clean_data = regex_data[0]
            create_date, update_date, expiry_date = replace_ph_data(raw_data)
            if create_date:
                pre_clean_data = pre_clean_data.replace('<span id="create-date"></span>', create_date)
            if update_date:
                pre_clean_data = pre_clean_data.replace('<span id="update-date"></span>', update_date)
            if expiry_date:
                pre_clean_data = pre_clean_data.replace('<span id="expiry-date"></span>', expiry_date)
            clean_data = BeautifulSoup(pre_clean_data, features='html.parser').get_text()
            if clean_data:
                result = clean_data.strip()
                del clean_data
    
    if result:
        result = re.sub(r'\n(?=\n)', '', result)
        result = re.sub('\s{2,}', ' ', result)
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
    req_get = False
    try:
        req_get = req.get('https://whois.dot.ph/?utf8=%E2%9C%93&search={0}&button='.format(domain), headers=headers, verify=False)
    except:
        pass
    
    result = []
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        if raw_data:
            whois_details = parse_ph_data('<pre>(.*?)</pre>', raw_data)
            
            if whois_details:
                result.append(whois_details)
            
    if result:
        result.append('Full WHOIS: https://www.dot.ph')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result