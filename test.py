def plus(a, b):
    return a+b


def minus(a, b):
    return a-b


def mulpip(a, b):
    return a*b


def divide(a, b):
    return a/b


txt = input("input= ")
txt = txt.split(" ")
a = int(txt[0])
b = int(txt[2])
r = "Answer is "
if txt[1] == "+":
    print("Answer is {:d}".format(plus(a, b)))
elif txt[1] == "-":
    print("Answer is {:d}".format(minus(a, b)))
elif txt[1] == "*":
    print("Answer is {:d}".format(mulpip(a, b)))
elif txt[1] == "/":
    # print("Answer is {:.2f}".format(divide(a, b)))
    print("Anwer is ", divide(a, b))
