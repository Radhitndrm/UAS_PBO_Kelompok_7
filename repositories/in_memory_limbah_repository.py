from repositories.limbah_repository import LimbahRepository
from models.limbah import Limbah

class InMemoryLimbahRepository(LimbahRepository):
    """
    Repository penyimpanan limbah berbasis list.
    """

    def __init__(self):
        self.__data: list[Limbah] = []

    def save(self, limbah: Limbah) -> None:
        self.__data.append(limbah)

    def get_all(self) -> list[Limbah]:
        return self.__data
