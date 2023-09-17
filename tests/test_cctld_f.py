# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestF(unittest.TestCase):
    
    def test_FI(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.fi"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.fi')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.fi: MarkMonitor Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'www.markmonitor.com', 'google.fi: www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '30.6.2006 00:00:00', 'google.fi: 30.6.2006 00:00:00?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.fi: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.fi: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.fi: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.fi: NS must be a value!')
        
    def test_FJ(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.com.fj"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.com.fj')
        self.assertEqual(data['parse']['registrar'] or False, 'USP Registrar', 'google.com.fj: USP Registrar?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'https://www.domains.fj', 'google.com.fj: https://www.domains.fj?')
        self.assertEqual(data['parse']['creation_date'] or False, '2003-04-27T12:00:00.0Z', 'google.com.fj: 2003-04-27T12:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.com.fj: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.com.fj: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.com.fj: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.com.fj: NS must be a value!')
    
    def test_FM(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.fm"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.fm')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor, Inc.', 'google.fm: MarkMonitor, Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.fm: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2000-09-05T23:59:59.0Z', 'google.fm: 2000-09-05T23:59:59.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.fm: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.fm: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.fm: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.fm: NS must be a value!')
        
    def test_FO(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.fo"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.fo')
        self.assertEqual(data['parse']['registrar'] or False, 'FO Umsitingin', 'google.fo: FO Umsitingin?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'https://www.økisnavn.fo', 'google.fo: https://www.økisnavn.fo?')
        self.assertEqual(data['parse']['creation_date'] or False, '2011-07-22T22:38:12.0Z', 'google.fo: 2011-07-22T22:38:12.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.fo: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.fo: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.fo: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.fo: NS must be a value!')
        
    def test_FR(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.fr"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.fr')
        self.assertEqual(data['parse']['registrar'] or False, 'MARKMONITOR Inc.', 'google.fr: MARKMONITOR Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.fr: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2000-07-26T22:00:00Z', 'google.fr: 2000-07-26T22:00:00Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.fr: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.fr: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.fr: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.fr: NS must be a value!')
    
if __name__ == '__main__':
    unittest.main()