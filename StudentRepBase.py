from abc import ABC, abstractmethod
import json
import yaml 


class StudentRepBase(ABC):
    """Базовый класс для репозиториев с общей логикой работы с данными."""

    def __init__(self, file_path: str, strategy: StudentStrategy):
        self.file_path = file_path
        self.strategy = strategy
        self.data = self.strategy.load(self.file_path)

    def load_data(self):
        """Загрузка данных из файла."""
        self.data = self.strategy.load(self.file_path)

    def save_data(self):
        """Сохранение данных в файл."""
        self.strategy.save(self.file_path, self.data)

    def get_all(self) -> list:
        """Получить все объекты."""
        return self.data

    def get_by_id(self, student_id: int) -> dict:
        """Получить объект по ID."""
        for student in self.data:
            if student.get("id") == student_id:
                return student
        raise ValueError(f"Объект с ID {student_id} не найден.")

    def add_student(self, student: dict):
        """Добавить объект в репозиторий."""
        new_id = max((item.get("id", 0) for item in self.data), default=0) + 1
        student["id"] = new_id
        self.data.append(student)
        self.save_data()

    def delete_by_id(self, student_id: int):
        """Удалить объект по ID."""
        self.data = [student for student in self.data if student.get("id") != student_id]
        self.save_data()

    def replace_by_id(self, student_id: int, updates: dict):
        """Заменить объект по ID."""
        student = self.get_by_id(student_id)
        valid_keys = {"id", "first_name", "last_name", "patronymic", "phone", "address"}
        updates = {k: v for k, v in updates.items() if k in valid_keys}
        student.update(updates)
        self.save_data()

    def get_k_n_short_list(self, k: int, n: int) -> list[StudentBrief]:
        """Получить k по счету n объектов."""
        start_index = (n - 1) * k
        end_index = start_index + k
        return self.data[start_index:end_index]

    def sort_by_field(self, field: str, reverse: bool = False) -> List[Product]:
        """Сортировать данные по указанному полю."""
        if not self.data or field not in self.data[0]:
            raise ValueError(f"Invalid field '{field}' for sorting.")
        self._data.sort(key=lambda x: x.get(field), reverse=reverse)
        return [Student.create_from_dict(student) for student in self._data]

    def get_count(self) -> int:
        """Получить количество объектов."""
        return len(self.data)
