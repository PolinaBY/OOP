from MyEntityRepBase import  MyEntityRepBase

class MyEntityRepDBAdapter:

    def __init__(self, entity_rep_base: MyEntityRepBase):
        self._entity_rep_base = entity_rep_base

    def get_k_n_short_list(self, k, n):
        return self._entity_rep_base.get_k_n_short_list(k, n)

    def get_by_id(self, student_id):
        return self._entity_rep_base.get_by_id(student_id)

    def delete_by_id(self, student_id):
        self._entity_rep_base.delete_by_id(student_id)
        self._entity_rep_base.write_data()

    def update_by_id(self, student_id, first_name, last_name, patronymic, phone):
        self._entity_rep_base.product_replace_by_id(student_id, first_name, last_name, patronymic, phone)
        self._entity_rep_base.write_data()

    def add(self, student):
        self._entity_rep_base.add_student(student)
        self._entity_rep_base.write_data()

    def get_count(self):
        return self._entity_rep_base.get_count()
