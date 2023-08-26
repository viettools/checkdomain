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
    
    def parse_registrar(self, data, tld_domain):
        result = ''
        if not data:
            return result
        
        raw_registrar = str(data)
        if tld_domain == 'be':
            pre_raw_registrar = re.findall('Name:(.*?)Website:', raw_registrar, re.DOTALL | re.IGNORECASE)
            if pre_raw_registrar:
                raw_registrar = self.remove_redundancy(pre_raw_registrar[-1])
                result = raw_registrar
                del pre_raw_registrar
        elif tld_domain == 'ee':
            '''
            Registrar:
            name:       Zone Media OÜ
            url:        http://www.zone.ee
            phone:      +372 6886886
            changed:    2020-07-01 13:55:58 +03:00
            --> Normal keyword --> Need to filter
            '''
            pre_raw_registrar = re.findall('Registrar:(.*?)url:', raw_registrar, re.DOTALL | re.IGNORECASE)
            if pre_raw_registrar:
                raw_registrar = pre_raw_registrar[-1]
                raw_registrar = raw_registrar.replace('name:', 'registrar:')
                del pre_raw_registrar

        registrar = re.findall('(Registrar:|Registrar Name:|registrar:|'
                                   'registrar............:|Referral URL:|'
                                   'registrar..........:)\s+(.+)', raw_registrar, re.IGNORECASE)
        if registrar:
            result = self.remove_redundancy(registrar[0][1])
        return result
    
    def parse_registrar_url(self, data, tld_domain):
        result = ''
        if not data:
            return result
        
        raw_registrar_url = str(data)
        if tld_domain == 'be':
            pre_raw_registrar_url = re.findall('Website:(.*?)Nameservers:', raw_registrar_url, re.DOTALL | re.IGNORECASE)
            if pre_raw_registrar_url:
                raw_registrar_url = self.remove_redundancy(pre_raw_registrar_url[-1])
                result = raw_registrar_url
                del pre_raw_registrar_url
        elif tld_domain == 'ee':
            pre_raw_registrar_url = re.findall('Registrar:(.*?)phone:', raw_registrar_url, re.DOTALL | re.IGNORECASE)
            if pre_raw_registrar_url:
                raw_registrar_url = pre_raw_registrar_url[-1]
                raw_registrar_url = raw_registrar_url.replace('url:', 'Registrar URL:')
                del pre_raw_registrar_url
        
        registrar_url = re.findall('(Registrar URL:|website:|www..................:|'
                                   'Referral URL:|www................:)\s+(.+)', raw_registrar_url, re.IGNORECASE)
        if registrar_url:
            result = self.remove_redundancy(registrar_url[0][1])
        return result
    
    def parse_creation_date(self, data, tld_domain):
        result = ''
        if not data:
            return result
        
        creation_date = re.findall('(Creation Date:|Registered:|\[Created on\]|created:|'
                                       'Registered on|created..............:|Registered On:|Fecha de activación:|'
                                       'Registration Time:|created............:)\s+(.+)', data, re.IGNORECASE)
        if creation_date:
            result = self.remove_redundancy(creation_date[0][1])
        return result
    
    def parse_updated_date(self, data, tld_domain):
        result = ''
        if not data:
            return result
        
        if tld_domain.find('au') > -1:
            updated_date = re.findall('Last Modified: (.+)', data, re.IGNORECASE)
            if updated_date:
                result = self.remove_redundancy(updated_date[0])
        else:
            updated_date = re.findall('(Updated Date:|Last modified:|\[Last Updated\]|Changed:|'
                                        'modified.............:|Modified Date:|modified...........:)\s+(.+)', data, re.IGNORECASE)
            if updated_date:
                result = self.remove_redundancy(updated_date[0][1])
        return result
    
    def parse_expiry_date(self, data, tld_domain):
        result = ''
        if not data:
            return result

        expiry_date = re.findall('(Registry Expiry Date:|Expires:|\[Expires on\]|'
                                    'option expiration date:|expiration date:|Registry fee due on|'
                                    'available............:|Expires On:|Fecha de corte:|'
                                    'Expiration Time:|expire:|available..........:)\s+(.+)', data, re.IGNORECASE)
        if expiry_date:
            result = self.remove_redundancy(expiry_date[0][1])
        return result
    
    def parse_domain_status(self, data, tld_domain):
        result = []
        if not data:
            return result

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
        # Special BE
        elif tld_domain in ['be']:
            pre_domain_status = re.findall('Flags:(.*?)Please visit', raw_domain_status, re.DOTALL | re.IGNORECASE)
            if pre_domain_status:
                raw_domain_status = pre_domain_status[-1]
                redundancy = self.remove_redundancy(raw_domain_status)
                # Avoid values of 'Keys:'
                if redundancy.find(' ') == -1:
                    result.append(redundancy)
                del pre_domain_status
                del redundancy
        
        if not domain_status:
            domain_status = re.findall('(Domain Status:|Status:|\[Status\]|'
                                        'eppstatus:|status...............:|status.............:)\s+(.+)', raw_domain_status, re.IGNORECASE)
        
        if domain_status:
            for item_status in domain_status:
                if tld_domain in ['pt', 'am', 'bg', 'cr']:
                    # [('Domain Status:', 'Pending Delete')]
                    result.append(self.remove_redundancy(item_status[1]))
                else:
                    # Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited
                    # Status: clientDeleteProhibited
                    # spl_item_status = ['clientDeleteProhibited', 'https://icann.org/epp#clientDeleteProhibited\r']
                    spl_item_status = item_status[1].split(' ')
                    if spl_item_status:
                        res_stt_rem_red = self.remove_redundancy(spl_item_status[0])
                        if res_stt_rem_red:
                            result.append(res_stt_rem_red)
        
        return result
    
    def parse_nameservers(self, data, tld_domain):
        result = []
        if not data:
            return result

        nameservers = []
        raw_nameservers = str(data)
        if tld_domain in ['as', 'je', 'gg', 'aw', 'be', 'bg']:
            if tld_domain in ['as', 'je', 'gg']:
                pre_nameservers = re.findall('Name servers:(.*?)WHOIS lookup made on', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'aw':
                pre_nameservers = re.findall('Domain nameservers:(.*?)Record maintained by:', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'be':
                pre_nameservers = re.findall('Nameservers:(.*?)Keys:', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'bg':
                pre_nameservers = re.findall('NAME SERVER INFORMATION:(.*?)DNSSEC:', raw_nameservers, re.DOTALL | re.IGNORECASE)
            
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
            nameservers = re.findall('(Name Server:|Nserver:|nserver:|Name servers:|'
                                        'nserver..............:|Hostname:|nserver............:)\s+(.+)', raw_nameservers, re.IGNORECASE)
        if nameservers:
            for item_ns in nameservers:
                res_ns_rem_red = self.remove_redundancy(item_ns[1])
                if res_ns_rem_red:
                    result.append(res_ns_rem_red)
                        
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
            result['registrar'] = self.parse_registrar(data, tld_domain)
            result['registrar_url'] = self.parse_registrar_url(data, tld_domain)
            result['creation_date'] = self.parse_creation_date(data, tld_domain)
            result['updated_date'] = self.parse_updated_date(data, tld_domain)
            result['expiry_date'] = self.parse_expiry_date(data, tld_domain)
            result['domain_status'] = self.parse_domain_status( data, tld_domain)
            result['nameservers'] = self.parse_nameservers( data, tld_domain)
            
            # print(result) # Check Result
        return result