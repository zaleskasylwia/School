class School:
    def __init__(self, name, classes=[]):
        self.name = name
        self.classes = classes

    def get_best_class(self):
        ''' tu rowniez musze sie odwolac dla class Class i do tej metody
        z get_average_grade?''''
        for classes in self.classes:
            for c in classes.get_average_grade():
                pass

        best_claasss = max(self,classes, get_average_grade())

    def get_all_teachers(self):
        teachers = []
        for class_ in self.classes:
            if teacher not in teachers:
                teachers.append(teacher)

        return teacher