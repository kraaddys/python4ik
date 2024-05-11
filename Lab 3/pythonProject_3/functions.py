# Функция для отображения списка товаров
def show_items(items):
  for i, item in enumerate(items, 1): # enumerate() - это функция,
# которая перебирает элементы списка и возвращает их порядковые номера и сами элементы.
    print(f"{i}. {item}")

# Функция для добавления товара
def add_item(items):
  item = input("Введите название товара: ")
  items.append(item) # append - метод для добавления элемента в конец списка. В данном случае принимает в качестве
# аргумента переменную item.

# Функция для удаления товара по порядковому номеру
def remove_item_by_index(items):
  while True:
    try:
      index = int(input("Введите порядковый номер товара (начиная с 1): "))
      if index <= 0 or index > len(items):
        raise ValueError # raise - ключевое слово для генерации исключения
      break # Выходит из цикла
    except ValueError:
      print("Неверный формат. Введите целое число больше 0.")
  del items[index - 1]
  print(f"Товар с индексом '{index}' успешно удален.")

# Функция для удаления товара по названию
def remove_item_by_name(items):
  item = input("Введите название товара: ")
  if item not in items:
    print(f"Товар '{item}' не найден.")
    return
  items.remove(item)
  print(f"Товар '{item}' успешно удален.")