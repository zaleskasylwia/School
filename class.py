class Class:
    def __init__(self, name, students=None, teachers=None):
        self.name = name
        self.students = students or []
        self.teachers = teachers or []

    def get_best_student(self):
        '''1. chcialabym wyciagnac najlepszego studenta korzystajac z metody get_average_grade
            z klasy Student, stworzylam tam tez metode __gt__ ale nie wiem czy tak w gl mozna
        2. patrzac na swoje algorytmu z max, korzystalam tam z dlugosci listy, 
            ale czy nie wystarczy po prostu przejsc po liscie?'''
        student = self.students[0]

        for checked_student in self.students:
            if checked_student > student:
                student = checked_student

        return student

    def get_average_grade(self):
        grade = 0
        count = 0
        for student in self.students:
            for grade in student.get_average_grade():
                grade += grade
                count += 1
        return grade/count

    def get_class_subjects(self):
        '''tu podobnie, jak dobrac sie do atrybutu subjects ktory jest w klasie Teacher
        i czy to ma byc zalezne od danej klasy, czyli tego name, np. 1A ?'''
        subjects = []
        for teacher in self.teacher:
            for subject in teacher.subjects:
                if subjects not in subjects:
                    subjects.append(subjects)
        return subjects

    def sort_students(self, attr):
        if not self.students: 
            return None
        
        try:
            attr = getattr(self.students[0], attr) # probuje wyciągnąć atrybut z obiektu studenta
        except AttributeError:
            return None
        else:

        '''mam sortowac alfabetycznie, albo przez srednia, nie wiem, czy dobrze rozumiem
        ale ten attr jako paramter to on ma decydowac jako co bede sortowac?'''
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
