class Petugas:
    """
    Kelas Petugas.

    Merepresentasikan petugas yang menangani limbah.
    """

    def __init__(self, id: str, nama: str, keahlian: str):
        """
        Inisialisasi petugas.

        Args:
            id (str): ID petugas.
            nama (str): Nama petugas.
            keahlian (str): Keahlian petugas.
        """
        self.__id = id
        self.__nama = nama
        self.__keahlian = keahlian

    def get_keahlian(self):
        """
        Mengambil keahlian petugas.

        Returns:
            str: Keahlian petugas.
        """
        return self.__keahlian

    def get_info(self):
        """
        Mengambil informasi petugas.

        Returns:
            dict: Data petugas.
        """
        return {
            "id": self.__id,
            "nama": self.__nama,
            "keahlian": self.__keahlian
        }
