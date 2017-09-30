import unittest

from lictionary import Lictionary

class TestLictionary(unittest.TestCase):
    def test_append(self):
        lict = Lictionary()
        lict.append(1)
        self.assertEqual(lict.items, [1])

    def test_numeric_lookup(self):
        lict = Lictionary([123])
        self.assertEqual(lict[0], 123)
        self.assertEqual(lict.get(0), 123)

    def test_string_lookup(self):
        lict = Lictionary([('key', 123)])
        self.assertEqual(lict['key'], 123)
        self.assertEqual(lict.get('key'), 123)

    def test_duplicate_key(self):
        lict = Lictionary([('key', 123),
                           ('key', 456)])
        self.assertEqual(lict[0], ('key', 123))
        self.assertEqual(lict[1], ('key', 456))
        self.assertEqual(lict['key'], 456)

    def test_not_found(self):
        lict = Lictionary()
        self.assertIs(lict.get(0), None)
        self.assertIs(lict.get('key'), None)
        with self.assertRaises(IndexError):
            _ = lict[0]
        with self.assertRaises(KeyError):
            _ = lict['key']
