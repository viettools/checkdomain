# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestL(unittest.TestCase):
    def test_LA(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.la"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.la')
        self.assertEqual(data['parse']['registrar'] or False, 'TLD Registrar Solutions Ltd', 'google.la: TLD Registrar Solutions Ltd')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.la ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2002-07-18T01:00:00.0Z', 'google.la: 2002-07-18T01:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.la: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.la: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.la: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.la: NS must be a value!')
        
    def test_LB(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.com.lb"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.com.lb')
        self.assertEqual(data['parse']['registrar'] or False, 'AGIP', 'google.com.lb: AGIP?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'https://www.tagidomains.com/tagidomains', 'google.com.lb: https://www.tagidomains.com/tagidomains?')
        self.assertEqual(data['parse']['creation_date'] or False, '2014-05-15T00:00:00.0Z', 'google.com.lb: 2014-05-15T00:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.com.lb: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.com.lb: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.com.lb: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.com.lb: NS must be a value!')

    def test_LC(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.lc"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.lc')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.lc: MarkMonitor Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.lc: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2007-05-30T00:00:00Z', 'google.lc: 2007-05-30T00:00:00Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.lc: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.lc: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.lc: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.lc: NS must be a value!')
        
    def test_LS(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ls"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ls')
        self.assertEqual(data['parse']['registrar'] or False, 'REG-ZEECOM', 'google.ls: REG-ZEECOM?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.ls ?')
        self.assertEqual(data['parse']['creation_date'] or False, '15.03.2019 04:46:36', 'google.ls: 15.03.2019 04:46:36?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ls: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ls: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.ls: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ls: NS must be a value!')

    def test_LT(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.lt"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.lt')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor, Inc.', 'google.lt: MarkMonitor, Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.lt: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2018-12-07', 'google.lt: 2018-12-07?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.lt: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.lt: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.lt: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.lt: NS must be a value!')

    def test_LU(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.lu"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.lu')
        self.assertEqual(data['parse']['registrar'] or False, 'Markmonitor', 'google.lu: Markmonitor?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com/', 'google.lu: http://www.markmonitor.com/?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'google.lu ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.lu: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.lu: Expiry Date must not be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.lu: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.lu: NS must be a value!')
        
    def test_LU(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.lv"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.lv')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.lv: MarkMonitor Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.lv ?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'google.lv ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.lv: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.lv: Expiry Date must not be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.lv: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.lv: NS must be a value!')

    def test_LY(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ly"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ly')
        self.assertEqual(data['parse']['registrar'] or False, 'Libyan Spider Network (int)', 'google.ly: Libyan Spider Network (int)?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.ly ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2007-10-02T22:00:00.0Z', 'google.ly: 2007-10-02T22:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ly: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ly: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ly: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ly: NS must be a value!')
    
if __name__ == '__main__':
    unittest.main()