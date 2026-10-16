"""Tests for textkit.truncate.truncate."""

import unittest

from textkit.truncate import truncate


class TruncateTests(unittest.TestCase):
    def test_non_positive_width_returns_empty_string(self):
        self.assertEqual(truncate("hello", 0), "")
        self.assertEqual(truncate("hello", -1), "")
        self.assertEqual(truncate("", 0), "")

    def test_text_fitting_within_width_is_unchanged(self):
        self.assertEqual(truncate("", 4), "")
        self.assertEqual(truncate("abc", 5), "abc")
        self.assertEqual(truncate("abcdef", 6), "abcdef")

    def test_width_below_three_hard_cuts_without_ellipsis(self):
        self.assertEqual(truncate("abcdef", 1), "a")
        self.assertEqual(truncate("abcdef", 2), "ab")
        self.assertEqual(truncate("abc", 2), "ab")

    def test_longer_text_is_shortened_and_ends_with_ellipsis(self):
        result = truncate("The quick brown fox", 12)
        self.assertNotEqual(result, "The quick brown fox")
        self.assertTrue(result.endswith("..."))

    def test_longer_text_keeps_its_first_character(self):
        self.assertTrue(truncate("abcdef", 4).startswith("a"))
        self.assertTrue(truncate("unbelievable", 8).startswith("u"))


if __name__ == "__main__":
    unittest.main()
