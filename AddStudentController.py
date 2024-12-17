import Adapter
from AddStudentWindow import AddStudentWindow
from Student import Student
from decimal import Decimal, InvalidOperation


class AddStudentController:
    """Контроллер для добавления нового студента."""

    def __init__(self, view: AddStudentWindow, repository_adapter: StudentAdapter):
        self.view = view
        self.repository_adapter = repository_adapter
        self.view.set_controller(self)

    def handle_save(self, data):
        try:
            new_student = Student.create_new_student(
                first_name=data['first_name_entry'],
                last_name=data['last_name_entry'],
                patronymic=data['patronymic_entry'],
                phone=data['phone_entry']
            )
            self.repository_adapter.add(new_student)
            self.view.destroy()  # Закрываем окно после успешного добавления
        except (ValueError, InvalidOperation) as e:
            self.view.show_error(f"Ошибка валидации: {str(e)}")
        except Exception as e:
            self.view.show_error(f"Ошибка сохранения студента: {str(e)}")
