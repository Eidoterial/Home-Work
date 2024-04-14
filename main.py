import random as ran


class SchoolMember:
    def __init__(self):
        self._first_name = None
        self._last_name = None

    def set_First_Name(self, name: str):
        self._first_name = name

    def set_Last_Name(self, name: str):
        self._last_name = name

    def get_First_Name(self):
        return self._first_name

    def get_Last_Name(self):
        return self._last_name


class Teacher(SchoolMember):
    def __init__(self):
        super().__init__()
        self._salary = None

    def set_Salary(self, salary: int):
        self._salary = salary

    def get_Salary(self):
        return self._salary

    def tell(self):
        print(f"Вчитель:  Ім'я - {self._first_name}, Прізвище - {self._last_name} Зарплата - {self._salary}")


class Student(SchoolMember):
    def __init__(self):
        super().__init__()
        self._score_1 = None
        self._score_2 = None
        self._score_3 = None

    def set_Score(self, score: list[int]):
        self._score_1 = score[0]
        self._score_2 = score[1]
        self._score_3 = score[2]

    def get_Score(self):
        return [self._score_1, self._score_2, self._score_3]

    def midle_score(self):
        return round((self._score_1 + self._score_2 + self._score_3) / 3, 1)
    def tell(self):
        print(f"Учень:    Ім'я - {self._first_name}, Прізвище - {self._last_name} Середній бал - {self.midle_score()}")

if __name__ == '__main__':
    f_names = ["Ivan", "Oleg", "Termon", "Termos", "Colos", "Paket", "Copical", "Printer", "Giga Brain", "Peta-Tree", "Micro-Gnom", "Pup"]
    l_names = ["Cocos", "King", "Forev", "Tera", "Ignis", "Valker", "Lup"]

    teachers = []
    students = []

    for i in range(2):
        teacher = Teacher()

        teacher.set_First_Name(ran.choice(f_names))
        teacher.set_Last_Name(ran.choice(l_names))
        teacher.set_Salary(ran.randint(10000, 30000))

        teachers.append(teacher)

        student = Student()

        student.set_First_Name(ran.choice(f_names))
        student.set_Last_Name(ran.choice(l_names))
        student.set_Score([ran.randint(1, 12), ran.randint(1, 12), ran.randint(1, 12)])

        students.append(student)


    for i in range(2):
        teachers[i].tell()
        students[i].tell()
