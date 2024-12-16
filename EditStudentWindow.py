import tkinter as tk
from tkinter import ttk, messagebox

class EditStudentWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Редактировать студента")
        self.geometry("400x600")
        # Делаем окно модальным
        self.transient(parent)
        self.grab_set()
        self.result = None
        # Создаем и размещаем элементы интерфейса
        self.create_widgets()
        # Центрируем окно относительно родительского
        self.center_window()
    def create_widgets(self):
        # Основной контейнер
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        # Создаем поля ввода
        fields = [
            ("Имя:", "first_name_entry"),
            ("Фамилия:", "last_name_entry"),
            ("Отчество:", "patronymic_entry"),
            ("Телефон:", "phone_entry")
        ]
        self.entries = {}
        for i, field_info in enumerate(fields):
            label_text = field_info[0]
            entry_name = field_info[1]
            ttk.Label(main_frame, text=label_text).grid(row=i * 2, column=0, sticky=tk.W, pady=(10, 0))
            entry = ttk.Entry(main_frame, width=40)
            entry.grid(row=i * 2 + 1, column=0, columnspan=2, sticky=tk.EW, pady=(5, 10))
            self.entries[entry_name] = entry
        # Фрейм для кнопок
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=len(fields) * 2, column=0, columnspan=2, pady=20)
        # Кнопки
        self.save_button = ttk.Button(button_frame, text="Сохранить", command=self.on_save)
        self.save_button.pack(side=tk.LEFT, padx=5)
        self.cancel_button = ttk.Button(button_frame, text="Отмена", command=self.destroy)
        self.cancel_button.pack(side=tk.LEFT, padx=5)

    def set_save_command(self, command):
        """Установка команды для кнопки сохранения"""
        self._save_command = command

    def get_student_data(self):
        """Получение данных из полей ввода"""
        data = {}
        for entry_name, entry in self.entries.items():
            data[entry_name] = entry.get().strip()
        return data

    def set_student_data(self, student):
        """Заполнение полей данными"""
        field_mapping = {
            'first_name_entry': student.first_name,
            'last_name_entry': student.last_name,
            'patronymic_entry': student.patronymic,
            'phone_entry': student.phone
        }
        for entry_name, value in field_mapping.items():
            entry = self.entries[entry_name]
            entry.delete(0, tk.END)
            entry.insert(0, value)
    
    def on_save(self):
        """Обработка нажатия кнопки сохранения"""
        if hasattr(self, '_save_command'):
            self._save_command(self.get_student_data())

    def show_error(self, message):
        """Отображение сообщения об ошибке"""
        messagebox.showerror("Ошибка", message, parent=self)

    def show_info(self, message):
        """Отображение информационного сообщения"""
        messagebox.showinfo("Информация", message, parent=self)

    def show_warning(self, message):
        """Отображение предупреждения"""
        messagebox.showwarning("Предупреждение", message, parent=self)
    
    def center_window(self):
        """Центрирование окна"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")
