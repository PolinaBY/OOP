import Adapter
from AddEditStudentWindow import AddEditStudentWindow
from Student import Student
from decimal import Decimal, InvalidOperation

class AddEditStudentController:
    def __init__(self, view: AddEditStudentWindow, repository_adapter: StudentAdapter, student=None):
        self.view = view
        self.repository_adapter = repository_adapter
        self.student = student
      
        # Если редактируем существующего студента, заполняем поля
        if student:
            self.view.set_student_data(student)
        # Устанавливаем обработчик сохранения
        self.view.set_save_command(self.handle_save)
      
    def handle_save(self, data):
        """Обработка сохранения студента"""
        try:
            # Создание или обновление 
            updated_student = Student.create_new_student(
                student_id=self.student.student_id,
                first_name=data['first_name_entry'],
                last_name=data['last_name_entry'],
                patronymic=data['patronymic_entry'],
                phone=data['phone_entry']
            )
            if self.student:
                self.repository_adapter.update_by_id(self.student.student_id, updated_student)
            else:  # Создание нового
                self.repository_adapter.add(updated_student)
            self.view.destroy()  # Закрываем окно после успешного сохранения
        except (ValueError, InvalidOperation) as e:
            self.view.show_error(f"Validation error: {str(e)}")
        except Exception as e:
            self.view.show_error(f"Error saving student: {str(e)}")

class AddStudentController:
    def __init__(self,view: AddEditStudentWindow, repository_adapter: StudentAdapter, student=None)
        self.view = view
        self.repository_adapter = repository_adapter
        self.student = student
    def 
