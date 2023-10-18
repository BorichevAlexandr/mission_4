from datetime import datetime

year = 0
flak = 0
while flak == 0 or year < 0:

    try:
        year = int(input("Введите год отбытия: "))
        flak = 1
    except ValueError:
        print("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО!!!")
        flak = 0
flak = 0
month = 0
while flak == 0 or month < 0:

    try:
        month = int(input("Введите месяц отбытия: "))
        flak = 1
    except ValueError:
        print("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО!!!")
        flak = 0
flak = 0
day = 0
while flak == 0 or day < 0:

    try:
        day = int(input("Введите день отбытия: "))
        flak = 1
    except ValueError:
        print("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО!!!")
        flak = 0
flak = 0
hour = 0
while flak == 0 or hour < 0:

    try:
        hour = int(input("Введите час отбытия: "))
        flak = 1
    except ValueError:
        print("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО!!!")
        flak = 0
flak = 0
minutes = 0
while flak == 0 or minutes < 0:

    try:
        minutes = int(input("Введите минуту отбытия: "))
        flak = 1
    except ValueError:
        print("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО!!!")
        flak = 0
flak = 0
year1 = 0
while flak == 0 or year1 < 0 or year1 < year:

    try:
        year1 = int(input("Введите год прибытия: "))
        flak = 1
    except ValueError:
        print("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО!!!")
        flak = 0
flak = 0
month1 = 0
while flak == 0 or month1 < 0 or (year1 == year and month1<month):

    try:
        month1 = int(input("Введите месяц прибытия: "))
        flak = 1
    except ValueError:
        print("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО!!!")
        flak = 0
flak = 0
day1 = 0
while flak == 0 or day1 < 0 or (year1 == year and month1==month and day1<day):

    try:
        day1 = int(input("Введите день прибытия: "))
        flak = 1
    except ValueError:
        print("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО!!!")
        flak = 0
flak = 0
hour1 = 0
while flak == 0 or hour < 0 or (year1 == year and month1==month and day1==day and hour1<hour):

    try:
        hour1 = int(input("Введите час прибытия: "))
        flak = 1
    except ValueError:
        print("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО!!!")
        flak = 0
flak = 0
minutes1 = 0
while flak == 0 or minutes1 < 0 or (year1 == year and month1==month and day1==day and hour1==hour and minutes1<minutes):

    try:
        minutes1 = int(input("Введите минуту прибытия: "))
        flak = 1
    except ValueError:
        print("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО!!!")
        flak = 0

date_str = f"{str(year)}-{str(month)}-{str(day)} {str(hour)}:{str(minutes)}"
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")


date_str1 = f"{str(year1)}-{str(month1)}-{str(day1)} {str(hour1)}:{str(minutes1)}"
dt1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M")


travel_time = dt1 - dt


print("Время в пути:", travel_time)
