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
