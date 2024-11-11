import re
import json

class StudentBase:
    """
    Базовый класс для представления студента.
    Содержит общие атрибуты и методы для валидации.
    """
    def __init__(self, student_id: int, first_name: str, last_name: str, patronymic: str, phone: str):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.phone = phone
        
    # Статические методы валидации
    @staticmethod
    def validate_student_id(student_id: int):
        if not isinstance(student_id, int):
            raise TypeError("ID студента должен быть целым числом.")
        if student_id <= 0:
            raise ValueError("ID студента должен быть положительным целым числом.")
        return student_id
    @staticmethod
    def validate_first_name(first_name: str):
        if not isinstance(first_name, str):
            raise TypeError("Имя должно быть строкой.")
        if not first_name.strip():
            raise ValueError("Имя должно быть непустой строкой.")
        if not re.match(r"^[a-zA-Zа-яА-ЯёЁ\s-]+$", first_name):
            raise ValueError("Имя должно содержать только буквы, пробелы или дефисы и не должно включать цифры или специальные символы.")
        return first_name.strip().title()
    @staticmethod
    def validate_last_name(last_name: str):
        if not isinstance(last_name, str):
            raise TypeError("Фамилия должна быть строкой.")
        if not last_name.strip():
            raise ValueError("Фамилия должна быть непустой строкой.")
        return last_name.strip().title()
    @staticmethod
    def validate_patronymic(patronymic: str):
        if not isinstance(patronymic, str):
            raise TypeError("Отчество должно быть строкой.")
        if not patronymic.strip():
            raise ValueError("Отчество должно быть непустой строкой.")
        return patronymic.strip().title()
    @staticmethod
    def validate_phone(phone: str):
        if not isinstance(phone, str):
            raise TypeError("Телефон должен быть строкой.")
        if not phone.strip():
            raise ValueError("Телефон должен быть непустой строкой.")
        # Проверка соответствия формату 8 (***) ***-**-**
        pattern = re.compile(r"^8 \(\d{3}\) \d{3}-\d{2}-\d{2}$")
        if not pattern.match(phone.strip()):
            raise ValueError("Телефон должен соответствовать формату: 8 (***) ***-**-**.")
        return phone.strip()
        
    # Свойства
    @property
    def student_id(self):
        return self.__student_id
    @student_id.setter
    def student_id(self, value: int):
        self.__student_id = self.validate_student_id(value)
    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, value: str):
        self.__first_name = self.validate_first_name(value)
    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, value: str):
        self.__last_name = self.validate_last_name(value)
    @property
    def patronymic(self):
        return self.__patronymic
    @patronymic.setter
    def patronymic(self, value: str):
        self.__patronymic = self.validate_patronymic(value)
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, value: str):
        self.__phone = self.validate_phone(value)
        
    # Методы для создания объекта из строки и JSON
    @staticmethod
    def from_string(student_str: str):
        """
        Создание объекта студента из строки формата:
        "ID, Имя, Фамилия, Отчество, Телефон"
        Пример: "1, Иван, Иванов, Иванович, 8 (123) 456-78-90"
        """
        try:
            parts = student_str.split(',')
            if len(parts) != 5:
                raise ValueError("Строка должна содержать 5 элементов, разделённых запятыми.")
            student_id = int(parts[0].strip())
            first_name = parts[1].strip()
            last_name = parts[2].strip()
            patronymic = parts[3].strip()
            phone = parts[4].strip()
            return StudentBase(student_id, first_name, last_name, patronymic, phone)
        except Exception as e:
            raise ValueError(f"Ошибка при создании объекта из строки: {e}")
    @classmethod
    def from_json(cls, json_str: str):
        """
        Создание объекта студента из JSON-строки.
        """
        try:
            data = json.loads(json_str)
            return cls(
                student_id=data['student_id'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                patronymic=data.get('patronymic', ''),
                phone=data['phone']
            )
        except json.JSONDecodeError:
            raise ValueError("Некорректный формат JSON.")
        except KeyError as e:
            raise ValueError(f"Отсутствует необходимое поле в JSON: {e}")
            
    # Методы для вывода информации
    def __str__(self):
        """Полная версия информации о студенте """
        return (f"Студент {self.last_name} {self.first_name} {self.patronymic}, "
                f"ID: {self.student_id}, Телефон: {self.phone}")
    def brief_info(self):
        """Краткая версия информации о студенте """
        return (f"ID: {self.student_id}, "
                f"Имя: {self.first_name} {self.last_name}, "
                f"Телефон: {self.phone}")
    def __eq__(self, other):
        if not isinstance(other, StudentBase):
            return NotImplemented
        return (self.phone == other.phone)


class Student:
     """
    Класс для представления полного студента, наследуется от StudentBase.
    Добавляет атрибут 'address'.
    """
    def __init__(self, student_id: int, first_name: str, last_name: str, patronymic: str, address: str, phone: str):
        # Поля инкапсулированы
        super().__init__(student_id, first_name, last_name, patronymic, phone)
        self.__address = address
        
    # Статические методы валидации
    @staticmethod
    def validate_address(address: str):
        if not isinstance(address, str):
            raise TypeError("Адрес должен быть строкой.")
        if not address.strip():
            raise ValueError("Адрес должен быть непустой строкой.")
        return address.strip()
        
    # Геттеры и Сеттеры с использованием свойств
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, value: str):
        self.__address = self.validate_address(value)

 @staticmethod
    def from_string(student_str: str):
        
       # Переопределение методов создания объекта из строки и JSON
         @staticmethod
    def from_string(student_str: str):
        """
        Создание объекта студента из строки формата:
        "ID, Имя, Фамилия, Отчество, Адрес, Телефон"
        Пример: "1, Иван, Иванов, Иванович, ул. Яблочная, д.1, 8 (123) 456-78-90"
        """
        try:
            parts = student_str.split(',')
            if len(parts) != 6:
                raise ValueError("Строка должна содержать 6 элементов, разделённых запятыми.")
            student_id = int(parts[0].strip())
            first_name = parts[1].strip()
            last_name = parts[2].strip()
            patronymic = parts[3].strip()
            address = parts[4].strip()
            phone = parts[5].strip()
            return Student(student_id, first_name, last_name, patronymic, address, phone)
        except Exception as e:
            raise ValueError(f"Ошибка при создании студента из строки: {e}")
            
    @classmethod
    def from_json(cls, json_str: str):
        
        # Создание объекта студента из JSON-строки
        try:
            data = json.loads(json_str)
            return cls(
                student_id=data['student_id'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                patronymic=data.get('patronymic', ''),
                address=data['address'],
                phone=data['phone']
            )
        except json.JSONDecodeError:
            raise ValueError("Некорректный формат JSON.")
        except KeyError as e:
            raise ValueError(f"Отсутствует необходимое поле в JSON: {e}")

    # Методы для вывода информации
    def __str__(self):
        """Полная версия информации о студенте"""
        return (f"Студент {self.__last_name} {self.__first_name} {self.__patronymic}, "
                f"ID: {self.__student_id}, Адрес: {self.__address}, Телефон: {self.__phone}")
    def brief_info(self):
        """Краткая версия информации о студенте"""
        return (f"ID: {self.__student_id}, "
                f"Имя: {self.__first_name} {self.__last_name}, "
                f"Телефон: {self.__phone}")


class StudentBrief(StudentBase):
    """
    Класс для представления краткой информации о студенте, наследуется от StudentBase.
    Предоставляет методы для получения краткой версии имени.
    """
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
        """Полная версия информации о StudentBrief"""
        return f"Студент: {self.get_brief_name()}, ID: {self.student_id}, Телефон: {self.phone}"
    def brief_info(self):
        """Краткая версия информации о StudentBrief"""
        return f"ID: {self.student_id}, Имя: {self.get_brief_name()}, Телефон: {self.phone}"
