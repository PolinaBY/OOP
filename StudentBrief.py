class StudentBrief:
    def __init__(self, student_id: int, brief_name: str, phone: str):
        self.student_id = student_id
        self.brief_name = brief_name
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
    def validate_brief_name(brief_name: str):
        if not isinstance(brief_name, str):
            raise TypeError("Имя должно быть строкой.")
        if not brief_name.strip():
            raise ValueError("Имя должно быть непустой строкой.")
        return brief_name.strip().title()
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
    # Геттеры и Сеттеры с использованием свойств
    @property
    def student_id(self):
        return self.__student_id
    @student_id.setter
    def student_id(self, value: int):
        self.__student_id = self.validate_student_id(value)
    @property
    def brief_name(self):
        return self.__brief_name
    @brief_name.setter
    def brief_name(self, value: str):
        self.__brief_name = self.validate_brief_name(value)
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, value: str):
        self.__phone = self.validate_phone(value)
    # Методы для создания объекта из Student
    @classmethod
    def from_student(cls, student: Student):
        """
        Создание объекта StudentBrief из объекта Student.
        Формат имени: "Фамилия И.О."
        """
        if not isinstance(student, Student):
            raise TypeError("Аргумент должен быть объектом класса Student.")
        brief_name = f"{student.last_name} {student.first_name[0]}.{student.patronymic[0]}."
        return cls(
            student_id=student.student_id,
            brief_name=brief_name,
            phone=student.phone
        )
    # Методы для вывода информации
    def __str__(self):
        """Полная версия информации о StudentBrief"""
        return (f"Студент: {self.brief_name}, ID: {self.student_id}, Телефон: {self.phone}")
    def brief_info(self):
        """Краткая версия информации о StudentBrief"""
        return f"ID: {self.student_id}, Имя: {self.brief_name}, Телефон: {self.phone}"
    def __repr__(self):
        """Официальное представление объекта"""
        return (f"StudentBrief(student_id={self.student_id}, brief_name='{self.brief_name}', "
                f"phone='{self.phone}')")
    # Метод для сравнения объектов на равенство
    def __eq__(self, other):
        if not isinstance(other, StudentBrief):
            return NotImplemented
        return (self.student_id == other.student_id and
                self.brief_name == other.brief_name and
                self.phone == other.phone)
