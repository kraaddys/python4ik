import datetime
import calendar
import re

def calculate_days_lived(birth_date, current_date):
    # Рассчитываем количество прожитых дней
    days_lived = (current_date - birth_date).days
    return days_lived


# Функция для проверки правильности ввода даты
def is_valid_date(date_str):
    pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return bool(pattern.match(date_str))


# Получаем дату рождения от пользователя
while True:
    birth_str = input("Введите дату рождения в формате ГГГГ-ММ-ДД: ")

    if is_valid_date(birth_str):
        year_of_birth, month_of_birth, day_of_birth = map(int, birth_str.split('-'))

        # Проверяем корректность введенной даты
        if calendar.isleap(year_of_birth) and month_of_birth == 2 and day_of_birth == 29:
            print("Вы ввели 29 февраля в високосном году. Это корректно.")
            break
        elif not calendar.isleap(year_of_birth) and month_of_birth == 2 and day_of_birth == 29:
            print("В этом году нет 29 февраля. Пожалуйста, введите корректную дату.")
        else:
            birth_date = datetime.date(year_of_birth, month_of_birth, day_of_birth)

            # Проверяем, что дата рождения не в будущем
            if birth_date > datetime.date.today():
                print("Ошибка: Вы ввели дату рождения в будущем. Пожалуйста, введите корректную дату.")
            else:
                break
    else:
        print("Неверный формат даты. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД.")

# Получаем текущую дату
current_date = datetime.date.today()

# Рассчитываем количество прожитых дней и выводим результат
days_lived = calculate_days_lived(birth_date, current_date)
print("Количество прожитых дней с момента вашего рождения до сегодняшнего дня:", days_lived)