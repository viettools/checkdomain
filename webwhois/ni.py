# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re, json

def whois_via_web(USER_AGENT, domain, domain_type):
    headers = {
        'User-Agent': USER_AGENT
    }
    
    final_result = {
        'status': False,
        'result': False
    }
    
    dict_idZona = {
        'ni': 1,
        'nom.ni': 2,
        'ac.ni': 3, # Not check
        'biz.ni': 4,
        'co.ni': 5,
        'com.ni': 6,
        'coop.ni': 7,
        'edu.ni': 8,
        'in.ni': 10, # Not check
        'info.ni': 11,
        'int.ni': 12, # Not check
        'net.ni': 14,
        'org.ni': 15,
        'pp.ni': 16, # Not check
        'tv.ni': 17, # Not check
        'web.ni': 18 # Not check
    }
    if domain.endswith('coop.ni'):
        domain_type = 'coop.ni'
    elif domain.endswith('pp.ni'):
        domain_type = 'pp.ni'
    elif domain.endswith('tv.ni'):
        domain_type = 'tv.ni'
    
    idZona = dict_idZona.get(domain_type, 1)
    domain = domain.replace('.' + domain_type, '')
    
    req = requests.Session()
    req_get = False
    try:
        req_get = req.get('https://apiecommercenic.uni.edu.ni/api/v1/dominios/whois?dominio={0}.{1}'.format(domain, domain_type), headers=headers, verify=False)
    except:
        pass
    
    result = []
    if req_get and req_get.status_code == 200 and req_get.text:
        json_data = req_get.json()
        if json_data and json_data.get('datos', {}):
            datos = json_data.get('datos', {})
            if datos.get('cliente', False):
                result.append('Registrant Name: {0}'.format(datos['cliente']))
            if datos.get('fechaExpiracion', False):
                result.append('Registry Expiry Date: {0}'.format(datos['fechaExpiracion']))
            
    if result:
        result.append('Full WHOIS: https://nic.ni/')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result