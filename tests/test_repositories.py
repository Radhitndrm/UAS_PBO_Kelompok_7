"""
Unit test untuk repositories.

Menguji fungsionalitas repository untuk penyimpanan data limbah.
"""

import unittest
from repositories.in_memory_limbah_repository import InMemoryLimbahRepository
from models.limbah_organik import LimbahOrganik
from models.limbah_medis import LimbahMedis
from models.limbah_b3 import LimbahB3


class TestInMemoryLimbahRepository(unittest.TestCase):
    """Test case untuk class InMemoryLimbahRepository."""

    def setUp(self):
        """Setup yang dijalankan sebelum setiap test."""
        self.repository = InMemoryLimbahRepository()

    def test_save_limbah(self):
        """Test menyimpan limbah ke repository."""
        limbah = LimbahOrganik("L001", 100.0, 5)
        self.repository.save(limbah)

        all_limbah = self.repository.get_all()
        self.assertEqual(len(all_limbah), 1)
        self.assertEqual(all_limbah[0].get_id(), "L001")

    def test_save_multiple_limbah(self):
        """Test menyimpan beberapa limbah."""
        limbah1 = LimbahOrganik("L001", 100.0, 5)
        limbah2 = LimbahMedis("L002", 50.0, 8)
        limbah3 = LimbahB3("L003", 30.0, "Merkuri")

        self.repository.save(limbah1)
        self.repository.save(limbah2)
        self.repository.save(limbah3)

        all_limbah = self.repository.get_all()
        self.assertEqual(len(all_limbah), 3)

    def test_get_all_empty(self):
        """Test get_all ketika repository kosong."""
        all_limbah = self.repository.get_all()
        self.assertEqual(len(all_limbah), 0)
        self.assertIsInstance(all_limbah, list)

    def test_get_by_id_found(self):
        """Test mencari limbah berdasarkan ID yang ada."""
        limbah1 = LimbahOrganik("L001", 100.0, 5)
        limbah2 = LimbahMedis("L002", 50.0, 8)

        self.repository.save(limbah1)
        self.repository.save(limbah2)

        found = self.repository.get_by_id("L001")
        self.assertIsNotNone(found)
        self.assertEqual(found.get_id(), "L001")
        self.assertIsInstance(found, LimbahOrganik)

    def test_get_by_id_not_found(self):
        """Test mencari limbah berdasarkan ID yang tidak ada."""
        limbah = LimbahOrganik("L001", 100.0, 5)
        self.repository.save(limbah)

        found = self.repository.get_by_id("L999")
        self.assertIsNone(found)

    def test_get_by_id_empty_repository(self):
        """Test get_by_id pada repository kosong."""
        found = self.repository.get_by_id("L001")
        self.assertIsNone(found)

    def test_repository_isolation(self):
        """Test bahwa setiap instance repository terpisah."""
        repo1 = InMemoryLimbahRepository()
        repo2 = InMemoryLimbahRepository()

        limbah = LimbahOrganik("L001", 100.0, 5)
        repo1.save(limbah)

        self.assertEqual(len(repo1.get_all()), 1)
        self.assertEqual(len(repo2.get_all()), 0)


if __name__ == "__main__":
    unittest.main()
