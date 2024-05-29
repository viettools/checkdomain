# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestE(unittest.TestCase):
    
    def test_EE(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ee"},
        )
        data = json.loads(response.content)
        if not data['status']:
            print('Please check .ee whois server!')
            return

        self.assertEqual(data['parse']['registrar'], 'Zone Media OÜ')
        self.assertEqual(data['parse']['registrar_url'], 'http://www.zone.ee')
        self.assertGreater(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)

        self.assertEqual(data['parse']['creation_date'], '2010-07-04 04:34:46 +03:00')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)
        
    def test_ET(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.et"},
        )
        data = json.loads(response.content)
        if not data['status']:
            print('Please check .et whois server!')
            return

        self.assertEqual(data['parse']['registrar'], 'ethio telecom')
        self.assertEqual(data['parse']['registrar_url'], 'https://www.ethiotelecom.et')
        self.assertGreater(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)

        self.assertEqual(data['parse']['creation_date'], '2015-09-07T09:28:11Z')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)
    
    def test_EU(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.eu"},
        )
        data = json.loads(response.content)
        if not data['status']:
            print('Please check .eu whois server!')
            return

        self.assertEqual(data['parse']['registrar'], 'Markmonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'], 'https://www.markmonitor.com/')
        self.assertEqual(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)

        self.assertEqual(data['parse']['creation_date'], '')
        self.assertEqual(len(data['parse']['updated_date']), 0)
        self.assertEqual(len(data['parse']['expiry_date']), 0)
    
if __name__ == '__main__':
    unittest.main()