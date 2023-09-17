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
        self.assertTrue(data['status'], 'Please check connection for google.ee')
        self.assertEqual(data['parse']['registrar'] or False, 'Zone Media OÜ', 'google.ee: Zone Media OÜ?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.zone.ee', 'google.ee: http://www.zone.ee?')
        self.assertEqual(data['parse']['creation_date'] or False, '2010-07-04 04:34:46 +03:00', 'google.ee: 2010-07-04 04:34:46 +03:00?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ee: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ee: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ee: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ee: NS must be a value!')
        
    def test_ET(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.et"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.dk')
        self.assertEqual(data['parse']['registrar'] or False, 'ethio telecom', 'google.dk: ethio telecom?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'https://www.ethiotelecom.et', 'google.dk: https://www.ethiotelecom.et?')
        self.assertEqual(data['parse']['creation_date'] or False, '2015-09-07T09:28:11Z', 'google.dk: 2015-09-07T09:28:11Z0?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.dk: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.dk: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.dk: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.dk: NS must be a value!')
    
    def test_EU(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.eu"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.eu')
        self.assertEqual(data['parse']['registrar'] or False, 'Name: MarkMonitor Inc.', 'google.eu: Name: MarkMonitor Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'https://www.markmonitor.com/', 'google.eu: https://www.markmonitor.com/?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'google.eu: ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.eu: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.eu: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.eu: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.eu: NS must be a value!')
    
if __name__ == '__main__':
    unittest.main()