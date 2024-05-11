import math

def calculate_fall_time(height):
    # Проверка введенного значения
    if math.isnan(height):
        print("Неверный формат высоты.")
        return

    # Расчет времени падения
    g = 9.8  # Ускорение свободного падения (м/с²)
    time = math.sqrt(2 * height / g)

    print(f"Время падения: {time:.2f} секунд")

# Ввод высоты
height = float(input("Введите высоту (в метрах): "))

# Расчет времени падения
calculate_fall_time(height)
