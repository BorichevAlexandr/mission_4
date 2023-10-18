a = 0
b = 0
c = 0
while a==0:
    try:
        int1 = int(input("Введите первое число(целое): "))
        c = int1
        a = 1
        int1 = abs(int1)
    except(ValueError):
        print("Пожалуйста, введите целое ЧИСЛО")
        a = 0
a = 0
while a==0:
    try:
        int2 = int(input("Введите второе число(целое): "))
        a = 1
        b = int2
        int2 = abs(int2)
    except(ValueError):
        print("Пожалуйста, введите целое ЧИСЛО")
        a = 0
if len(str(int1))>len(str(int2)):
    print(f"Цифр в числе {b} больше чем в {c}")
elif len(str(int1))<len(str(int2)):
    print(f"Цифр в числе {b} больше чем в {c}")
else:
    print(f"Цифр в {b} столько же, сколько и в {c}")

