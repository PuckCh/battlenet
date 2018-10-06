import os
import battlenet
from battlenet.utils import client_id
from battlenet.utils import client_secret

try:
    import unittest2 as unittest
except ImportError:
    import unittest as unittest

class RegionsTest(unittest.TestCase):
    def setUp(self):
        self.connection = battlenet.Connection(client_id=client_id(), client_secret=client_secret())

    def test_us(self):
        realms = self.connection.get_all_realms(battlenet.UNITED_STATES)
        self.assertTrue(len(realms) > 0)

    def test_eu(self):
        realms = self.connection.get_all_realms(battlenet.EUROPE)
        self.assertTrue(len(realms) > 0)

    def test_kr(self):
        realms = self.connection.get_all_realms(battlenet.KOREA)
        self.assertTrue(len(realms) > 0)

    @unittest.skip('Taiwan wow api not running at this time')
    def test_tw(self):
        realms = self.connection.get_all_realms(battlenet.TAIWAN)
        self.assertTrue(len(realms) > 0)

    @unittest.skip('China wow api not supported at this time')
    def test_cn(self):
        realms = self.connection.get_all_realms(battlenet.CHINA)
        self.assertTrue(len(realms) > 0)

    def tearDown(self):
        del self.connection

if __name__ == '__main__':
    unittest.main()
