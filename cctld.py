# -*- coding: utf-8 -*-
# https://check.rs/

class WhOISccTLD:
    
    def get_whois_server(self, extension):
        dict_extension = {
            'ac': 'whois.nic.ac',
            'ae': 'whois.aeda.net.ae',
            'af': 'whois.nic.af',
            'ag': 'whois.nic.ag',
            'ai': 'whois.nic.ai',
            'am':'whois.amnic.net',
            'ar': 'whois.nic.ar',
            'as': 'whois.nic.as',
            'ki': 'whois.coccaregistry.org',
        }
        return dict_extension.get(extension, False)