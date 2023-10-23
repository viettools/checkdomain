# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestPQ(unittest.TestCase):

    def test_PE(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.pe"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.pe')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.pe: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.pe ?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'google.pe ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.pe: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.pe: Expiry Date must not be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.pe: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.pe: NS must be a value!')  
    
    def test_PE(self):
        pass
    
    def test_PK(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.pk"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.pk')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.pk ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.pk ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2005-12-01', 'google.pk: 2005-12-01?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.pk: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.pk: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.pk: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.pk: NS must be a value!')
    
    def test_PL(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.pl"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.pl')
        self.assertEqual(data['parse']['registrar'] or False, 'Markmonitor, Inc.', 'google.pl: Markmonitor, Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.pl ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2002.09.19 13:00:00', 'google.pl: 2002.09.19 13:00:00?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.pl: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.pl: Expiry Date must not be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.pl: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.pl: NS must be a value!')

    def test_PM(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.pm"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.pm')
        self.assertEqual(data['parse']['registrar'] or False, 'MARKMONITOR Inc.', 'google.pm: MARKMONITOR Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.pm: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2011-12-06T09:12:15Z', 'google.pm: 2011-12-06T09:12:15Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.pm: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.pm: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.pm: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.pm: NS must be a value!')
    
    def test_PN(self):
        pass
    
    def test_PR(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.pr"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.pr')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.pr: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.pr: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2005-09-15T16:10:10Z', 'google.pr: 2005-09-15T16:10:10Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.pr: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.pr: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.pr: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.pr: NS must be a value!')
        
    def test_PS(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ps"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ps')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.ps: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.ps ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2004-05-18T22:00:00.0Z', 'google.ps: 2004-05-18T22:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ps: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ps: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ps: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ps: NS must be a value!')
        
    def test_PT(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.pt"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.pt')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.pt ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.pt ?')
        self.assertEqual(data['parse']['creation_date'] or False, '09/01/2003 00:00:00', 'google.pt: 09/01/2003 00:00:00?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.pt: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.pt: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.pt: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.pt: NS must be a value!')
        
    def test_PW(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.pw"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.pw')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor, Inc.', 'google.pw: MarkMonitor, Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.pw ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2012-10-12T10:19:46.0Z', 'google.pw: 2012-10-12T10:19:46.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.pw: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.pw: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.pw: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.pw: NS must be a value!')
    
    def test_QA(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.qa"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.qa')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc', 'google.qa: MarkMonitor Inc')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.qa ?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'google.qa ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.qa: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.qa: Expiry Date must not be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.qa: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.qa: NS must be a value!')
    
if __name__ == '__main__':
    unittest.main()