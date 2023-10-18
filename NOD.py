import math


flak = 0
def NOD(x, y):
    if x <= 0 or y <= 0:
        return "ОШИБКА!!!! ВВЕДИТЕ НАТУРАЛЬНЫЕ ЧИСЛА!!!!"
    delit = []
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            delit.append(i)
    if x == y:
        return y
    return max(delit)


while flak == 0:

    try:
        x = int(input("Введите первое число: "))
        flak = 1
    except ValueError:
        print("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО!!!")
        flak = 0
flak = 0
while flak == 0:

    try:
        y = int(input("Введите второе число: "))
        flak = 1
    except ValueError:
        print("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО!!!")
        flak = 0
print(f"НОД {x} и {y} равен {NOD(x, y)} по моей функции\n{math.gcd(x,y)} по функции gcd из модуля math")