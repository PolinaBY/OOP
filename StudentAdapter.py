from StudentRepBase import  StudentRepBase
from Observer import Observable

class StudentAdapter(Observable):

    def __init__(self, student_rep_base: StudentRepBase):
        super().__init__()
        self._student_rep_base = student_rep_base
        self._student_rep_base.load_data()  # Читаем начальные данные при создании адаптера

    def get_k_n_short_list(self, k, n, sort_field=None, sort_order="ASC"):
        return self._student_rep_base.get_k_n_short_list(k, n, sort_field, sort_order)

    def get_by_id(self, student_id):
        return self._student_rep_base.get_by_id(student_id)

    def delete_by_id(self, student_id):
        self._student_rep_base.delete_by_id(student_id)
        self._student_rep_base.load_data() 
        self.notify_observers()
        
    def update_by_id(self, student_id, updates: dict):
        self._student_rep_base.replace_by_id(student_id, updates)
        self._product_repository.load_data()
        self.notify_observers()

    def add(self, student: dict):
        self._student_rep_base.add_student(student)
        self.notify_observers()

    def get_count(self):
        return self._student_rep_base.get_count()
