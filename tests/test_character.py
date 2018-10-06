# -*- coding: utf-8 -*-

import os
import battlenet
import datetime
from battlenet import Character
from battlenet.utils import normalize

try:
    import unittest2 as unittest
except ImportError:
    import unittest as unittest

class CharacterTest(unittest.TestCase):

    _character_name = 'Scobomb'
    _region = battlenet.EUROPE
    _realm_name = 'Tarren Mill'
    _guild_name = 'Method'
    _faction = Character.HORDE
    _race = Character.TAUREN
    _class = Character.DRUID
    _level = 120
    _gender = Character.FEMALE
    _professions = (
         Character.MINING,
         Character.HERBALISM,
        'Legion ' + Character.MINING,
        'Legion ' + Character.HERBALISM,
    )
    _professions_secondary = (
        Character.ARCHAEOLOGY,
        Character.COOKING,
        Character.FISHING,
        'Draenor ' + Character.COOKING,
        'Legion ' + Character.COOKING,
    )
    _appearance_face = 2
    _appearance_feature = 3
    _appearance_hair_color = 0
    _appearance_show_cloak = True
    _appearance_show_helm = True
    _appearance_hair = 3

    _character_name_unicode = 'Knüppler'
    _character_name_hunter = 'Rogerbrown'
    _pet_name = 'DEVAJR'

    _characters = (
        (battlenet.UNITED_STATES, 'illidan', 'Zonker'),
        (battlenet.UNITED_STATES, 'Mannoroth', 'Doubleagent'),
        (battlenet.EUROPE, 'Tarren Mill', 'Scobomb'),
        (battlenet.KOREA, '헬스크림', '천우회'),
        ## new taiwan api is not available now
        ##(battlenet.TAIWAN, '水晶之刺', '憂郁的風'),
        ## china api is not available now
        ##(battlenet.CHINA, '灰谷', '小蠬蝦'),
    )

    def test_general(self):
        character = Character(self._region, self._realm_name, self._character_name)

        self.assertEqual(character.name, self._character_name)
        self.assertEqual(str(character), self._character_name)

        self.assertEqual(character.get_realm_name(), normalize(self._realm_name))
        self.assertEqual(character.realm.name, normalize(self._realm_name))
        self.assertEqual(str(character.realm), normalize(self._realm_name))

        self.assertEqual(character.faction, self._faction)

        self.assertEqual(character.get_race_name(), self._race)

        self.assertEqual(character.get_class_name(), self._class)

        self.assertIsInstance(character.level, int)
        self.assertGreaterEqual(character.level, self._level)

        self.assertIsInstance(character.achievement_points, int)

        self.assertEqual(character.gender, self._gender)

    def test_guild(self):
        character = Character(self._region, self._realm_name, self._character_name, fields=[Character.GUILD])

        self.assertEqual(character.guild.name, self._guild_name)

    def test_stats(self):
        character = Character(self._region, self._realm_name, self._character_name, fields=[Character.STATS])

        self.assertIsInstance(character.stats.agility, int)

    def test_professions(self):
        character = Character(self._region, self._realm_name, self._character_name, fields=[Character.PROFESSIONS])

        primary = character.professions['primary']

        profession_1 = primary[0]
        profession_2 = primary[1]

        for profession in (profession_1, profession_2):
            self.assertIn(profession.name, self._professions)
            self.assertIsInstance(profession.rank, int)
            self.assertIsInstance(profession.recipes, list)

        secondary = [p.name for p in character.professions['secondary']]

        for p in self._professions_secondary:
            self.assertIn(p, secondary)
        for p in secondary:
            self.assertIn(p, self._professions_secondary)

    def test_appearance(self):
        character = Character(self._region, self._realm_name, self._character_name, fields=[Character.APPEARANCE])

        self.assertEqual(character.appearance.face, self._appearance_face)
        self.assertEqual(character.appearance.feature, self._appearance_feature)
        self.assertEqual(character.appearance.hair_color, self._appearance_hair_color)
        self.assertEqual(character.appearance.show_cloak, self._appearance_show_cloak)
        self.assertEqual(character.appearance.show_helm, self._appearance_show_helm)
        self.assertEqual(character.appearance.hair, self._appearance_hair)

    def test_lazyload(self):
        character = Character(self._region, self._realm_name, self._character_name)

        self.assertIsInstance(repr(character), str)
        self.assertEqual(character.guild.realm.name, normalize(self._realm_name))

    def test_unicode(self):
        character = Character(self._region, self._realm_name, self._character_name_unicode)

        self.assertIsInstance(repr(character), str)
        self.assertEqual(character.name, self._character_name_unicode)

    def test_hunter_pet_class(self):
        character = Character(battlenet.UNITED_STATES, 'Kiljaeden', 'Tandisse', fields=[Character.HUNTER_PETS])

        self.assertTrue(hasattr(character, 'hunter_pets'))
        self.assertIn('Rudebull', [pet.name for pet in character.hunter_pets])

    def test_achievements(self):
        character = Character(self._region, self._realm_name, self._character_name, fields=[Character.ACHIEVEMENTS])

        self.assertEqual(character.achievements[513], datetime.datetime(2008, 10, 15, 17, 13, 0))

    def test_progression(self):
        character = Character(self._region, self._realm_name, self._character_name, fields=[Character.PROGRESSION])

        for instance in character.progression['raids']:
            if instance.name == 'Antorus, the Burning Throne':
                self.assertTrue(instance.is_complete('normal'))

                for boss in instance.bosses:
                    if boss.name == 'Argus the Unmaker':
                        self.assertGreater(boss.normal, 0)
                        break
                else:
                    self.fail('Boss not found')

                break
        else:
            self.fail('Raid instance not found')

    def test_talents(self):
        character = Character(self._region, self._realm_name, self._character_name, fields=[Character.TALENTS])
        self.assertEqual(len(character.talents), 9)

    def test_talents_worldwide(self):
        for region, realm, character_name in self._characters:
            character = Character(region, realm, character_name, fields=[Character.TALENTS])
            self.assertEqual(len(character.talents), 9)

    def test_characters_worldwide(self):
        for region, realm, character_name in self._characters:
            character = Character(region, realm, character_name)
            self.assertEqual(character.name, character_name)

if __name__ == '__main__':
    unittest.main()
