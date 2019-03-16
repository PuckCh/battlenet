import os
import battlenet
from operator import itemgetter
from battlenet.utils import client_id
from battlenet.utils import client_secret

try:
    import unittest2 as unittest
except ImportError:
    import unittest as unittest

class DataTest(unittest.TestCase):
    def setUp(self):
        self.connection = battlenet.Connection(client_id=client_id(), client_secret=client_secret())

    def test_races(self):
        races = self.connection.get_character_races(battlenet.UNITED_STATES)

        self.assertEqual(battlenet.RACE, dict([(race.id, race.name) for race in races]))
        self.assertEqual(
                dict([(k, v.lower().replace('?', 'neutral'))
                    for k, v in battlenet.RACE_TO_FACTION.items()]),
                dict([(race.id, race.side) for race in races]))

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
