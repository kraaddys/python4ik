import calendar

def get_day_of_week(year, month, day):
    weekday_number = calendar.weekday(year, month, day)
    weekday_names = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return weekday_names[weekday_number]

# Ввод даты
year = int(input("Введите год: "))
month = int(input("Введите месяц: "))
day = int(input("Введите день: "))

# Проверка даты
if not (1 <= month <= 12 and 1 <= day <= 31 and year >= 1):
    print("Неверный формат даты.")
    exit()

# Определение дня недели
weekday = get_day_of_week(year, month, day)

print(f"{year}-{month}-{day} - {weekday}")
