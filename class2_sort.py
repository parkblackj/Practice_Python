class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return "{}:{}".format(self.name, self.score)


students = [Student("김이수", 30),
            Student("김삼수", 10),
            Student("김사수", 20)
            ]


def print_students():
    print("============================")
    for i in students:
        print(i)


# sorted(students, key=lambda stu: stu.score)

print_students()

students.sort(key=lambda stu: stu.score)

print_students()

print(students[1])
