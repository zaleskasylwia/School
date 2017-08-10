from person import Person


class Student(Person):

    def __init__(self, first_name, last_name, grades=[]):
        super().__init__(first_name, last_name)
        self.grades = grades

    def get_average_grade(self):
        grade = 0
        for grade in self.grades:
            grade += self.grades[g]
        avg_grade = grade/len(self.grades)

        return avg_grade
        #jesli moge uzywac wbudowanych funkcji to:
        #return sum(self.grades)/len(self.grades)

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()

