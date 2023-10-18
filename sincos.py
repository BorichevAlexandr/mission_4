import math

x = 0
flak = 0

while flak==0:
    try:
        x = int(input("Введите величину угла(в градусах): "))
        flak = 1
    except ValueError:
        print("Пожалуйста введите реальное значение угла")
        flak = 0


print(f"cos угла {x}° = {math.cos(math.radians(x)): .2f}")
print(f"sin угла {x}° = {math.sin(math.radians(x)): .2f}")
print(f"tan угла {x}° = {math.tan(math.radians(x)): .2f}")
