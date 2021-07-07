class Featurs:
    def __init__(self):
        print("{} Created".format(self.name))

    def input_data(self):
        datum = input(self.msg1)
        datum1 = input(self.msg2)
        return int(datum), int(datum1)

    def calc_1(self, x, y):
        r = x*y
        print("{}의 넓이는 {}입니다.".format(self.name, r))


class Quadrangle(Featurs):
    name = "사각형"
    msg1 = "가로의 값을 넣으세요??"
    msg2 = "세로의 값을 넣으세요??"


class Recticle(Featurs):
    name = "직사각형"
    msg1 = "가로의 값을 넣으세요??"
    msg2 = "세로의 값을 넣으세요??"


class Parall(Featurs):
    name = "평행사변형"
    msg1 = "밑변의 값을 넣으세요??"
    msg2 = "높이의 값을 넣으세요??"


class Recticle_1(Featurs):
    name = "정사각형"
    msg1 = "한변의 값을 넣으세요??"
    msg2 = msg1


all_features = [Quadrangle(), Recticle(), Parall(), Recticle_1()]

first_msg = "사각형의 종류는??\n"

for i, r in enumerate(all_features):
    first_msg += "{}.{}\n".format(i+1, r.name)

first_msg = first_msg + "(quit=q)\n >>"

type_features = input(first_msg)

if type_features == "q":
    exit()


features_index = int(type_features)-1

if features_index >= len(all_features):
    features_index = 0

recticle = all_features[features_index]
value_x, value_y = recticle.input_data()
recticle.calc_1(value_x, value_y)
