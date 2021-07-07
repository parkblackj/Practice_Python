class Quadrangle:
    def __init__(self):
        print("Quadrangle Created")

    def input_data(self, msg1, mag2):
        datum = input(msg1, mag2)
        value_x, value_y = int(datum[0]), int(datum[1])


class Recticle(Quadrangle):
    def calc(self, x, y):
        return x*y


class Parall(Quadrangle):
    def calc(self, x, y):
        return x*y


type_features = input("사각형의 종류는??\n 1.Recticle\n 2.Parall\n (quit=q)\n >>")

if type_features == "q":
    exit()

if type_features == "1":
    recticle = Recticle()
    value_x = input("가로의 값을 넣으세요??")
    value_y = input("세로의 값을 넣으세요??")
    value_x, value_y = int(value_x), int(value_y)

    result = recticle.calc(value_x, value_y)
    print("직사각형의 넓이는 {}".format(result))

else:
    parall = Parall()
    value_x = input("밑변의 값을 넣으세요??")
    value_y = input("높이의 값을 넣으세요??")
    value_x, value_y = int(value_x), int(value_y)
    result = parall.calc(value_x, value_y)
    print("평행사변형의 넓이는 {}".format(result))
