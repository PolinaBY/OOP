class StudentRepDB:
    """Класс для работы с базой данных и манипуляций с объектами."""
    
    def __init__(self, host, user, password, database, port=3306):
        self.db_connection = DBConnection(host, user, password, database, port)
    
    def get_by_id(self, student_id: int) -> dict:
        """Получить объект по ID."""
        conn = self.db_connection.get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
            student = cursor.fetchone()
            if not student:
                raise ValueError(f"Студент с ID {student_id} не найден.")
            return dict(student)

    
    def get_k_n_short_list(self, k: int, n: int):
        """Получить список k по счету n объектов """
        offset = (n - 1) * k
        conn = self.db_connection.get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM students ORDER BY id LIMIT %s OFFSET %s", (k, offset))
            return [dict(row) for row in cursor.fetchall()]
    
    def add_student(self, student: Student):
        """Добавить объект в базу данных (сгенерировать новый ID)."""
        conn = self.db_connection.get_connection()
        unique_fields = ("phone")
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(*) FROM students WHERE phone = %s",
                (student['phone'])
            )
        if cursor.fetchone()[0] > 0:
            raise ValueError("Студент с такими данными уже существует.")
        cursor.execute(
            "INSERT INTO students (first_name, last_name, patronymic, phone) VALUES (%s, %s, %s, %s) RETURNING id",
            (student['first_name'], student['last_name'], student['patronymic'], student['phone'])
        )
        student_id = cursor.fetchone()[0]
        conn.commit()
        return student_id
    
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
    
    def get_count(self) -> int:
        """Получить количество элементов в базе данных."""
        conn = self.db_connection.get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM students")
            return cursor.fetchone()[0]
