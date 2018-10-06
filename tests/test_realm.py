# -*- coding: utf-8 -*-

import os
import battlenet
from battlenet import Realm
from battlenet.utils import normalize
from battlenet.utils import client_id
from battlenet.utils import client_secret

try:
    import unittest2 as unittest
except ImportError:
    import unittest as unittest


class RealmTest(unittest.TestCase):
    def _realm_for(self, region, name, useLocaleEn=False):
        if useLocaleEn:
            realm = self.connection_en.get_realm(region, name)
        else:
            realm = self.connection.get_realm(region, name)
        self.assertEqual(realm.name, name)

    def setUp(self):
        self.connection = battlenet.Connection(
            client_id=client_id(), client_secret=client_secret(),
            locale='not-specified')
        self.connection_en = battlenet.Connection(
            client_id=client_id(), client_secret=client_secret(),
            locale='en')

    def test_realm_by_name(self):
        name = "Kil'jaeden"

        realm = self.connection.get_realm(battlenet.UNITED_STATES, name)
        self.assertEqual(realm.name, normalize(name))

        realm = Realm(battlenet.UNITED_STATES, name)
        self.assertEqual(realm.name, normalize(name))

    def test_realm_by_slug(self):
        slug = 'kiljaeden'

        realm = self.connection.get_realm(battlenet.UNITED_STATES, slug)

        self.assertEqual(slug, realm.slug)

    def test_all_realms(self):
        realms = self.connection.get_all_realms(battlenet.UNITED_STATES)

        self.assertGreater(len(realms), 0)

    def test_all_realms_europe(self):
        realms = self.connection.get_all_realms(battlenet.EUROPE)

        self.assertGreater(len(realms), 0)

    def test_all_realms_korea(self):
        realms = self.connection.get_all_realms(battlenet.KOREA)

        self.assertGreater(len(realms), 0)

    @unittest.skip('Taiwan wow api not running at this time')
    def test_all_realms_taiwan(self):
        realms = self.connection.get_all_realms(battlenet.TAIWAN)

        self.assertGreater(len(realms), 0)

    @unittest.skip('China wow api not supported at this time')
    def test_all_realms_china(self):
        realms = self.connection.get_all_realms(battlenet.CHINA)

        self.assertGreater(len(realms), 0)

    def test_realms(self):
        names = sorted(['Blackrock', 'Nazjatar'])

        realms = self.connection.get_realms(battlenet.UNITED_STATES, names)

        self.assertEqual(names, sorted([realm.name for realm in realms]))

    def test_realm_type(self):
        realm = self.connection.get_realm(battlenet.UNITED_STATES, 'Nazjatar')

        self.assertEqual(realm.type, Realm.NORMAL)

    def test_realm_population(self):
        realm = self.connection.get_realm(battlenet.UNITED_STATES, 'Nazjatar')

        self.assertIn(realm.population, [Realm.LOW, Realm.MEDIUM, Realm.HIGH])

    def test_realm_united_state(self):
        self._realm_for(battlenet.UNITED_STATES, 'Blackrock')

    def test_realm_europe(self):
        self._realm_for(battlenet.EUROPE, 'Khaz Modan')

    def test_realm_korea(self):
        self._realm_for(battlenet.KOREA, '줄진')

    def test_realm_korea_en(self):
        self._realm_for(battlenet.KOREA, 'Hyjal', useLocaleEn=True)

    @unittest.skip('Taiwan wow api not running at this time')
    def test_realm_taiwan(self):
        self._realm_for(battlenet.TAIWAN, '世界之樹')

    @unittest.skip('Taiwan wow api not running at this time')
    def test_realm_taiwan_en(self):
        self._realm_for(battlenet.TAIWAN, 'Dragonmaw', useLocaleEn=True)

    @unittest.skip('China wow api not supported at this time')
    def test_realm_china(self):
        self._realm_for(battlenet.CHINA, '灰谷')

    @unittest.skip('China wow api not supported at this time')
    def test_realm_china_en(self):
        self._realm_for(battlenet.CHINA, 'Abbendis', useLocaleEn=True)

    def test_unicode(self):
        self._realm_for(battlenet.KOREA, '줄진')

    def tearDown(self):
        del self.connection
        del self.connection_en

if __name__ == '__main__':
    unittest.main()
