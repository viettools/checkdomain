# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestZA(unittest.TestCase):
    def test_ac_za(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "uct.ac.za"},
        )
        data = json.loads(response.content)
        
        if not data['status']:
            print('Please check .ac.za whois server!')
            return
        
        self.assertEqual(data['parse']['registrar'], 'TENET')
        self.assertEqual(data['parse']['registrar_url'], 'https://www.tenet.ac.za/')
        self.assertGreater(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)
        
        self.assertEqual(data['parse']['creation_date'], '2002-06-21T14:22:15Z')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)
    
    def test_co_za(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.co.za"},
        )
        data = json.loads(response.content)
        
        if not data['status']:
            print('Please check .co.za whois server!')
            return
        
        self.assertEqual(data['parse']['registrar'], 'MarkMonitor')
        self.assertEqual(data['parse']['registrar_url'], 'https://www.markmonitor.com/')
        self.assertGreater(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)
        
        self.assertEqual(data['parse']['creation_date'], '2001-06-25T20:37:59Z')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)

    def test_net_za(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "asap.net.za"},
        )
        data = json.loads(response.content)
        
        if not data['status']:
            print('Please check .net.za whois server!')
            return
        
        self.assertEqual(data['parse']['registrar'], 'ASAP')
        self.assertEqual(data['parse']['registrar_url'], 'http://www.asap.co.za')
        self.assertGreater(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)
        
        self.assertEqual(data['parse']['creation_date'], '2015-12-18T11:22:08Z')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)

    def test_org_za(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "icrc.org.za"},
        )
        data = json.loads(response.content)
        
        if not data['status']:
            print('Please check .org.za whois server!')
            return
        
        self.assertEqual(data['parse']['registrar'], 'AmpleHosting')
        self.assertEqual(data['parse']['registrar_url'], 'www.greycell.co.za')
        self.assertGreater(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)
        
        self.assertEqual(data['parse']['creation_date'], '2011-04-05T09:59:46Z')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)

    def test_web_za(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "virtual.web.za"},
        )
        data = json.loads(response.content)
        
        if not data['status']:
            print('Please check .web.za whois server!')
            return
        
        self.assertEqual(data['parse']['registrar'], 'Posix Systems')
        self.assertEqual(data['parse']['registrar_url'], 'https://vweb.co.za')
        self.assertGreater(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)
        
        self.assertEqual(data['parse']['creation_date'], '1998-11-20T07:21:02Z')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)

    def test_gov_za(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "dirco.gov.za"},
        )
        data = json.loads(response.content)
        
        if not data['status']:
            print('Please check .gov.za whois server!')
            return
        
        self.assertEqual(data['parse']['registrar'], '')
        self.assertEqual(data['parse']['registrar_url'], '')
        self.assertEqual(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)
        
        self.assertEqual(data['parse']['creation_date'], '')
        self.assertEqual(len(data['parse']['updated_date']), 0)
        self.assertEqual(len(data['parse']['expiry_date']), 0)

if __name__ == '__main__':
    unittest.main()