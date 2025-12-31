class Lokasi:
    """
    Kelas Lokasi.

    Merepresentasikan lokasi terjadinya bencana.

    Attributes:
        __id (str): ID unik lokasi.
        __nama (str): Nama lokasi.
        __jenis_bencana (str): Jenis bencana yang terjadi.
    """

    def __init__(self, id: str, nama: str, jenis_bencana: str):
        """
        Inisialisasi lokasi bencana.

        Args:
            id (str): ID lokasi.
            nama (str): Nama lokasi.
            jenis_bencana (str): Jenis bencana.

        Raises:
            ValueError: Jika id, nama, atau jenis_bencana kosong.
        """
        if not id or not id.strip():
            raise ValueError("ID lokasi tidak boleh kosong")
        if not nama or not nama.strip():
            raise ValueError("Nama lokasi tidak boleh kosong")
        if not jenis_bencana or not jenis_bencana.strip():
            raise ValueError("Jenis bencana tidak boleh kosong")

        self.__id = id.strip()
        self.__nama = nama.strip()
        self.__jenis_bencana = jenis_bencana.strip()

    def get_id(self) -> str:
        """
        Mengambil ID lokasi.

        Returns:
            str: ID lokasi.
        """
        return self.__id

    def get_nama(self) -> str:
        """
        Mengambil nama lokasi.

        Returns:
            str: Nama lokasi.
        """
        return self.__nama

    def get_jenis_bencana(self) -> str:
        """
        Mengambil jenis bencana.

        Returns:
            str: Jenis bencana.
        """
        return self.__jenis_bencana

    def set_nama(self, nama: str) -> None:
        """
        Mengatur nama lokasi.

        Args:
            nama (str): Nama lokasi baru.

        Raises:
            ValueError: Jika nama kosong.
        """
        if not nama or not nama.strip():
            raise ValueError("Nama lokasi tidak boleh kosong")
        self.__nama = nama.strip()

    def set_jenis_bencana(self, jenis_bencana: str) -> None:
        """
        Mengatur jenis bencana.

        Args:
            jenis_bencana (str): Jenis bencana baru.

        Raises:
            ValueError: Jika jenis bencana kosong.
        """
        if not jenis_bencana or not jenis_bencana.strip():
            raise ValueError("Jenis bencana tidak boleh kosong")
        self.__jenis_bencana = jenis_bencana.strip()

    def get_info(self) -> dict:
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

    def __str__(self) -> str:
        """
        Representasi string dari objek Lokasi.

        Returns:
            str: Deskripsi lokasi dalam format yang mudah dibaca.
        """
        return f"Lokasi(ID: {self.__id}, Nama: {self.__nama}, Jenis Bencana: {self.__jenis_bencana})"
