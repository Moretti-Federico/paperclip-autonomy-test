"""Tests for textkit.slugify."""

import unittest

from textkit import slugify


class SlugifyTests(unittest.TestCase):
    def test_empty_input_returns_empty_string(self):
        self.assertEqual(slugify(""), "")

    def test_whitespace_only_input_returns_empty_string(self):
        self.assertEqual(slugify(" "), "")
        self.assertEqual(slugify(" \t \r\n \x0b\x0c "), "")
        self.assertEqual(slugify("\u00a0\u2003\u3000"), "")

    def test_punctuation_only_input_returns_empty_string(self):
        self.assertEqual(slugify("!!!"), "")
        self.assertEqual(slugify(",.;:?!"), "")
        self.assertEqual(slugify(" - _ / - "), "")

    def test_roadmap_examples(self):
        self.assertEqual(slugify("  Caffè, già!  "), "caffe-gia")
        self.assertEqual(slugify("Hello___WORLD / 42"), "hello-world-42")

    def test_accented_latin_letters_become_ascii(self):
        self.assertEqual(slugify("Caffè latte"), "caffe-latte")
        self.assertEqual(slugify("ÀÉÎÕÜ"), "aeiou")
        self.assertEqual(slugify("àéîõü"), "aeiou")
        self.assertEqual(slugify("ÇàÉñÜ"), "caenu")
        self.assertEqual(slugify("ÿ"), "y")

    def test_combining_marks_are_stripped_without_separators(self):
        self.assertEqual(slugify("cafe\u0301"), "cafe")
        self.assertEqual(slugify("ite\u0301ms everywhere"), "items-everywhere")
        self.assertEqual(slugify("a\u0301b\u0301c"), "abc")

    def test_mixed_case_is_lowercased(self):
        self.assertEqual(slugify("HeLLo-WoRLD"), "hello-world")
        self.assertEqual(slugify("MiXeD CaSe TeXt"), "mixed-case-text")

    def test_punctuation_runs_become_single_hyphen(self):
        self.assertEqual(slugify("hello, world!"), "hello-world")
        self.assertEqual(slugify("a!!!b???c"), "a-b-c")

    def test_repeated_separators_collapse_to_one_hyphen(self):
        self.assertEqual(slugify("a --- b ___ c"), "a-b-c")
        self.assertEqual(slugify("one///two\\\\\\three"), "one-two-three")
        self.assertEqual(slugify("a - _ - b"), "a-b")

    def test_leading_and_trailing_separators_are_stripped(self):
        self.assertEqual(slugify("---hello---"), "hello")
        self.assertEqual(slugify(" !!! hello ??? "), "hello")

    def test_digits_are_preserved(self):
        self.assertEqual(slugify("route 66"), "route-66")
        self.assertEqual(slugify("v2.0.1"), "v2-0-1")
        self.assertEqual(slugify("2024!"), "2024")
        self.assertEqual(slugify("a1b2c3"), "a1b2c3")

    def test_unicode_whitespace_separates_words(self):
        self.assertEqual(slugify("hello\u00a0world"), "hello-world")
        self.assertEqual(slugify("alpha\u2003beta\tgamma"), "alpha-beta-gamma")

    def test_non_ascii_scripts_are_dropped(self):
        self.assertEqual(slugify("hello 你好 world"), "hello-world")
        self.assertEqual(slugify("こんにちは"), "")

    def test_result_is_deterministic(self):
        for source in ("  Caffè, già!  ", "Hello___WORLD / 42", "V2 — beta!"):
            self.assertEqual(slugify(source), slugify(source))

    def test_t1_normalization_is_reused(self):
        self.assertEqual(
            slugify("The\t quick\u00a0 brown\n\n fox —   jumps!"),
            "the-quick-brown-fox-jumps",
        )


if __name__ == "__main__":
    unittest.main()
