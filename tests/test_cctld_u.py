# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestU(unittest.TestCase):
    def test_UA(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ua"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ua')
        self.assertEqual(data['parse']['registrar'] or False, 'ua.markmonitor', 'google.ua: ua.markmonitor')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://markmonitor.com', 'google.ua: http://markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2011-07-21 18:03:50+03', 'google.ua: 2011-07-21 18:03:50+03?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ua: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ua: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ua: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ua: NS must be a value!')

    def test_UG(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ug"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ug')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.ug ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.ug: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2004-08-03', 'google.ug: 2004-08-03?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ug: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ug: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ug: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ug: NS must be a value!')       

    def test_UK(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.uk"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.uk')
        self.assertEqual(data['parse']['registrar'] or False, 'Markmonitor Inc. [Tag = MARKMONITOR]', 'google.uk: Markmonitor Inc. [Tag = MARKMONITOR]')
        self.assertEqual(data['parse']['registrar_url'] or False, 'https://www.markmonitor.com', 'google.uk: https://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '11-Jun-2014', 'google.uk: 11-Jun-2014?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.uk: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.uk: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.uk: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.uk: NS must be a value!')

    def testUS(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.us"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.us')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor, Inc.', 'google.us: MarkMonitor, Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'www.markmonitor.com', 'google.us: www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2002-04-19T23:16:01Z', 'google.us: 2002-04-19T23:16:01Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.us: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.us: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.us: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.us: NS must be a value!')
        
    def test_UZ(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.uz"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.uz')
        self.assertEqual(data['parse']['registrar'] or False, 'Tomas', 'google.uz: Tomas')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.cctld.uz/', 'google.uz: http://www.cctld.uz/?')
        self.assertEqual(data['parse']['creation_date'] or False, '13-Apr-2006', 'google.uz: 13-Apr-2006?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.uz: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.uz: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.uz: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.uz: NS must be a value!')
    
if __name__ == '__main__':
    unittest.main()