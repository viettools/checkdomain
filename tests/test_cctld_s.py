# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestS(unittest.TestCase):
    def test_SA(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.sa"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.sa')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.sa ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.sa ?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'google.sa ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.sa: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.sa: Expiry Date must not be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.sa: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.sa: NS must be a value!')

    def test_SB(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.sb"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.sb')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.sb: MarkMonitor')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.sb: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2015-11-29T23:00:00.0Z', 'google.sb: 2015-11-29T23:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.sb: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.sb: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.sb: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.sb: NS must be a value!')

    def test_SC(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.sc"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.sc')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.sc: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.sc: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2004-02-03T19:19:12Z', 'google.sc: 2004-02-03T19:19:12Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.sc: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.sc: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.sc: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.sc: NS must be a value!')
        
    def test_SD(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.sd"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.sd')
        self.assertEqual(data['parse']['registrar'] or False, 'AfriRegister', 'google.sd: AfriRegister')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.sd ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2020-05-12T15:03:41.109Z', 'google.sd: 2020-05-12T15:03:41.109Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.sd: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.sd: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.sd: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.sd: NS must be a value!')

    def test_SE(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.se"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.se')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc', 'google.se: MarkMonitor Inc')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.se ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2003-08-27', 'google.se: 2003-08-27?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.se: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.se: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.se: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.se: NS must be a value!')

    def test_SG(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.sg"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.sg')
        self.assertEqual(data['parse']['registrar'] or False, 'MARKMONITOR INC', 'google.sg: MARKMONITOR INC')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.sg ?')
        self.assertEqual(data['parse']['creation_date'] or False, '03-Jan-2005 12:00:00', 'google.sg: 03-Jan-2005 12:00:00?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.sg: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.sg: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.sg: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.sg: NS must be a value!')

    def test_SH(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.sh"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.sh')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.sh: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.sh: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '1999-06-07T17:23:46Z', 'google.sh: 1999-06-07T17:23:46Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.sh: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.sh: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.sh: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.sh: NS must be a value!')

    def test_SI(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.si"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.si')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.si: MarkMonitor')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.si: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2005-04-04', 'google.si: 2005-04-04?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.si: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.si: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.si: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.si: NS must be a value!')

    def test_SK(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.sk"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.sk')
        self.assertEqual(data['parse']['registrar'] or False, 'MARK-0292', 'google.sk: MARK-0292')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.sk ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2003-07-24', 'google.sk: 2003-07-24?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.sk: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.sk: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.sk: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.sk: NS must be a value!')

    def test_SL(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.sl"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.sl')
        self.assertEqual(data['parse']['registrar'] or False, 'nicsl', 'google.sl: nicsl')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.sl ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2008-05-17T21:00:00.0Z', 'google.sl: 2008-05-17T21:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.sl: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.sl: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.sl: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.sl: NS must be a value!')

    def test_SM(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.sm"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.sm')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.sm ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.sm ?')
        self.assertEqual(data['parse']['creation_date'] or False, '03/04/2003', 'google.sm: 03/04/2003?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.sm: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.sm: Expiry Date must not be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.sm: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.sm: NS must be a value!')

    def test_SN(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.sn"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.sn')
        self.assertEqual(data['parse']['registrar'] or False, 'MARKMONITOR Inc.', 'google.sn: MARKMONITOR Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.sn: ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2003-03-22T00:00:00Z', 'google.sn: 2003-03-22T00:00:00Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.sn: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.sn: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.sn: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.sn: NS must be a value!')

    def test_SO(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.so"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.so')
        self.assertEqual(data['parse']['registrar'] or False, 'Mark Monitor', 'google.so: Mark Monitor')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.so ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2011-01-24T00:00:00.0Z', 'google.so: 2011-01-24T00:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.so: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.so: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.so: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.so: NS must be a value!')

    def test_SS(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.com.ss"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.com.ss')
        self.assertEqual(data['parse']['registrar'] or False, 'Afriregister South Sudan', 'google.com.ss: Afriregister South Sudan')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.com.ss ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2020-07-06T08:29:03.885Z', 'google.com.ss: 2020-07-06T08:29:03.885Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.com.ss: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.com.ss: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.com.ss: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.com.ss: NS must be a value!')

    def test_ST(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.st"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.st')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.st: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'www.markmonitor.com', 'google.st: www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2004-06-15', 'google.st: 2004-06-15?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.st: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.st: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.st: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.st: NS must be a value!')

    def test_SU(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.su"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.su')
        self.assertEqual(data['parse']['registrar'] or False, 'RUCENTER-SU', 'google.su: RUCENTER-SU')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.su ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2005-10-15T20:00:00Z', 'google.su: 2005-10-15T20:00:00Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.su: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.su: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.su: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.su: NS must be a value!')
        
    def test_SX(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.sx"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.sx')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor Inc.', 'google.sx: MarkMonitor Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'www.markmonitor.com', 'google.sx: www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2012-09-22T02:52:06Z', 'google.sx: 2012-09-22T02:52:06Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.sx: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.sx: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.sx: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.sx: NS must be a value!')

    def test_SY(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "tld.sy"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for tld.sy')
        self.assertEqual(data['parse']['registrar'] or False, 'National Agency for Network Services', 'tld.sy: National Agency for Network Services')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'tld.sy ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2010-12-02T16:01:27.664Z', 'tld.sy: 2010-12-02T16:01:27.664Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'tld.sy: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'tld.sy: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'tld.sy: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'tld.sy: NS must be a value!')
     
if __name__ == '__main__':
    unittest.main()