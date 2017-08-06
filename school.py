class School:
    def __init__(self, name, classes=None):
        self.name = name
        self.classes = classes or []

    def get_best_class(self):
        ''' tu rowniez musze sie odwolac dla class Class i do tej metody
        z get_average_grade?''''
        for classes in self.classes:
            for c in classes.get_average_grade():
                pass

    def get_all_teachers(self):
        teachers = []
        for teacher in self.classes:
            if teacher not in teachers:
                teachers.append(teacher)

        return teacher