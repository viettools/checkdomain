# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestI(unittest.TestCase):
    def test_ID(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.id"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.id')
        self.assertEqual(data['parse']['registrar'] or False, 'Digital Registra', 'google.id: Digital Registra')
        self.assertEqual(data['parse']['registrar_url'] or False, 'www.digitalregistra.co.id', 'google.id: www.digitalregistra.co.id?')
        self.assertEqual(data['parse']['creation_date'] or False,'2014-04-17 10:09:04', 'google.id: 2014-04-17 10:09:04?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.id: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.id: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.id: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.id: NS must be a value!')
        
    def test_IE(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ie"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ie')
        self.assertEqual(data['parse']['registrar'] or False, 'Markmonitor Inc', 'google.ie: Markmonitor Inc')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.eMarkmonitor.com', 'google.ie: http://www.eMarkmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2002-03-21T00:00:00Z', 'google.ie: 2002-03-21T00:00:00Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ie: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ie: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ie: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ie: NS must be a value!')
        
    def test_IL(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.co.il"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.co.il')
        self.assertEqual(data['parse']['registrar'] or False, 'Domain The Net Technologies Ltd', 'google.co.il: Domain The Net Technologies Ltd')
        self.assertEqual(data['parse']['registrar_url'] or False, 'https://www.domainthenet.com', 'google.co.il: https://www.domainthenet.com?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'google.co.il: ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.co.il: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.co.il: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.co.il: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.co.il: NS must be a value!')
    
    def test_IM(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.im"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.im')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.im ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.im ?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'google.im ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.im !')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.im: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.im !')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.im: NS must be a value!')
        
    def test_IN(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.in"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.in')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.in: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.in: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2005-02-14T20:35:14Z', 'google.in: 2005-02-14T20:35:14Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.in: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.in: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.in: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.in: NS must be a value!')
        
    def test_IO(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.io"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.io')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.io: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.io: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2002-10-01T01:00:00Z', 'google.io: 2002-10-01T01:00:00Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.io: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.io: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.io: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.io: NS must be a value!')
        
    def test_IR(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ir"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ir')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.ir ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.ir ?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'google.ir ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.ir !')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.ir !')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.ir !')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ir: NS must be a value!')
        
    def test_IS(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.is"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.is')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.is ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.is ?')
        self.assertEqual(data['parse']['creation_date'] or False, 'May 22 2002', 'google.is: May 22 2002?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.is !')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.is: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.is !')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.is: NS must be a value!')
        
    def test_IT(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.it"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.it')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor International Limited', 'google.it: MarkMonitor International Limited')
        self.assertEqual(data['parse']['registrar_url'] or False, 'https://www.markmonitor.com/', 'google.it: https://www.markmonitor.com/?')
        self.assertEqual(data['parse']['creation_date'] or False, '1999-12-10 00:00:00', 'google.it: 1999-12-10 00:00:00?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.it: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.it: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.it: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.it: NS must be a value!')
        
if __name__ == '__main__':
    unittest.main()