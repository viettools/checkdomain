# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re
from bs4 import BeautifulSoup

def parse_hm_data(regex_input, raw_data):
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
        req_get = req.get('https://www.registry.hm', headers=headers, verify=False)
    except:
        pass
    
    req_cookie = req.cookies.get_dict()
    payload = {
        'domain_name': domain,
        'submit': 'Check WHOIS record'
    }
    
    try:
        req_post = requests.post('https://www.registry.hm/HR_whois2.php', data=payload, headers=headers, cookies=req_cookie, verify=False)
    except:
        pass
    
    result = []
    if req_post and req_post.status_code == 200 and req_post.text:
        raw_data = req_post.text
        if raw_data:
            registrar_details = parse_hm_data('Registrar:(.*?)Referral URL:', raw_data)
            registrar_details_url = parse_hm_data('Referral URL:(.*?)Domain Registrant:', raw_data)
            registrant_details = parse_hm_data('Domain Registrant:(.*?)Administrative Contact:', raw_data)
            admin_details = parse_hm_data('Administrative Contact:(.*?)Technical Contact:', raw_data)
            technical_details = parse_hm_data('Technical Contact:(.*?)Billing Contact:', raw_data)
            billing_details = parse_hm_data('Billing Contact:(.*?)Name Server:', raw_data)
            creation_date_details = parse_hm_data('Domain creation date:(.*?)<br>', raw_data)
            expiry_date_details = parse_hm_data('Domain expiration date:(.*?)<br>', raw_data)
            
            if registrar_details:
                result.append('Registrar: {0}'.format(registrar_details))
            if registrar_details_url:
                result.append('Registrar URL: {0}'.format(registrar_details_url))
            if registrant_details:
                spl_registrant = registrant_details.split('\n')
                result.append('Registry Registrant:\n\t{0}'.format('\n\t'.join(spl_registrant)))
            if admin_details:
                spl_admin = admin_details.split('\n')
                result.append('Registry Admin:\n\t{0}'.format('\n\t'.join(spl_admin)))
            if technical_details:
                spl_technical = technical_details.split('\n')
                result.append('Registry Tech:\n\t{0}'.format('\n\t'.join(spl_technical)))
            if billing_details:
                spl_billing = billing_details.split('\n')
                result.append('Registry Billing:\n\t{0}'.format('\n\t'.join(spl_billing)))
            if creation_date_details:
                result.append('Creation Date: {0}'.format(creation_date_details))
            if expiry_date_details:
                result.append('Registry Expiry Date: {0}'.format(expiry_date_details))
    
    if result:
        result.append('Full WHOIS: https://www.registry.hm/HR_whois.php')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result