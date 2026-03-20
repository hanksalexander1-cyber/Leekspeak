import unittest
from leek import LeetSpeak

cliss = LeetSpeak()

class TestLeetSpeak(unittest.TestCase):

    def test_translate(self):
        self.assertEqual(LeetSpeak.translate("apple", 0), "4|*|*13")
        self.assertEqual(LeetSpeak.translate("apple", 1), "@|o|o|_€")
        self.assertEqual(LeetSpeak.translate("apple", 2), "4|*|*13")
        self.assertEqual(LeetSpeak.translate("apple", 3), "@|o|o|_€")
        self.assertEqual(LeetSpeak.translate("AppLE", 0), "4|*|*13")
        self.assertEqual(LeetSpeak.translate("5 ApPLE piEs", 1), "5 @|o|o|_€|o!€$")
        with self.assertRaises(ValueError):
            LeetSpeak.translate("apple", -1)
        with self.assertRaises(TypeError):
            LeetSpeak.translate("apple","dog")
        with self.assertRaises(TypeError):
            LeetSpeak.translate("apple", 1.5)

