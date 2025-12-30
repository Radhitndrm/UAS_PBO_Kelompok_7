from models.limbah import Limbah

class LimbahB3(Limbah):
    """
    Kelas LimbahB3 (Bahan Berbahaya dan Beracun).

    Digunakan untuk limbah dengan kandungan kimia berbahaya
    yang membutuhkan penanganan khusus.
    """

    def __init__(self, id: str, volume: float, kandungan_kimia: str):
        """
        Inisialisasi Limbah B3.

        Args:
            id (str): ID limbah.
            volume (float): Volume limbah.
            kandungan_kimia (str): Jenis kandungan kimia.
        """
        super().__init__(id, volume)
        self.__kandungan_kimia = kandungan_kimia

    def hitung_risiko(self) -> float:
        """
        Menghitung risiko limbah B3.

        Returns:
            float: Nilai risiko limbah B3.
        """
        return self.volume * 2.0

    def proses_pengolahan(self):
        """
        Proses pengolahan limbah B3 secara khusus.

        Returns:
            str: Informasi proses pengolahan.
        """
        self.set_status("Diproses Khusus")
        return f"Limbah B3 dengan kandungan {self.__kandungan_kimia} diproses secara khusus"
