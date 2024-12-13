import tkinter as tk
from tkinter import ttk

class StudentDetailsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Подробная информация о студенте")
        self.geometry("400x500")
        # Делаем окно модальным
        self.transient(parent)
        self.grab_set()
        # Создаем и размещаем элементы интерфейса
        self.create_widgets()
        # Центрируем окно относительно родительского
        self.center_window()
      
    def create_widgets(self):
        # Основной контейнер
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        # Создаем и размещаем лейблы для всех полей
        fields = [
            ("ID:", "id_label"),
            ("first_name:", "first_name_label"),
            ("last_name:", "last_name_label"),
            ("patronymic:", "patronymic_label"),
            ("phone:", "phone_label")
        ]
        for i, (text, attr_name) in enumerate(fields):
            ttk.Label(main_frame, text=text).grid(row=i, column=0, sticky=tk.W, pady=5)
            value_label = ttk.Label(main_frame, text="")
            value_label.grid(row=i, column=1, sticky=tk.W, pady=5, padx=5)
            setattr(self, attr_name, value_label)
        # Кнопка закрытия
        self.close_button = ttk.Button(main_frame, text="Close", command=self.destroy)
        self.close_button.grid(row=len(fields), column=0, columnspan=2, pady=20)
    
    def display_student(self, student):
        """Отображение информации о студенте"""
        self.id_label.config(text=str(student.student_id))
        self.first_name_label.config(text=student.first_name)
        self.last_name_label.config(text=student.last_name)
        self.patronymic_label.config(text=student.patronymic)
        self.phone_label.config(text=student.phone)
