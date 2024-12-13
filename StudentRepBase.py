from abc import ABC, abstractmethod
import json
import yaml 


class StudentRepBase(ABC):
    """Базовый класс для репозиториев с общей логикой работы с данными."""

    def __init__(self, strategy: StudentStrategy):
        self._data = []
        self.strategy = strategy
        self._valid_sort_fields = {'first_name', 'last_name', 'patronymic'}
        self.load_data()

    def load_data(self):
        """Загрузка данных из файла."""
        self.strategy.load(self.data)

    def save_data(self):
        """Сохранение данных в файл."""
        self.data = self.strategy.save()

    def get_all(self) -> list:
        """Получить все объекты."""
        return self.data

    def get_by_id(self, student_id: int) -> dict:
        """Получить объект по ID."""
        for student in self.data:
            if student.get("id") == student_id:
                return student
        raise ValueError(f"Объект с ID {student_id} не найден.")

    def add_student(self, student: Student):
        """Добавить объект в репозиторий."""
        student_dict = student.to_dict()
        students = [Student.create_from_dict(student) for student in self.data]
        if not self.check_unique_code(student, students):
            raise ValueError(f"Студент уже существует.")
        self.data.append(student_dict)

    def check_unique_code(self, student, students):
        for student_data in students:
            if student_data == student:
                 raise ValueError(f"Студент уже существует.")
        return True

    def delete_by_id(self, student_id: int):
        """Удалить объект по ID."""
        student = self.get_by_id(student_id)
        if not student:
            raise ValueError(f"Студент с ID {student_id} не найден.")
        self.data = [p for p in self.data if p['student_id'] != student_id]

    def replace_by_id(self, student_id: int, first_name=None, last_name=None, patronymic=None, phone=None, address=None):
        """Заменить объект по ID."""
        student = self.get_by_id(student_id)
        if not student:
            raise ValueError(f"Студент с ID {student_id} не найден.")

        students = [Student.create_from_dict(student) for student in self._data]
        if not self.check_unique_code(student, students):
            raise ValueError(f"Студент уже существует.")

        if first_name:
            student.first_name = first_name
        if last_name:
            student.last_name = last_name
        if patronymic:
            student.patronymic = patronymic
        if phone:
            student.phone = phone
        if address:
            student.address = address

        for i, p in enumerate(self.data):
            if p['student_id'] == student_id:
                self.data[i] = student.to_dict()
                break

    def get_k_n_short_list(self, k: int, n: int, sort_field: Optional[str] = None, sort_order: str = "ASC") -> list[StudentBrief]:
        """Получить k по счету n объектов."""
        if sort_field and sort_field not in self._valid_sort_fields:
            raise ValueError(f"Недопустимое поле сортировки. Допустимые поля: {', '.join(self._valid_sort_fields)}")
        if sort_order.upper() not in ("ASC", "DESC"):
            raise ValueError("Порядок сортировки должен быть ASC или DESC.")

        data = self._data.copy()
        # Применяем сортировку, если указано поле
        if sort_field:
            reverse = sort_order.upper() == "DESC"
            data.sort(key=lambda x: x[sort_field], reverse=reverse)
        start_index = (n - 1) * k
        end_index = start_index + k
        page_data = data[start_index:end_index]
        return [
            StudentBrief(
                student_id=student['student_id'],
                first_name=student['first_name'],
                last_name=student['last_name'],
                patronymic=student['patronymic'],
                phone=student['phone']
            )
            for student in page_data
        ]

    def sort_by_field(self, field: str, reverse: bool = False) -> List[Student]:
        """Сортировать данные по указанному полю."""
        if field not in ['student_id', 'first_name', 'last_name', 'patronymic', 'phone', 'address']:
            raise ValueError(f"Invalid field '{field}' for sorting.")
        self._data.sort(key=lambda x: x.get(field), reverse=reverse)
        return [Student.create_from_dict(student) for student in self._data]

    def get_count(self) -> int:
        """Получить количество объектов."""
        return len(self.data)

    def get_all_students(self) -> List[Student]:
        """Получить все продукты"""
        return [Student.create_from_dict(student) for student in self._data]
