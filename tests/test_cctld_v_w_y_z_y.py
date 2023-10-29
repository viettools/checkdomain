# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestVtoY(unittest.TestCase):
    def test_VC(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.vc"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.vc')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.vc: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.vc: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2005-06-29T00:58:18Z', 'google.vc: 2005-06-29T00:58:18Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.vc: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.vc: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.vc: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.vc: NS must be a value!')

    def test_VE(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.com.ve"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.com.ve')
        self.assertEqual(data['parse']['registrar'] or False, 'NIC-VE', 'google.com.ve: NIC-VE')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.com.ve ?')
        self.assertEqual(data['parse']['creation_date'] or False, '05.06.2002 20:00:00', 'google.com.ve: 05.06.2002 20:00:00?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.com.ve: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.com.ve: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.com.ve: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.com.ve: NS must be a value!')

    def test_VG(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.vg"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.vg')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor, Inc.', 'google.vg: MarkMonitor, Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.vg ?')
        self.assertEqual(data['parse']['creation_date'] or False, '1999-06-05T00:00:00.0Z', 'google.vg: 1999-06-05T00:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.vg: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.vg: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.vg: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.vg: NS must be a value!')

    def test_VU(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.vu"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.vu')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor, Inc.', 'google.vu: MarkMonitor, Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'www.markmonitor.com', 'google.vu: www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2003-08-21T09:32:17Z', 'google.vu: 2003-08-21T09:32:17Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.vu: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.vu: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.vu: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.vu: NS must be a value!')

    def test_WF(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.wf"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.wf')
        self.assertEqual(data['parse']['registrar'] or False, 'MARKMONITOR Inc.', 'google.wf: MARKMONITOR Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.wf: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2011-12-06T09:03:53Z', 'google.wf: 2011-12-06T09:03:53Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.wf: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.wf: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.wf: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.wf: NS must be a value!')

    def test_WS(self):
        # Sometime it doesn't work
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ws"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ws')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.ws: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com/whois.asp', 'google.ws: http://www.markmonitor.com/whois.asp?')
        self.assertEqual(data['parse']['creation_date'] or False, '2002-03-03T17:00:26Z', 'google.ws: 2002-03-03T17:00:26Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.ws: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.ws: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.ws: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ws: NS must be a value!')
        
    def test_YT(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.yt"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.yt')
        self.assertEqual(data['parse']['registrar'] or False, 'MARKMONITOR Inc.', 'google.yt: MARKMONITOR Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.yt: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2011-12-06T09:03:45Z', 'google.yt: 2011-12-06T09:03:45Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.yt: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.yt: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.yt: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.yt: NS must be a value!')

    def test_ZM(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.co.zm"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.co.zm')
        self.assertEqual(data['parse']['registrar'] or False, 'Zamnet', 'google.co.zm: Zamnet')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.co.zm ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2013-03-14T22:00:00.0Z', 'google.co.zm: 2013-03-14T22:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.co.zm: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.co.zm: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.co.zm: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.co.zm: NS must be a value!')
        
    def test_YE(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ye"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.ye')
        self.assertEqual(data['parse']['registrar'] or False, 'Yemen Net - Sales', 'google.ye: Yemen Net - Sales')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.ye ?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'google.ye ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.ye: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.ye: Expiry Date must not be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.ye: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.ye: NS must be a value!')
    
if __name__ == '__main__':
    unittest.main()