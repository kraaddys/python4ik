import re

def check_phone_number(input_str):
    # Паттерн для проверки номера телефона
    phone_pattern = re.compile(r'^(\+?373|00373)?(\d{8}|\d{7})$')

    # Попытка найти совпадение с паттерном. Метод match использован для проверки
    # совпадает ли начало строки заданному регулярному выражению.
    match = re.match(phone_pattern, input_str)

    # Если найдено совпадение, то номер телефона корректен
    if match:
        return True
    else:
        return False

def main():
    while True:
        try:
            # Ввод номера телефона
            phone_number = input("Введите номер телефона: ")

            # Проверка номера телефона
            if check_phone_number(phone_number):
                print("Номер телефона корректен.")
                break
            else:
                print("Некорректный номер телефона. Попробуйте еще раз.")
        except KeyboardInterrupt:
            print("\nПрограмма завершена.")
            break

if __name__ == "__main__":
    main()
