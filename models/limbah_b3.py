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

    def get_kandungan_kimia(self) -> str:
        """
        Mengambil kandungan kimia limbah B3.

        Returns:
            str: Jenis kandungan kimia.
        """
        return self.__kandungan_kimia

    def __str__(self) -> str:
        """
        Representasi string dari objek LimbahB3 untuk output yang dapat dibaca manusia.

        Returns:
            str: Deskripsi limbah B3 dalam format yang mudah dibaca.
        """
        return (f"LimbahB3(ID: {self.get_id()}, Volume: {self.get_volume()} kg, "
                f"Status: {self.get_status()}, Kandungan Kimia: {self.__kandungan_kimia}, "
                f"Risiko: {self.hitung_risiko():.2f})")

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
