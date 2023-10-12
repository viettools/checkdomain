# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestK(unittest.TestCase):
    def test_KE(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ke"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ke')
        self.assertEqual(data['parse']['registrar'] or False, 'Afriregister Limited', 'google.ke: Afriregister Limited')
        self.assertEqual(data['parse']['registrar_url'] or False, 'RegistrarURL', 'google.ke: RegistrarURL?')
        self.assertEqual(data['parse']['creation_date'] or False, '2018-01-10T11:43:08.531Z', 'google.ke: 2018-01-10T11:43:08.531Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ke: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ke: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ke: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ke: NS must be a value!')
        
    def test_KG(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.kg"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.kg')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.kg ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.kg ?')
        self.assertEqual(data['parse']['creation_date'] or False, 'Tue Feb 10 09:42:42 2004', 'google.kg: Tue Feb 10 09:42:42 2004?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.kg: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.kg: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.kg: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.kg: NS must be a value!')
        
    def test_KI(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ki"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ki')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.ki: MarkMonitor')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.ki: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2006-05-15T12:00:00.0Z', 'google.ki: 2006-05-15T12:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ki: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ki: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ki: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ki: NS must be a value!')
    
    def test_KN(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.kn"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.kn')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.kn: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.kn ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2011-04-04T04:00:00.0Z', 'google.kn: 2011-04-04T04:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.kn: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.kn: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.kn: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.kn: NS must be a value!')
        
    def test_KR(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.kr"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.kr')
        self.assertEqual(data['parse']['registrar'] or False, 'Whois Corp.(http://whois.co.kr)', 'google.kr: Whois Corp.(http://whois.co.kr)')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.kr ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2007. 03. 02.', 'google.kr: 2007. 03. 02.?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.kr: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.kr: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.kr: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.kr: NS must be a value!')
        
    def test_KW(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.com.kw"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.com.kw')
        self.assertEqual(data['parse']['registrar'] or False, 'Solutions by STC', 'google.com.kw: Solutions by STC')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.com.kw ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2007-03-17T00:00:00.0Z', 'google.com.kw: 2007-03-17T00:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.com.kw: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.com.kw: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.com.kw: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.com.kw: NS must be a value!')
        
    def test_KY(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ky"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ky')
        self.assertEqual(data['parse']['registrar'] or False, 'Uniregistrar Corp', 'google.ky: Uniregistrar Corp')
        self.assertEqual(data['parse']['registrar_url'] or False, 'uniregistrar.com', 'google.ky: uniregistrar.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2015-03-03T15:19:12.167Z', 'google.ky: 2015-03-03T15:19:12.167Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ky: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ky: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ky: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ky: NS must be a value!')
        
    def test_KZ(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.kz"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.kz')
        self.assertEqual(data['parse']['registrar'] or False, 'KAZNIC', 'google.kz: KAZNIC')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.kz ?')
        self.assertEqual(data['parse']['creation_date'] or False, '1999-06-07 20:01:43 (GMT+0:00)', 'google.kz: 1999-06-07 20:01:43 (GMT+0:00)?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.kz: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.kz: Expiry Date must not be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.kz: Domain status must be a value!')
        self.assertEqual(len(data['parse']['nameservers'] or []), 0, 'google.kz: NS must not be a value!')
        
if __name__ == '__main__':
    unittest.main()