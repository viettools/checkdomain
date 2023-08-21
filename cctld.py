# -*- coding: utf-8 -*-
# https://check.rs/

class WhOISccTLD:
    
    def get_whois_server(self, extension):
        dict_extension = {
            'ac': 'whois.nic.ac',
            # 'ad': 'https://www.andorratelecom.ad/',
            'ae': 'whois.aeda.net.ae',
            'af': 'whois.nic.af',
            'ag': 'whois.nic.ag',
            'ai': 'whois.nic.ai',
            # 'al': 'https://akep.al/en/domain-e-application/',
            'am':'whois.amnic.net',
            # 'ao': 'https://www.dns.ao/ao/gca/index.php?id=19',
            # 'aq': 'No Information',
            'ar': 'whois.nic.ar',
            'as': 'whois.nic.as',
            'at': 'whois.nic.at',
            'au': 'whois.auda.org.au',
            'aw': 'whois.nic.aw',
            'ax': 'whois.ax',
            # 'az': 'http://whois.az/',
            'ki': 'whois.coccaregistry.org',
        }
        return dict_extension.get(extension, False)