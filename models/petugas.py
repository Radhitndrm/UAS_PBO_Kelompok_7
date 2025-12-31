class Petugas:
    """
    Kelas Petugas.

    Merepresentasikan petugas yang menangani limbah.

    Attributes:
        __id (str): ID unik petugas.
        __nama (str): Nama petugas.
        __keahlian (str): Keahlian petugas.
    """

    def __init__(self, id: str, nama: str, keahlian: str):
        """
        Inisialisasi petugas.

        Args:
            id (str): ID petugas.
            nama (str): Nama petugas.
            keahlian (str): Keahlian petugas.

        Raises:
            ValueError: Jika id, nama, atau keahlian kosong.
        """
        if not id or not id.strip():
            raise ValueError("ID petugas tidak boleh kosong")
        if not nama or not nama.strip():
            raise ValueError("Nama petugas tidak boleh kosong")
        if not keahlian or not keahlian.strip():
            raise ValueError("Keahlian petugas tidak boleh kosong")

        self.__id = id.strip()
        self.__nama = nama.strip()
        self.__keahlian = keahlian.strip()

    def get_id(self) -> str:
        """
        Mengambil ID petugas.

        Returns:
            str: ID petugas.
        """
        return self.__id

    def get_nama(self) -> str:
        """
        Mengambil nama petugas.

        Returns:
            str: Nama petugas.
        """
        return self.__nama

    def get_keahlian(self) -> str:
        """
        Mengambil keahlian petugas.

        Returns:
            str: Keahlian petugas.
        """
        return self.__keahlian

    def set_nama(self, nama: str) -> None:
        """
        Mengatur nama petugas.

        Args:
            nama (str): Nama petugas baru.

        Raises:
            ValueError: Jika nama kosong.
        """
        if not nama or not nama.strip():
            raise ValueError("Nama petugas tidak boleh kosong")
        self.__nama = nama.strip()

    def set_keahlian(self, keahlian: str) -> None:
        """
        Mengatur keahlian petugas.

        Args:
            keahlian (str): Keahlian petugas baru.

        Raises:
            ValueError: Jika keahlian kosong.
        """
        if not keahlian or not keahlian.strip():
            raise ValueError("Keahlian petugas tidak boleh kosong")
        self.__keahlian = keahlian.strip()

    def get_info(self) -> dict:
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

    def __str__(self) -> str:
        """
        Representasi string dari objek Petugas.

        Returns:
            str: Deskripsi petugas dalam format yang mudah dibaca.
        """
        return f"Petugas(ID: {self.__id}, Nama: {self.__nama}, Keahlian: {self.__keahlian})"
