from person import Person


class Teacher(Person):

    def __init__(self, first_name, last_name, subjects=[]):
        if type(first_name) is string and type(last_name) is string and type(subjects) is list:
            super().__init__(first_name, last_name)
            self.subjects = subjects
        else:
            raise TypeError
