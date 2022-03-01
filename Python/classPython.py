class ProfileGlobal():
    def __init__(self, name, id_no):
        self.name = name
        self.id = id_no

    def list_it(self):
        empid_list = []
        empid_list.append(self.id)
        return empid_list

    def dict_it(self):
        emp_dict = {}
        emp_dict={self.name: self.id}
        return emp_dict

class ProfileLocal(ProfileGlobal):
    pass
