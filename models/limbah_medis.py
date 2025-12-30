from models.limbah import Limbah

class LimbahMedis(Limbah):
    """
    Kelas LimbahMedis.

    Digunakan untuk menangani limbah medis yang memiliki
    tingkat risiko tinggi akibat infeksi.
    """

    def __init__(self, id: str, volume: float, tingkat_infeksi: int):
        """
        Inisialisasi Limbah Medis.

        Args:
            id (str): ID limbah.
            volume (float): Volume limbah.
            tingkat_infeksi (int): Tingkat infeksi limbah.
        """
        super().__init__(id, volume)
        self.__tingkat_infeksi = tingkat_infeksi

    def hitung_risiko(self) -> float:
        """
        Menghitung risiko limbah medis berdasarkan tingkat infeksi.

        Returns:
            float: Nilai risiko limbah medis.
        """
        return self.volume * self.__tingkat_infeksi * 1.5

    def proses_pengolahan(self):
        """
        Proses pengolahan limbah medis dengan metode pemusnahan.

        Returns:
            str: Informasi proses pengolahan.
        """
        self.set_status("Dimusnahkan")
        return "Limbah medis dimusnahkan dengan insinerator"
