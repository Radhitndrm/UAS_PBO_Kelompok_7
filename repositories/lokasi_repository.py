from abc import ABC, abstractmethod
from models.lokasi import Lokasi


class LokasiRepository(ABC):
    """
    Interface (Abstract Base Class) untuk penyimpanan data Lokasi.

    Prinsip:
    - SRP: Repository hanya bertanggung jawab pada penyimpanan Lokasi
    - DIP: Service bergantung pada abstraksi, bukan implementasi konkret
    """

    @abstractmethod
    def save(self, lokasi: Lokasi) -> None:
        """
        Menyimpan data lokasi.

        Args:
            lokasi (Lokasi): objek lokasi bencana
        """
        pass

    @abstractmethod
    def get_all(self) -> list[Lokasi]:
        """
        Mengambil seluruh data lokasi.

        Returns:
            list[Lokasi]: daftar lokasi yang tersimpan
        """
        pass
