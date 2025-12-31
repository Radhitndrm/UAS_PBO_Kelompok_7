"""
Unit test untuk utils.

Menguji fungsionalitas utility functions (validator, date_helper).
"""

import unittest
from utils.validator import validate_volume, validate_status
from utils.date_helper import get_current_timestamp


class TestValidator(unittest.TestCase):
    """Test case untuk module validator."""

    def test_validate_volume_positive(self):
        """Test validasi volume dengan nilai positif."""
        try:
            validate_volume(100.0)
            validate_volume(0.1)
            validate_volume(999.99)
        except ValueError:
            self.fail("validate_volume() raised ValueError unexpectedly!")

    def test_validate_volume_zero(self):
        """Test validasi volume dengan nilai nol."""
        with self.assertRaises(ValueError):
            validate_volume(0)

    def test_validate_volume_negative(self):
        """Test validasi volume dengan nilai negatif."""
        with self.assertRaises(ValueError):
            validate_volume(-10.0)

    def test_validate_status_valid(self):
        """Test validasi status dengan nilai valid."""
        valid_statuses = ["TERCATAT", "DALAM_PENGANGKUTAN", "DIPROSES", "SELESAI"]
        for status in valid_statuses:
            try:
                validate_status(status)
            except ValueError:
                self.fail(f"validate_status() raised ValueError for valid status: {status}")

    def test_validate_status_invalid(self):
        """Test validasi status dengan nilai invalid."""
        invalid_statuses = ["PENDING", "CANCEL", "UNKNOWN", ""]
        for status in invalid_statuses:
            with self.assertRaises(ValueError):
                validate_status(status)


class TestDateHelper(unittest.TestCase):
    """Test case untuk module date_helper."""

    def test_get_current_timestamp_format(self):
        """Test format timestamp yang dihasilkan."""
        timestamp = get_current_timestamp()

        # Cek apakah timestamp adalah string
        self.assertIsInstance(timestamp, str)

        # Cek format YYYY-MM-DD HH:MM:SS
        parts = timestamp.split(" ")
        self.assertEqual(len(parts), 2)

        # Cek format tanggal YYYY-MM-DD
        date_parts = parts[0].split("-")
        self.assertEqual(len(date_parts), 3)
        self.assertEqual(len(date_parts[0]), 4)  # Year
        self.assertEqual(len(date_parts[1]), 2)  # Month
        self.assertEqual(len(date_parts[2]), 2)  # Day

        # Cek format waktu HH:MM:SS
        time_parts = parts[1].split(":")
        self.assertEqual(len(time_parts), 3)
        self.assertEqual(len(time_parts[0]), 2)  # Hour
        self.assertEqual(len(time_parts[1]), 2)  # Minute
        self.assertEqual(len(time_parts[2]), 2)  # Second

    def test_get_current_timestamp_not_empty(self):
        """Test timestamp tidak kosong."""
        timestamp = get_current_timestamp()
        self.assertTrue(len(timestamp) > 0)

    def test_get_current_timestamp_unique(self):
        """Test timestamp berbeda di waktu yang berbeda."""
        import time
        timestamp1 = get_current_timestamp()
        time.sleep(1.1)  # Tunggu lebih dari 1 detik
        timestamp2 = get_current_timestamp()

        # Karena format hanya sampai detik, seharusnya berbeda
        self.assertNotEqual(timestamp1, timestamp2)


if __name__ == "__main__":
    unittest.main()
