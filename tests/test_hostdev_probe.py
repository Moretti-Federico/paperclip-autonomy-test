"""Tests for textkit.hostdev_probe.host_summary."""

import unittest

from textkit.hostdev_probe import host_summary


class HostSummaryTests(unittest.TestCase):
    def test_host_summary_returns_hostdev_ok(self):
        self.assertEqual(host_summary(), "hostdev-ok")


if __name__ == "__main__":
    unittest.main()
