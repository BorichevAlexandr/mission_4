from  random import randint
N = randint(4, 30)
flak = 0
step = 4
winner = 4
spis_connect = ["Я хожу 😈", "Теперь мой ход 😋", "Сделаем так 😁"]
print(len(spis_connect))
print(f"Количество камней будет равно {N}")


while N > 1:
    stepT = randint(1, 3)

    while(flak == 0 or step > 3 or step < 1):
        try:
            step = int(input("Сколько возьмете камней(допустимо: 1, 2, 3)? \n"))
            flak = 1
            if step > 3 or step < 1 or step > N:
                print("ХОХОХО, не смешно 😐, введите допустимые значения")
                flak = 0
        except ValueError:
            print("ХОХОХО, не смешно 😐, введите допустимые значения")
            flak = 0
    flak = 0
    N -= step

    if  int(str(N)[len(str(N)) - 1]) > 4 or N in [10, 11, 12, 13, 14]:
        print(f"Окей, в куче осталось {N} камней")
    elif int(str(N)[len(str(N)) - 1]) >= 2 and int(str(N)[len(str(N)) -1]) <= 4:
        print(f"Окей, в куче осталось {N} камня")
    else:
        print(f"Окей, в куче остался {N} камень")


    winner = 0
    if N == 1:
        break
    print(spis_connect[randint(0, len(spis_connect))-1])
    if N == 4:
        print("Уберу из кучи 3 камня")
        N -= 3
        print(f"Теперь в куче остался {N} камень")
    elif N == 3:
        N-= 2
        print("Уберу из кучи 2 камня")
        print(f"Теперь в куче остался {N} камень")
    elif N == 2:
        print("Уберу из кучи камень")
        N-=1
        print(f"Отныне в куче остался {N} камень")
    else:
        N -= stepT
        if stepT != 1:
            print(f"Уберу из кучи {stepT} камня")
        else:
            print(f"Уберу из кучи {stepT} камень")

        if int(str(N)[len(str(N)) - 1]) > 4 or N in [10, 11, 12, 13, 14]:
            print(f"Теперь в куче осталось {N} камней")
        elif int(str(N)[len(str(N)) - 1]) >= 2 and int(str(N)[len(str(N)) - 1]) <= 4:
            print(f"Отныне в куче осталось {N} камня")
        else:
            print(f"Ну всё, в куче остался {N} камень")
    winner = 1
    if N == 1:
        break


if winner == 0 and N!=0:
    print("Ваша взяла😝")
else:
    print("Изи победа 😎")

