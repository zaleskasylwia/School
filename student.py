from person import Person


class Student(Person):

    def __init__(first_name, last_name, grades=None):
        super().__init__(first_name, last_name)
        self.grades = None or []

    def get_average_grade(self):
        grade = 0
        for g in range(len(self.grades)):
            grade += self.grades[g]
        avg_grade = grade/len(self.grades)

        return avg_grade

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()

