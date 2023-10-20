# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re, json
from bs4 import BeautifulSoup

def parse_pa_data(regex_input, raw_data):
    result = False
    if raw_data:
        regex_data = re.findall(regex_input, raw_data, re.DOTALL|re.M)
        if regex_data:
            pre_clean_data = regex_data[0]
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
        req_get = req.get('http://www.nic.pa/en/whois/dominio/{0}'.format(domain), headers=headers, verify=False)
    except:
        pass
    
    result = []
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        if raw_data:
            billing_details = parse_pa_data('Financial Contact:(.*?)</li>', raw_data)
            admin_details = parse_pa_data('Administrative Contact:(.*?)</li>', raw_data)
            technical_details = parse_pa_data('Technical Contact:(.*?)</li>', raw_data)
            creation_details = parse_pa_data('Creation Date:(.*?)</li>', raw_data)
            updated_date_details = parse_pa_data('Last Update Date:(.*?)</li>', raw_data)
            renewal_date_details = parse_pa_data('Renewal Date:(.*?)</li>', raw_data)
            
            if billing_details:
                result.append('Financial Contact: {0}'.format(billing_details))
            if admin_details:
                result.append('Admin Name: {0}'.format(admin_details))
            if technical_details:
                result.append('Tech Name: {0}'.format(technical_details))
            if creation_details:
                result.append('Creation Date: {0}'.format(creation_details))
            if updated_date_details:
                result.append('Updated Date: {0}'.format(updated_date_details))
            if renewal_date_details:
                result.append('Renewal Date: {0}'.format(renewal_date_details))
            
            ns_details = re.findall('DNS Hostname:(.*?)</li>', raw_data, re.DOTALL|re.M)
            for ns_server in ns_details:
                result.append('Name Server: {0}'.format(ns_server.strip()))
            
    if result:
        result.append('Full WHOIS: http://www.nic.pa/en')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result