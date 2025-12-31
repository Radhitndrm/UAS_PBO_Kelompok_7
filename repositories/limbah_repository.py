from abc import ABC, abstractmethod
from typing import Optional
from models.limbah import Limbah

class LimbahRepository(ABC):
    """
    Interface repository untuk Limbah.

    Mendefinisikan kontrak untuk operasi penyimpanan dan pengambilan
    data limbah (Dependency Inversion Principle).
    """

    @abstractmethod
    def save(self, limbah: Limbah) -> None:
        """
        Menyimpan objek limbah ke repository.

        Args:
            limbah (Limbah): Objek limbah yang akan disimpan.
        """
        pass

    @abstractmethod
    def get_all(self) -> list[Limbah]:
        """
        Mengambil semua data limbah dari repository.

        Returns:
            list[Limbah]: Daftar semua limbah.
        """
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[Limbah]:
        """
        Mencari limbah berdasarkan ID.

        Args:
            id (str): ID limbah yang dicari.

        Returns:
            Optional[Limbah]: Objek limbah jika ditemukan, None jika tidak.
        """
        pass
