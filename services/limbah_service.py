import logging
from datetime import datetime
from typing import Optional

from models.limbah import Limbah
from models.limbah_b3 import LimbahB3
from models.limbah_medis import LimbahMedis
from models.limbah_organik import LimbahOrganik
from repositories.limbah_repository import LimbahRepository
from utils.validator import validate_volume

logger = logging.getLogger(__name__)

class LimbahService:
    """
    Service untuk proses bisnis Limbah.

    Mengelola alur utama terkait limbah, seperti:
    - registrasi limbah berdasarkan jenisnya
    - validasi input sebelum membuat objek limbah
    - pengambilan data limbah dari penyimpanan
    - perhitungan total risiko
    - menjalankan proses pengolahan dan memperbarui status limbah
    """

    def __init__(self, limbah_repository: LimbahRepository):
        """
        Inisialisasi LimbahService.

        Args:
            limbah_repository (LimbahRepository): repository abstrak untuk penyimpanan limbah.
        """
        self.__limbah_repository = limbah_repository

    def __validate_id(self, id: str) -> None:
        """
        Validasi ID limbah.

        Args:
            id (str): ID limbah.

        Raises:
            ValueError: Jika id bukan string atau kosong.
        """
        if not isinstance(id, str) or not id.strip():
            logger.error("Validasi gagal: id limbah tidak valid: %r", id)
            raise ValueError("ID limbah wajib berupa string dan tidak boleh kosong")

    def __validate_volume(self, volume: float) -> None:
        """
        Validasi volume limbah menggunakan utility validator.

        Args:
            volume (float): Volume limbah.

        Raises:
            ValueError: Jika volume bukan angka atau < 0.
        """
        if not isinstance(volume, (int, float)):
            logger.error("Validasi gagal: volume harus angka, dapat: %r", type(volume))
            raise ValueError("Volume limbah harus berupa angka")

        # Gunakan validator dari utils
        try:
            validate_volume(volume)
        except ValueError as e:
            logger.error("Validasi gagal: %s", str(e))
            raise

    def __validate_tingkat_infeksi(self, tingkat_infeksi: int) -> None:
        """
        Validasi tingkat infeksi limbah medis.

        Args:
            tingkat_infeksi (int): Tingkat infeksi.

        Raises:
            ValueError: Jika tingkat_infeksi bukan integer atau < 1.
        """
        if not isinstance(tingkat_infeksi, int):
            logger.error("Validasi gagal: tingkat_infeksi harus int, dapat: %r", type(tingkat_infeksi))
            raise ValueError("Tingkat infeksi harus berupa integer")
        if tingkat_infeksi < 1:
            logger.error("Validasi gagal: tingkat_infeksi < 1, dapat: %r", tingkat_infeksi)
            raise ValueError("Tingkat infeksi minimal 1")

    def __validate_tingkat_pembusukan(self, tingkat_pembusukan: int) -> None:
        """
        Validasi tingkat pembusukan limbah organik.

        Args:
            tingkat_pembusukan (int): Tingkat pembusukan.

        Raises:
            ValueError: Jika tingkat_pembusukan bukan integer atau < 1.
        """
        if not isinstance(tingkat_pembusukan, int):
            logger.error("Validasi gagal: tingkat_pembusukan harus int, dapat: %r", type(tingkat_pembusukan))
            raise ValueError("Tingkat pembusukan harus berupa integer")
        if tingkat_pembusukan < 1:
            logger.error("Validasi gagal: tingkat_pembusukan < 1, dapat: %r", tingkat_pembusukan)
            raise ValueError("Tingkat pembusukan minimal 1")

    def __validate_kandungan_kimia(self, kandungan_kimia: str) -> None:
        """
        Validasi kandungan kimia limbah B3.

        Args:
            kandungan_kimia (str): Kandungan kimia.

        Raises:
            ValueError: Jika kandungan_kimia bukan string atau kosong.
        """
        if not isinstance(kandungan_kimia, str) or not kandungan_kimia.strip():
            logger.error("Validasi gagal: kandungan_kimia tidak valid: %r", kandungan_kimia)
            raise ValueError("Kandungan kimia wajib berupa string dan tidak boleh kosong")

    def registrasi_limbah_medis(self, id: str, volume: float, tingkat_infeksi: int) -> LimbahMedis:
        """
        Registrasi limbah medis dan simpan ke repository.

        Args:
            id (str): ID limbah.
            volume (float): volume limbah.
            tingkat_infeksi (int): tingkat infeksi.

        Returns:
            LimbahMedis: objek limbah medis yang tersimpan.
        """
        self.__validate_id(id)
        self.__validate_volume(volume)
        self.__validate_tingkat_infeksi(tingkat_infeksi)

        limbah = LimbahMedis(id=id, volume=volume, tingkat_infeksi=tingkat_infeksi)
        self.__limbah_repository.save(limbah)

        logger.info(
            "Registrasi LimbahMedis sukses | id=%s volume=%.2f tingkat_infeksi=%d ts=%s",
            id, volume, tingkat_infeksi, datetime.now().isoformat()
        )
        return limbah

    def registrasi_limbah_organik(self, id: str, volume: float, tingkat_pembusukan: int) -> LimbahOrganik:
        """
        Membuat dan menyimpan objek LimbahOrganik ke repository.

        Args:
            id (str): ID limbah.
            volume (float): Volume limbah.
            tingkat_pembusukan (int): Tingkat pembusukan limbah.

        Returns:
            LimbahOrganik: Objek LimbahOrganik yang berhasil dibuat dan disimpan.

        Raises:
            ValueError: Jika validasi input gagal.
        """
        self.__validate_id(id)
        self.__validate_volume(volume)
        self.__validate_tingkat_pembusukan(tingkat_pembusukan)

        limbah = LimbahOrganik(id=id, volume=volume, tingkat_pembusukan=tingkat_pembusukan)
        self.__limbah_repository.save(limbah)

        logger.info(
            "Registrasi LimbahOrganik sukses | id=%s volume=%.2f tingkat_pembusukan=%d ts=%s",
            id, volume, tingkat_pembusukan, datetime.now().isoformat()
        )
        return limbah

    def registrasi_limbah_b3(self, id: str, volume: float, kandungan_kimia: str) -> LimbahB3:
        """
        Membuat dan menyimpan objek LimbahB3 ke repository.

        Args:
            id (str): ID limbah.
            volume (float): Volume limbah.
            kandungan_kimia (str): Kandungan kimia limbah B3.

        Returns:
            LimbahB3: Objek LimbahB3 yang berhasil dibuat dan disimpan.

        Raises:
            ValueError: Jika validasi input gagal.
        """
        self.__validate_id(id)
        self.__validate_volume(volume)
        self.__validate_kandungan_kimia(kandungan_kimia)

        limbah = LimbahB3(id=id, volume=volume, kandungan_kimia=kandungan_kimia)
        self.__limbah_repository.save(limbah)

        logger.info(
            "Registrasi LimbahB3 sukses | id=%s volume=%.2f kandungan_kimia=%s ts=%s",
            id, volume, kandungan_kimia, datetime.now().isoformat()
        )
        return limbah

    def get_semua_limbah(self) -> list[Limbah]:
        """
        Mencari limbah berdasarkan ID.

        Args:
            id (str): ID limbah.

        Returns:
            Optional[Limbah]: Objek limbah jika ditemukan, jika tidak maka None.

        Raises:
            ValueError: Jika id tidak valid.
        """
        data = self.__limbah_repository.get_all()
        logger.info("Ambil semua limbah | total=%d ts=%s", len(data), datetime.now().isoformat())
        return data

    def cari_limbah_by_id(self, id: str) -> Optional[Limbah]:
        """
        Mencari limbah berdasarkan ID menggunakan repository.

        Args:
            id (str): ID limbah.

        Returns:
            Optional[Limbah]: objek limbah jika ditemukan, else None.
        """
        self.__validate_id(id)

        limbah = self.__limbah_repository.get_by_id(id)

        if limbah:
            logger.info("Limbah ditemukan | id=%s ts=%s", id, datetime.now().isoformat())
        else:
            logger.warning("Limbah tidak ditemukan | id=%s ts=%s", id, datetime.now().isoformat())

        return limbah

    def hitung_total_risiko(self) -> float:
        """
        Menghitung total risiko dari seluruh limbah yang tersimpan.

        Returns:
            float: Total risiko.
        """
        total = 0.0
        for item in self.__limbah_repository.get_all():
            total += item.hitung_risiko()

        logger.info("Hitung total risiko | total=%.2f ts=%s", total, datetime.now().isoformat())
        return total

    def proses_pengolahan_limbah(self, id: str) -> str:
        """
        Menjalankan proses pengolahan untuk limbah tertentu berdasarkan ID.

        Args:
            id (str): ID limbah.

        Returns:
            str: Informasi hasil proses pengolahan.

        Raises:
            ValueError: Jika id tidak valid.
            LookupError: Jika limbah tidak ditemukan.
        """
        limbah = self.cari_limbah_by_id(id)
        if limbah is None:
            logger.error("Proses pengolahan gagal: limbah tidak ditemukan | id=%s", id)
            raise LookupError(f"Limbah dengan id '{id}' tidak ditemukan")

        hasil = limbah.proses_pengolahan()
        logger.info("Proses pengolahan sukses | id=%s status=%s ts=%s", id, limbah.get_status(), datetime.now().isoformat())
        return hasil
