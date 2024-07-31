# -*- coding: utf-8 -*-
# https://check.rs/

import re

class VerifiedRegistrar:
    def check_registrar(self, data):
        result = False
        domain_id = False
        
        raw_registrar = str(data)
        regex_data = re.findall('Registry Domain ID:(.*?)\n', raw_registrar, re.DOTALL|re.M)
        if regex_data:
            domain_id = regex_data[0]
            if domain_id:
                domain_id = domain_id.strip()
        
        if domain_id in ['4013247_DOMAIN_COM-VRSN', '32797606_DOMAIN_COM-VRSN', '1566083588_DOMAIN_COM-VRSN',
                         '92496457_DOMAIN_COM-VRSN', '91721384_DOMAIN_COM-VRSN', '108966382_DOMAIN_COM-VRSN',
                         '16002259_DOMAIN_COM-VRSN', '2287435_DOMAIN_COM-VRSN', '6683836_DOMAIN_NET-VRSN',
                         '1542998887_DOMAIN_COM-VRSN', '340491054_DOMAIN_COM-VRSN', '1477422972_DOMAIN_NET-VRSN',
                         '126154408_DOMAIN_COM-VRSN', '999590542_DOMAIN_COM-VRSN', '5314977_DOMAIN_COM-VRSN', '105900-NIRA'
                         ]:
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
    
    Registrar: HOSTINGER operations, UAB
    Registrar IANA ID: 1636
    Registry Domain ID: 92496457_DOMAIN_COM-VRSN
    
    Registrar: Sav.com, LLC
    Registrar IANA ID: 609
    Registry Domain ID: 2287435_DOMAIN_COM-VRSN
    
    Registrar: Gandi SAS
    Registrar IANA ID: 81
    Registry Domain ID: 6683836_DOMAIN_NET-VRSN
    
    Registrar: AFRIREGISTER S.A.
    Registrar IANA ID: 1381
    Registry Domain ID: 340491054_DOMAIN_COM-VRSN
    
    Registrar: Internet Domain Service BS Corp
    Registrar IANA ID: 2487
    Registry Domain ID: 1477422972_DOMAIN_NET-VRSN
    
    Registrar: Web4Africa (Pty) Ltd
    Registrar IANA ID: 664
    Registry Domain ID: 126154408_DOMAIN_COM-VRSN
    
    Registrar: GO54 Limited (formerly Whogohost Limited)
    Registrar IANA ID: 3954
    Registry Domain ID: 999590542_DOMAIN_COM-VRSN

    Registrar: Rebel Ltd
    Registrar IANA ID: 600
    Registry Domain ID: 5314977_DOMAIN_COM-VRSN
    
    Registrar: Upperlink Limited
    Registrar IANA ID: 1749
    Registry Domain ID: 105900-NIRA
'''