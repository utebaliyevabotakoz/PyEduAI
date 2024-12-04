from DatabaseManager import DatabaseManager
from Bookstore import Bookstore

db = DatabaseManager("bookstore.db")

class Person:
    def __init__(self, title):
        self.title  = title
        self.books_list = []

    def buy_book(self, title):
        book = Bookstore(None, None, None, None, None, None)
        book.select_book(title)
        print("Оформляем покупку. Пожалуйста подождите ...")
        book.update_book("amount = amount - 1", title)
        print("Спасибо за покупку! Ваша покупка оформлена!")
        book.select_book(title)

