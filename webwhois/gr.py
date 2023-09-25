# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re
from bs4 import BeautifulSoup

def parse_gr_data(regex_input, raw_data):
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

def get_gr_post_data(req, headers, domain, domain_type):   
    result = {
    }
    req_get = False
    try:
        req_get = req.get('https://easy.gr/en/domains/whois/business-information', headers=headers, verify=False)
    except:
        pass
    
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        if raw_data:
            myantispam = re.findall('<input type="text" class="input" name="myantispam" style="display: none;"  value="(.*?)"/>', raw_data, re.DOTALL|re.M)
            if myantispam:
                result.update({
                    'action': '14',
                    'domain': domain,
                    'antispam': '10',
                    'myantispam_registry': 'nongr',
                    'myantispam': myantispam[0]
                })
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
    
    gr_post_data = get_gr_post_data(req, headers, domain, domain_type)
    if gr_post_data:
        req_post = False
        try:
            req_post = req.post('https://easy.gr/en/domains/whois/business-information?ajax=1&this_page=domains-whois-business-information',
                                headers=headers,
                                data=gr_post_data,
                                verify=False)
        except:
            pass
        
        result = []
        if req_post and req_post.status_code == 200 and req_post.json():
            json_data = req_post.json()
            if json_data.get('status', False) == 1 and json_data.get('html', False):
                raw_data = json_data.get('html')
                protocol_number_details = parse_gr_data('Protocol Number(.*?)Creation Date', raw_data)
                creation_date_details = parse_gr_data('Creation Date(.*?)Expiration Date', raw_data)
                expiration_date_details = parse_gr_data('Expiration Date(.*?)Updated Date', raw_data)
                updated_date_details = parse_gr_data('Updated Date(.*?)Bundle Name', raw_data)
                
                registrar_details = parse_gr_data('<td>Name</td>(.*?)<td>URL</td>', raw_data)
                registrar_url_details = parse_gr_data('<td>URL</td>(.*?)<td>Email</td>', raw_data)
                registrar_phone_details = parse_gr_data('<td>Telephone</td>(.*?)Whois Extra Info', raw_data)
                registrar_email_details = parse_gr_data('<td>Email</td>(.*?)<td>Telephone</td>', raw_data)
                
                if protocol_number_details:
                    result.append('Protocol Number: {0}'.format(protocol_number_details))
                if creation_date_details:
                    result.append('Creation Date: {0}'.format(creation_date_details))
                if updated_date_details:
                    result.append('Updated Date: {0}'.format(updated_date_details))
                if expiration_date_details:
                    result.append('Registry Expiry Date: {0}'.format(expiration_date_details))
                
                if registrar_details:
                    result.append('Registrar: {0}'.format(registrar_details))
                if registrar_url_details:
                    result.append('Registrar URL: {0}'.format(registrar_url_details))
                if registrar_phone_details:
                    result.append('Registrar Phone: {0}'.format(registrar_phone_details))
                if registrar_email_details:
                    result.append('Registrar Email: {0}'.format(registrar_email_details))
        
        if result:
            result.append('Full WHOIS: https://grweb.ics.forth.gr/public/?lang=en')
            final_result = {
                'status': True,
                'result': '\n'.join(result)
            }
    
    return final_result