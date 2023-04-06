class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []
      
    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
      courses_in_progress_stud = ', '.join(self.courses_in_progress)
      finished_courses_stud = ', '.join(self.finished_courses)
      a1 = self.average_rating_stud()
      outpoot = f'Имя: {self.name}\nФамилия: {self.surname}\nСредний балл: {round(a1, 2)}\nКурсы в процессе обучения: {courses_in_progress_stud}\nЗавершенные курсы: {finished_courses_stud}\n'
      return outpoot

    def average_rating_stud(self):
      grades_count = 0
      if not self.grades:
        return 0
      else:
        for k in self.grades:
          grades_count += len(self.grades[k])
          average_value = sum(map(sum, self.grades.values())) / grades_count
        return average_value

    def __lt__(self, other):
      if not isinstance(other, Student):
        raise Exception('Неверный ввод!')
      return self.average_rating_stud() < other.average_rating_stud()

    def __eq__(self, other):
      if not isinstance(other, Student):
        raise Exception('Неверный ввод!')
      return self.average_rating_stud() == other.average_rating_stud()

    def __le__(self, other):
      if not isinstance(other, Student):
        raise Exception('Неверный ввод!')
      return self.average_rating_stud() <= other.average_rating_stud()
  
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
      outpoot = f'Имя: {self.name}\nФамилия: {self.surname}\nСредний балл: {round(self.average_rating_lec(), 2)}\n'
      return outpoot

    def __lt__(self, other):
      if not isinstance(other, Lecturer):
        raise Exception('Неверный ввод!')
      return self.average_rating_lec() < other.average_rating_lec()

    def __eq__(self, other):
      if not isinstance(other, Lecturer):
        raise Exception('Неверный ввод!')
      return self.average_rating_lec() == other.average_rating_lec()

    def __le__(self, other):
      if not isinstance(other, Lecturer):
        raise Exception('Неверный ввод!')
      return self.average_rating_lec() <= other.average_rating_lec()

    def average_rating_lec (self):
      grades_count = 0
      if not self.grades:
        return 0
      else:
        for j in self.grades:
          grades_count += len(self.grades[j])
          a1 = sum(map(sum, self.grades.values())) / grades_count
        return a1


class Reviewer(Mentor):
          
    def __str__(self):
      outpoot = f'Имя: {self.name}\nФамилия: {self.surname}'
      return outpoot

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def universal_average(persons, course):
    if not isinstance(persons, list):
        return "Not list"
    average_grade = []
    for per in persons:
        average_grade.extend(per.grades.get(course, []))
    if not average_grade:
        return "По такому курсу ни у кого нет оценок"
    return round(sum(average_grade) / len(average_grade), 2)

stud1 = Student('Alla', 'Pugacheva', 'Female')
stud1.courses_in_progress += ['C++']
stud1.courses_in_progress += ['Python']
stud1.finished_courses += ['Pesnya_goda']
stud2 = Student('Maksim', 'Galkin', 'Male')
stud2.courses_in_progress += ['Python']
stud2.finished_courses += ['Anshlag']

lect1 = Lecturer('Sergay', 'Drobotenko')
lect1.courses_attached += ['C++']
lect2 = Lecturer('Vladimir', 'Vinokur')
lect2.courses_attached += ['Python']

review1 = Reviewer('Regina','Dubovitskaya')
review1.courses_attached += ['C++']
review2 = Reviewer('Lev', 'Leshenko')
review2.courses_attached += ['Python']

stud1.rate_lc(lect1, 'C++', 10)
stud1.rate_lc(lect1, 'С++', 7)
stud1.rate_lc(lect1, 'С++', 4)
stud2.rate_lc(lect2, 'Python', 2)
stud2.rate_lc(lect2, 'Python', 10)
stud2.rate_lc(lect2, 'Python', 5)
stud1.rate_lc(lect1, 'C++', 10)
stud1.rate_lc(lect1, 'C++', 1)
stud1.rate_lc(lect1, 'C++', 7)
stud2.rate_lc(lect2, 'Python', 8)
stud2.rate_lc(lect2, 'Python', 10)
stud2.rate_lc(lect2, 'Python', 2)
stud1.rate_lc(lect1, 'C++', 3)
stud2.rate_lc(lect2, 'Python', 10)

review1.rate_hw(stud1, 'C++', 4)
review1.rate_hw(stud1, 'C++', 10)
review1.rate_hw(stud1, 'C++', 10)
review1.rate_hw(stud1, 'C++', 10)
review1.rate_hw(stud1, 'C++', 10)
review2.rate_hw(stud2, 'Python', 10)
review2.rate_hw(stud2, 'Python', 10)
review2.rate_hw(stud2, 'Python', 10)
review2.rate_hw(stud2, 'Python', 10)
review2.rate_hw(stud2, 'Python', 10)
print(f'Студенты:\n\n{stud1}\n{stud2}')
print(f'Лекторы:\n\n{lect1}\n{lect2}')

print (f'Пример сравнения №1 Студента 1 > Студента 2: {stud1 > stud2}')
print (f'Пример сравнения №2 Студента 1 < Студента 2: {stud1 < stud2}')
print (f'Пример сравнения №3 Студента 1 >= Студента 2: {stud1 >= stud2}')
print (f'Пример сравнения №4 Студента 1 <= Студента 2: {stud1 <= stud2}')
print (f'Пример сравнения №5 Студента 1 == Студента 2: {stud1 == stud2}\n')
print (f'Пример сравнения №1 Лектора 1 > Лектора 2: {lect1 > lect2}')
print (f'Пример сравнения №2 Лектора 1 < Лектора 2: {lect1 < lect2}')
print (f'Пример сравнения №3 Лектора 1 >= Лектора 2: {lect1 >= lect2}')
print (f'Пример сравнения №4 Лектора 1 <= Лектора 2: {lect1 <= lect2}')
print (f'Пример сравнения №5 Лектора 1 == Лектора 2: {lect1 == lect2}\n')  

student_list = [stud1]
lect_list = [lect1]
courses = 'C++'
print (f'Пример подсчёта средней оценки студентов: {universal_average (student_list, courses)}')
print (f'Пример подсчёта средней оценки лектора: {universal_average (lect_list, courses)}')