# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re
from bs4 import BeautifulSoup

def parse_gw_general_data(regex_input, next_regex, raw_data):
    result = False
    pre_result = []
    if raw_data:
        raw_data = raw_data.replace('\n', '')
        raw_data = raw_data.replace('\t', '')
        raw_data = raw_data.replace('\r', '')
        
        regex_data = re.findall(regex_input, raw_data, re.DOTALL|re.M)
        if regex_data:
            regex_item_data = re.findall(next_regex, regex_data[0], re.DOTALL|re.M)
            for arr in regex_item_data:
                clean_data = BeautifulSoup(arr, features='html.parser').get_text()
                if clean_data:
                    clean_data = result = re.sub('\s{2,}', ' ', clean_data)
                    clean_data = clean_data.strip()
                    
                    pre_result.append(clean_data)
    if pre_result:
        result = '\n'.join(pre_result)
    return result

def parse_gw_contact_data(regex_input, raw_data):
    result = False
    if raw_data:
        arr_rep = [['\n', ''], ['\t', ''], ['\r', ''], ['<label>', '\n'], ['</label>', ' ']]
        for item_rep in arr_rep:
            raw_data = raw_data.replace(item_rep[0], item_rep[1])
        
        regex_data = re.findall(regex_input, raw_data, re.DOTALL|re.M)
        if regex_data:
            clean_data = BeautifulSoup(regex_data[0], features='html.parser').get_text()
            
            if clean_data:
                spl_clean = clean_data.split('\n')
                pre_result = []
                for item_spl in spl_clean:
                    item_spl = item_spl.strip()
                    if item_spl:
                        pre_result.append(item_spl)
                
                if pre_result:
                    result = '\n\t'.join(pre_result)
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
    req_get = False
    try:
        req_get = req.get('https://nic.gw/en/whois/{0}/'.format(domain), headers=headers, verify=False)
    except:
        pass
    
    result = []
    raw_data = ''
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        if raw_data:
            
            registrant = parse_gw_contact_data('<span>Registrant</span>(.*?)</fieldset>', raw_data)
            if registrant:
                result.append('Registry Registrant:\n\t{0}'.format(registrant))
            
            admin = parse_gw_contact_data('<span>Administrative Contact</span>(.*?)</fieldset>', raw_data)
            if admin:
                result.append('Registry Admin:\n\t{0}'.format(admin))
                
            tech = parse_gw_contact_data('<span>Technical Contact</span>(.*?)</fieldset>', raw_data)
            if tech:
                result.append('Registry Tech:\n\t{0}'.format(tech))
                
            creation_details = parse_gw_general_data('<span>General data</span>(.*?)</fieldset>', 'Submission Date:(.*?)Expiration Date:', raw_data)
            if creation_details:
                result.append('Creation Date: {0}'.format(creation_details))
            
            expiry_details = parse_gw_general_data('<span>General data</span>(.*?)</fieldset>', 'Expiration Date:(.*?)Status:', raw_data)
            if expiry_details:
                result.append('Registry Expiry Date: {0}'.format(expiry_details))
            
            status_details = parse_gw_general_data('<span>General data</span>(.*?)</fieldset>', 'Status:(.*?)</fieldset>', raw_data)
            if status_details:
                result.append('Domain Status: {0}'.format(status_details))
            
            ns_server = parse_gw_contact_data('<span>DNS Technical Information</span>(.*?)</fieldset>', raw_data)
            if ns_server:
                arr_ns_server = ns_server.split('\n\t')
                for item_ns in arr_ns_server:
                    if item_ns and item_ns.find('HOSTNAME') > -1:
                        item_ns = item_ns.replace('NAMESERVER (HOSTNAME):', '')
                        item_ns = item_ns.strip()
                        result.append('Name Server: {0}'.format(item_ns))
            
    if result:
        result.append('Full WHOIS: https://nic.gw/en/')
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result