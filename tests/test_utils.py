# -*- coding: utf-8 -*-

import battlenet
from battlenet import utils

try:
    import unittest2 as unittest
except ImportError:
    import unittest as unittest
    
class UtilsTest(unittest.TestCase):

    def test_normalize(self):
        for s in ('Simple', 'Sample name', u'Iso éè', u'灰谷', u"Some'with'"):
            new_s = utils.normalize(s)
            self.assertTrue(isinstance(new_s, str))

if __name__ == '__main__':
    unittest.main()
