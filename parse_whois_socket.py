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
        def registrar_short_replace(data, regex_string, before_replace, after_replace):
            result = str(data)
            short_filtered = re.findall(regex_string, result, re.DOTALL | re.IGNORECASE)
            if short_filtered:
                result = short_filtered[-1]
                result = result.replace(before_replace, after_replace)
                del short_filtered
            return result
        
        result = ''
        if not data:
            return result
        
        raw_registrar = str(data)
        if tld_domain in ['be', 'gh', 'sy', 'tg', 'tr', 'ua', 'ac.za']:
            pre_raw_registrar = []
            if tld_domain == 'be':
                pre_raw_registrar = re.findall('Name:(.*?)Website:', raw_registrar, re.DOTALL | re.IGNORECASE)
            elif tld_domain in ['gh', 'sy']:
                pre_raw_registrar = re.findall('Sponsoring Registrar:(.*?)Sponsoring Registrar IANA ID:', raw_registrar, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'tg':
                pre_raw_registrar = re.findall('Registrar:..........(.*?)Activation:.........', raw_registrar, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'tr':
                pre_raw_registrar = re.findall('Organization Name	:(.*?)Address', raw_registrar, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'ua':
                pre_raw_registrar = re.findall('% Registrar:(.*?)organization:', raw_registrar, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'ac.za':
                pre_raw_registrar = re.findall('Registrar:(.*?)Registrar WHOIS Server:', raw_registrar, re.DOTALL | re.IGNORECASE)
            
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
            raw_registrar = registrar_short_replace(raw_registrar, 'Registrar:(.*?)url:', 'name:', 'registrar:')
        elif tld_domain == 'it':
            raw_registrar = registrar_short_replace(raw_registrar, 'Registrar(.*?)Name:', 'Organization:', 'registrar:')
        elif tld_domain == 'lv':
            raw_registrar = registrar_short_replace(raw_registrar, '\[Registrar\](.*?)\[Nservers\]', 'Name:', 'registrar:')

        registrar = re.findall('(Registrar:|Registrar Name:|registrar:|'
                                   'registrar............:|Referral URL:|'
                                   'registrar..........:|Sponsoring Registrar:|'
                                   'Sponsoring Registrar Organization:|'
                                   'Authorized Agency           :|Current Registar:|'
                                   'registrar-name:|Registrar                :|'
                                   'Registrar Company Name :|Registrar...........:|'
                                   'Registration Service Provider:)\s+(.+)', raw_registrar, re.IGNORECASE)
        if registrar:
            result = self.remove_redundancy(registrar[0][1])
        return result
    
    def parse_registrar_url(self, data, tld_domain):
        
        def registrar_url_short_replace(data, regex_string, before_replace, after_replace):
            result = str(data)
            short_filtered = re.findall(regex_string, result, re.DOTALL | re.IGNORECASE)
            if short_filtered:
                result = short_filtered[-1]
                result = result.replace(before_replace, after_replace)
                del short_filtered
            return result
            
        result = ''
        if not data:
            return result
        
        raw_registrar_url = str(data)
        if tld_domain in ['be', 'gh', 'gi', 'gl', 'la', 'kw', 'ps', 'rw', 'so', 'vg', 'bh', 'bm', 'do']:
            pre_raw_registrar_url = []
            if tld_domain == 'be':
                pre_raw_registrar_url = re.findall('Website:(.*?)Nameservers:', raw_registrar_url, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'gh':
                pre_raw_registrar_url = re.findall('Sponsoring Registrar URL:(.*?)Sponsoring Registrar Country:', raw_registrar_url, re.DOTALL | re.IGNORECASE)
            # Related DONUTS, CoCCA, CNIC
            elif tld_domain in ['gi', 'gl', 'la', 'kw', 'ps', 'rw', 'so', 'vg', 'bh', 'bm', 'do']:
                pre_raw_registrar_url = re.findall('Registrar URL:(.*?)Updated Date:', raw_registrar_url, re.DOTALL | re.IGNORECASE)
            
            if pre_raw_registrar_url:
                raw_registrar_url = self.remove_redundancy(pre_raw_registrar_url[-1])
                result = raw_registrar_url
                del pre_raw_registrar_url
        elif tld_domain == 'ee':
            raw_registrar_url = registrar_url_short_replace(data, 'Registrar:(.*?)phone:', 'url:', 'Registrar URL:')
        elif tld_domain == 'it':
            raw_registrar_url = registrar_url_short_replace(data, 'Registrar(.*?)DNSSEC:', 'Web:', 'Registrar URL:')
        elif tld_domain == 'mx':
            raw_registrar_url = registrar_url_short_replace(data, 'Registrar:(.*?)Registrant:', 'URL:', 'Registrar URL:')
        elif tld_domain == 'no':
            raw_registrar_url = ''
        elif tld_domain == 'st':
            raw_registrar_url = registrar_url_short_replace(data,
                                                            'REGISTRATION-SERVICE-PROVIDER:(.*?)created-date:',
                                                            'URL:',
                                                            'Registrar URL:')
        elif tld_domain == 'sy':
            raw_registrar_url = registrar_url_short_replace(data, 'WHOIS Server:(.*?)Creation Date:', 'Referral URL:', 'Registrar URL:')
        elif tld_domain == 'ua':
            raw_registrar_url = registrar_url_short_replace(data, '% Registrar:(.*?)abuse-email:', 'url:', 'Registrar URL:')
        elif tld_domain == 'uk':
            raw_registrar_url = registrar_url_short_replace(data, 'Registrar:(.*?)Relevant dates:', 'URL:', 'Registrar URL:')
        elif tld_domain == 'de':
            raw_registrar_url = ''
        
        registrar_url = re.findall('(Registrar URL:|website:|www..................:|'
                                   'Referral URL:|www................:|registrar info:|'
                                   'registrar-url:|Registration Service URL:)\s+(.+)', raw_registrar_url, re.IGNORECASE)
        if registrar_url:
            result = self.remove_redundancy(registrar_url[0][1])
        return result
    
    def parse_creation_date(self, data, tld_domain):
        result = ''
        if not data:
            return result
        
        creation_date = re.findall('(Creation Date:|Registered:|\[Created on\]|created:|'
                                       'Registered on|created..............:|Registered On:|Fecha de activación:|'
                                       'Registration Time:|created............:|Date de création:|'
                                       'Domain Name Commencement Date:|Created On:|'
                                       'Registered Date             :|Record created on|'
                                       'Created on               :|Created \(JJ/MM/AAAA\) :|'
                                       'Registration date:|Created date:|Creation date.......:|'
                                       'Created on..............:)\s+(.+)', data, re.IGNORECASE)
        if creation_date:
            result = self.remove_redundancy(creation_date[0][1])
        return result
    
    def parse_updated_date(self, data, tld_domain):
        result = ''
        if not data:
            return result
        
        if tld_domain in ['au', 'sk', 'tz', 'ac.ru']:
            updated_date = []
            if tld_domain == 'au':
                updated_date = re.findall('Last Modified: (.+)', data, re.IGNORECASE)
            elif tld_domain == 'sk':
                updated_date = re.findall('Updated:(.+)', data, re.IGNORECASE)
            elif tld_domain == 'tz':
                updated_date = re.findall('changed:(.+)expire:', data, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'ac.ru':
                arr_small_area = re.findall('created:(.+)organization', data, re.DOTALL | re.IGNORECASE)
                if arr_small_area:
                    updated_date = re.findall('updated:(.+)source:', arr_small_area[0], re.DOTALL | re.IGNORECASE)
            
            if updated_date:
                result = self.remove_redundancy(updated_date[0])
        else:
            updated_date = re.findall('(Updated Date:|Last modified:|\[Last Updated\]|Changed:|'
                                        'modified.............:|Modified Date:|modified...........:|'
                                        'Dernière modification:|Last Updated On:|Last Update:|'
                                        'Last Updated Date           :|Last modified :|'
                                        'Last updated on          :|modified:|Last renewed \(JJ/MM/AAAA\) :|'
                                        'Modification date:|Last updated:|LastMod:|Entry updated:)\s+(.+)', data, re.IGNORECASE)
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
                                    'Expiration Time:|expire:|available..........:|'
                                    'Date d\'expiration:|Expiry Date:|validity:|Expire Date:|'
                                    'Expiration Date             :|Expires    on:|Record expires on|'
                                    'Expires on               :|Expire \(JJ/MM/AAAA\) :|'
                                    'Expiration date:|free-date:|Valid Until:|Exp date:|'
                                    'Expiry :|Expires on..............:)\s+(.+)', data, re.IGNORECASE)
        if expiry_date:
            result = self.remove_redundancy(expiry_date[0][1])
        else:
            if tld_domain == 'tg':
                expiry_date_tg = re.findall('Expiration:.........(.*?)Status:.............', data, re.DOTALL | re.IGNORECASE)
                if expiry_date_tg:
                    result = self.remove_redundancy(expiry_date_tg[0])
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
        # Special BE, HK, TK
        elif tld_domain in ['be', 'hk', 'tg', 'net.ru', 'org.ru', 'pp.ru']:
            pre_domain_status = []
            if tld_domain == 'be':
                pre_domain_status = re.findall('Flags:\r\n\t(.*?)Please visit', raw_domain_status, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'hk':
                pre_domain_status = re.findall('Domain Status:(.*?)DNSSEC:', raw_domain_status, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'tg':
                pre_domain_status = re.findall('Status:.............(.*?)Contact Type:', raw_domain_status, re.DOTALL | re.IGNORECASE)
            elif tld_domain in ['net.ru', 'org.ru', 'pp.ru']:
                pre_domain_status = re.findall('state:(.+)', raw_domain_status, re.IGNORECASE)
            
            if pre_domain_status:
                raw_domain_status = pre_domain_status[-1]
                redundancy = self.remove_redundancy(raw_domain_status)
                result.append(redundancy)
                del pre_domain_status
                del redundancy
        
        if not domain_status:
            domain_status = re.findall('(Domain Status:|Status:|\[Status\]|'
                                        'eppstatus:|status...............:|status.............:|'
                                        'Statut:|Domain status :|domaintype:|'
                                        'Domain  state:|Status :|Status :|Domain status.......:|'
                                        'Status.:)\s+(.+)', raw_domain_status, re.IGNORECASE)
        
        if domain_status:
            for item_status in domain_status:
                if tld_domain in ['pt', 'am', 'bg', 'cr', 'il', 'lu', 'pk', 'sg', 'si', 'sk', 'st', 'tm', 'tr', 'uk']:
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
        if tld_domain in ['as', 'je', 'gg', 'aw', 'be', 'bg', 'hk', 'am', 'eu',
                          'im', 'it', 'kg', 'mx', 'nc', 'nl', 'pf', 'pl', 'rs',
                          'sa', 'sg', 'sm', 'tm', 'tn', 'tr', 'tw', 'uk', 'co.pl']:
            if tld_domain in ['as', 'je', 'gg']:
                pre_nameservers = re.findall('Name servers:(.*?)WHOIS lookup made on', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'aw':
                pre_nameservers = re.findall('Domain nameservers:(.*?)Record maintained by:', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'be':
                pre_nameservers = re.findall('Nameservers:(.*?)Keys:', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'bg':
                pre_nameservers = re.findall('NAME SERVER INFORMATION:(.*?)DNSSEC:', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'hk':
                pre_nameservers = re.findall('Name Servers Information:(.*?)Status Information:', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'im':
                pre_nameservers = re.findall('Name Server:(.+)', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'it':
                pre_nameservers = re.findall('Nameservers(.+)', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'kg':
                pre_nameservers = re.findall('Name servers in the listed order:(.+)', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'mx':
                pre_nameservers = re.findall('Name Servers:(.+)DNSSEC DS Records:', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'nc':
                pre_nameservers = re.findall('Domain server(.+)Registrar', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'nl':
                pre_nameservers = re.findall('Domain nameservers:(.+)Record maintained by:', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'pf':
                pre_nameservers = re.findall('Name server(.+)Registrant Company Name', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'pl':
                pre_nameservers = re.findall('nameservers:(.+)last modified:', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'rs':
                pre_nameservers = re.findall('DNS:(.+)DNSSEC signed:', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain in ['sa', 'sg']:
                pre_nameservers = re.findall('Name Servers:(.+)DNSSEC:', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'sm':
                pre_nameservers = re.findall('DNS Servers:(.+)', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'tm':
                pre_nameservers = re.findall('NS 1   :(.+)Owner Name', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'tn':
                pre_nameservers = re.findall('DNS servers(.+)', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'tr':
                pre_nameservers = re.findall('Domain Servers:(.+)\*\* Additional Info:', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'tw':
                pre_nameservers = re.findall('Domain servers in listed order:(.+)Registration Service Provider:', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'uk':
                pre_nameservers = re.findall('Name servers:(.+)WHOIS lookup made at', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'am':
                pre_nameservers = re.findall('DNS servers:(.+)Registered:', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'co.pl':
                pre_nameservers = re.findall('Nameservers:(.+)Holder data:', raw_nameservers, re.DOTALL | re.IGNORECASE)
            elif tld_domain == 'eu':
                pre_nameservers = re.findall('Name servers:(.+)Please visit', raw_nameservers, re.DOTALL | re.IGNORECASE)
            
            if pre_nameservers:
                arr_reformat = re.findall('(.+)\n', pre_nameservers[0], re.IGNORECASE)
                for item_reformat in arr_reformat:
                    item_reformat = item_reformat.replace(' ', '')
                    if item_reformat:
                        # 'im' ['ns1.google.com.', 'NameServer:ns2.google.com.', 'NameServer:ns3.google.com.', 'NameServer:ns4.google.com.']'
                        if tld_domain == 'im':
                            item_reformat = item_reformat.replace('NameServer:', '')
                        elif tld_domain in ['mx', 'rs']:
                            item_reformat = item_reformat.replace('DNS:', '')
                        elif tld_domain in ['nc', 'pf', 'tm', 'tn', 'co.pl']:
                            spl_irf = item_reformat.split(':')
                            if len(spl_irf) == 2:
                                item_reformat = spl_irf[1]
                        elif tld_domain == 'pl':
                            if item_reformat.find('created:') > -1:
                                continue
                        
                        nameservers.append([item_reformat, item_reformat])
                    del item_reformat
                del arr_reformat
            del pre_nameservers
        
        if not nameservers:
            nameservers = re.findall('(Name Server:|Nserver:|nserver:|Name servers:|'
                                        'nserver..............:|Hostname:|nserver............:|'
                                        'Serveur de noms:|nameserver:|\[Name Server\]|'
                                        'Host Name                :)\s+(.+)', raw_nameservers, re.IGNORECASE)
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