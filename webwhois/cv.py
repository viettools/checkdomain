# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re
from bs4 import BeautifulSoup

def parse_cv_data(regex_input, raw_data):
    result = False
    if raw_data:
        regex_data = re.findall(regex_input, raw_data, re.DOTALL|re.M)
        if regex_data:
            pre_clean_data = regex_data[0]
            #
            pre_clean_data = pre_clean_data.replace('</span>\n', '\t')
            clean_data = BeautifulSoup(pre_clean_data, features='html.parser').get_text()
            if clean_data:
                result = clean_data.strip()
                del clean_data
    
    if result:
        result = re.sub(r'\n(?=\n)', '', result)
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
        req_get = req.get('http://www.dns.cv/tldcv_si'
                          '/do?com=DS;9905235048;online.200002;+PAGE(online.300110)+RCNT(100)+F_WHOIS({0})'.format(domain),
                          headers=headers, verify=False)
    except:
        pass
    
    result = []
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        if raw_data:
            domain_details = parse_cv_data('Resultado da pesquisa(.*?)Titular', raw_data)
            customer_details = parse_cv_data('Titular(.*?)Entidade Gestora', raw_data)
            admin_details = parse_cv_data('Contacto Administrativo(.*?)Responsável Técnico', raw_data)
            technical_details = parse_cv_data('Responsável Técnico(.*?)Nameserver Information', raw_data)
            billing_details = parse_cv_data('Entidade Gestora(.*?)Contacto Administrativo', raw_data)
            
            if domain_details:
                result.append('\nResultado da pesquisa')
                result.append(domain_details)
            if customer_details:
                result.append('\nTitular')
                result.append(customer_details)
            if technical_details:
                result.append('\nResponsável Técnico')
                result.append(technical_details)
            if billing_details:
                result.append('\nEntidade Gestora')
                result.append(billing_details)
            if admin_details:
                result.append('\nEntidade Gestora')
                result.append(admin_details)
    if result:
        result.append('Full WHOIS: http://www.dns.cv')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result