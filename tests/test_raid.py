# -*- coding: utf-8 -*-

import unittest
import os
import battlenet
import datetime
from battlenet import Character
from battlenet import Raid

class RaidTest(unittest.TestCase):

    _character_name = 'Sejta'
    _region = battlenet.EUROPE
    _realm_name = "Lightning's Blade"

    _characters = (
        (battlenet.UNITED_STATES, 'illidan', 'Zonker'),
        (battlenet.EUROPE, "Lightning's Blade", 'Sejta'),
        (battlenet.KOREA, '헬스크림', '천우회'),
        ## new taiwan api is not available now
        ##(battlenet.TAIWAN, '水晶之刺', '憂郁的風'),
        ## china api is not available now
        ##(battlenet.CHINA, '灰谷', '小蠬蝦'),
    )

    def test_ids(self):
        character = Character(self._region, self._realm_name, self._character_name)
        for raid in character.progression['raids']:
            expansion_short, expansion_long = Raid(raid.id).expansion()
            self.assertIsNotNone(expansion_short)
            self.assertIsNotNone(expansion_long)

    def test_order(self):
        expansions = ('wow', 'bc', 'lk', 'cata', 'mop', 'wod', 'legion', 'bfa')
        keys = sorted(battlenet.EXPANSION.keys())
        for i in range(len(keys)):
            self.assertEqual(battlenet.EXPANSION[i][0], expansions[i])

    def test_raids_worldwide(self):
        for region, realm, character_name in self._characters:
            character = Character(region, realm, character_name)
            for raid in character.progression['raids']:
                self.assertIsNotNone(raid)

if __name__ == '__main__':
    unittest.main()
