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
            # 'ba': 'https://nic.ba/?culture=en',
            # 'bb': 'https://whois.telecoms.gov.bb/search/',
            # 'bd': 'http://domainreg.btcl.com.bd/',
            'be': 'whois.dns.be',
            'bf': 'whois.registre.bf',
            'bg': 'whois.register.bg',
            'bh': 'whois.nic.bh',
            'bi': 'whois1.nic.bi',
            'bj': 'whois.nic.bj',
            'bm': 'whois.afilias-srs.net',
            'bn': 'whois.bnnic.bn',
            'bo': 'whois.nic.bo',
            'br': 'whois.registro.br',
            # 'bs': 'http://www.register.bs/',
            # 'bt': 'https://www.nic.bt/',
            'bw': 'whois.nic.net.bw',
            'by': 'whois.cctld.by',
            'bz': 'whois.afilias-srs.net',
            'ki': 'whois.coccaregistry.org',
            'my': 'rdap.mynic.my',
            'ye': 'whois.y.net.ye',
        }
        
        pseudo_sld = {
            'br.com': 'whois.centralnic.net',
            'cn.com': 'whois.centralnic.net',
            'de.com': 'whois.centralnic.net',
            'eu.com': 'whois.centralnic.net',
            'gb.net': 'whois.centralnic.net',
            'gr.com': 'whois.centralnic.net',
            'in.net': 'whois.centralnic.net',
            'ru.com': 'whois.centralnic.net',
            'sa.com': 'whois.centralnic.net',
            'se.net': 'whois.centralnic.net',
            'uk.com': 'whois.centralnic.net',
            'uk.net': 'whois.centralnic.net',
            'us.com': 'whois.centralnic.net',
            'za.com': 'whois.centralnic.net',
            'jpn.com': 'whois.centralnic.net',
            'it.com': 'whois.it.com'
        }
        dict_extension.update(pseudo_sld)
        return dict_extension.get(extension, False)