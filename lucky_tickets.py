a = 0
n = 0
m = 0

while a == 0:
    try:
        n = int(input("Введите меньший номер билета(6-ти значное число): "))
        a = 1
    except(ValueError):
        print("Пожалуйста, введите 6-ти значное ЧИСЛО: ")
        a = 0
print(len(str(n)))
while len(str(n)) != 6:
    a = 0
    while a == 0:
        try:
            n = int(input("Пожалуйста, введите 6-ти значное ЧИСЛО: "))
            a = 1
        except(ValueError):
            print("Пожалуйста, введите 6-ти значное ЧИСЛО: ")
            a = 0

a = 0
while a == 0:
    try:
        m = int(input("Введите больший номер билета(6-ти значное число): "))
        a = 1
    except(ValueError):
        print("Пожалуйста, введите 6-ти значное ЧИСЛО: ")
        a = 0
while len(str(m)) != 6:
    a = 0
    while a == 0:
        try:
            m = int(input("Пожалуйста, введите 6-ти значное ЧИСЛО: "))
            a = 1
        except(ValueError):
            print("Пожалуйста, введите 6-ти значное ЧИСЛО: ")
            a = 0

cnt = 0
for i in range(n, m+1):
    i = str(i)
    x = 0
    y = 0
    for j in range(3):
        x += int(i[j])
        y += int(i[::-1][j])

    if x == y:
        cnt += 1
print("Количество счастливых билетов равно: ", cnt)
