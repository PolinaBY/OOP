import re
import json
class Student:
    def __init__(self, student_id: int, first_name: str, last_name: str, patronymic: str, address: str, phone: str):
        # Поля инкапсулированы
        self.__student_id = student_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__patronymic = patronymic
        self.__address = address
        self.__phone = phone
        
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
        if not isinstance.strip():
            raise ValueError("Отчество должно быть непустой строкой.")
        return patronymic.strip().title()
    @staticmethod
    def validate_address(address: str):
        if not isinstance(address, str):
            raise TypeError("Адрес должен быть строкой.")
        if not address.strip():
            raise ValueError("Адрес должен быть непустой строкой.")
        return address.strip()
    @staticmethod
    def validate_phone(phone: str):
        if not isinstance(phone, str):
            raise TypeError("Телефон должен быть строкой.")
        if not phone.strip():
            raise ValueError("Телефон должен быть непустой строкой.")
        # Дополнительная проверка формата телефона (8 (888) 888-88-88)
        import re
        pattern = re.compile(r"^8 \(\d{3}\) \d{3}-\d{2}-\d{2}$")
        if not pattern.match(phone.strip()):
            raise ValueError("Телефон должен соответствовать формату: 8 (***) ***-**-**.")
        return phone.strip()
        
    # Геттеры и Сеттеры с использованием свойств
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
    def address(self):
        return self.__address
    @address.setter
    def address(self, value: str):
        self.__address = self.validate_address(value)
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, value: str):
        self.__phone = self.validate_phone(value)

 @staticmethod
    def from_string(student_str: str):
        
       # Создание объекта студента из строки формата: "ID, Имя, Фамилия, Отчество, Адрес, Телефон"
        
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
        
    # Метод для сравнения объектов на равенство
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return (self.student_id == other.student_id and
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.patronymic == other.patronymic and
                self.address == other.address and
                self.phone == other.phone)
    except (ValueError, TypeError) as e:
        print(f"Ошибка: {e}")
