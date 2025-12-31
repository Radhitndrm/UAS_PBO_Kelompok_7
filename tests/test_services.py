"""
Unit test untuk services.

Menguji fungsionalitas business logic di LimbahService dan PengangkutanService.
"""

import unittest
from unittest.mock import Mock
from repositories.in_memory_limbah_repository import InMemoryLimbahRepository
from services.limbah_service import LimbahService
from services.pengangkutan_service import PengangkutanService
from models.limbah_organik import LimbahOrganik
from models.limbah_medis import LimbahMedis
from models.limbah_b3 import LimbahB3


class TestLimbahService(unittest.TestCase):
    """Test case untuk class LimbahService."""

    def setUp(self):
        """Setup yang dijalankan sebelum setiap test."""
        self.repository = InMemoryLimbahRepository()
        self.service = LimbahService(self.repository)

    def test_registrasi_limbah_organik_success(self):
        """Test registrasi limbah organik berhasil."""
        limbah = self.service.registrasi_limbah_organik("L001", 100.0, 5)

        self.assertIsNotNone(limbah)
        self.assertEqual(limbah.get_id(), "L001")
        self.assertEqual(limbah.get_volume(), 100.0)
        self.assertEqual(limbah.get_tingkat_pembusukan(), 5)

    def test_registrasi_limbah_organik_invalid_id(self):
        """Test registrasi limbah organik dengan ID invalid."""
        with self.assertRaises(ValueError):
            self.service.registrasi_limbah_organik("", 100.0, 5)

    def test_registrasi_limbah_organik_invalid_volume(self):
        """Test registrasi limbah organik dengan volume invalid."""
        with self.assertRaises(ValueError):
            self.service.registrasi_limbah_organik("L001", -10.0, 5)

    def test_registrasi_limbah_organik_invalid_tingkat_pembusukan(self):
        """Test registrasi limbah organik dengan tingkat pembusukan invalid."""
        with self.assertRaises(ValueError):
            self.service.registrasi_limbah_organik("L001", 100.0, 0)

    def test_registrasi_limbah_medis_success(self):
        """Test registrasi limbah medis berhasil."""
        limbah = self.service.registrasi_limbah_medis("L002", 50.0, 8)

        self.assertIsNotNone(limbah)
        self.assertEqual(limbah.get_id(), "L002")
        self.assertEqual(limbah.get_volume(), 50.0)
        self.assertEqual(limbah.get_tingkat_infeksi(), 8)

    def test_registrasi_limbah_medis_invalid_tingkat_infeksi(self):
        """Test registrasi limbah medis dengan tingkat infeksi invalid."""
        with self.assertRaises(ValueError):
            self.service.registrasi_limbah_medis("L002", 50.0, 0)

    def test_registrasi_limbah_b3_success(self):
        """Test registrasi limbah B3 berhasil."""
        limbah = self.service.registrasi_limbah_b3("L003", 30.0, "Merkuri")

        self.assertIsNotNone(limbah)
        self.assertEqual(limbah.get_id(), "L003")
        self.assertEqual(limbah.get_volume(), 30.0)
        self.assertEqual(limbah.get_kandungan_kimia(), "Merkuri")

    def test_registrasi_limbah_b3_invalid_kandungan_kimia(self):
        """Test registrasi limbah B3 dengan kandungan kimia invalid."""
        with self.assertRaises(ValueError):
            self.service.registrasi_limbah_b3("L003", 30.0, "")

    def test_get_semua_limbah_empty(self):
        """Test get semua limbah ketika kosong."""
        semua_limbah = self.service.get_semua_limbah()
        self.assertEqual(len(semua_limbah), 0)

    def test_get_semua_limbah_with_data(self):
        """Test get semua limbah dengan data."""
        self.service.registrasi_limbah_organik("L001", 100.0, 5)
        self.service.registrasi_limbah_medis("L002", 50.0, 8)
        self.service.registrasi_limbah_b3("L003", 30.0, "Merkuri")

        semua_limbah = self.service.get_semua_limbah()
        self.assertEqual(len(semua_limbah), 3)

    def test_cari_limbah_by_id_found(self):
        """Test mencari limbah berdasarkan ID yang ada."""
        self.service.registrasi_limbah_organik("L001", 100.0, 5)

        found = self.service.cari_limbah_by_id("L001")
        self.assertIsNotNone(found)
        self.assertEqual(found.get_id(), "L001")

    def test_cari_limbah_by_id_not_found(self):
        """Test mencari limbah berdasarkan ID yang tidak ada."""
        found = self.service.cari_limbah_by_id("L999")
        self.assertIsNone(found)

    def test_cari_limbah_by_id_invalid_id(self):
        """Test mencari limbah dengan ID invalid."""
        with self.assertRaises(ValueError):
            self.service.cari_limbah_by_id("")

    def test_hitung_total_risiko_empty(self):
        """Test hitung total risiko ketika tidak ada limbah."""
        total = self.service.hitung_total_risiko()
        self.assertEqual(total, 0.0)

    def test_hitung_total_risiko_with_data(self):
        """Test hitung total risiko dengan data."""
        self.service.registrasi_limbah_organik("L001", 100.0, 5)  # 100 * 5 * 0.8 = 400
        self.service.registrasi_limbah_medis("L002", 50.0, 8)     # 50 * 8 * 1.5 = 600
        self.service.registrasi_limbah_b3("L003", 30.0, "Merkuri")  # 30 * 2.0 = 60

        total = self.service.hitung_total_risiko()
        expected = 400.0 + 600.0 + 60.0
        self.assertEqual(total, expected)

    def test_proses_pengolahan_limbah_success(self):
        """Test proses pengolahan limbah berhasil."""
        self.service.registrasi_limbah_organik("L001", 100.0, 5)

        hasil = self.service.proses_pengolahan_limbah("L001")
        self.assertIsNotNone(hasil)
        self.assertIn("kompos", hasil)

        limbah = self.service.cari_limbah_by_id("L001")
        self.assertEqual(limbah.get_status(), "Didaur Ulang")

    def test_proses_pengolahan_limbah_not_found(self):
        """Test proses pengolahan limbah yang tidak ditemukan."""
        with self.assertRaises(LookupError):
            self.service.proses_pengolahan_limbah("L999")


class TestPengangkutanService(unittest.TestCase):
    """Test case untuk class PengangkutanService."""

    def setUp(self):
        """Setup yang dijalankan sebelum setiap test."""
        self.repository = InMemoryLimbahRepository()
        self.limbah_service = LimbahService(self.repository)
        self.pengangkutan_service = PengangkutanService(self.repository)

    def test_angkut_limbah_success(self):
        """Test angkut limbah berhasil."""
        self.limbah_service.registrasi_limbah_organik("L001", 100.0, 5)

        catatan = self.pengangkutan_service.angkut_limbah(
            id_limbah="L001",
            kendaraan="Truk Besar",
            tujuan="TPS Kalibata"
        )

        self.assertIsNotNone(catatan)
        self.assertEqual(catatan["id_limbah"], "L001")
        self.assertEqual(catatan["kendaraan"], "Truk Besar")
        self.assertEqual(catatan["tujuan"], "TPS Kalibata")
        self.assertIn("waktu_angkut", catatan)

        # Cek status limbah berubah
        limbah = self.repository.get_by_id("L001")
        self.assertEqual(limbah.get_status(), "Dalam Pengangkutan")

    def test_angkut_limbah_not_found(self):
        """Test angkut limbah yang tidak ditemukan."""
        with self.assertRaises(LookupError):
            self.pengangkutan_service.angkut_limbah(
                id_limbah="L999",
                kendaraan="Truk",
                tujuan="TPS"
            )

    def test_angkut_limbah_invalid_id(self):
        """Test angkut limbah dengan ID invalid."""
        with self.assertRaises(ValueError):
            self.pengangkutan_service.angkut_limbah(
                id_limbah="",
                kendaraan="Truk",
                tujuan="TPS"
            )

    def test_angkut_limbah_empty_kendaraan(self):
        """Test angkut limbah dengan kendaraan kosong."""
        self.limbah_service.registrasi_limbah_organik("L001", 100.0, 5)

        with self.assertRaises(ValueError):
            self.pengangkutan_service.angkut_limbah(
                id_limbah="L001",
                kendaraan="",
                tujuan="TPS"
            )

    def test_angkut_limbah_empty_tujuan(self):
        """Test angkut limbah dengan tujuan kosong."""
        self.limbah_service.registrasi_limbah_organik("L001", 100.0, 5)

        with self.assertRaises(ValueError):
            self.pengangkutan_service.angkut_limbah(
                id_limbah="L001",
                kendaraan="Truk",
                tujuan=""
            )


if __name__ == "__main__":
    unittest.main()
