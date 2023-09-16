# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestC(unittest.TestCase):
    
    def test_CA(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ca"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ca')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor International Canada Ltd.', 'google.ca: MarkMonitor International Canada Ltd.?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'Markmonitor.com', 'google.ca: Markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2000-10-04T02:21:23Z', 'google.ca: 2000-10-04T02:21:23Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ca: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ca: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ca: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ca: NS must be a value!')
        
    def test_CC(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.cc"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.cc')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.cc: MarkMonitor Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.cc: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '1999-06-07T04:00:00Z', 'google.cc: 1999-06-07T04:00:00Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.cc: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.cc: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.cc: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.cc: NS must be a value!')
    
    def test_CD(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.cd"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.cd')
        self.assertEqual(data['parse']['registrar'] or False, 'Markmonitor', 'google.cd: Markmonitor?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.cd: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2021-01-15T00:00:00.0Z', 'google.cd: 2021-01-15T00:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.cd: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.cd: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.cd: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.cd: NS must be a value!')
        
    def test_CI(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ci"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ci')
        self.assertEqual(data['parse']['registrar'] or False, 'AFRIREGISTER', 'google.ci: AFRIREGISTER?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.ci: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2013-02-14T00:00:00.0Z', 'google.ci: 2013-02-14T00:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ci: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ci: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ci: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ci: NS must be a value!')
        
    def test_CL(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.cl"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.cl')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.cl: MarkMonitor Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'https://markmonitor.com/', 'google.cl: https://markmonitor.com/?')
        self.assertEqual(data['parse']['creation_date'] or False, '2002-10-22 17:48:23 CLST', 'google.cl: 2002-10-22 17:48:23 CLST?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.cl: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.cl: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.cl: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.cl: NS must be a value!')
        
    def test_CM(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.cm"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.cm')
        self.assertEqual(data['parse']['registrar'] or False, 'Netcom.cm Sarl', 'google.cm: Netcom.cm Sarl?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.cm: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2009-10-07T09:02:24.951Z', 'google.cm: 2009-10-07T09:02:24.951Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.cm: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.cm: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.cm: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.cm: NS must be a value!')
        
    def test_CN(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.cn"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.cn')
        self.assertEqual(data['parse']['registrar'] or False, '厦门易名科技股份有限公司', 'google.cn:厦门易名科技股份有限公司?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.cn: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2003-03-17 12:20:05', 'google.cn: 2003-03-17 12:20:05?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.cn: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.cn: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.cn: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.cn: NS must be a value!')
    
    def test_CO(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.co"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.co')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor, Inc.', 'google.co: MarkMonitor, Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'www.markmonitor.com', 'google.co: www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2010-02-25T01:04:59Z', 'google.co: 2010-02-25T01:04:59Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.co: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.co: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.co: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.co: NS must be a value!')
        
    def test_CR(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.cr"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.cr')
        self.assertEqual(data['parse']['registrar'] or False, 'NIC-REG1', 'google.cr: NIC-REG1?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.cr: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '02.03.2008 18:00:00', 'google.cr: 02.03.2008 18:00:00?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.cr: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.cr: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.cr: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.cr: NS must be a value!')
        
    def test_CX(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.cx"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.cx')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.cx: MarkMonitor?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.cx: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2010-07-29T18:15:42.56Z', 'google.cx: 2010-07-29T18:15:42.56Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.cx: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.cx: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.cx: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.cx: NS must be a value!')
        
    def test_CZ(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.cz"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.cz')
        if data['result'].find('Your connection limit exceeded') == -1:
            self.assertEqual(data['parse']['registrar'] or False, 'REG-MARKMONITOR', 'google.cz: REG-MARKMONITOR?')
            self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.cz: ?')
            self.assertEqual(data['parse']['creation_date'] or False, '21.07.2000 15:21:00', 'google.cz: 21.07.2000 15:21:00?')
            self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.cz: Updated Date must be a value!')
            self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.cz: Expiry Date must be a value!')
            self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.cz: Domain status must be a value!')
            self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.cz: NS must be a value!')
        else:
            print('Google.cz: Your connection limit exceeded. Please slow down and try again later.')
    
if __name__ == '__main__':
    unittest.main()