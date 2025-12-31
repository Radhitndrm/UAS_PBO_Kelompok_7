from abc import ABC, abstractmethod

class Limbah(ABC):
    """
    Abstract base class Limbah.

    Merepresentasikan entitas limbah secara umum pada sistem
    penanganan limbah pasca bencana. Kelas ini menjadi induk
    bagi seluruh jenis limbah (Medis, Organik, B3).

    Attributes:
        __id (str): ID unik limbah.
        __volume (float): Volume limbah.
        __status (str): Status penanganan limbah.
    """

    def __init__(self, id: str, volume: float):
        """
        Inisialisasi objek Limbah.

        Args:
            id (str): ID limbah.
            volume (float): Volume limbah.
        """
        self.__id = id
        self.volume = volume
        self.__status = "Terdaftar"

    def get_id(self):
        """
        Mengambil ID limbah.

        Returns:
            str: ID limbah.
        """
        return self.__id

    def get_volume(self):
        """
        Mengambil volume limbah.

        Returns:
            float: Volume limbah.
        """
        return self.__volume

    def get_status(self):
        """
        Mengambil status limbah.

        Returns:
            str: Status limbah.
        """
        return self.__status

    def set_volume(self, volume: float):
        """
        Mengatur volume limbah dengan validasi.

        Args:
            volume (float): Volume limbah baru.

        Raises:
            ValueError: Jika volume <= 0.
        """
        if volume <= 0:
            raise ValueError("Volume limbah harus lebih dari 0")
        self.__volume = volume

    def set_status(self, status: str):
        """
        Mengatur status limbah.

        Args:
            status (str): Status baru limbah.
        """
        self.__status = status

    volume = property(get_volume, set_volume)

    def __str__(self) -> str:
        """
        Representasi string dari objek Limbah untuk output yang dapat dibaca manusia.

        Returns:
            str: Deskripsi limbah dalam format yang mudah dibaca.
        """
        return f"{self.__class__.__name__}(ID: {self.__id}, Volume: {self.__volume} kg, Status: {self.__status})"

    @abstractmethod
    def hitung_risiko(self) -> float:
        """
        Menghitung tingkat risiko limbah.

        Returns:
            float: Nilai risiko limbah.
        """
        pass

    @abstractmethod
    def proses_pengolahan(self):
        """
        Melakukan proses pengolahan limbah sesuai jenisnya.
        """
        pass
