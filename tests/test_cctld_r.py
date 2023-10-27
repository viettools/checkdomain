# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestR(unittest.TestCase):
    def test_RE(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.re"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.re')
        self.assertEqual(data['parse']['registrar'] or False, 'MARKMONITOR Inc.', 'google.re: MARKMONITOR Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.re: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2008-11-19T09:40:52Z', 'google.re: 2008-11-19T09:40:52Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.re: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.re: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.re: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.re: NS must be a value!')

    def test_RO(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ro"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ro')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.ro: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'www.markmonitor.com', 'google.ro: www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2000-07-17', 'google.ro: 2000-07-17?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.ro: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ro: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ro: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ro: NS must be a value!')
        
    def test_RS(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.rs"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.rs')
        self.assertEqual(data['parse']['registrar'] or False, 'Webglobe d.o.o.', 'google.rs: Webglobe d.o.o.')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.rs: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '10.03.2008 12:31:19', 'google.rs: 10.03.2008 12:31:19?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.rs: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.rs: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.rs: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.rs: NS must be a value!')

    def test_RU(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ru"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ru')
        self.assertEqual(data['parse']['registrar'] or False, 'RU-CENTER-RU', 'google.ru: RU-CENTER-RU')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.ru: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2004-03-03T21:00:00Z', 'google.ru: 2004-03-03T21:00:00Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.ru: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ru: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.ru: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ru: NS must be a value!')


    def test_RW(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.rw"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.rw')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.rw: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.rw: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '1999-05-22T22:00:00.0Z', 'google.rw: 1999-05-22T22:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.rw: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.rw: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.rw: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.rw: NS must be a value!')
    
if __name__ == '__main__':
    unittest.main()