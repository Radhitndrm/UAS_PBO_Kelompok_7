class Lokasi:
    """
    Kelas Lokasi.

    Merepresentasikan lokasi terjadinya bencana.
    """

    def __init__(self, id: str, nama: str, jenis_bencana: str):
        """
        Inisialisasi lokasi bencana.

        Args:
            id (str): ID lokasi.
            nama (str): Nama lokasi.
            jenis_bencana (str): Jenis bencana.
        """
        self.__id = id
        self.__nama = nama
        self.__jenis_bencana = jenis_bencana

    def get_info(self):
        """
        Mengambil informasi lokasi.

        Returns:
            dict: Data lokasi bencana.
        """
        return {
            "id": self.__id,
            "nama": self.__nama,
            "jenis_bencana": self.__jenis_bencana
        }
