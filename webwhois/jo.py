# -*- coding: utf-8 -*-
# https://check.rs/

import requests
import re, json
from bs4 import BeautifulSoup


def parse_jo_data(regex_input, raw_data):
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

def FirstPageEn(req, headers, raw_data, domain, ddl):
    next_view_state_details = False
    next_view_state_generator_details = False
    next_event_validation_details = False
    if raw_data:
        view_state_details = parse_jo_data('<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)" />', raw_data)
        view_state_generator_details = parse_jo_data('<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*?)" />', raw_data)
        event_validation_details = parse_jo_data('<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)" />', raw_data)

        req_cookie = req.cookies.get_dict()
        payload = {
            'ctl00': 'ResultsUpdatePanel|b1',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': view_state_details,
            '__VIEWSTATEGENERATOR': view_state_generator_details,
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': event_validation_details,
            'SkinChooser': 'Default',
            'SkinChooser_ClientState': '',
            'TextBox1': domain,
            'ddl': ddl,
            '__ASYNCPOST': 'true',
            'b1': 'WhoIs'
        }
        headers.update({
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://dns.jo/firstpageEn.aspx'
        })
        req_post = False

        try:
            req_post = requests.post('https://dns.jo/FirstPageen.aspx', data=payload, headers=headers, cookies=req_cookie, verify=False)
        except:
            pass
        
        if req_post and req_post.status_code == 200 and req_post.text:
            raw_data = req_post.text
            next_view_state_details = parse_jo_data('__VIEWSTATE\|(.*?)\|8\|hiddenField\|__VIEWSTATEGENERATOR', raw_data)
            next_view_state_generator_details = parse_jo_data('__VIEWSTATEGENERATOR\|(.*?)\|0\|hiddenField\|__VIEWSTATEENCRYPTED', raw_data)
            next_event_validation_details = parse_jo_data('__EVENTVALIDATION\|(.*?)\|0\|asyncPostBackControlIDs\|', raw_data)

    return next_view_state_details, next_view_state_generator_details, next_event_validation_details

def whois_via_web(USER_AGENT, domain, domain_type):
    ddl = '7' # '.jo'
    if domain_type:
        domain_type = '.{0}'.format(domain_type)
        if domain_type == '.com.jo':
            ddl = '1'
        elif domain_type == '.gov.jo':
            ddl = '2'
        elif domain_type == '.net.jo':
            ddl = '3'
        elif domain_type == '.org.jo':
            ddl = '4'
        elif domain_type == '.edu.jo':
            ddl = '5'
        elif domain_type == '.mil.jo':
            ddl = '6'
        elif domain_type == '.sch.jo':
            ddl = '9'
        elif domain_type == '.per.jo':
            ddl = '10'
        elif domain_type == '.phd.jo':
            ddl = '11'
        # 12 .الاردن
    if domain:
        domain = domain.replace(domain_type, '')
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
        req_get = req.get('https://dns.jo/FirstPageEn.aspx', headers=headers, verify=False)
    except:
        pass
    
    result = []
    if req_get and req_get.status_code == 200 and req_get.text:
        raw_data = req_get.text
        if raw_data:
            next_view_state_details, next_view_state_generator_details, \
                    next_event_validation_details = FirstPageEn(req, headers, raw_data, domain, ddl)

            if next_view_state_details and next_view_state_generator_details and next_event_validation_details:
                req_cookie = req.cookies.get_dict()
                payload = {
                    'SkinChooser': 'Default',
                    'SkinChooser_ClientState': '',
                    'TextBox1': domain,
                    'ddl': ddl,
                    '__EVENTTARGET': 'DG$ctl02$lbYear',
                    '__EVENTARGUMENT': '',
                    '__VIEWSTATE': next_view_state_details,
                    '__VIEWSTATEGENERATOR': next_view_state_generator_details,
                    '__VIEWSTATEENCRYPTED': '',
                    '__EVENTVALIDATION': next_event_validation_details
                }
                headers.update({
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Referer': 'https://dns.jo/firstpageEn.aspx'
                })
                req_post = False
                
                try:
                    req_post = requests.post('https://dns.jo/FirstPageen.aspx', data=payload, headers=headers, cookies=req_cookie, verify=False)
                except:
                    pass

                if req_post and req_post.status_code == 200 and req_post.text:
                    raw_data = req_post.text
                    if raw_data:
                        creation_date_details = parse_jo_data('<input name="ctl00\$ContentPlaceHolder1\$reg_date" type="text" value="(.*?)"', raw_data)
                        if creation_date_details:
                            result.append('Creation Date: {0}'.format(creation_date_details))
                        
                        ns1_details = parse_jo_data('<input name="ctl00\$ContentPlaceHolder1\$PrimaryNameServerTextBox" type="text" value="(.*?)"', raw_data)
                        if ns1_details:
                            result.append('Name Server: {0}'.format(ns1_details))
                        
                        ns2_details = parse_jo_data('<input name="ctl00\$ContentPlaceHolder1\$SecondServer5TextBox" type="text" value="(.*?)"', raw_data)
                        if ns2_details:
                            result.append('Name Server: {0}'.format(ns2_details))
                        
                        admin_details = parse_jo_data('<input name="ctl00\$ContentPlaceHolder1\$AdminTextBox" type="text" value="(.*?)"', raw_data)
                        if admin_details:
                            result.append('AdminOrganization: {0}'.format(admin_details))
                        
                        tech_details = parse_jo_data('<input name="ctl00\$ContentPlaceHolder1\$TechTextBox" type="text" value="(.*?)"', raw_data)
                        if tech_details:
                            result.append('TechOrganization: {0}'.format(tech_details))
                            
                        billing_details = parse_jo_data('<input name="ctl00\$ContentPlaceHolder1\$BillTextBox" type="text" value="(.*?)"', raw_data)
                        if billing_details:
                            result.append('BillingOrganization: {0}'.format(billing_details))
                        
                        
    result.append('\nFull WHOIS: https://dns.jo\nSometime, this page can not get data!!!')
    if result:
        
        final_result = {
            'status': True,
            'result': '\n'.join(result)
        }
    
    return final_result