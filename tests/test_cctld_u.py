# -*- coding: utf-8 -*-
# https://check.rs/

import unittest
from fastapi.testclient import TestClient
import sys, os, json

sys.path.append(os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__)))))

from main import app
client = TestClient(app)

class TestU(unittest.TestCase):
    def test_UA(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ua"},
        )
        data = json.loads(response.content)
        if not data['status']:
            print('Please check .ua whois server!')
            return

        self.assertEqual(data['parse']['registrar'], 'ua.markmonitor')
        self.assertEqual(data['parse']['registrar_url'], 'http://markmonitor.com')
        self.assertGreater(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)

        self.assertEqual(data['parse']['creation_date'], '2011-07-21 18:03:50')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)

    def test_UG(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.ug"},
        )
        data = json.loads(response.content)
        if not data['status']:
            print('Please check .ug whois server!')
            return

        self.assertEqual(data['parse']['registrar'], '')
        self.assertEqual(data['parse']['registrar_url'], '')
        self.assertGreater(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)

        self.assertEqual(data['parse']['creation_date'], '2004-08-03')
        self.assertEqual(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)      

    def test_UK(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.uk"},
        )
        data = json.loads(response.content)
        if not data['status']:
            print('Please check .uk whois server!')
            return

        self.assertEqual(data['parse']['registrar'], 'Markmonitor Inc. [Tag = MARKMONITOR]')
        self.assertEqual(data['parse']['registrar_url'], 'https://www.markmonitor.com')
        self.assertEqual(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)

        self.assertEqual(data['parse']['creation_date'], '11-Jun-2014')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)

    def test_US(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.us"},
        )
        data = json.loads(response.content)
        if not data['status']:
            print('Please check .us whois server!')
            return

        self.assertEqual(data['parse']['registrar'], 'MarkMonitor, Inc.')
        self.assertEqual(data['parse']['registrar_url'], 'www.markmonitor.com')
        self.assertGreater(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)

        self.assertEqual(data['parse']['creation_date'], '2002-04-19T23:16:01Z')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)
        
    def test_UZ(self):
        response = client.post(
            '/api/v1/whois',
            headers={'X-Requested-With': 'XMLHttpRequest'},
            json={"domain": "google.uz"},
        )
        data = json.loads(response.content)
        if not data['status']:
            print('Please check .uz whois server!')
            return

        self.assertEqual(data['parse']['registrar'], 'Tomas')
        self.assertEqual(data['parse']['registrar_url'], 'http://www.cctld.uz/')
        self.assertGreater(len(data['parse']['domain_status']), 0)
        self.assertGreater(len(data['parse']['nameservers']), 0)

        self.assertEqual(data['parse']['creation_date'], '13-Apr-2006')
        self.assertGreater(len(data['parse']['updated_date']), 0)
        self.assertGreater(len(data['parse']['expiry_date']), 0)
    
if __name__ == '__main__':
    unittest.main()