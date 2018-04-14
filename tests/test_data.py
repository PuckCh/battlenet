import os
import battlenet
from operator import itemgetter
from battlenet.utils import api_key

try:
    import unittest2 as unittest
except ImportError:
    import unittest as unittest

PUBLIC_KEY = os.environ.get('BNET_PUBLIC_KEY')
PRIVATE_KEY = os.environ.get('BNET_PRIVATE_KEY')

class DataTest(unittest.TestCase):
    def setUp(self):
        self.connection = battlenet.Connection(
            api_key=api_key(), public_key=PUBLIC_KEY, private_key=PRIVATE_KEY)

    def test_races(self):
        races = self.connection.get_character_races(battlenet.UNITED_STATES)

        self.assertEqual({
            1: u'Human',
            2: u'Orc',
            3: u'Dwarf',
            4: u'Night Elf',
            5: u'Undead',
            6: u'Tauren',
            7: u'Gnome',
            8: u'Troll',
            9: u'Goblin',
            10: u'Blood Elf',
            11: u'Draenei',
            22: u'Worgen',
            24: u'Pandaren',
            25: u'Pandaren',
            26: u'Pandaren',
            27: 'Nightborne',
            28: 'Highmountain Tauren',
            29: 'Void Elf',
            30: 'Lightforged Draenei',
        }, dict([(race.id, race.name) for race in races]))

        for race in races:
            self.assertIn(race.side, ['alliance', 'horde', 'neutral'])

    def test_classes(self):
        classes = self.connection.get_character_classes(
            battlenet.UNITED_STATES, raw=True)

        classes_ = [{
            'powerType': 'focus',
            'mask': 4,
            'id': 3,
        }, {
            'powerType': 'energy',
            'mask': 8,
            'id': 4,
        }, {
            'powerType': 'rage',
            'mask': 1,
            'id': 1,
        }, {
            'powerType': 'mana',
            'mask': 2,
            'id': 2,
        }, {
            'powerType': 'mana',
            'mask': 64,
            'id': 7,
        }, {
            'powerType': 'mana',
            'mask': 128,
            'id': 8,
        }, {
            'powerType': 'mana',
            'mask': 16,
            'id': 5,
        }, {
            'powerType': 'runic-power',
            'mask': 32,
            'id': 6,
        }, {
            'powerType': 'mana',
            'mask': 1024,
            'id': 11,
        }, {
            'powerType': 'mana',
            'mask': 256,
            'id': 9,
        }, {
            'powerType': 'energy',
            'mask': 512,
            'id': 10,
        }, {
            'powerType': 'fury',
            'mask': 2048,
            'id': 12,
        }]

        for i in range(len(classes_)):
            classes_[i]['name'] = battlenet.CLASS[classes_[i]['id']]

        classes_.sort(key=itemgetter('id'))
        classes.sort(key=itemgetter('id'))

        self.assertEqual(classes, classes_)

        classes = self.connection.get_character_classes(battlenet.UNITED_STATES)

        for class_ in classes:
            self.assertIn(class_.power_type,
                ['mana', 'energy', 'runic-power', 'focus', 'rage', 'fury'])

    def test_items(self):
        item = self.connection.get_item(battlenet.UNITED_STATES, 60249)
        # TODO

    def test_spell(self):
        spell = self.connection.get_spell(battlenet.UNITED_STATES, 215183)
        # TODO

if __name__ == '__main__':
    unittest.main()
