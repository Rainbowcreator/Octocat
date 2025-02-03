import unittest
from firewall.firewall_core import check_connection


class TestFirewall(unittest.TestCase):
    def test_allowed_connection(self):
        result = check_connection('192.168.1.100', 80)
        self.assertEqual(result, True)

    def test_disallowed_connection(self):
        result = check_connection('192.168.1.101', 81)
        self.assertEqual(result, False)


