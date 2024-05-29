# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestUK(unittest.TestCase):
    def test_ac_uk(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "core.ac.uk"},
        )
        data = json.loads(response.content)
        
        if not data['status']:
            print('Please check .ac.uk whois server!')
            return
        
        self.assertEqual(data['parse']['registrar'], '')
        self.assertEqual(data['parse']['registrar_url'], '')
        self.assertEqual(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)
        
        self.assertEqual(data['parse']['creation_date'], 'Monday 19th January 2015')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)

    def test_gov_uk(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "tfl.gov.uk"},
        )
        data = json.loads(response.content)
        
        if not data['status']:
            print('Please check .gov_uk whois server!')
            return
        
        self.assertEqual(data['parse']['registrar'], '')
        self.assertEqual(data['parse']['registrar_url'], '')
        self.assertEqual(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)
        
        self.assertEqual(data['parse']['creation_date'], 'Wednesday 17th September 2003')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)
    
if __name__ == '__main__':
    unittest.main()