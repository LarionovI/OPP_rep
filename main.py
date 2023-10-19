class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}'

    def avg_grade(self):
        if len(self.grades) == 0:
            return 0
        all_grade = 0
        sum_grades = 0
        for course_grade in self.grades.values():
            sum_grades += sum(course_grade)
            all_grade += len(course_grade)
        return sum_grades / all_grade

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()

    def __ne__(self, other):
        return self.avg_grade() != other.avg_grade()

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() <= other.avg_grade()

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __ge__(self, other):
        return self.avg_grade() >= other.avg_grade()

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_Lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее' \
               f' задание: {self.avg_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def avg_grade(self):
        if len(self.grades) == 0:
            return 0
        all_grade = 0
        sum_grades = 0
        for course_grade in self.grades.values():
            sum_grades += sum(course_grade)
            all_grade += len(course_grade)
        return sum_grades / all_grade

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()

    def __ne__(self, other):
        return self.avg_grade() != other.avg_grade()

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() <= other.avg_grade()

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __ge__(self, other):
        return self.avg_grade() >= other.avg_grade()

best_student = Student('Ruoy', 'Eman', 'MAN')
best_student.courses_in_progress += ['Python']

cool_lec = Lecturer('Some', 'Buddy')
cool_lec.courses_attached += ['Python']

best_student.rate_Lecturer(cool_lec, 'Python', 10)
best_student.rate_Lecturer(cool_lec, 'Python', 10)


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def avg_stud_grade(students, course):
    len_grades = 0
    sum_grades = 0
    for student in students:
        if course not in student.grades:
            continue
        sum_grades += sum(student.grades[course])
        len_grades += len(student.grades[course])
    if len_grades != 0:
        return sum_grades / len_grades
    return 0

def avg_lecturer_grade(lecturer, course):
    len_grades = 0
    sum_grades = 0
    for lecturer in lecturer:
        if course not in lecturer.grades:
            continue
        sum_grades += sum(lecturer.grades[course])
        len_grades += len(lecturer.grades[course])
    if len_grades != 0:
        return sum_grades / len_grades
    return 0

student1 = Student('Tom', 'Boy', 'm')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Java']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Java']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_lecturer = Lecturer('Kate', 'Perry')
cool_lecturer.courses_attached += ['Python', 'Git']
student1.rate_Lecturer(cool_lecturer, 'Python', 7.7)
student1.rate_Lecturer(cool_lecturer, 'Git', 6)
student1.rate_Lecturer(cool_lecturer, 'Java', 9.9)
print(cool_lecturer)
print()

lecturer1 = Lecturer('Tom', 'Holand')
lecturer1.courses_attached += ['Python', 'Git']
student1.rate_Lecturer(lecturer1, 'Python', 5)
student1.rate_Lecturer(lecturer1, 'Git', 10)
student1.rate_Lecturer(lecturer1, 'Java', 8)
print(lecturer1)
print()
print(avg_lecturer_grade([cool_lecturer, lecturer1], 'Python'))

# print(student1 != best_student)
# print(student1 == best_student)
# print(student1 > best_student)
# print(student1 < best_student)
# print(student1 <= best_student)
# print(student1 >= best_student)
#
# print(avg_stud_grade([best_student, student1], 'Python'))
# print(avg_stud_grade([best_student, student1], 'Git'))
# print(avg_stud_grade([best_student, student1], 'Java'))
