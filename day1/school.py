class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher


class Teacher:
    def __init__(self, name, course):
        self.name = name
        self.course = course


class School:
    def __init__(self, name, teachers, courses, students):
        self.name = name
        self.teachers = teachers
        self.courses = courses
        self.students = students

    def get_students_name(self):
        for student in self.students:
            print(student.name)


school_name = 'RMIT'

ds_course = Course('Data Structure', 'Shekhar Kalra')
algo_course = Course('Intro to Algorithms', 'Falk Scholar')

teacher1 = Teacher('Shekhar Kalra', ds_course)
teacher2 = Teacher('Falk Scholar', algo_course)

student1 = Student('Saalim Shadman', 99, 1)
student2 = Student('Albert Einstein', 18, 2)
student3 = Student('Isacc Newton', 29, 3)

teachers = [teacher1, teacher2]
courses = [ds_course, algo_course]
students = [student1, student2, student3]


my_school = School(school_name, teachers, courses, students)
print(my_school.get_students_name())
