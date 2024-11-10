


#? === Тема: Регулярные выражения: Синтаксис и использование ===
#* Регулярные выражения (regex) — это шаблоны для поиска текста и работы со строками.
# Они позволяют находить, изменять или извлекать информацию в строках на основе заданных шаблонов.
# Используя регулярные выражения, мы можем легко обрабатывать текст с сложными структурами.
#! Основные функции: re.match(), re.search(), re.findall(), re.sub()

import re  # Импортируем модуль re для работы с регулярными выражениями

#* === 1. Базовый синтаксис и пример поиска с помощью регулярных выражений ===
def regex_basic_example():
    # Пример шаблона для поиска текста "Python" в строке
    pattern = r"Python"  # Ищет точное совпадение с текстом "Python"
    text = "I am learning Python programming. Python12, Pythonq, Python, Python09"

    #! Используем re.search() для поиска первого вхождения
    match = re.search(pattern, text)
    if match:
        print("Найдено совпадение:", match.group())
    else:
        print("Совпадение не найдено.")

# regex_basic_example()

#* === 2. Использование специальных символов ===
def regex_special_characters():
    text = "Email me at test123@example.com or at admin@sample.org, test123@example.com, test123@example.com "
    
    # Шаблон для поиска email-адресов
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    # \b             - Начало слова, указывает на границу слова
    # [A-Za-z0-9._%+-]+ - Любое сочетание букв, цифр и символов `._%+-`
    # @             - Символ "собачка" в адресах
    # [A-Za-z0-9.-]+ - Домен, включающий буквы, цифры, точки и тире
    # \.            - Обычная точка (экранированная)
    # [A-Z|a-z]{2,} - Окончание домена (2+ букв), например, com, org

    # Используем re.findall() для нахождения всех вхождений
    matches = re.findall(pattern, text)
    print("Найденные email-адреса:", matches)

# regex_special_characters()

#* === 3. Методы поиска: match(), search(), findall(), finditer() ===
def regex_methods_example():
    text = "The price of item A is $20 and item B is $35."

    # Используем re.match() для поиска в начале строки
    match = re.match(r"The price", text)  # Ищет "The price" только в начале строки
    if match:
        print("Результат match():", match.group())
    else:
        print("Совпадение не найдено.")
    
    # Используем re.search() для поиска первого вхождения
    search = re.search(r"\$\d+", text)  
    # \$       - Ищет символ "$" (экранированный)
    # \d+      - Одну или более цифр после "$" (цена)
    print("Результат search():", search.group() if search else "Совпадение не найдено.")

    # Используем re.findall() для нахождения всех вхождений
    pattern = r"\$\d+"
    all_prices = re.findall(pattern, text)  # Найдет все цены, указанные в тексте
    print("Результат findall():", all_prices)

    # Используем re.finditer() для получения всех совпадений с итерацией
    print("Результат finditer():")
    for match in re.finditer(pattern, text):
        print("Совпадение:", match.group(), "на позиции:", match.start())
    # .start()
    # .group()
regex_methods_example()

#* === 4. Замена текста с использованием re.sub() ===
def regex_substitute_example():
    text = "The color is red, but it could also be blue or green."

    # Заменяем все цвета на "COLOR"
    pattern = r"red|blue|green"
    # red|blue|green - Ищет слова "red", "blue" или "green" для замены
    replaced_text = re.sub(pattern, "COLOR", text)
    print("Текст после замены:", replaced_text)

# regex_substitute_example()

#* === 5. Использование группировок и обратных ссылок ===
def regex_grouping_example():
    text = "My phone number is (123) 456-7890."

    # Группируем части телефонного номера
    pattern = r"\((\d{3})\) (\d{3})-(\d{4})"
    # \(          - Открывающая скобка "(" (экранированная)
    # (\d{3})     - Группа: три цифры для кода города
    # \)          - Закрывающая скобка ")" (экранированная)
    # (\d{3})     - Группа: три цифры (первые три цифры номера)
    # -           - Символ "-"
    # (\d{4})     - Группа: четыре цифры (последняя часть номера)

    # Используем re.search() для поиска с группировкой
    match = re.search(pattern, text)
    if match:
        print("Полный номер:", match.group(0))  # Полный номер
        print("Код города:", match.group(1))    # Код города
        print("Первые три цифры:", match.group(2))  # Первые три цифры
        print("Последние четыре цифры:", match.group(3))  # Последние четыре цифры

# regex_grouping_example()

#* === 6. Пример работы с проверкой и валидацией формата ===
def regex_validation_example():
    # Проверка правильности формата email
    email = input("Введите email для проверки: ")
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$"
    # ^              - Начало строки
    # [A-Za-z0-9._%+-]+ - Сочетание символов для локальной части email
    # @              - Символ "@"
    # [A-Za-z0-9.-]+ - Доменное имя
    # \.             - Точка перед доменом верхнего уровня
    # [A-Z|a-z]{2,}  - Минимум две буквы для домена верхнего уровня
    # $              - Конец строки

    if re.match(pattern, email):    
        print("Email в корректном формате.")
    else:
        print("Неверный формат email!")

# regex_validation_example()

#* === 7. Пример: поиск слов, начинающихся с заглавной буквы ===
def regex_capitalized_words():
    text = "London and Paris are beautiful cities. So is New York."

    # Ищем слова, которые начинаются с заглавной буквы
    pattern = r"\b[A-Z][a-z]*\b"
    # \b       - Граница слова
    # [A-Z]    - Заглавная буква в начале слова
    # [a-z]*   - Ноль или более строчных букв
    # \b       - Граница слова

    capitalized_words = re.findall(pattern, text)
    print("Слова с заглавной буквы:", capitalized_words)

# regex_capitalized_words()

#* === 8. Пример обработки списка с регулярными выражениями ===
def regex_list_processing():
    items = ["apple", "banana", "cherry", "date", "elderberry"]

    # Ищем элементы, которые содержат букву 'e'
    pattern = r"e"  # Ищет букву "e" в каждом элементе списка
    items_with_e = [item for item in items if re.search(pattern, item)]
    print("Элементы с буквой 'e':", items_with_e)

# regex_list_processing()

#* === 9. Обработка строк с многократными пробелами и чистка текста ===
def regex_clean_text():
    text = "Это   пример   текста    с   лишними пробелами."
    
    # Убираем лишние пробелы
    clean_text = re.sub(r"\s+", " ", text).strip()
    # \s+     - Один или более пробельных символов для замены на один пробел
    print("Текст после очистки:", clean_text)

# regex_clean_text()
