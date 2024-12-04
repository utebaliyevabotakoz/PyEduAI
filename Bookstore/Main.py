from Bookstore import Bookstore
from Person import Person
def main():


    while True:
        print("\nНаш любимый BookStore")
        print("1. Добавить книгу в магазин")
        print("2. Удалить книгу из магазина")
        print("3. Обновить данные книги")
        print("4. Поиск книги по критериям (например, по title, author, году выпуска year, жанру genre)")
        print("5. Просмотреть все книги")
        print("6. Купить книгу по названию")
        print("7. Выход")


        choice = input("Введите ваш выбор: ")

        # Обработка выбора пользователя
        if choice == "1":
            title = input("Введите Название книги: ")
            author = input("Введите Автор книги: ")
            year = input("Введите Год выпуска книги (формат: YYYY-MM-DD): ")
            genre = input("Введите Жанр книги: ")
            price = int(input("Введите Цена книги: "))
            amount = int(input("Введите Количество доступных экземпляров книги: "))

            book = Bookstore (title,author, year, genre, price, amount)
            book.add_new_book(title,author, year, genre, price, amount)


        elif choice == "2":
            title = input("Введите Название книги для удаления: (шаблон title='Harry Potter') ")
            book = Bookstore(title,None,None,None,None,None)
            book.delete_book(title)

        elif choice == "3":
            updates = input("Введите нужные изменения через запятую (шаблон title='The Lord of the Ring', amount=5): ")
            condition = input("Введите условие для изменения (шаблон title='Harry Potter'): ")
            book = Bookstore(None,None,None,None,None,None)
            book.update_book(updates, condition)

        elif choice == "4":
            condition = input("Введите условие для поиска (шаблон title='Harry Potter'): ")
            book = Bookstore(None,None,None,None,None,None)
            book.select_book(condition)

        elif choice == "5":
            book = Bookstore(None,None,None,None,None,None)
            book.select_all_book()

        elif choice == "6":
            book = Bookstore(None, None, None, None, None, None)
            print("Доступные книги в ассортименте")
            book.select_all_book()
            title = input("Введите Название книги для покупки (шаблон title='Harry Potter'): ")
            person = Person(title)
            person.buy_book(title)

        elif choice == "7":
            print("До свидания! Приходите к нам еще")
            book = Bookstore(None, None, None, None, None, None)
            book.close_connection()
            break

        else:
            print("Неверный выбор, пожалуйста, попробуйте снова.")



# Запуск основной программы
# if __name__ == "__Zoo__":
main()
