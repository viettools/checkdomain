# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re
from bs4 import BeautifulSoup

def parse_es_data(regex_input, raw_data, is_ns=False):
    result = False
    if raw_data:
        regex_data = re.findall(regex_input, raw_data, re.DOTALL|re.M)
        if regex_data:
            pre_clean_data = regex_data[0]
            if is_ns:
                arr_rep = ['<br />', '<br/>', '<br>']
                for rep in arr_rep:
                    pre_clean_data = pre_clean_data.replace(rep, '\n')
            clean_data = BeautifulSoup(pre_clean_data, features='html.parser').get_text()
            if clean_data:
                result = clean_data
                del clean_data
    return result

def whois_via_web(USER_AGENT, domain, domain_type):
    headers = {
        'User-Agent': USER_AGENT
    }
    if domain and domain_type:
        domain = domain.replace('.{0}'.format(domain_type), '')
    
    final_result = {
        'status': False,
        'result': False
    }
    
    req = requests.Session()
    req_get = False
    try:
        req_get = req.get('https://www.loading.es/whois/?sld={0}&tld={1}'.format(domain, domain_type), headers=headers, verify=False)
    except:
        pass
    
    result = []
    raw_data = ''
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        if raw_data:
            registrar = parse_es_data('Agente registrador:(.*?)Contacto registrante:', raw_data)
            if registrar:
                result.append('Registrar: {0}'.format(registrar))

            registrant = parse_es_data('Contacto registrante:(.*?)Contacto administrativo:', raw_data)
            if registrant:
                result.append('Registry Registrant ID: {0}'.format(registrant))
            
            admin = parse_es_data('Contacto administrativo:(.*?)Contacto tecnico:', raw_data)
            if admin:
                result.append('Registry Admin ID: {0}'.format(admin))
                
            tech = parse_es_data('Contacto tecnico:(.*?)Fecha Creación:', raw_data)
            if tech:
                result.append('Registry Tech ID: {0}'.format(tech))
                
            creation = parse_es_data('Fecha Creación:(.*?)Fecha Expiración:', raw_data)
            if creation:
                result.append('Creation Date: {0}'.format(creation))
                
            expiry = parse_es_data('Fecha Expiración:(.*?)Servidores DNS:', raw_data)
            if expiry:
                result.append('Registry Expiry Date: {0}'.format(expiry))
            
            ns_server = parse_es_data('Servidores DNS:(.*?)</div>', raw_data, is_ns=True)
            if ns_server:
                arr_ns_server = ns_server.split('\n')
                for item_ns in arr_ns_server:
                    item_ns = item_ns.strip()
                    if item_ns:
                        result.append('Name Server: {0}'.format(item_ns))
            
    if result:
        result.append('Full WHOIS: https://www.dominios.es/en')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result