from abc import ABC, abstractmethod
from typing import List


class StudentStrategy(ABC):
    """Интерфейс стратегии для работы с хранилищем данных."""

    @abstractmethod
    def load(self, file_path: str) -> List[dict]:
        """Загрузка данных из файла."""
        pass

    @abstractmethod
    def save(self, file_path: str, data: List[dict]):
        """Сохранение данных в файл."""
        pass

    @abstractmethod
    def display(self):
        """Отображает содержимое файла."""
        pass
