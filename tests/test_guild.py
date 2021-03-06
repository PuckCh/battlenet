# -*- coding: utf-8 -*-

import os
import battlenet
import datetime
from battlenet import Guild
from battlenet.utils import normalize

try:
    import unittest2 as unittest
except ImportError:
    import unittest as unittest
    
class GuildTest(unittest.TestCase):
    _guild_region = battlenet.EUROPE
    _guild_realm_name = "Lightning's Blade"
    _guild_name = 'Paragon'

    _guilds = (
        (battlenet.UNITED_STATES, 'illidan', 'Blood Legion'),
        (battlenet.EUROPE, "Lightning's Blade", 'Paragon'),
        (battlenet.KOREA, 'Azshara', 'AFK R'),   # realm in english...
        (battlenet.KOREA, '아즈샤라', 'AFK R'),  # same realm in kr
        ## new taiwan api is not available now
        ##(battlenet.TAIWAN, '水晶之刺', 'Stars'),
        ## china api is not available now
        ##(battlenet.CHINA, '灰谷', '星之轨迹'),
    )

    def test_general(self):
        guild = Guild(self._guild_region, self._guild_realm_name, self._guild_name)

        self.assertEqual(guild.name, self._guild_name)
        self.assertEqual(str(guild), self._guild_name)

        self.assertEqual(guild.get_realm_name(), normalize(self._guild_realm_name))
        self.assertEqual(guild.realm.name, normalize(self._guild_realm_name))
        self.assertEqual(str(guild.realm), normalize(self._guild_realm_name))

    def test_len(self):
        guild = Guild(self._guild_region, self._guild_realm_name, self._guild_name, fields=[Guild.MEMBERS])

        self.assertGreater(len(guild), 1)

    def test_leader(self):
        guild = Guild(self._guild_region, self._guild_realm_name, self._guild_name, fields=[Guild.MEMBERS])

        character = guild.get_leader()

        self.assertEqual(character.name, 'Lavosheppe')

    def test_lazyload_member_character(self):
        guild = Guild(self._guild_region, self._guild_realm_name, self._guild_name)

        self.assertIsInstance(repr(guild), str)

        character = guild.get_leader()

        self.assertRegex(character.get_full_class_name(), r'^Marksmanship Hunter$')

    def test_achievements(self):
        guild = Guild(self._guild_region, self._guild_realm_name, self._guild_name, fields=[Guild.ACHIEVEMENTS])

        for id_, completed_ts in guild.achievements.items():
            self.assertIsInstance(id_, int)
            self.assertIsInstance(completed_ts, datetime.datetime)

    def test_guilds_worldwide(self):
        for region, realm, guild_name in self._guilds:
            guild = Guild(region, realm, guild_name)
            self.assertIsInstance(repr(guild), str)
            self.assertEqual(guild.name, guild_name)

if __name__ == '__main__':
    unittest.main()
