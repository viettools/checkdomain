# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestH(unittest.TestCase):
    def test_HK(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.hk"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.hk')
        self.assertEqual(data['parse']['registrar'] or False, 'MARKMONITOR INC.', 'google.hk: MARKMONITOR INC.?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.hk ?')
        self.assertEqual(data['parse']['creation_date'] or False, '06-04-2004', 'google.hk: 06-04-2004?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.hk: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.hk: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.hk: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.hk: NS must be a value!')

    def test_HN(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.hn"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.hn')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.hn: MarkMonitor?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.hn: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2003-03-07T05:00:00.0Z', 'google.hn: 2003-03-07T05:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.hn: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.hn: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.hn: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.hn: NS must be a value!')

    def test_HR(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.hr"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.hr')
        self.assertEqual(data['parse']['registrar'] or False, 'Sayber d.o.o.', 'google.hr: Sayber d.o.o.?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://whois.dns.hr', 'google.hr: http://whois.dns.hr?')
        self.assertEqual(data['parse']['creation_date'] or False, '2011-09-20T22:00:00Z', 'google.hr: 2011-09-20T22:00:00Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.hr: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.hr: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.hr: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.hr: NS must be a value!')

    def test_HT(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ht"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ht')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.ht: MarkMonitor?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.ht ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2004-06-17T23:00:00.0Z', 'google.ht: 2004-06-17T23:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ht: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ht: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ht: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ht: NS must be a value!')

    def test_HU(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.hu"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.hu')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.hu ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.hu ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2000-03-25 23:20:39', 'google.hu: 2000-03-25 23:20:39?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.hu: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.hu: Expiry Date must not be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.hu: Domain status must not be a value!')
        self.assertEqual(len(data['parse']['nameservers'] or []), 0, 'google.hu: NS must not be a value!')

if __name__ == '__main__':
    unittest.main()