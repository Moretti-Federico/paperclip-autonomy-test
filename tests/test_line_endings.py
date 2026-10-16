"""Tests for textkit.line_endings.normalize_line_endings."""

import unittest

from textkit.line_endings import normalize_line_endings


class NormalizeLineEndingsTests(unittest.TestCase):
    def test_empty_input_returns_empty_string(self):
        self.assertEqual(normalize_line_endings(""), "")

    def test_lf_only_input_is_unchanged(self):
        self.assertEqual(normalize_line_endings("alpha\nbeta"), "alpha\nbeta")
        self.assertEqual(normalize_line_endings("\n\n\n"), "\n\n\n")

    def test_crlf_becomes_lf(self):
        self.assertEqual(normalize_line_endings("alpha\r\nbeta"), "alpha\nbeta")
        self.assertEqual(
            normalize_line_endings("a\r\nb\r\nc\r\n"), "a\nb\nc\n"
        )

    def test_lone_cr_becomes_lf(self):
        self.assertEqual(normalize_line_endings("alpha\rbeta"), "alpha\nbeta")
        self.assertEqual(normalize_line_endings("a\rb\rc"), "a\nb\nc")

    def test_mixed_terminators_all_become_lf(self):
        self.assertEqual(normalize_line_endings("a\r\nb\rc\nd"), "a\nb\nc\nd")
        self.assertEqual(normalize_line_endings("\r\n\n"), "\n\n")
        self.assertEqual(
            normalize_line_endings("one\r\r\ntwo\rthree\n\nfour"),
            "one\n\ntwo\nthree\n\nfour",
        )

    def test_other_characters_are_preserved(self):
        source = "  Hello,   World!\t \u00a0— mixed content "
        self.assertEqual(normalize_line_endings(source), source)

    def test_idempotent(self):
        samples = [
            "",
            "\n",
            "a\r\nb\rc\nd",
            "\r\n\n\r",
            "mixed \t text\r\nwith\rspaces\n",
        ]
        for sample in samples:
            with self.subTest(sample=sample):
                once = normalize_line_endings(sample)
                self.assertEqual(normalize_line_endings(once), once)


if __name__ == "__main__":
    unittest.main()
