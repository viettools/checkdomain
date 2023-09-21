# -*- coding: utf-8 -*-
# https://check.rs/

import re

class VerifiedRegistrar:
    def check_registrar(self, data):
        result = False
        domain_id = False
        
        raw_registrar = str(data)
        regex_data = re.findall('Registry Domain ID:(.*?)Registrar WHOIS Server', raw_registrar, re.DOTALL|re.M)
        if regex_data:
            domain_id = regex_data[0]
            if domain_id:
                domain_id = domain_id.strip()
        
        if domain_id in ['4013247_DOMAIN_COM-VRSN', '32797606_DOMAIN_COM-VRSN', '91721384_DOMAIN_COM-VRSN',
                         '1566083588_DOMAIN_COM-VRSN', '108966382_DOMAIN_COM-VRSN', '1542998887_DOMAIN_COM-VRSN',
                         '16002259_DOMAIN_COM-VRSN']:
            result = True
        return result

'''
    Registrar: NameSilo, LLC
    Registrar IANA ID: 1479
    Registry Domain ID: 1566083588_DOMAIN_COM-VRSN
    
    Registrar: Porkbun LLC
    Registrar IANA ID: 1861
    Registry Domain ID: 16002259_DOMAIN_COM-VRSN
    
    Registrar: GoDaddy.com, LLC
    Registrar IANA ID: 146
    Registry Domain ID: 4013247_DOMAIN_COM-VRSN
    
    Registrar: NameCheap, Inc.
    Registrar IANA ID: 1068
    Registry Domain ID: 32797606_DOMAIN_COM-VRSN
    
    Registrar: Dynadot Inc
    Registrar IANA ID: 472
    Registry Domain ID: 91721384_DOMAIN_COM-VRSN
    
    Registrar: PDR Ltd. d/b/a PublicDomainRegistry.com
    Registrar IANA ID: 303
    Registry Domain ID: 108966382_DOMAIN_COM-VRSN
    
    Registrar: CloudFlare, Inc.
    Registrar IANA ID: 1910
    Registry Domain ID: 1542998887_DOMAIN_COM-VRSN
'''