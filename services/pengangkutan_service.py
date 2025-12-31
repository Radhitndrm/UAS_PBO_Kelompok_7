import logging
from datetime import datetime
from typing import Optional

from models.limbah import Limbah
from repositories.limbah_repository import LimbahRepository

logger = logging.getLogger(__name__)

class PengangkutanService:
    """
    Service untuk proses bisnis pengangkutan limbah.

    Mengelola alur pengankutan limbah, meliputi:
    - validasi input pengangkutan (ID limbah, kendaraan, tujuan)
    - pengecekan ketersediaan limbah berdasarkan ID
    - perubahan status limbah menjadi "Diangkut" jika memenuhi syarat
    - pembuatan catatan pengangkutan dengan timestamp untuk keperluan audit/log
    """

    def __init__(self, limbah_repository: LimbahRepository):
        """
        Inisialisasi PengangkutanService.

        Args:
            limbah_repository (LimbahRepository): repository limbah (abstrak).
        """
        self.__limbah_repository = limbah_repository

    def __cari_limbah_by_id(self, id: str) -> Optional[Limbah]:
        """
        Mencari limbah berdasarkan ID pada repository.

        Args:
            id (str): ID limbah.

        Returns:
            Optional[Limbah]: Objek limbah jika ditemukan, jika tidak maka None.
        """
        for item in self.__limbah_repository.get_all():
            if item.get_id() == id:
                return item
        return None

    def __validate_kendaraan(self, kendaraan: str) -> None:
        """
        Validasi input kendaraan.

        Args:
            kendaraan (str): Nama/jenis kendaraan.

        Raises:
            ValueError: Jika kendaraan bukan string atau kosong.
        """
        if not isinstance(kendaraan, str) or not kendaraan.strip():
            logger.error("Validasi gagal: kendaraan tidak valid: %r", kendaraan)
            raise ValueError("Nama/tipe kendaraan wajib string dan tidak boleh kosong")

    def angkut_limbah(self, id_limbah: str, kendaraan: str, tujuan: str) -> dict:
        """
        Melakukan proses pengangkutan limbah dan membuat catatan pengangkutan.

        Args:
            id_limbah (str): ID limbah yang diangkut.
            kendaraan (str): Nama/jenis kendaraan.
            tujuan (str): Tujuan pengangkutan (contoh: TPS, insinerator, fasilitas B3).

        Returns:
            dict: Data catatan pengangkutan (audit log sederhana).

        Raises:
            ValueError: Jika input tidak valid atau limbah tidak memenuhi syarat untuk diangkut.
            LookupError: Jika limbah tidak ditemukan.
        """
        if not isinstance(id_limbah, str) or not id_limbah.strip():
            logger.error("Validasi gagal: id_limbah tidak valid: %r", id_limbah)
            raise ValueError("ID limbah wajib string dan tidak boleh kosong")

        self.__validate_kendaraan(kendaraan)

        if not isinstance(tujuan, str) or not tujuan.strip():
            logger.error("Validasi gagal: tujuan tidak valid: %r", tujuan)
            raise ValueError("Tujuan wajib string dan tidak boleh kosong")

        limbah = self.__cari_limbah_by_id(id_limbah)
        if limbah is None:
            logger.error("Pengangkutan gagal: limbah tidak ditemukan | id=%s", id_limbah)
            raise LookupError(f"Limbah dengan id '{id_limbah}' tidak ditemukan")

        status = limbah.get_status()
        if status in ("Dimusnahkan", "Didaur Ulang", "Diproses Khusus"):
            logger.warning(
                "Pengangkutan ditolak: limbah sudah diproses | id=%s status=%s",
                id_limbah, status
            )
            raise ValueError(f"Limbah id '{id_limbah}' sudah diproses (status: {status}) dan tidak bisa diangkut")

        limbah.set_status("Diangkut")
        ts = datetime.now().isoformat()

        catatan = {
            "timestamp": ts,
            "id_limbah": limbah.get_id(),
            "volume": limbah.get_volume(),
            "status_baru": limbah.get_status(),
            "kendaraan": kendaraan,
            "tujuan": tujuan,
        }

        logger.info(
            "Pengangkutan sukses | id=%s kendaraan=%s tujuan=%s ts=%s",
            limbah.get_id(), kendaraan, tujuan, ts
        )
        return catatan
