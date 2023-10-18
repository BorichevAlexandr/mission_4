from datetime import datetime, timedelta

year = 0
flak = 0
while flak == 0 or year < 0:

    try:
        year = int(input("Введите год рождения: "))
        flak = 1
    except ValueError:
        print("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО!!!")
        flak = 0
flak = 0
month = 0
while flak == 0 or month < 0:

    try:
        month = int(input("Введите месяц рождения: "))
        flak = 1
    except ValueError:
        print("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО!!!")
        flak = 0
flak = 0
day = 0
while flak == 0 or day < 0:

    try:
        day = int(input("Введите день рождения: "))
        flak = 1
    except ValueError:
        print("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО!!!")
        flak = 0
flak = 0
date_str = f"{year}-{month}-{day}"
birthday = datetime.strptime(date_str, "%Y-%m-%d")


date_10000_days = birthday + timedelta(days=10000)
print("Через 10 000 дней:", date_10000_days.date())


date_1000000_minutes = birthday + timedelta(minutes=1000000)
print("Через 1 000 000 минут:", date_1000000_minutes.date())


date_1000000000_seconds = birthday + timedelta(seconds=1000000000)
print("Через 1 000 000 000 секунд:", date_1000000000_seconds.date())