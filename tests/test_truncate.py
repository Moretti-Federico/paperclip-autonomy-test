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

    def test_exact_equalities(self):
        self.assertEqual(truncate("abcdef", 4), "a...")
        self.assertEqual(truncate("abcdef", 5), "ab...")

    def test_width_three_collapses_to_ellipsis(self):
        self.assertEqual(truncate("abcd", 3), "...")

    def test_truncated_result_has_exact_width(self):
        texts = ["abc", "abcd", "abcdef", "The quick brown fox jumps"]
        for text in texts:
            for width in range(1, len(text) + 1):
                with self.subTest(text=text, width=width):
                    self.assertEqual(len(truncate(text, width)), width)

    def test_boundary_texts(self):
        self.assertEqual(truncate("", 1), "")
        self.assertEqual(truncate("", 3), "")
        self.assertEqual(truncate("a", 1), "a")
        self.assertEqual(truncate("ab", 2), "ab")
        self.assertEqual(truncate("abc", 3), "abc")
        self.assertEqual(truncate("abcd", 4), "abcd")

    def test_idempotency(self):
        texts = ["abcdef", "abcd", "The quick brown fox jumps"]
        for text in texts:
            for width in range(1, len(text) + 2):
                with self.subTest(text=text, width=width):
                    once = truncate(text, width)
                    self.assertEqual(truncate(once, width), once)


if __name__ == "__main__":
    unittest.main()
