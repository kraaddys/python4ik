import re

def input_data():
    while True:
        surname = input("Введите фамилию сотрудника: ")
        if not re.match(r'^(?!.*(.)\1{2,})[a-zA-Z]+(?:-[a-zA-Z]+)?$', surname.strip()):
            print("Ошибка: Фамилия должна содержать только буквы и дефис, от 2 до 20 символов, и не должна быть слишком простой.")
            continue

        name = input("Введите имя сотрудника: ")
        if not re.match(r'^(?!.*(.)\1{2,})[a-zA-Z]+(?:-[a-zA-Z]+)?$', name.strip()):
            print("Ошибка: Имя должно содержать только буквы и дефис, от 2 до 20 символов, и не должно быть слишком простым.")
            continue

        department = input("Введите отдел, в котором работает сотрудник: ")
        if not re.match(r'^[a-zA-Z0-9]+(?: [a-zA-Z0-9]+)?$', department.strip()):
            print("Ошибка: Название отдела должно содержать буквы и цифры, от 2 до 20 символов.")
            continue

        try:
            children = int(input("Введите количество детей сотрудника (0-19): "))
            if not 0 <= children <= 19:
                print("Ошибка: Количество детей должно быть целым числом от 0 до 19.")
                continue
        except ValueError:
            print("Ошибка: Введите целое число от 0 до 19.")
            continue

        # Если все проверки пройдены успешно, сохраняем данные в файл
        with open("data.txt", "a") as file:
            file.write(f"{surname}\t{name}\t{department}\t{children}\n")

        print("Данные успешно сохранены.")
        break




def view_data():
    total_children = 0
    with open("data.txt", "r") as file:
        for line in file:
            surname, name, department, children = line.strip().split('\t')
            print(f"{surname} {name}, отдел: {department}, количество детей: {children}")
            total_children += int(children)
    print(f"Всего детей: {total_children}")


def find_childless():
    pass


def menu():
    print("Меню:")
    print("1. Ввод данных в файл")
    print("2. Просмотр данных о детях сотрудников")
    print("3. Поиск и вывод списка бездетных сотрудников")
    print("4. Выход из программы")


def main():
    while True:
        menu()
        choice = input("Выберите опцию (1-4): ")

        if choice == '1':
            input_data()
        elif choice == '2':
            view_data()
        elif choice == '3':
            find_childless()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите опцию от 1 до 4.")


if __name__ == "__main__":
    main()
