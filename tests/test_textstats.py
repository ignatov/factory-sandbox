import unittest

from src import textstats


class TextStatsTest(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(textstats.word_count("one two  three"), 3)

    def test_average_word_length(self):
        self.assertEqual(textstats.average_word_length("ab abcd"), 3)

    def test_average_word_length_empty(self):
        self.assertEqual(textstats.average_word_length(""), 0.0)
        self.assertEqual(textstats.average_word_length("   "), 0.0)
        self.assertEqual(textstats.average_word_length("\t\n "), 0.0)

    def test_longest_word(self):
        self.assertEqual(textstats.longest_word("a bbb cc"), "bbb")
        self.assertEqual(textstats.longest_word(""), "")


if __name__ == "__main__":
    unittest.main()
