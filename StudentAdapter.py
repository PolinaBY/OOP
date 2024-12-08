from StudentRepBase import  StudentRepBase
class StudentAdapter:

    def __init__(self, student_rep_base: StudentRepBase):
        self._student_rep_base = student_rep_base

    def get_k_n_short_list(self, k, n):
        return self._student_rep_base.get_k_n_short_list(k, n)

    def get_by_id(self, student_id):
        return self._student_rep_base.get_by_id(student_id)

    def delete_by_id(self, student_id):
        self._student_rep_base.delete_by_id(student_id)
        
    def update_by_id(self, student_id, updates: dict):
        self._student_rep_base.replace_by_id(student_id, updates)

    def add(self, student: dict):
        self._student_rep_base.add_student(student)

    def get_count(self):
        return self._student_rep_base.get_count()
