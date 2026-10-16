"""Tests for textkit.normalize_whitespace."""

import unittest

from textkit import normalize_whitespace


class NormalizeWhitespaceTests(unittest.TestCase):
    def test_empty_input_returns_empty_string(self):
        self.assertEqual(normalize_whitespace(""), "")

    def test_whitespace_only_input_returns_empty_string(self):
        self.assertEqual(normalize_whitespace(" "), "")
        self.assertEqual(normalize_whitespace("\t"), "")
        self.assertEqual(normalize_whitespace("\n"), "")
        self.assertEqual(normalize_whitespace(" \t \r\n \x0b\x0c "), "")

    def test_leading_and_trailing_whitespace_removed(self):
        self.assertEqual(normalize_whitespace("  hello  "), "hello")
        self.assertEqual(normalize_whitespace("\t\n  hello \t\n"), "hello")

    def test_tabs_and_newlines_between_words_become_single_space(self):
        self.assertEqual(normalize_whitespace("alpha\tbeta"), "alpha beta")
        self.assertEqual(normalize_whitespace("alpha\nbeta"), "alpha beta")
        self.assertEqual(normalize_whitespace("alpha\r\nbeta"), "alpha beta")
        self.assertEqual(normalize_whitespace("alpha \t\n\r beta"), "alpha beta")

    def test_repeated_spaces_collapse_to_single_space(self):
        self.assertEqual(normalize_whitespace("one    two     three"), "one two three")

    def test_unicode_whitespace_collapses_to_ascii_space(self):
        self.assertEqual(normalize_whitespace("a\u00a0b"), "a b")
        self.assertEqual(normalize_whitespace("a\u2003b"), "a b")
        self.assertEqual(normalize_whitespace("a\u3000b"), "a b")
        self.assertEqual(normalize_whitespace("a\u00a0\u2003 \t b"), "a b")
        self.assertEqual(
            normalize_whitespace("\u00a0\u2003hello\u3000\u00a0"), "hello"
        )

    def test_punctuation_and_case_are_preserved(self):
        self.assertEqual(
            normalize_whitespace("  Hello,   World!  "), "Hello, World!"
        )
        self.assertEqual(
            normalize_whitespace("\tMiXeD\u2003CaSe;   'quoted'...\n"),
            "MiXeD CaSe; 'quoted'...",
        )

    def test_already_normalized_text_is_unchanged(self):
        self.assertEqual(normalize_whitespace("Hello, World!"), "Hello, World!")

    def test_mixed_whitespace_everywhere(self):
        source = "  The\t quick\u00a0 brown\n\n fox —   jumps!  "
        self.assertEqual(
            normalize_whitespace(source), "The quick brown fox — jumps!"
        )


if __name__ == "__main__":
    unittest.main()
