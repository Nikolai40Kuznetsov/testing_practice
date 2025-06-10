class Error(Exception):
    pass


from math import pi
def area(a):
    return pi * a * a
def circumference(a):
    return a * pi * 2

user_input = input("Введите радиус круга ")
try:
    if user_input == "":
        raise Error 
    u_input = float(eval(user_input))
except NameError:
    print("Not number")
    raise SystemExit
except Error:
    print("Empty")
    raise SystemExit
if u_input < 0:
    print("Number can't be below 0")
    raise SystemExit
print(f"Длина окружности: {circumference(u_input)} единиц")
print(f"Площадь круга: {area(u_input)} квадратных единиц")
# Радиус = 1 ++++, 0 ++++, 0.0001 -+++, -5 --++, abc --++, "" --++, 10**-9 ---+