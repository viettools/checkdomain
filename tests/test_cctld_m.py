# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestM(unittest.TestCase):
    def test_MA(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ma"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ma')
        self.assertEqual(data['parse']['registrar'] or False, 'GENIOUS COMMUNICATION', 'google.ma: GENIOUS COMMUNICATION')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.ma ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2009-03-24T00:00:00.000Z', 'google.ma: 2009-03-24T00:00:00.000Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ma: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ma: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ma: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ma: NS must be a value!')

    def test_MD(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.md"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.md')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.md ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.md ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2006-05-02', 'google.md: 2006-05-02?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.md: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.md: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.md: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.md: NS must be a value!')
        
    def test_ME(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.me"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.me')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.me: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.me: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2008-06-13T17:17:40Z', 'google.me: 2008-06-13T17:17:40Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.me: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.me: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.me: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.me: NS must be a value!')
        
    def test_MG(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.mg"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.mg')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.mg: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.mg ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2009-06-18T08:38:20.671Z', 'google.mg: 2009-06-18T08:38:20.671Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.mg: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.mg: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.mg: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.mg: NS must be a value!')
        
    def test_MK(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.mk"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.mk')
        self.assertEqual(data['parse']['registrar'] or False, 'UNET-REG', 'google.mk: UNET-REG')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.mk ?')
        self.assertEqual(data['parse']['creation_date'] or False, '13.05.2008 14:00:00', 'google.mk: 13.05.2008 14:00:00?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.mk: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.mk: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.mk: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.mk: NS must be a value!')
    
    def test_ML(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "apple.ml"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for apple.ml')
        self.assertEqual(data['parse']['registrar'] or False, 'CSC Corporate Domains, Inc.', 'apple.ml: CSC Corporate Domains, Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'apple.ml ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2023-07-17T00:00:00.0Z', 'apple.ml: 2023-07-17T00:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'apple.mlk: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'apple.ml: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'apple.ml: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'apple.ml: NS must be a value!')
    
    def test_MN(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.mn"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.mn')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.mn: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.mn: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2003-04-07T00:00:00Z', 'google.mn: 2003-04-07T00:00:00Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.mn: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.mn: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.mn: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.mn: NS must be a value!')
        
    def test_MO(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "monic.mo"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for monic.mo')
        self.assertEqual(data['parse']['registrar'] or False, False, 'monic.mo ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'monic.mo ?')
        self.assertEqual(data['parse']['creation_date'] or False, '1993-01-01 08:00:00', 'monic.mo: 1993-01-01 08:00:00?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'monic.mo: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'monic.mo: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'monic.mo: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'monic.mo: NS must be a value!')

    def test_MQ(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.mq"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.mq')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.mq ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.mq ?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'google.mq ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.mq: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.mq: Expiry Date must not be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.mq: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.mq: NS must be a value!')
    
    def test_MR(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "nic.mr"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for nic.mr')
        self.assertEqual(data['parse']['registrar'] or False, 'NIC-Mauritanie', 'nic.mr: NIC-Mauritanie')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'nic.mr ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2017-08-10T00:00:00.0Z', 'nic.mr: 2017-08-10T00:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'nic.mr: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'nic.mr: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'nic.mr: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'nic.mr: NS must be a value!')
    
    def test_MS(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ms"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ms')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.ms: MarkMonitor')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.ms ?')
        self.assertEqual(data['parse']['creation_date'] or False, '1999-06-04T12:00:00.0Z', 'google.ms: 1999-06-04T12:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ms: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ms: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ms: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ms: NS must be a value!')
    
    def test_MU(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.mu"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.mu')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.mu: MarkMonitor')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.mu ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2000-12-20T13:00:00.0Z', 'google.mu: 2000-12-20T13:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.mu: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.mu: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.mu: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.mu: NS must be a value!')

    def test_MW(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.mw"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.mw')
        self.assertEqual(data['parse']['registrar'] or False, 'MARKMONITOR-REG', 'google.mw: MARKMONITOR-REG')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.mw ?')
        self.assertEqual(data['parse']['creation_date'] or False, '20.12.2002 16:08:33', 'google.mw: 20.12.2002 16:08:33?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.mw: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.mw: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.mw: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.mw: NS must be a value!')
        
    def test_MX(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.mx"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.mx')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.mx: MarkMonitor')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com/', 'google.mx: http://www.markmonitor.com/?')
        self.assertEqual(data['parse']['creation_date'] or False, '2009-05-12', 'google.mx: 2009-05-12?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.mx: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.mx: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.mx: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.mx: NS must be a value!')

    def test_MY(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.my"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.my')
        self.assertEqual(data['parse']['registrar'] or False, 'MYNIC Berhad', 'google.my:MYNIC Berhad')
        self.assertEqual(data['parse']['registrar_url'] or False, 'https://whois.mynic.my', 'google.my: https://whois.mynic.my?')
        self.assertEqual(data['parse']['creation_date'] or False, '2009-05-12T16:00:00.000Z', 'google.my: 2009-05-12T16:00:00.000Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.my: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.my: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.my: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.my: NS must be a value!')

    def test_MZ(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.co.mz"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.co.mz')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.co.mz:MarkMonitor')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.co.mz: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2014-08-19T22:00:00.0Z', 'google.co.mz: 2014-08-19T22:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.co.mz: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.co.mz: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.co.mz: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.co.mz: NS must be a value!')
    
if __name__ == '__main__':
    unittest.main()