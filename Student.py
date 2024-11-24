import re
import json


class StudentBase:
    """Базовый класс для представления студента."""

    def __init__(self, student_id: int = None, first_name: str = '', last_name: str = '', patronymic: str = '', phone: str = ''):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.phone = phone

    # Статические методы валидации
    @staticmethod
    def validate_student_id(student_id: int) -> bool:
        return isinstance(student_id, int) and student_id > 0

    @staticmethod
    def validate_first_name(first_name: str) -> bool:
        return bool(first_name and re.match(r"^[a-zA-Zа-яА-ЯёЁ\s-]+$", first_name))

    @staticmethod
    def validate_last_name(last_name: str) -> bool:
        return bool(last_name and re.match(r"^[a-zA-Zа-яА-ЯёЁ\s-]+$", last_name))

    @staticmethod
    def validate_patronymic(patronymic: str) -> bool:
        return bool(patronymic and re.match(r"^[a-zA-Zа-яА-ЯёЁ\s-]+$", patronymic))

    @staticmethod
    def validate_phone(phone: str) -> bool:
        pattern = re.compile(r"^8 \(\d{3}\) \d{3}-\d{2}-\d{2}$")
        return bool(phone and pattern.match(phone))

    # Свойства с геттерами и сеттерами
    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value: int):
        if not self.validate_student_id(value):
            raise ValueError("Некорректный ID студента.")
        self.__student_id = value

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        if not self.validate_first_name(value):
            raise ValueError("Некорректное имя.")
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        if not self.validate_last_name(value):
            raise ValueError("Некорректная фамилия.")
        self.__last_name = value

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value: str):
        if not self.validate_patronymic(value):
            raise ValueError("Некорректное отчество.")
        self.__patronymic = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        if not self.validate_phone(value):
            raise ValueError("Некорректный номер телефона.")
        self.__phone = value

    # Методы создания объекта
    @staticmethod
    def from_string(student_str: str):
        parts = student_str.split(',')
        if len(parts) != 5:
            raise ValueError("Строка должна содержать 5 элементов, разделённых запятыми.")
        student_id = int(parts[0].strip())
        first_name, last_name, patronymic, phone = map(str.strip, parts[1:])
        return StudentBase(student_id, first_name, last_name, patronymic, phone)

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        return cls(
            student_id=data.get('student_id'),
            first_name=data['first_name'],
            last_name=data['last_name'],
            patronymic=data.get('patronymic', ''),
            phone=data['phone']
        )

    def __str__(self):
        return (f"Студент {self.last_name} {self.first_name} {self.patronymic}, "
                f"ID: {self.student_id}, Телефон: {self.phone}")


class Student(StudentBase):
    """Класс для представления студента с адресом."""

    def __init__(self, student_id: int = None, first_name: str = '', last_name: str = '', patronymic: str = '',
                 address: str = '', phone: str = ''):
        super().__init__(student_id, first_name, last_name, patronymic, phone)
        self.address = address

    @staticmethod
    def validate_address(address: str) -> bool:
        return bool(address and isinstance(address, str))

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value: str):
        if not self.validate_address(value):
            raise ValueError("Некорректный адрес.")
        self.__address = value

    def __str__(self):
        return (f"Студент {self.last_name} {self.first_name} {self.patronymic}, "
                f"ID: {self.student_id}, Адрес: {self.address}, Телефон: {self.phone}")


class StudentBrief(StudentBase):
    """Класс для краткой информации о студенте."""

    def __init__(self, student_id: int, first_name: str, last_name: str, patronymic: str, phone: str):
        super().__init__(student_id, first_name, last_name, patronymic, phone)

    @classmethod
    def from_student(cls, student: Student):
        """
        Создание объекта StudentBrief из объекта Student.
        Формат имени: "Фамилия И.О."
        """
        if not isinstance(student, Student):
            raise TypeError("Аргумент должен быть объектом класса Student.")
        return cls(
            student_id=student.student_id,
            first_name=student.first_name,
            last_name=student.last_name,
            patronymic=student.patronymic,
            phone=student.phone
        )

    def get_brief_name(self):
        """
        Возвращает фамилию и инициалы в формате "Фамилия И.О."
        """
        first_initial = f"{self.first_name[0]}." if self.first_name else ""
        patronymic_initial = f"{self.patronymic[0]}." if self.patronymic else ""
        return f"{self.last_name} {first_initial}{patronymic_initial}"

    def __str__(self):
        return f"Студент: {self.get_brief_name()}, ID: {self.student_id}, Телефон: {self.phone}"


# Пример использования классов
if __name__ == "__main__":
    # Создание объекта Student
    student = Student(
        student_id=1,
        first_name="Иван",
        last_name="Иванов",
        patronymic="Иванович",
        address="ул. Ленина, д.10",
        phone="8 (123) 456-78-90"
    )

    # Полная версия
    print(student)

    # Создание краткой версии StudentBrief
    student_brief = StudentBrief.from_student(student)
    print(student_brief)

    
