# encoding: utf-8
# test.py for Rabbit-Python

import unittest
from rabbit import Rabbit

class RabbitTests(unittest.TestCase):
    def setUp(self):
        testing = True

    def test_uni2zg(self):
        print("converting Unicode to Zawgyi")
        converted = Rabbit.uni2zg(u"မင်္ဂလာပါ")
        self.assertEqual(converted, u"မဂၤလာပါ")

    def test_zg2uni(self):
        print("converting Zawgyi to Unicode")
        converted = Rabbit.zg2uni(u"မဂၤလာပါ")
        self.assertEqual(converted, u"မင်္ဂလာပါ")

if __name__ == "__main__":
    unittest.main()
