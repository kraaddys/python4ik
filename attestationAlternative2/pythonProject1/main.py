import re
def check_name(name):
  """Проверяет, состоит ли имя из букв, дефисов и апострофов,
      а также не начинается и не заканчивается дефисом."""
  pattern = r"^[a-zA-Z]+(?:[-\s][a-zA-Z]+)*$"
  return re.match(pattern, name) is not None

def main():
  # Списки для хранения данных о сотрудниках
  names = []
  departments = []
  salaries = []

  # Словарь для хранения информации о департаментах
  department_info = {}

  while True:
    # Отображение меню
    print("\nГлавное меню:")
    print("1. Ввести данные о сотруднике")
    print("2. Вывести среднюю зарплату сотрудников ")
    print("3. Вывести среднюю зарплату по департаментам")
    print("4. Найти сотрудника с самой высокой зарплатой")
    print("5. Найти сотрудника с наименьшей зарплатой")
    print("0. Выход")

    # Получение выбора пользователя
    choice = input("Введите номер пункта меню: ")

    # Обработка выбора пользователя
    if choice == '1':
      # Ввод данных о сотруднике
      name = input("Введите фамилию и имя: ")
      while not check_name(name):
        print("Неверный формат имени или фамилии. Повторите ввод.")
        name = input("Введите фамилию и имя: ")

      department = input("Введите название департамента: ").lower()
      salary = input("Введите зарплату: ")

      try:
        salary = float(salary)
        if not 1000 <= salary <= 77000:
          print("Зарплата должна быть в диапазоне от 1000.00 до 77000.00.")
          continue
      except ValueError:
        print("Неверный формат зарплаты.")
        continue

      names.append(name)
      departments.append(department)
      salaries.append(salary)

      if department in department_info:
        department_info[department]['count'] += 1
        department_info[department]['total_salary'] += salary
      else:
        department_info[department] = {'count': 1, 'total_salary': salary}

    elif choice == '2':
        # Вывод данных о сотрудниках
        if not names:
            print("Список сотрудников пуст.")
        else:
            total_salary = sum(salaries)
            average_salary = total_salary / len(salaries)
            print(f"\nСредняя зарплата сотрудников: {average_salary:.2f}")


    elif choice == '3':
      # Вывод информации о средней зарплате по департаментам
      if not department_info:
        print("Информация о департаментах отсутствует.")
      else:
        print("\nСредняя зарплата по департаментам:")
        with open("average_salaries.txt", 'w') as file:
          for department, info in department_info.items():
            average_salary = info['total_salary'] / info['count']
            print(f"{department}: {average_salary:.2f}")
            file.write(f"{department}: {average_salary:.2f}\n")

    elif choice == '4':
      # Поиск сотрудника с самой высокой зарплатой
      if not names:
        print("Список сотрудников пуст.")
      else:
        highest_salary = max(salaries)
        highest_paid_employee_index = salaries.index(highest_salary)
        print(f"\nСотрудник с самой высокой зарплатой: {names[highest_paid_employee_index]}: "
              f"{departments[highest_paid_employee_index]}, "
              f"{highest_salary:.2f}")


    elif choice == '5':
      # Поиск сотрудника с наименьшей зарплатой
      if not names:
        print("Список сотрудников пуст.")
      else:
        lowest_salary = min(salaries)
        lowest_paid_employee_index = salaries.index(lowest_salary)
        print(
          f"\nСотрудник с наименьшей зарплатой: {names[lowest_paid_employee_index]}: "
          f"{departments[lowest_paid_employee_index]}, "
          f"{lowest_salary:.2f}")

    elif choice == '0':
      print("Вы вышли из программы.")
      break

    else:
      # Неверный выбор
      print("Неверный номер пункта меню. Повторите попытку.")

if __name__ == "__main__":
  main()