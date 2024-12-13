from decimal import Decimal
from typing import List, Optional
from Student import Student
from Observer import Observable
from StudentBrief import StudentBrief
from pymysql import MySQLError
from DBConnection import DBConnection

class StudentRepDB(Observable):
    """Класс для работы с базой данных и манипуляций с объектами."""
    
    def __init__(self, host, user, password, database, port=3306):
        super().__init__()
        self.db_connection = DBConnection(host, user, password, database, port)
        self._valid_sort_fields = {'first_name', 'last_name', 'patronymic'}
    
    def get_by_id(self, student_id: int) -> Student:
        """Получить объект по ID."""
        conn = self.db_connection.get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
            student = cursor.fetchone()
            if not student:
                raise ValueError(f"Студент с ID {student_id} не найден.")
            return Student(
                    student_id=student['student_id'],
                    first_name=student['first_name'],
                    last_name=student['last_name'],
                    patronymic=student['patronymic'],
                    phone=student['phone']
            )

    
    def get_k_n_short_list(self, k: int, n: int, sort_field: Optional[str] = None, sort_order: str = "ASC") -> List[StudentBrief]:
        """Получить список k по счету n объектов """
        offset = (n - 1) * k
        conn = self.db_connection.get_connection()
        if sort_field and sort_field not in self._valid_sort_fields:
            raise ValueError(f"Недопустимое поле сортировки. Допустимые поля: {', '.join(self._valid_sort_fields)}")
        if sort_order.upper() not in ("ASC", "DESC"):
            raise ValueError("Порядок сортировки должен быть ASC или DESC.")
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM students {order_clause} LIMIT %s OFFSET %s", (k, offset))
            order_clause = f"ORDER BY {sort_field} {sort_order}" if sort_field else ""
            sql = sql.format(order_clause=order_clause)
            student = cursor.fetchone()
            return [
                StudentBrief(
                    student_id=student['student_id'],
                    first_name=student['first_name'],
                    last_name=student['last_name'],
                    patronymic=student['patronymic'],
                    phone=student['phone']
                ) for row in student
            ]
    
    def add_student(self, student: Student):
        """Добавить объект в базу данных (сгенерировать новый ID)."""
        conn = self.db_connection.get_connection()
        try:
            query = """
                INSERT INTO students (first_name, last_name, patronymic, phone) VALUES (%s, %s, %s, %s)
            """
            values = (student.first_name, student.last_name, student.patronymic, student.phone)
            with conn.cursor() as cursor:
                cursor.execute(query, values)
                conn.commit()
                student.student_id = cursor.lastrowid
            self.notify_observers()

        except MySQLError as e:
            if e.args[0] == 1062:
                raise ValueError(f"Студент с номероом {student.phone} уже существует.")
            else:
                raise Exception("При добавлении студента произошла непредвиденная ошибка.")
    
    def replace_by_id(self, student_id: int, new_student: dict):
        """Заменить элемент списка по ID."""
        valid_keys = {"first_name", "last_name", "patronymic", "phone"}
        updates = {k: v for k, v in updates.items() if k in valid_keys}
        if not updates:
            raise ValueError("Нет валидных полей для обновления.")

        conn = self.db_connection.get_connection()
        set_clause = ", ".join([f"{key} = %s" for key in updates.keys()])
        values = list(updates.values()) + [student_id]
        
        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE students SET {set_clause} WHERE id = %s", values)
            conn.commit()
    
    def delete_by_id(self, student_id: int):
        """Удалить элемент списка по ID."""
        conn = self.db_connection.get_connection()
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
            conn.commit()
            success = cursor.rowcount > 0
            if success:
                self.notify_observers()
            return success
    
    def get_count(self) -> int:
        """Получить количество элементов в базе данных."""
        conn = self.db_connection.get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM students")
            return cursor.fetchone()[0]
