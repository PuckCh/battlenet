import os
import battlenet
from battlenet.utils import client_id
from battlenet.utils import client_secret

try:
    import unittest2 as unittest
except ImportError:
    import unittest as unittest

class ExceptionTest(unittest.TestCase):
    def setUp(self):
        self.connection = battlenet.Connection(client_id=client_id(), client_secret=client_secret())

    def test_character_not_found(self):
        self.assertRaises(battlenet.CharacterNotFound,
            lambda: self.connection.get_character(battlenet.UNITED_STATES, 'Fake Realm', 'Fake Character'))

    def test_guild_not_found(self):
        self.assertRaises(battlenet.GuildNotFound,
            lambda: self.connection.get_guild(battlenet.UNITED_STATES, 'Fake Realm', 'Fake Guild'))

    def test_realm_not_found(self):
        self.assertRaises(battlenet.RealmNotFound, lambda: self.connection.get_realm(battlenet.EUROPE, 'Fake Realm'))

    def tearDown(self):
        del self.connection

if __name__ == '__main__':
    unittest.main()
