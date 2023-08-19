# -*- coding: utf-8 -*-
# https://check.rs/

import socket
import re
from tld import get_tld

class Whois:

    def __init__(self, domain, tld_domain):
        self.domain = domain
        self.timeout = 60
        self.hostname = 'whois.iana.org'
        self.tld_domain = tld_domain

    def set_timeout_connect(self, timeout):
        self.timeout = timeout
        
    def set_hostname(self, hostname):
        self.hostname = hostname

    '''
        Connect Port 43 - Whois Server
    '''

    def _connect_port(self):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(self.timeout)

        if self.hostname == 'whois.iana.org':
            self.domain = '.' + self.tld_domain
        result = False
        
        try:
            sk.connect((self.hostname, 43))
            query = self.domain

            if self.hostname != 'whois.iana.org':
                # DE + DK + JP --> args
                if self.tld_domain == 'dk':
                    query = ' --show-handles ' + self.domain
                elif self.tld_domain == 'de':
                    query = '-T dn,ace -C UTF-8 ' + self.domain
                elif self.tld_domain == 'jp':
                    query = self.domain + '/e'
            sk.send(bytes(query, 'utf-8') + b'\r\n')

            response = b''
            try:
                while True:
                    data = sk.recv(4096)
                    response += data
                    if not data:
                        break
            except:
                pass
            
            sk.close()
            result = response.decode('utf-8', 'ignore')

        except socket.error as ex:
            sk.close()

        return result
    
    def get_data(self):
        result = {'status': False, 'result': False}
        data = self._connect_port()
        if data:
            result = {'status': True, 'result': data}
        return result