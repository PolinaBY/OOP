class EditStudentController:
    """Контроллер для редактирования существующего студента."""

    def __init__(self, view: EditStudentWindow, repository_adapter: StudentAdapter, student: Student):
        self.view = view
        self.repository_adapter = repository_adapter
        self.student = student
        self.view.set_student_data(student)
        self.view.set_save_command(self.handle_save)

    def handle_save(self, data):
        try:
            updated_student = Student.create_new_student(
                student_id=self.student.student_id,
                first_name=data['first_name_entry'],
                last_name=data['last_name_entry'],
                patronymic=data['patronymic_entry'],
                phone=data['phone_entry']
            )
            self.repository_adapter.update_by_id(self.student.student_id, updated_student)
            self.view.destroy()  # Закрываем окно после успешного изменения
        except (ValueError, InvalidOperation) as e:
            self.view.show_error(f"Ошибка валидации: {str(e)}")
        except Exception as e:
             self.view.show_error(f"Ошибка сохранения студента: {str(e)}")
