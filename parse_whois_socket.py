# -*- coding: utf-8 -*-
# https://check.rs/

import re

class ParseWhoisSocket:
    
    def remove_redundancy(self, raw_data):
        result = False
        if raw_data:
            result = raw_data.strip()
            result = re.sub('\n|\r', '', result)
        return result
    
    def parse_socket_data(self, data, tld_domain):
        result = {
            'registrar': '',
            'registrar_url': '',
            'domain_status': [],
            'nameservers': [],
            'creation_date': '',
            'updated_date': '',
            'expiry_date': '',
        }
        if data:
            registrar = re.findall('(Registrar:|Registrar Name:|registrar:)\s+(.+)', data, re.IGNORECASE)
            if registrar:
                result['registrar'] = self.remove_redundancy(registrar[0][1])
            
            registrar_url = re.findall('(Registrar URL:|website:)\s+(.+)', data, re.IGNORECASE)
            if registrar_url:
                result['registrar_url'] = self.remove_redundancy(registrar_url[0][1])
            
            creation_date = re.findall('(Creation Date:|Registered:|\[Created on\]|created:|Registered on)\s+(.+)', data, re.IGNORECASE)
            if creation_date:
                result['creation_date'] = self.remove_redundancy(creation_date[0][1])
                
            updated_date = re.findall('(Updated Date:|Last modified:|\[Last Updated\]|Changed:)\s+(.+)', data, re.IGNORECASE)
            if updated_date:
                result['updated_date'] = self.remove_redundancy(updated_date[0][1])
            
            expiry_date = re.findall('(Registry Expiry Date:|Expires:|\[Expires on\]|'
                                     'option expiration date:|expiration date:|Registry fee due on)\s+(.+)', data, re.IGNORECASE)
            if expiry_date:
                result['expiry_date'] = self.remove_redundancy(expiry_date[0][1])
            
            domain_status = []
            raw_domain_status = str(data)
            if tld_domain in ['fr', 'tf', 'wf', 'yt', 'pm', 're']:
                pre_domain_status = re.findall('domain:(.*?)hold:', raw_domain_status, re.DOTALL | re.IGNORECASE)
                if pre_domain_status:
                    raw_domain_status = pre_domain_status[0]
                    del pre_domain_status
            elif tld_domain in ['as', 'je', 'gg']:
                pre_domain_status = re.findall('Domain Status:(.*?)Registrant:', raw_domain_status, re.DOTALL | re.IGNORECASE)
                if pre_domain_status:
                    # Format [..., ...] to [[..., ...], [..., ...]]
                    arr_reformat = re.findall('(.+)\n', pre_domain_status[0], re.IGNORECASE)
                    for item_reformat in arr_reformat:
                        item_reformat = item_reformat.replace(' ', '')
                        if item_reformat:
                            domain_status.append([item_reformat, item_reformat])
                        del item_reformat
                    del arr_reformat
                del pre_domain_status
            
            if not domain_status:
                domain_status = re.findall('(Domain Status:|Status:|\[Status\]|eppstatus:)\s+(.+)', raw_domain_status, re.IGNORECASE)
            
            if domain_status:
                for item_status in domain_status:
                    if tld_domain in ['pt']:
                        # [('Domain Status:', 'Pending Delete')]
                        result['domain_status'].append(self.remove_redundancy(spl_item_status[1]))
                    else:
                        # Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited
                        # Status: clientDeleteProhibited
                        # spl_item_status = ['clientDeleteProhibited', 'https://icann.org/epp#clientDeleteProhibited\r']
                        spl_item_status = item_status[1].split(' ')
                        if spl_item_status:
                            result['domain_status'].append(self.remove_redundancy(spl_item_status[0]))
            
            nameservers = []
            raw_nameservers = data
            if tld_domain in ['as', 'je', 'gg']:
                pre_nameservers = re.findall('Name servers:(.*?)WHOIS lookup made on', raw_domain_status, re.DOTALL | re.IGNORECASE)
                if pre_nameservers:
                    arr_reformat = re.findall('(.+)\n', pre_nameservers[0], re.IGNORECASE)
                    for item_reformat in arr_reformat:
                        item_reformat = item_reformat.replace(' ', '')
                        if item_reformat:
                            nameservers.append([item_reformat, item_reformat])
                        del item_reformat
                    del arr_reformat
                del pre_nameservers
            
            if not nameservers:
                nameservers = re.findall('(Name Server:|Nserver:|nserver:|Name servers:)\s+(.+)', raw_nameservers, re.IGNORECASE)
            if nameservers:
                for item_ns in nameservers:
                    result['nameservers'].append(self.remove_redundancy(item_ns[1]))
        return result