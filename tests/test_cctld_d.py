# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestD(unittest.TestCase):
    
    def test_DE(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.de"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.de')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.de: ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.de: ?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'google.de: ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.de: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.de: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.de: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.de: NS must be a value!')
        
    def test_DK(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.dk"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.dk')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.dk: MarkMonitor Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.dk: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '1999-01-10', 'google.dk: 1999-01-10?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.dk: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.dk: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.dk: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.dk: NS must be a value!')
    
    def test_DM(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.dm"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.dm')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.dm: MarkMonitor Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.dm: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2004-08-23T23:00:00.000Z', 'google.dm: 2004-08-23T23:00:00.000Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.dm: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.dm: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.dm: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.dm: NS must be a value!')
        
    def test_DO(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.do"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.do')
        self.assertEqual(data['parse']['registrar'] or False, 'Registrar NIC .DO (midominio.do)', 'google.do: Registrar NIC .DO (midominio.do)?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.do: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2010-03-08T04:00:00.0Z', 'google.do: 2010-03-08T04:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.do: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.do: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.do: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.do: NS must be a value!')
    
if __name__ == '__main__':
    unittest.main()