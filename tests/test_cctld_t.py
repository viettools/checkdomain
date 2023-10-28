# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestT(unittest.TestCase):
    def test_TC(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "nic.tc"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for nic.tc')
        self.assertEqual(data['parse']['registrar'] or False, 'NICTC Internal', 'nic.tc: NICTC Internal')
        self.assertEqual(data['parse']['registrar_url'] or False, 'https://www.nic.tc', 'nic.tc: https://www.nic.tc?')
        self.assertEqual(data['parse']['creation_date'] or False, '1998-08-25T21:00:00.000Z', 'nic.tc: 1998-08-25T21:00:00.000Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'nic.tc: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'nic.tc: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'nic.tc: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'nic.tc: NS must be a value!')

    def test_TD(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.td"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.td')
        self.assertEqual(data['parse']['registrar'] or False, 'Afriregister Tchad', 'google.td: Afriregister Tchad')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.td ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2019-09-05T00:00:00.0Z', 'google.td: 2019-09-05T00:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.td: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.td: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.td: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.td: NS must be a value!')

    def test_TF(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.tf"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.tf')
        self.assertEqual(data['parse']['registrar'] or False, 'MARKMONITOR Inc.', 'google.tf: MARKMONITOR Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com', 'google.tf: http://www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2011-12-06T09:12:58Z', 'google.tf: 2011-12-06T09:12:58Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.tf: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.tf: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.tf: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.tf: NS must be a value!')

    def test_TG(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.tg"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.tg')
        self.assertEqual(data['parse']['registrar'] or False, 'NETMASTER SARL', 'google.tg: NETMASTER SARL')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.tg ?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'google.tg ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.tg: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.tg: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.tg: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.tg: NS must be a value!')

    def test_TH(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.th"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.th')
        self.assertEqual(data['parse']['registrar'] or False, 'THNIC', 'google.th: THNIC')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.th ?')
        self.assertEqual(data['parse']['creation_date'] or False, '17 Jul 2014', 'google.th: 17 Jul 2014?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.th: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.th: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.th: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.th: NS must be a value!')

    def test_TL(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.tl"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.tl')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor', 'google.tl: MarkMonitor')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.tl ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2003-05-23T12:00:00.0Z', 'google.tl: 2003-05-23T12:00:00.0Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.tl: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.tl: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.tl: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.tl: NS must be a value!')

    def test_TM(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.tm"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.tm')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.tm ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.tm ?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'google.tm ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.tm: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.tm: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.tm: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.tm: NS must be a value!')

    def test_TN(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.tn"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.tn')
        self.assertEqual(data['parse']['registrar'] or False, 'ELB', 'google.tn: ELB')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.tn ?')
        self.assertEqual(data['parse']['creation_date'] or False, '05-12-2018 11:02:02 GMT+1', 'google.tn: 05-12-2018 11:02:02 GMT+1?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.tn: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.tn: Expiry Date must not be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.tn: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.tn: NS must be a value!')

    def test_TO(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.to"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.to')
        self.assertEqual(data['parse']['registrar'] or False, False, 'google.to ?')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.to ?')
        self.assertEqual(data['parse']['creation_date'] or False, False, 'google.to ?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.to: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), bool, 'google.to: Expiry Date must not be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.to: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.to: NS must be a value!')

    def test_TR(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.com.tr"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.com.tr')
        self.assertEqual(data['parse']['registrar'] or False, 'ODTÜ GELİŞTİRME VAKFI BİLGİ TEKNOLOJİLERİ SAN. VE TİC. A.Ş.', 'google.com.tr: ODTÜ GELİŞTİRME VAKFI BİLGİ TEKNOLOJİLERİ SAN. VE TİC. A.Ş.')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.com.tr ?')
        self.assertEqual(data['parse']['creation_date'] or False, '2001-Aug-23.', 'google.com.tr: 2001-Aug-23.?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.com.tr: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.com.tr: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.com.tr: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.com.tr: NS must be a value!')

    def test_TV(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.tv"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.tv')
        self.assertEqual(data['parse']['registrar'] or False, 'MarkMonitor, Inc.', 'google.tv: MarkMonitor, Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'www.markmonitor.com', 'google.tv: www.markmonitor.com?')
        self.assertEqual(data['parse']['creation_date'] or False, '2002-08-02T16:43:36Z', 'google.tv: 2002-08-02T16:43:36Z?')
        self.assertEqual(type(data['parse']['updated_date'] or False), str, 'google.tv: Updated Date must be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.tv: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.tv: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.tv: NS must be a value!')

    def test_TW(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.tw"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.tw')
        self.assertEqual(data['parse']['registrar'] or False, 'Markmonitor, Inc.', 'google.tw: Markmonitor, Inc.')
        self.assertEqual(data['parse']['registrar_url'] or False, 'http://www.markmonitor.com/', 'google.tw: http://www.markmonitor.com/?')
        self.assertEqual(data['parse']['creation_date'] or False, '2005-10-27 17:02:34 (UTC+8)', 'google.tw: 2005-10-27 17:02:34 (UTC+8)?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.tw: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.tw: Expiry Date must be a value!')
        self.assertGreater(len(data['parse']['domain_status'] or []), 0, 'google.tw: Domain status must be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.tw: NS must be a value!')

    def test_TZ(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.tz"},
        )
        data = json.loads(response.content)
        self.assertTrue(data['status'], 'Please check connection for google.tz')
        self.assertEqual(data['parse']['registrar'] or False, 'REG-ITFARM', 'google.tz: REG-ITFARM')
        self.assertEqual(data['parse']['registrar_url'] or False, False, 'google.tz ?')
        self.assertEqual(data['parse']['creation_date'] or False, '05.03.2022 08:48:34', 'google.tz: 05.03.2022 08:48:34?')
        self.assertEqual(type(data['parse']['updated_date'] or False), bool, 'google.tz: Updated Date must not be a value!')
        self.assertEqual(type(data['parse']['expiry_date'] or False), str, 'google.tz: Expiry Date must be a value!')
        self.assertEqual(len(data['parse']['domain_status'] or []), 0, 'google.tz: Domain status must not be a value!')
        self.assertGreater(len(data['parse']['nameservers'] or []), 0, 'google.tz: NS must be a value!')
    
if __name__ == '__main__':
    unittest.main()