from Observer import Observer
from MainWindow import MainWindow
from AddStudentWindow import AddStudentWindow
from EditStudentWindow import EditStudentWindow
from AddStudentController import AddStudentController
from EditStudentController import EditStudentController
from StudentDetailsWindow import StudentDetailsWindow
from StudentDetailsController import StudentDetailsController
from StudentAdapter import StudentAdapter

class ApplicationController(Observer):
    def __init__(self, repository: StudentAdapter):
        self.repository = repository
        self.main_window = MainWindow()
        self.repository.add_observer(self)
        self._current_sort_field = None
        self._current_sort_order = "ASC"

    # Привязка обработчиков событий
        self.main_window.set_add_command(self.handle_add)
        self.main_window.set_edit_command(self.handle_edit)
        self.main_window.set_delete_command(self.handle_delete)
        self.main_window.set_view_command(self.handle_view)
        self.main_window.set_sort_command(self.handle_sort)
        self.main_window.set_page_callback(self.handle_page_change)
     
    # Начальное обновление данных
        self.update()
    
    def run(self):
        """Запуск главного окна"""
        self.main_window.mainloop()

    def update(self):
        """Обновление данных в представлении (реализация Observer)"""
        self.handle_page_change(self.main_window.current_page)

    # Добавляем методы для взаимодействия с репозиторием
    def handle_add(self):
        """Обработка добавления нового студента"""
        add_window = AddStudentWindow(self.main_window)
        controller = AddStudentController(add_window, self.repository)
      
    def handle_edit(self):
        """Обработка редактирования студента"""
        selected_item = self.main_window.get_selected_item()
        if not selected_item:
            self.main_window.show_error("Пожалуйста, выберите запись для редактирования")
            return
        try:
            student_id = selected_item[0]  # Первый элемент - ID студента
            student = self.repository.get_by_id(student_id)
            if not student:
                self.main_window.show_error(f"Студент с ID {student_id} не найден")
                return
            edit_window = EditStudentWindow(self.main_window)
            controller = EditStudentController(edit_window, self.repository, student)
        except Exception as e:
            self.main_window.show_error(f"Ошибка загрузки студента: {str(e)}")
    
    def handle_delete(self):
        """Обработка удаления студента"""
        selected_item = self.main_window.get_selected_item()
        if not selected_item:
            self.main_window.show_error("Пожалуйста, выберите запись для удаления")
            return
        try:
            student_id = selected_item[0]
            first_name = selected_item[1] 
            if self.main_window.show_confirmation(f"Вы уверены, что хотите удалить студента '{first_name}'?"):
                self.repository.delete_by_id(student_id)
                self.main_window.show_info("Студент успешно удален")
        except Exception as e:
            self.main_window.show_error(f"Ошибка удаления студента: {str(e)}")
          
    def handle_view(self):
        """Обработка просмотра деталей студента"""
        selected_item = self.main_window.get_selected_item()
        if not selected_item:
            self.main_window.show_error("Пожалуйста, выберите запись для просмотра")
            return
        try:
            student_id = selected_item[0]
            student = self.repository.get_by_id(student_id)
            if not student:
                self.main_window.show_error(f"Студент с ID {student_id} не найден")
                return
            details_window = StudentDetailsWindow(self.main_window)
            controller = StudentDetailsController(details_window, student)
        except Exception as e:
            self.main_window.show_error(f"Ошибка загрузки детальных записей студента: {str(e)}")
          
    def handle_sort(self, event):
        """Обработка сортировки"""
        sort_field = self.main_window.sort_combobox.get().lower()
        field_mapping = {
            'Имя': 'first_name',
            'Фамилия': 'last_name'
        }
        try:
            self._current_sort_field = field_mapping.get(sort_field.lower())
            self.update()
        except ValueError as e:
            self.main_window.show_error(f"Ошибка сортировки: {str(e)}")
          
    def handle_page_change(self, page_number):
        """Обработка изменения страницы"""
        students = self.repository.get_k_n_short_list(
            self.main_window.items_per_page,
            page_number,
            sort_field=self._current_sort_field,
            sort_order=self._current_sort_order
        )
        total_items = self.repository.get_count()
        self.main_window.update_students(students, total_items)
