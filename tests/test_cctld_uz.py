# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestUZ(unittest.TestCase):
    def test_co_uz(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.co.uz"},
        )
        data = json.loads(response.content)
        
        if not data['status']:
            print('Please check .co.uz whois server!')
            return
        
        self.assertEqual(data['parse']['registrar'], 'Euracom Group GmbH')
        self.assertEqual(data['parse']['registrar_url'], '')
        self.assertGreater(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)
        
        self.assertEqual(data['parse']['creation_date'], '2003-03-11 13:35:24')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)

    def test_com_uz(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.com.uz"},
        )
        data = json.loads(response.content)
        
        if not data['status']:
            print('Please check .com.uz whois server!')
            return
        
        self.assertEqual(data['parse']['registrar'], 'Euracom Group GmbH')
        self.assertEqual(data['parse']['registrar_url'], '')
        self.assertGreater(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)
        
        self.assertEqual(data['parse']['creation_date'], '2003-03-14 13:35:33')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)

    def test_org_uz(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "iso.org.uz"},
        )
        data = json.loads(response.content)
        
        if not data['status']:
            print('Please check .org.uz whois server!')
            return
        
        self.assertEqual(data['parse']['registrar'], 'Euracom Group GmbH')
        self.assertEqual(data['parse']['registrar_url'], '')
        self.assertGreater(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)
        
        self.assertEqual(data['parse']['creation_date'], '2023-10-20 00:05:34')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)
    
if __name__ == '__main__':
    unittest.main()