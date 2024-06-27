class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.average = (m1 + m2 + m3) / 3

class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, m1, m2, m3):
        student = Student(name, m1, m2, m3)
        self.students.append(student)

    def input_students(self):
        number_of_students = int(input("Enter the number of students: "))
        for _ in range(number_of_students):
            name = input("Enter student's name: ")
            m1 = int(input("Enter m1: "))
            m2 = int(input("Enter m2: "))
            m3 = int(input("Enter m3: "))
            self.add_student(name, m1, m2, m3)

    def sort_students_by_avg(self):
        n = len(self.students)

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.students[j].average < self.students[j + 1].average:
                    self.students[j], self.students[j + 1] = self.students[j + 1], self.students[j]

    def print_students(self):
        if not self.students:
            print("No students available.")
            return

        print("Students sorted by average:")
        for rank, student in enumerate(self.students, start=1):
            print(f'Rank {rank}: {student.name} - Average: {student.average:.2f}')

school = School()
school.input_students()
school.sort_students_by_avg()
school.print_students()
