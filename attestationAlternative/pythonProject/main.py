from library import *

def main():
    authors = {}

    while True:
        print("\n--- Меню ---")
        print("1. Добавить нового автора")
        print("2. Добавить новую книгу")
        print("3. Показать список авторов и их книг")
        print("4. Показать количество книг у каждого автора")
        print("5. Удалить автора и его произведения")
        print("6. Выход")

        choice = input("Введите номер пункта меню: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Формат ввода неверный.")
            continue

        if choice not in range(1, 7):
            print("Неверный пункт меню.")
            continue

        if choice == 1:
            name = input("Введите имя нового автора: ")
            add_author(authors, name)

        elif choice == 2:
            name = input("Введите имя автора: ")
            book = input("Введите название книги: ")
            add_book(authors, name, book)

        elif choice == 3:
            list_authors(authors)

        elif choice == 4:
            book_count(authors)

        elif choice == 5:
            name = input("Введите имя автора: ")
            remove_author(authors, name)

        elif choice == 6:
            print("Благодарю за использование программы.")
            break

if __name__ == "__main__":
    main()
