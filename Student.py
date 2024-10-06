class Student:
    def __init__(self, student_id: int, first_name: str, last_name: str, patronymic: str, address: str, phone: str):
        # Поля инкапсулированы
        self.__student_id = student_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__patronymic = patronymic
        self.__address = address
        self.__phone = phone
    # Геттеры 
    
    @property
    def student_id(self):
        return self.__student_id
    @property
    def first_name(self):
        return self.__first_name
    @property
    def last_name(self):
        return self.__last_name
    @property
    def patronymic(self):
        return self.__patronymic
    @property
    def address(self):
        return self.__address
    @property
    def phone(self):
        return self.__phone
