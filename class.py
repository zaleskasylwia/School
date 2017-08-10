class Class:
    def __init__(self, name, students=[], teachers=[]):
        self.name = name
        self.students = students
        self.teachers = teachers

    def get_best_student(self):
        '''1. chcialabym wyciagnac najlepszego studenta korzystajac z metody get_average_grade
            z klasy Student, stworzylam tam tez metode __gt__ ale nie wiem czy tak w gl mozna
        2. patrzac na swoje algorytmu z max, korzystalam tam z dlugosci listy, 
            ale czy nie wystarczy po prostu przejsc po liscie?'''

        if self.students == []:
            raise IndexError
        else:
            best_student = self.students[0]

        for checked_student in self.students:
            if checked_student > best_student:
                best_student = checked_student

        #best_student = max(self.students, key=lambda x: x.get_average_grade())


        return best_student

    def get_average_grade(self):
        grade = 0
        count = len(self.students)
        for student in self.students:
            grade += student.get_average_grade()
        return grade/count

    def get_class_subjects(self):
        '''tu podobnie, jak dobrac sie do atrybutu subjects ktory jest w klasie Teacher
        i czy to ma byc zalezne od danej klasy, czyli tego name, np. 1A ?'''
        subjects = []
        for teacher in self.teachers:
            for subject in teacher.subjects:
                if subject not in subjects:
                    subjects.append(subject)
        return subjects

    def sort_students(self, attr):
        '''mam sortowac alfabetycznie, albo przez srednia, nie wiem, czy dobrze rozumiem
        ale ten attr jako paramter to on ma decydowac jako co bede sortowac?'''
        if not self.students:
            return None

        if attr == "alpha":
        sorted = False
        length = len(self.students) - 1

        '''z racji zaimplementowanej metody __gt__ w student, czy tu skorzysta z niej przez > ?'''
        while not sorted:
            sorted = True
            for index in range(length):
                if self.students[index] > self.students[index + 1]:
                    sorted = False
                    self.students[index], self.students[index + 1] = self.students[index + 1], self.students[index]
            return self.students

        elif attr == "avg":
            avg_sorted_student = sorted(self.students, key=lambda x: x.get_full_name())
            return avg_sorted_student

