from models.limbah import Limbah

class LimbahOrganik(Limbah):
    """
    Kelas LimbahOrganik.

    Digunakan untuk limbah yang dapat terurai secara alami
    dan berpotensi untuk didaur ulang.
    """

    def __init__(self, id: str, volume: float, tingkat_pembusukan: int):
        """
        Inisialisasi Limbah Organik.

        Args:
            id (str): ID limbah.
            volume (float): Volume limbah.
            tingkat_pembusukan (int): Tingkat pembusukan limbah.
        """
        super().__init__(id, volume)
        self.__tingkat_pembusukan = tingkat_pembusukan

    def get_tingkat_pembusukan(self) -> int:
        """
        Mengambil tingkat pembusukan limbah organik.

        Returns:
            int: Tingkat pembusukan.
        """
        return self.__tingkat_pembusukan

    def __str__(self) -> str:
        """
        Representasi string dari objek LimbahOrganik untuk output yang dapat dibaca manusia.

        Returns:
            str: Deskripsi limbah organik dalam format yang mudah dibaca.
        """
        return (f"LimbahOrganik(ID: {self.get_id()}, Volume: {self.get_volume()} kg, "
                f"Status: {self.get_status()}, Tingkat Pembusukan: {self.__tingkat_pembusukan}, "
                f"Risiko: {self.hitung_risiko():.2f})")

    def hitung_risiko(self) -> float:
        """
        Menghitung risiko limbah organik.

        Returns:
            float: Nilai risiko limbah organik.
        """
        return self.volume * self.__tingkat_pembusukan * 0.8

    def proses_pengolahan(self):
        """
        Proses pengolahan limbah organik dengan daur ulang.

        Returns:
            str: Informasi proses pengolahan.
        """
        self.set_status("Didaur Ulang")
        return "Limbah organik diproses menjadi kompos"
