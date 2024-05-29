# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestSLD(unittest.TestCase):
    
    def test_CO_CA(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "ttmc.co.ca"},
        )
        data = json.loads(response.content)
        if not data['status']:
            print('Please check .co.ca whois server!')
            return
        
        self.assertEqual(data['parse']['registrar'], 'Reg.Ca (RegCA Enterprises Inc.)')
        self.assertEqual(data['parse']['registrar_url'], 'http://www.reg.ca')
        self.assertEqual(len(data['parse']['domain_status']), 0)
        self.assertEqual(len(data['parse']['nameservers']), 0)
        
        self.assertEqual(data['parse']['creation_date'], '2023-09-03 06:46:01')
        self.assertEqual(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)
        
    def test_CO_PL(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "ankor.co.pl"},
        )
        data = json.loads(response.content)
        if not data['status']:
            print('Please check .co.pl whois server!')
            return
        
        self.assertEqual(data['parse']['registrar'], '')
        self.assertEqual(data['parse']['registrar_url'], '')
        self.assertGreater(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)
        
        self.assertEqual(data['parse']['creation_date'], '2012.02.23 16:50:02')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)
        
if __name__ == '__main__':
    unittest.main()