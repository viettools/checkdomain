# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestA(unittest.TestCase):
    def test_AC(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ac"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ac')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.ac: MarkMonitor Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.ac: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2006-04-03T13:38:02Z', 'google.ac: 2006-04-03T13:38:02Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ac: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ac: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ac: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ac: NS must be a value!')
        
    def test_AE(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ae"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ae')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.ae: MarkMonitor?')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ae: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ae: NS must be a value!')
        
    def test_AF(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.af"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.af')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.af: MarkMonitor?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.af: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2009-10-05T03:51:17.979Z', 'google.af: 2009-10-05T03:51:17.979Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.af: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.af: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.af: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.af: NS must be a value!')
        
    def test_AG(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ag"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ag')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.ag: MarkMonitor Inc.?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.ag: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2003-01-05T14:06:59Z', 'google.ag: 2003-01-05T14:06:59Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ag: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ag: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ag: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ag: NS must be a value!')
    
    def test_AI(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ai"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ai')
        self.assertEqual(data['parse']['registrar'] or False, 'Markmonitor', 'google.ai: Markmonitor?')
        self.assertEqual(data['parse']['creation_date'] or False, '2017-12-16T05:37:20.801Z', 'google.ai: 2017-12-16T05:37:20.801Z?')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ai: NS must be a value!')
    
    def test_AM(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.am"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.am')
        self.assertEqual(data['parse']['registrar'] or False, 'abcdomain (ABCDomain LLC)', 'google.am: abcdomain (ABCDomain LLC)?')
        self.assertEqual(data['parse']['creation_date'] or False, '1999-06-05', 'google.am: 1999-06-05?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.am: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.am: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.am: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.am: NS must be a value!')
    
    def test_AR(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ar"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ar')
        self.assertEqual(data['parse']['registrar'] or False, 'nicar', 'google.ar: nicar?')
        self.assertEqual(data['parse']['creation_date'] or False, '2019-11-01 12:21:37.677445', 'google.ar: 2019-11-01 12:21:37.677445?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ar: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ar: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ar: NS must be a value!')
    
    def test_AS(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.as"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.as')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc. (http://www.markmonitor.com)', 'google.as: MarkMonitor Inc. (http://www.markmonitor.com)?')
        self.assertEqual(data['parse']['creation_date'] or False, '02nd August 2000 at 00:00:00.000', 'google.as: 02nd August 2000 at 00:00:00.000?')
        self.assertEqual(data['parse']['expiry_date'] or False, '02nd August each year', 'google.as: 02nd August each year?')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.as: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.as: NS must be a value!')
    
    def test_AT(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.at"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.at')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc. ( https://nic.at/registrar/434 )', 'google.at: MarkMonitor Inc. ( https://nic.at/registrar/434 )?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.at: Updated Date must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.at: NS must be a value!')
    
    def test_AU(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.au"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.au')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Corporate Services Inc', 'google.au: MarkMonitor Corporate Services Inc?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'https://whois-webform.markmonitor.com/whois/', 'google.au: https://whois-webform.markmonitor.com/whois/?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.au: Updated Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.au: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.au: NS must be a value!')
    
    def test_AW(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.aw"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.aw')
        self.assertEqual(data['parse']['registrar'] or False, 'SETAR N.V.', 'google.aw: SETAR N.V.?')
        self.assertEqual(data['parse']['creation_date'] or False, '2017-09-13', 'google.aw: 2017-09-13?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.aw: Updated Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.aw: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.aw: NS must be a value!')
    
    def test_AX(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "whois.ax"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for whois.ax')
        self.assertEqual(data['parse']['registrar'] or False, 'Ålands landskapsregering', 'whois.ax: Ålands landskapsregering?')
        self.assertEqual(data['parse']['registrar_url'] or False, 'https://regeringen.ax', 'whois.ax: https://regeringen.ax?')
        self.assertEqual(data['parse']['creation_date'] or False, '02.02.2012', 'whois.ax: 02.02.2012?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'whois.ax: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'whois.ax: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'whois.ax: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'whois.ax: NS must be a value!')
    
if __name__ == '__main__':
    unittest.main()