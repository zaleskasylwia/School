class Class:
    def __init__(self, name, students=None, teachers=None):
        self.name = name
        self.students = None or []
        self.teachers = None or []

    def get_best_student(self):
        '''1. chcialabym wyciagnac najlepszego studenta korzystajac z metody get_average_grade
            z klasy Student, stworzylam tam tez metode __gt__ ale nie wiem czy tak w gl mozna
            2. i tez nie wiem czy w tym wypadku po dlugosci listy (range(len...)) 
            czy nie wystarczylo by sama self.students'''
        student = self.students[0]
        for i in range(len(self.students)):
            if student < students[0]:
                student = students[i]
        return student

    def get_average_grade(self):
        pass

    def get_class_subjects(self):
        '''tu podobnie, jak dobrac sie do atrybutu subjects ktory jest w klasie Teacher
        i czy to ma byc zalezne od danej klasy, czyli tego name, np. 1A ?'''
        pass

    def sort_students(self, attr):
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
