# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestB(unittest.TestCase):
    
    def test_BE(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.be"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.be')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.be: MarkMonitor Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'https://www.markmonitor.com', 'google.be: https://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, 'Tue Dec 12 2000', 'google.be:Tue Dec 12 2000?')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.be: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.be: NS must be a value!')

    def test_BF(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.bf"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.bf')
        self.assertEqual(data['parse']['registrar'] or False, 'AFRIREGISTER BURKINA', 'google.bf: AFRIREGISTER BURKINA?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'RegistrarURL', 'google.bf: RegistrarURL?')
        self.assertEqual(data['parse']['creation_date'] or False, '2021-01-01T00:00:00.0Z', 'google.bf: 2021-01-01T00:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.bf: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.bf: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.bf: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.bf: NS must be a value!')
        
    # BG --> Check on web to get full details
    
    def test_BH(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.bh"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.bh')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor, Inc.', 'google.bh: MarkMonitor, Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.bh: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2020-07-02T12:23:45.0Z', 'google.bh: 2020-07-02T12:23:45.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.bh: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.bh: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.bh: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.bh: NS must be a value!')
        
    def test_BI(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.bi"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.bi')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.bi: MarkMonitor?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.bi: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2002-09-29T22:00:00.0Z', 'google.bi: 2002-09-29T22:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.bi: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.bi: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.bi: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.bi: NS must be a value!')
    
    def test_BJ(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.bj"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.bj')
        self.assertEqual(data['parse']['registrar'] or False, 'OPEN SOLUTIONS_ENTREPRISES', 'google.bj: OPEN SOLUTIONS_ENTREPRISES?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.bj: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2015-01-29T11:16:22.808Z', 'google.bj: 2015-01-29T11:16:22.808Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.bj: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.bj: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.bj: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.bj: NS must be a value!')
    
    def test_BM(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "apple.bm"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for apple.bm')
        self.assertEqual(data['parse']['registrar'] or False, 'The Registry General, Government of Bermuda', 'apple.bm: The Registry General, Government of Bermuda?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'apple.bm: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2016-03-23T00:00:00Z', 'apple.bm: 2016-03-23T00:00:00Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'apple.bm: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'apple.bm: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'apple.bm: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'apple.bm: NS must be a value!')
    
    def test_BN(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.com.bn"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.com.bn')
        self.assertEqual(data['parse']['registrar'] or False, 'IMAGINE SDN BHD', 'google.com.bn: IMAGINE SDN BHD?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.com.bn: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '13-Nov-2006 00:00:00', 'google.com.bn: 13-Nov-2006 00:00:00?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.com.bn: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.com.bn: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.com.bn: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.com.bn: NS must be a value!')
    
    def test_BR(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.com.br"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.com.br')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.com.br: ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.com.br: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '19990518 #162310', 'google.com.br: 19990518 #162310?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.com.br: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.com.br: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.com.br: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.com.br: NS must be a value!')
    
    def test_BW(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.co.bw"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.co.bw')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc', 'google.co.bw: MarkMonitor Inc?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.co.bw: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2012-11-12T22:00:00.0Z', 'google.co.bw: 2012-11-12T22:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.co.bw: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.co.bw: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.co.bw: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.co.bw: NS must be a value!')
        
    def test_BY(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.by"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.by')
        self.assertEqual(data['parse']['registrar'] or False, 'Open Contact, Ltd', 'google.by: Open Contact, Ltd?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.by: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2004-05-14', 'google.by: 2004-05-14?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.by: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.by: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.by: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.by: NS must be a value!')
    
    def test_BZ(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.bz"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.bz')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.bz: MarkMonitor Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.bz: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2006-02-12T18:08:52Z', 'google.bz: 2006-02-12T18:08:52Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.bz: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.bz: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.bz: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.bz: NS must be a value!')
    
if __name__ == '__main__':
    unittest.main()