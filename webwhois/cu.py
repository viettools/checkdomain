# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re
from bs4 import BeautifulSoup

def parse_cu_data(regex_input, raw_data):
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
        result = result.replace('\n', '')
        result = result.replace('\xa0\xa0', '\n')
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
        req_get = req.get('https://www.nic.cu/dom_det.php?domsrch={0}'.format(domain), headers=headers, verify=False)
    except:
        pass
    
    result = []
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        if raw_data:
            domain_details = parse_cu_data('Informaci&oacute;n general del dominio(.*?)DNS Primario', raw_data)
            customer_details = parse_cu_data('Contacto Administrativo(.*?)Contacto Técnico', raw_data)
            technical_details = parse_cu_data('Contacto Técnico(.*?)Contacto Financiero', raw_data)
            billing_details = parse_cu_data('Contacto Financiero(.*?)<td align="right" class="centermenulink">', raw_data)
            ns_details = parse_cu_data('DNS Primario(.*?)Contacto Administrativo', raw_data)
            
            def clean_first_space(data):
                arr_str = []
                if data:
                    spl_data = data.split('\n')
                    for item in spl_data:
                        arr_str.append(item.strip())
                return arr_str
                
            if domain_details:
                result.extend(clean_first_space(domain_details))
            if customer_details:
                result.append('\n')
                result.extend(clean_first_space(customer_details))
            if technical_details:
                result.extend(clean_first_space(technical_details))
            if billing_details:
                result.append('\n')
                result.extend(clean_first_space(billing_details))
            if ns_details:
                result.append('\n')
                result.append('DNS Primario')
                result.extend(clean_first_space(ns_details))
            
    if result:
        result.append('Full WHOIS: https://www.nic.cu/')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result