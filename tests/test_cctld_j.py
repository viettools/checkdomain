# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestJ(unittest.TestCase):
    def test_JE(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.je"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.je')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc. (http://www.markmonitor.com)', 'google.je: MarkMonitor Inc. (http://www.markmonitor.com)?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.je ?')
        self.assertEqual(data['parse']['creation_date'] or False, '31st October 2002 at 00:00:00.000', 'google.jp: 31st October 2002 at 00:00:00.000?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.jp: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.jp: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.jp: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.jp: NS must be a value!')
    
    def test_JP(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.jp"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.jp')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.jp ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.jp ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2005/05/30', 'google.jp: 2005/05/30?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.jp: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.jp: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.jp: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.jp: NS must be a value!')
        
if __name__ == '__main__':
    unittest.main()