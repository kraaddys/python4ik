from collections import defaultdict
def add_author(authors, name):
    if name in authors:
        print(f"Автор '{name}' уже существует.")
    else:
        authors[name] = []
        print(f"Автор '{name}' был добавлен в список.")

def add_book(authors, name, book):
    if name not in authors:
        print(f"Автор '{name}' не найден.")
    else:
        authors[name].append(book)
        print(f"Книга '{book}' успешно добавлена автору '{name}'.")

def list_authors(authors):
    for name, books in authors.items():
        if books:
            print(f"\n**{name}**")
            for book in books:
                print(f"- {book}")
        else:
            print(f"\n**{name}** - Нет книг")

def book_count(authors):
    for name, books in authors.items():
        print(f"{name}: {len(books)}")

def remove_author(authors, name):
    if name not in authors:
        print(f"Автор '{name}' не найден.")
    else:
        del authors[name]
        print(f"Автор '{name}' и его произведения успешно удалены из словаря.")