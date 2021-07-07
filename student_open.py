from functools import reduce

g_grades = ["A", "B", "C", "D", "E"]
g_grades.reverse()


class Student:
    grade = ''

    def __init__(self, line):
        name, gender, age, score = line.strip().split(",")
        self.name = name
        self.gender = gender
        self.age = age
        self.score = int(score)

    def __str__(self):
        return "{}**\t{}\t{}\t{}".format(self.name[0], self.gender, self.age, self.grade)

    def make_grade(self):
        if self.score == 100:
            self.grade = "A+"
        else:
            self.grade = g_grades[self.score // 10 - 5]


students = []

with open("students.csv", "r", encoding="utf-8") as file:
    for index, line in enumerate(file):
        if index == 0:
            continue
        else:
            students.append(Student(line))

students.sort(key=lambda stu: stu.score, reverse=True)
set_grade = map(lambda std: std.make_grade(), students)
list(set_grade)

total = reduce(lambda x, y: (
    x if type(x) == int else x.score) + y.score, students)


print("total : {} , Average : {}".format(total, total / len(students)))
print("이름\t성별\t나이\t학점")
print("====\t====\t====\t====")

for s in students:
    print(s)

print("====\t====\t====\t====")

# average_upper = filter(lambda x: x.score > total / len(students), students)

# for i in average_upper:
#     print(i.name, i.score)

for i in students:
    if i.score >= total / len(students):
        print(i.name, i.score)
