from typing import Optional
from repositories.limbah_repository import LimbahRepository
from models.limbah import Limbah

class InMemoryLimbahRepository(LimbahRepository):
    """
    Repository penyimpanan limbah berbasis list in-memory.

    Implementasi konkret dari LimbahRepository untuk penyimpanan
    sementara di memori (runtime).
    """

    def __init__(self):
        """
        Inisialisasi repository dengan list kosong.
        """
        self.__data: list[Limbah] = []

    def save(self, limbah: Limbah) -> None:
        """
        Menyimpan objek limbah ke list.

        Args:
            limbah (Limbah): Objek limbah yang akan disimpan.
        """
        self.__data.append(limbah)

    def get_all(self) -> list[Limbah]:
        """
        Mengambil semua data limbah.

        Returns:
            list[Limbah]: Daftar semua limbah yang tersimpan.
        """
        return self.__data

    def get_by_id(self, id: str) -> Optional[Limbah]:
        """
        Mencari limbah berdasarkan ID.

        Args:
            id (str): ID limbah yang dicari.

        Returns:
            Optional[Limbah]: Objek limbah jika ditemukan, None jika tidak.
        """
        for limbah in self.__data:
            if limbah.get_id() == id:
                return limbah
        return None
