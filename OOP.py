class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_rev = {}

    '''Оценка лектору от студента'''

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades_stud:
                lecturer.grades_stud[course] += [grade]
            else:
                lecturer.grades_stud[course] = [grade]
        else:
            print('Ошибка')

    '''Средняя оценка студента'''

    def average(self):
        for k, v in self.grades_rev.items():
            return int(sum(v) / len(v))


    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average()} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: Введение в программирование'


    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Необходимо сравнивать студентов друг с другом')
            return
        return self.average() < other.average()

    def comparison_text(self, other):
        if self.__lt__(other) is True:
            print(f'Средняя оценка {self.name} меньше {other.name}')
        else:
            print(f'Средняя оценка {self.name} больше {other.name}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_stud = {}
        self.courses_attached = []

    '''Средняя оценка за лекции'''

    def average(self):
        for k, v in self.grades_stud.items():
            return int(sum(v) / len(v))

    '''Магический метод'''

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Необходимо сравнивать лекторов друг с другом')
            return
        return self.average() < other.average()

    def comparison_text(self, other):
        if self.__lt__(other) is True:
            print(f'Средняя оценка {self.name} меньше {other.name}')
            return
        else:
            print(f'Средняя оценка {self.name} больше {other.name}')




class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    '''Оценка студенту за ДЗ'''

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_rev:
                student.grades_rev[course] += [grade]
            else:
                student.grades_rev[course] = [grade]
        else:
            print('Ошибка')


    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


# 1 Student
HarryPotter = Student('Harry', 'Potter', 'wizard')
HarryPotter.courses_in_progress += ['Python']
HarryPotter.courses_in_progress += ['Git']
# # 2 Student
GermionaGranger = Student('Germiona', 'Granger', 'witch')
GermionaGranger.courses_in_progress += ['Python']
GermionaGranger.courses_in_progress += ['Git']

# 1 Reviwer
AlbusDambldor = Reviewer('Albus', 'Dambldor')
AlbusDambldor.courses_attached += ['Python']
# 2 Reviwer
MinervaMc = Reviewer('Minerva', 'McGonagall')
MinervaMc.courses_attached += ['Git']
# 3 Reviwer
HagridRubeus = Reviewer('Hagrid', 'Rubeus')
HagridRubeus.courses_attached += ['Python']
# 4 Reviwer
MoodyAlastor = Reviewer('Moody', 'Alastor')
MoodyAlastor.courses_attached += ['Git']

# # 1 Lecturer
SeverusSnape = Lecturer('Severus', 'Snape')
SeverusSnape.courses_attached += ['Python']
# # 2 Lecturer
RemusLupin = Lecturer('Remus', 'Lupin')
RemusLupin.courses_attached += ['Git']

# Оценка 1му студенту
AlbusDambldor.rate_hw(HarryPotter, 'Python', 3)
MinervaMc.rate_hw(HarryPotter, 'Git', 10)
HagridRubeus.rate_hw(HarryPotter, 'Python', 4)
MoodyAlastor.rate_hw(HarryPotter, 'Git', 6)

# print(f'{HarryPotter.name} получил оценки за домашнее задание: {HarryPotter.grades_rev}')

# # Оценка 2му студенту
AlbusDambldor.rate_hw(GermionaGranger, 'Python', 8)
MinervaMc.rate_hw(GermionaGranger, 'Git', 7)
HagridRubeus.rate_hw(GermionaGranger, 'Python', 10)
MoodyAlastor.rate_hw(GermionaGranger, 'Git', 10)

# print(f'{GermionaGranger.name} получила оценки за домашнее задание: {GermionaGranger.grades_rev}')

# # Оценка 1му лектору
# estimation_Harry = int(input('Поставьте оценку лектору: '))
# estimation_Germiona = int(input('Поставьте оценку лектору: '))
# print()
HarryPotter.rate_lec(SeverusSnape, 'Python', 4)
GermionaGranger.rate_lec(SeverusSnape, 'Python', 2)

# print(f'{SeverusSnape.name} {SeverusSnape.surname} справился с лекцией и получает {SeverusSnape.grades_stud}')

# # Оценка 2му лектору
HarryPotter.rate_lec(RemusLupin, 'Git', 10)
GermionaGranger.rate_lec(RemusLupin, 'Git', 10)

# print(f'{RemusLupin.name} {RemusLupin.surname} справился с лекцией и получает {RemusLupin.grades_stud}')

# Перегрузка магических методов

# print(AlbusDambldor)
# print(MinervaMc)
# print(SeverusSnape)
# print(RemusLupin)
# print(HarryPotter)
# print(GermionaGranger)
#
# print(HarryPotter.__lt__(GermionaGranger))
# HarryPotter.comparison_text(GermionaGranger)
#
# print(SeverusSnape.__lt__(RemusLupin))
# RemusLupin.comparison_text(SeverusSnape)







Harry_stud = []
Germiona_stud = []
Harry_stud.append(HarryPotter.grades_rev)
Germiona_stud.append(GermionaGranger.grades_rev)


def average_course(Harry_stud, Germiona_stud, course):
    for harry in Harry_stud:
        for k, v in harry.items():
            if course == k:
                h = sum(harry[k]) / len(harry[k])
                break
        else:
            print(f'Harry не изучает курс {course}')


    for germiona in Germiona_stud:
        for k, v in germiona.items():
            if course == k:
                g = sum(germiona[k]) / len(germiona[k])
                break
        else:
            print(f'Germiona не изучает курс {course}')

        print(f'Средняя оценка студентов по курсу {course}: {h + g}')



average_course(Harry_stud, Germiona_stud, 'Git')




