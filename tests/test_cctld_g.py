# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestG(unittest.TestCase):
    def test_GA(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ga"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ga')
        self.assertEqual(data['parse']['registrar'] or False, 'MARKMONITOR Inc.', 'google.ga: MARKMONITOR Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.ga ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2023-06-06T19:15:12.718385Z', 'google.ga: 2023-06-06T19:15:12.718385Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ga: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ga: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ga: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ga: NS must be a value!')

    def test_GD(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.gd"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.gd')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor, Inc.', 'google.gd: MarkMonitor, Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.gd ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2006-12-11T00:00:00.0Z', 'google.gd: 2006-12-11T00:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.gd: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.gd: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.gd: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.gd: NS must be a value!')

    def test_GE(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ge"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ge')
        self.assertEqual(data['parse']['registrar'] or False, 'proservice ltd', 'google.ge: proservice ltd?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.ge ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2006-07-28', 'google.ge: 2006-07-28?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.ge: Updated Date must not be a value')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ge: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ge: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ge: NS must be a value!')

    def test_GF(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.gf"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.gf')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.gf: ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.gf ?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'google.gf ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.gf: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.gf: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.gf: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.gf: NS must be a value!')

    def test_GG(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.gg"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.gg')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc. (http://www.markmonitor.com)', 'google.gg: MarkMonitor Inc. (http://www.markmonitor.com)?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.gg ?')
        self.assertEqual(data['parse']['creation_date'] or False, '30th April 2003 at 00:00:00.000', 'google.gg: 30th April 2003 at 00:00:00.000?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.gg: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.gg: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.gg: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.gg: NS must be a value!')

    def test_GH(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.com.gh"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.com.gh')
        self.assertEqual(data['parse']['registrar'] or False, 'Ghana Dot Com', 'google.com.gh: Ghana Dot Com?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.com.gh ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2007-01-08T05:00:00.000Z', 'google.com.gh: 2007-01-08T05:00:00.000Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.com.gh: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.com.gh: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.com.gh: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.com.gh: NS must be a value!')

    def test_GI(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "apple.gi"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for apple.gi')
        self.assertEqual(data['parse']['registrar'] or False, 'GibNet Registrar', 'apple.gi: GibNet Registrar?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'apple.gi ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2009-10-19T13:55:20Z', 'apple.gi: 2009-10-19T13:55:20Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'apple.gi: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'apple.gi: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'apple.gi: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'apple.gi: NS must be a value!')

    def test_GL(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.gl"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.gl')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor, Inc.', 'google.gl: MarkMonitor, Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.gl ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2003-03-11T03:00:00.0Z', 'google.gl: 2003-03-11T03:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.gl: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.gl: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.gl: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.gl: NS must be a value!')

    # def test_GQ(self):
    #     pass

    def test_GS(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.gs"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.gs')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.gs: MarkMonitor?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.gs: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2004-07-08T12:00:00.0Z', 'google.gs: 2004-07-08T12:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.gs: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.gs: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.gs: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.gs: NS must be a value!')

    def test_GY(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.gy"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.gy')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.gy: MarkMonitor?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.gy: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2008-05-12T17:56:23.90Z', 'google.gy: 2008-05-12T17:56:23.90Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.gy: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.gy: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.gy: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.gy: NS must be a value!')

if __name__ == '__main__':
    unittest.main()