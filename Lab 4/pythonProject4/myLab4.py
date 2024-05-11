def ideal_weight(age, height, gender):
    if gender == 'М':
        ideal_weight = height - 100 - ((height - 150) / 4 + (age - 20) / 4)
    elif gender == 'Ж':
        ideal_weight = height - 100 - ((height - 150) / 2.5 + (age - 20) / 6)
    return ideal_weight

def weight_recommendation(actual_weight, ideal_weight):
    if actual_weight < ideal_weight:
        return "Рекомендуется набрать вес."
    elif actual_weight > ideal_weight:
        return "Рекомендуется снизить вес."
    else:
        return "Ваш вес идеальный."

def main():
    while True:
        height = int(input("Введите ваш рост: "))
        if height <= 0:
            print("Вы ввели неверное значение роста.")
        else:
           break

    while True:
        age = int(input("Введите ваш возраст: "))
        if age <= 0:
            print("Не бойся, когда ты один, бойся когда ты ноль.")
        else:
            break

    gender = input("Введите ваш пол (М/Ж): ").upper()
    while gender not in ('М', 'Ж'):  # цикл для повторного запроса пола, пока не введен корректный вариант
        print("Некорректное значение пола. Пожалуйста, введите 'М' или 'Ж'.")
        gender = input("Введите ваш пол (М/Ж): ").upper()

    ideal = ideal_weight(age, height, gender)
    if ideal is not None:
        print("Ваш идеальный вес составляет: {:.2f} кг".format(ideal))

        while True:
            actual_weight = float(input("Введите ваш текущий вес (кг): "))
            if actual_weight <= 0:
                print("Неверное значение веса, введите значение еще раз.")
            else:
                break
        recommendation = weight_recommendation(actual_weight, ideal)
        print(recommendation)


if __name__ == "__main__":
    main()
