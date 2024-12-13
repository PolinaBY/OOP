from StudentDetailsWindow import StudentDetailsWindow
from Student import Student

class StudentDetailsController:
    def __init__(self, view: StudentDetailsWindow, student: Student):
        self.view = view
        self.student = student
        self.display_student()
      
    def display_student(self):
        """Отображение информации о студенте"""
        self.view.display_student(self.student)
