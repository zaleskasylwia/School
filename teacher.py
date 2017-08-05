from person import Person


class Teacher(Person):

    def __init__(first_name, last_name, subjects=None):
        super().__init__(first_name, last_name)
        self.subjects = None or []