import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Управление студентами")
        self.geometry("800x600")
       
        # Добавляем атрибуты для пагинации
        self.items_per_page = 5
        self.current_page = 1
        self.total_pages = 1
        
        # Верхняя панель с кнопками
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Кнопки действий
        self.add_button = ttk.Button(self.button_frame, text="Добавить")
        self.add_button.pack(side=tk.LEFT, padx=5)
        self.edit_button = ttk.Button(self.button_frame, text="Редактировать")
        self.edit_button.pack(side=tk.LEFT, padx=5)
        self.delete_button = ttk.Button(self.button_frame, text="Удалить")
        self.delete_button.pack(side=tk.LEFT, padx=5)
        self.view_button = ttk.Button(self.button_frame, text="Просмотреть")
        self.view_button.pack(side=tk.LEFT, padx=5)
      
        # Фрейм для сортировки
        self.sort_frame = ttk.Frame(self.button_frame)
        self.sort_frame.pack(side=tk.RIGHT, padx=5)
        self.sort_label = ttk.Label(self.sort_frame, text="Sort by:")
        self.sort_label.pack(side=tk.LEFT, padx=5)
        self.sort_combobox = ttk.Combobox(
            self.sort_frame,
            values=["first_name", "last_name", "patronymic"],
            state="readonly",
            width=15
        )
        self.sort_combobox.pack(side=tk.LEFT, padx=5)
        self.sort_combobox.set("first_name")
        # Таблица продуктов
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.tree = ttk.Treeview(
            self.tree_frame,
            columns=("first_name", "last_name", "patronymic"),
            show="headings"
        )
      
        # Определение заголовков
        self.tree.heading("first_name", text="Имя", command=lambda: self.on_heading_click("first_name"))
        self.tree.heading("last_name", text="Фамилия", command=lambda: self.on_heading_click("last_name"))
        self.tree.heading("patronymic", text="Отчество", command=lambda: self.on_heading_click("patronymic"))
      
        # Настройка колонок
        self.tree.column("first_name", width=300)
        self.tree.column("last_name", width=300)
        self.tree.column("patronymic", width=300)
      
        # Добавление скроллбара
        self.scrollbar = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
      
        # Добавляем фрейм для пагинации
        self.pagination_frame = ttk.Frame(self)
        self.pagination_frame.pack(fill=tk.X, padx=5, pady=5)
      
        # Кнопки пагинации
        self.prev_button = ttk.Button(self.pagination_frame, text="Назад", command=self.prev_page)
        self.prev_button.pack(side=tk.LEFT, padx=5)
        self.page_label = ttk.Label(self.pagination_frame, text="Страница 1 из 1")
        self.page_label.pack(side=tk.LEFT, padx=5)
        self.next_button = ttk.Button(self.pagination_frame, text="Вперед", command=self.next_page)
        self.next_button.pack(side=tk.LEFT, padx=5)
      
        # Привязка событий
        self.tree.bind("<Double-1>", self.on_double_click)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
      
        # Словарь для хранения соответствия
        self.student_code_to_id = {}
    def on_heading_click(self, column):
        """Заглушка для сортировки по колонке"""
        pass
    def on_double_click(self, event):
        """Заглушка для двойного клика по строке"""
        pass
    def on_select(self, event):
        """Заглушка для выбора строки"""
        pass
    def set_add_command(self, command):
        self.add_button.configure(command=command)
    def set_edit_command(self, command):
        self.edit_button.configure(command=command)
    def set_delete_command(self, command):
        self.delete_button.configure(command=command)
    def set_view_command(self, command):
        self.view_button.configure(command=command)
    def set_sort_command(self, command):
        self.sort_combobox.bind("<<ComboboxSelected>>", command)
    def get_selected_item(self):
        """Получение выбранного элемента"""
        selected_items = self.tree.selection()
        if not selected_items:
            return None
        # Получаем значения выбранной строки
        values = self.tree.item(selected_items[0])["values"]
        if not values or len(values) < 3:  # Проверяем, что у нас есть все необходимые значения
            return None
        # Получаем student_code из значений (он последний в списке)
        student_code = str(values[2]) 
      
        # Получаем соответствующий ID из словаря
        student_id = self.student_code_to_id.get(student_code)
        if student_id is None:
            return None
          
        # Возвращаем кортеж с ID и значениями
        return (student_id,) + tuple(values)
      
    def show_error(self, message):
        messagebox.showerror("Error", message)
    def show_info(self, message):
        messagebox.showinfo("Information", message)
    def show_confirmation(self, message):
        return messagebox.askyesno("Confirmation", message)
      
    def prev_page(self):
        """Переход на предыдущую страницу"""
        if self.current_page > 1:
            self.current_page -= 1
            self._page_callback(self.current_page)
            self.update_pagination_buttons()
          
    def next_page(self):
        """Переход на следующую страницу"""
        if self.current_page < self.total_pages:
            self.current_page += 1
            self._page_callback(self.current_page)
            self.update_pagination_buttons()
    def set_page_callback(self, callback):
        """Установка callback для смены страницы"""
        self._page_callback = callback
    def update_pagination_buttons(self):
        """Обновление состояния кнопок пагинации"""
        self.prev_button["state"] = "normal" if self.current_page > 1 else "disabled"
        self.next_button["state"] = "normal" if self.current_page < self.total_pages else "disabled"
        self.page_label["text"] = f"Page {self.current_page} of {self.total_pages}"
    def update_students(self, students, total_items=0):
        """Обновление списка студентов в таблице"""
        # Очистка текущего содержимого
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Очистка словаря соответствий
        self.student_code_to_id.clear()
        # Добавление новых данных
        for student in students:
            student_code = str(student.student_code)
            self.tree.insert(
                "",
                tk.END,
                values=(
                    student.first_name,
                    student.last_name,
                    student.patronymic,
                    student_code
                )
            )
            self.student_code_to_id[student_code] = student.student_id
        # Обновление информации о пагинации
        self.total_pages = max(1, (total_items + self.items_per_page - 1) // self.items_per_page)
        self.update_pagination_buttons()
