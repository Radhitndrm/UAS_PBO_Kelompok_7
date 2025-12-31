"""
Unit test untuk models.

Menguji fungsionalitas class Limbah dan turunannya
(LimbahOrganik, LimbahMedis, LimbahB3, Petugas, Lokasi).
"""

import unittest
from models.limbah_organik import LimbahOrganik
from models.limbah_medis import LimbahMedis
from models.limbah_b3 import LimbahB3
from models.petugas import Petugas
from models.lokasi import Lokasi


class TestLimbahOrganik(unittest.TestCase):
    """Test case untuk class LimbahOrganik."""

    def test_init_success(self):
        """Test inisialisasi limbah organik berhasil."""
        limbah = LimbahOrganik("L001", 100.0, 5)
        self.assertEqual(limbah.get_id(), "L001")
        self.assertEqual(limbah.get_volume(), 100.0)
        self.assertEqual(limbah.get_status(), "Terdaftar")
        self.assertEqual(limbah.get_tingkat_pembusukan(), 5)

    def test_hitung_risiko(self):
        """Test perhitungan risiko limbah organik."""
        limbah = LimbahOrganik("L001", 100.0, 5)
        # Risiko = volume * tingkat_pembusukan * 0.8
        expected = 100.0 * 5 * 0.8
        self.assertEqual(limbah.hitung_risiko(), expected)

    def test_proses_pengolahan(self):
        """Test proses pengolahan limbah organik."""
        limbah = LimbahOrganik("L001", 100.0, 5)
        hasil = limbah.proses_pengolahan()
        self.assertEqual(limbah.get_status(), "Didaur Ulang")
        self.assertEqual(hasil, "Limbah organik diproses menjadi kompos")

    def test_set_volume_valid(self):
        """Test mengubah volume dengan nilai valid."""
        limbah = LimbahOrganik("L001", 100.0, 5)
        limbah.volume = 150.0
        self.assertEqual(limbah.get_volume(), 150.0)

    def test_set_volume_invalid(self):
        """Test mengubah volume dengan nilai invalid."""
        limbah = LimbahOrganik("L001", 100.0, 5)
        with self.assertRaises(ValueError):
            limbah.volume = -10.0

    def test_str_representation(self):
        """Test representasi string limbah organik."""
        limbah = LimbahOrganik("L001", 100.0, 5)
        str_repr = str(limbah)
        self.assertIn("LimbahOrganik", str_repr)
        self.assertIn("L001", str_repr)
        self.assertIn("100.0", str_repr)


class TestLimbahMedis(unittest.TestCase):
    """Test case untuk class LimbahMedis."""

    def test_init_success(self):
        """Test inisialisasi limbah medis berhasil."""
        limbah = LimbahMedis("L002", 50.0, 8)
        self.assertEqual(limbah.get_id(), "L002")
        self.assertEqual(limbah.get_volume(), 50.0)
        self.assertEqual(limbah.get_tingkat_infeksi(), 8)

    def test_hitung_risiko(self):
        """Test perhitungan risiko limbah medis."""
        limbah = LimbahMedis("L002", 50.0, 8)
        # Risiko = volume * tingkat_infeksi * 1.5
        expected = 50.0 * 8 * 1.5
        self.assertEqual(limbah.hitung_risiko(), expected)

    def test_proses_pengolahan(self):
        """Test proses pengolahan limbah medis."""
        limbah = LimbahMedis("L002", 50.0, 8)
        hasil = limbah.proses_pengolahan()
        self.assertEqual(limbah.get_status(), "Dimusnahkan")
        self.assertEqual(hasil, "Limbah medis dimusnahkan dengan insinerator")


class TestLimbahB3(unittest.TestCase):
    """Test case untuk class LimbahB3."""

    def test_init_success(self):
        """Test inisialisasi limbah B3 berhasil."""
        limbah = LimbahB3("L003", 30.0, "Merkuri")
        self.assertEqual(limbah.get_id(), "L003")
        self.assertEqual(limbah.get_volume(), 30.0)
        self.assertEqual(limbah.get_kandungan_kimia(), "Merkuri")

    def test_hitung_risiko(self):
        """Test perhitungan risiko limbah B3."""
        limbah = LimbahB3("L003", 30.0, "Merkuri")
        # Risiko = volume * 2.0
        expected = 30.0 * 2.0
        self.assertEqual(limbah.hitung_risiko(), expected)

    def test_proses_pengolahan(self):
        """Test proses pengolahan limbah B3."""
        limbah = LimbahB3("L003", 30.0, "Merkuri")
        hasil = limbah.proses_pengolahan()
        self.assertEqual(limbah.get_status(), "Diproses Khusus")
        self.assertIn("Merkuri", hasil)


class TestPetugas(unittest.TestCase):
    """Test case untuk class Petugas."""

    def test_init_success(self):
        """Test inisialisasi petugas berhasil."""
        petugas = Petugas("P001", "Ahmad", "Pengangkutan")
        self.assertEqual(petugas.get_id(), "P001")
        self.assertEqual(petugas.get_nama(), "Ahmad")
        self.assertEqual(petugas.get_keahlian(), "Pengangkutan")

    def test_init_with_whitespace(self):
        """Test inisialisasi petugas dengan whitespace."""
        petugas = Petugas("  P001  ", "  Ahmad  ", "  Pengangkutan  ")
        self.assertEqual(petugas.get_id(), "P001")
        self.assertEqual(petugas.get_nama(), "Ahmad")
        self.assertEqual(petugas.get_keahlian(), "Pengangkutan")

    def test_init_empty_id(self):
        """Test inisialisasi dengan ID kosong."""
        with self.assertRaises(ValueError):
            Petugas("", "Ahmad", "Pengangkutan")

    def test_init_empty_nama(self):
        """Test inisialisasi dengan nama kosong."""
        with self.assertRaises(ValueError):
            Petugas("P001", "", "Pengangkutan")

    def test_init_empty_keahlian(self):
        """Test inisialisasi dengan keahlian kosong."""
        with self.assertRaises(ValueError):
            Petugas("P001", "Ahmad", "")

    def test_set_nama_valid(self):
        """Test mengubah nama petugas dengan nilai valid."""
        petugas = Petugas("P001", "Ahmad", "Pengangkutan")
        petugas.set_nama("Budi")
        self.assertEqual(petugas.get_nama(), "Budi")

    def test_set_nama_invalid(self):
        """Test mengubah nama petugas dengan nilai invalid."""
        petugas = Petugas("P001", "Ahmad", "Pengangkutan")
        with self.assertRaises(ValueError):
            petugas.set_nama("")

    def test_get_info(self):
        """Test mendapatkan informasi petugas."""
        petugas = Petugas("P001", "Ahmad", "Pengangkutan")
        info = petugas.get_info()
        self.assertEqual(info["id"], "P001")
        self.assertEqual(info["nama"], "Ahmad")
        self.assertEqual(info["keahlian"], "Pengangkutan")

    def test_str_representation(self):
        """Test representasi string petugas."""
        petugas = Petugas("P001", "Ahmad", "Pengangkutan")
        str_repr = str(petugas)
        self.assertIn("Petugas", str_repr)
        self.assertIn("P001", str_repr)
        self.assertIn("Ahmad", str_repr)


class TestLokasi(unittest.TestCase):
    """Test case untuk class Lokasi."""

    def test_init_success(self):
        """Test inisialisasi lokasi berhasil."""
        lokasi = Lokasi("LOK001", "Jakarta Barat", "Banjir")
        self.assertEqual(lokasi.get_id(), "LOK001")
        self.assertEqual(lokasi.get_nama(), "Jakarta Barat")
        self.assertEqual(lokasi.get_jenis_bencana(), "Banjir")

    def test_init_with_whitespace(self):
        """Test inisialisasi lokasi dengan whitespace."""
        lokasi = Lokasi("  LOK001  ", "  Jakarta Barat  ", "  Banjir  ")
        self.assertEqual(lokasi.get_id(), "LOK001")
        self.assertEqual(lokasi.get_nama(), "Jakarta Barat")
        self.assertEqual(lokasi.get_jenis_bencana(), "Banjir")

    def test_init_empty_id(self):
        """Test inisialisasi dengan ID kosong."""
        with self.assertRaises(ValueError):
            Lokasi("", "Jakarta Barat", "Banjir")

    def test_init_empty_nama(self):
        """Test inisialisasi dengan nama kosong."""
        with self.assertRaises(ValueError):
            Lokasi("LOK001", "", "Banjir")

    def test_init_empty_jenis_bencana(self):
        """Test inisialisasi dengan jenis bencana kosong."""
        with self.assertRaises(ValueError):
            Lokasi("LOK001", "Jakarta Barat", "")

    def test_set_nama_valid(self):
        """Test mengubah nama lokasi dengan nilai valid."""
        lokasi = Lokasi("LOK001", "Jakarta Barat", "Banjir")
        lokasi.set_nama("Jakarta Timur")
        self.assertEqual(lokasi.get_nama(), "Jakarta Timur")

    def test_set_jenis_bencana_valid(self):
        """Test mengubah jenis bencana dengan nilai valid."""
        lokasi = Lokasi("LOK001", "Jakarta Barat", "Banjir")
        lokasi.set_jenis_bencana("Gempa")
        self.assertEqual(lokasi.get_jenis_bencana(), "Gempa")

    def test_get_info(self):
        """Test mendapatkan informasi lokasi."""
        lokasi = Lokasi("LOK001", "Jakarta Barat", "Banjir")
        info = lokasi.get_info()
        self.assertEqual(info["id"], "LOK001")
        self.assertEqual(info["nama"], "Jakarta Barat")
        self.assertEqual(info["jenis_bencana"], "Banjir")

    def test_str_representation(self):
        """Test representasi string lokasi."""
        lokasi = Lokasi("LOK001", "Jakarta Barat", "Banjir")
        str_repr = str(lokasi)
        self.assertIn("Lokasi", str_repr)
        self.assertIn("LOK001", str_repr)
        self.assertIn("Jakarta Barat", str_repr)


if __name__ == "__main__":
    unittest.main()
