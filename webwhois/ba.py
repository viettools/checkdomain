# -*- coding: utf-8 -*-
# https://check.rs/

def whois_via_web(USER_AGENT, domain, domain_type):
    final_result = {
        'status': True,
        'result': '\n'.join(['Full WHOIS: https://nic.ba/?culture=en'])
    }
    
    return final_result