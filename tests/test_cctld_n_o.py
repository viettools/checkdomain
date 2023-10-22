# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestNO(unittest.TestCase):
    def test_NA(self):
        pass
    
    def test_NC(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "whois.nc"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for whois.nc')
        self.assertEqual(data['parse']['registrar'] or False, 'NONE', 'whois.nc: NONE')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'whois.nc ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2007-07-05T08:46:31.000Z', 'whois.nc:2007-07-05T08:46:31.000Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'whois.nc: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'whois.nc: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'whois.nc: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'whois.nc: NS must be a value!')
    
    def test_NF(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.nf"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.nf')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.nf: MarkMonitor')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.nf: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2005-11-27T11:00:00.0Z', 'google.nf: 2005-11-27T11:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.nf: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.nf: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.nf: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.nf: NS must be a value!')
    
    def test_NG(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ng"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ng')
        self.assertEqual(data['parse']['registrar'] or False, 'markmonitor', 'google.ng: markmonitor')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.ng: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2011-01-19T13:24:01.299Z', 'google.ng: 2011-01-19T13:24:01.299Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ng: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ng: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ng: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ng: NS must be a value!')
        
    def test_NL(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.nl"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.nl')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.nl: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.nl ?')
        self.assertEqual(data['parse']['creation_date'] or False, '1999-05-27', 'google.nl: 1999-05-27?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.nl: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.nl: Expiry Date must not be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.nl: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.nl: NS must be a value!')

    def test_NO(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.no"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.no')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.no ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.no ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2001-02-26', 'google.no: 2001-02-26?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.no: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.no: Expiry Date must not be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.no: Domain status must not be a value!')
        self.assertEqual(len(data['parse']['nameservers'] or []), 0, 'google.no: NS must not be a value!')

    def test_NU(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.nu"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.nu')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc', 'google.nu: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.nu ?')
        self.assertEqual(data['parse']['creation_date'] or False, '1999-06-07', 'google.nu: 1999-06-07?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.nu: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.nu: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.nu: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.nu: NS must be a value!')

    def test_NZ(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "apple.nz"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for apple.nz')
        self.assertEqual(data['parse']['registrar'] or False, 'Nom-IQ Ltd, dba Com Laude', 'apple.nz: Nom-IQ Ltd, dba Com Laude')
        self.assertEqual(data['parse']['registrar_url'] or False, 'www.comlaude.com', 'apple.nz: www.comlaude.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2017-10-31T11:37:27Z', 'apple.nz: 2017-10-31T11:37:27Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'apple.nz: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'apple.nz: Expiry Date must nit be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'apple.nz: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'apple.nz: NS must be a value!')

    def test_OM(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "apple.om"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for apple.om')
        self.assertEqual(data['parse']['registrar'] or False, 'Abu Ghazaleh Intellectual Property (AGIP)', 'apple.om: Abu Ghazaleh Intellectual Property (AGIP)')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'apple.om ?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'apple.om ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'apple.om: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'apple.om: Expiry Date must not be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'apple.om: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'apple.om: NS must be a value!')
    
if __name__ == '__main__':
    unittest.main()