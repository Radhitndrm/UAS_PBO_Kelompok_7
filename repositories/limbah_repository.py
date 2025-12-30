from abc import ABC, abstractmethod
from models.limbah import Limbah

class LimbahRepository(ABC):
    """
    Interface repository untuk Limbah.
    """

    @abstractmethod
    def save(self, limbah: Limbah) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[Limbah]:
        pass
