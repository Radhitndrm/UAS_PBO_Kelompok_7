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

    def get_tingkat_infeksi(self) -> int:
        """
        Mengambil tingkat infeksi limbah medis.

        Returns:
            int: Tingkat infeksi.
        """
        return self.__tingkat_infeksi

    def __str__(self) -> str:
        """
        Representasi string dari objek LimbahMedis untuk output yang dapat dibaca manusia.

        Returns:
            str: Deskripsi limbah medis dalam format yang mudah dibaca.
        """
        return (f"LimbahMedis(ID: {self.get_id()}, Volume: {self.get_volume()} kg, "
                f"Status: {self.get_status()}, Tingkat Infeksi: {self.__tingkat_infeksi}, "
                f"Risiko: {self.hitung_risiko():.2f})")

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
