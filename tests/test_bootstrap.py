"""Smoke-test the clean repository scaffold before feature work starts."""

import importlib
from pathlib import Path
import unittest


class BootstrapTests(unittest.TestCase):
    def test_import_resolves_to_this_repository(self):
        module = importlib.import_module("textkit")
        expected = Path(__file__).resolve().parents[1] / "textkit" / "__init__.py"
        self.assertEqual(Path(module.__file__).resolve(), expected)


if __name__ == "__main__":
    unittest.main()
