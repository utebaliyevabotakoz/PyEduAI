
#* Создание файла и запись чисел
def create_and_write_numbers_into_new_files():
    """ Создаёт файл и записывает в него числа. """

    with open("numbers.txt", "w") as file:  # * Открытие файла для записи (w)
        numbers = [10, 20, 30, 40, 50]  # ? Список чисел для записи
        for number in numbers:
            file.write(f"{number}\n")  # ? Запись каждого числа в файл

# create_and_write_numbers_into_new_files()  # ! Создаст файл и запишет числа в него








#* Чтение чисел из файла и выполнение вычислений
def read_numbers_and_calculate():
    """ Читает числа из файла и выполняет вычисления. """
    numbers = []  # ? Создание пустого списка для хранения чисел

    with open("numbers.txt", "r") as file:  # ? Открытие файла для чтения (r)
        for line in file:  # ? Чтение файла построчно
            number = int(line.strip())  # Преобразование строки в число
            numbers.append(number)  # ? Добавление числа в список

    total = sum(numbers)  # ? Вычисление суммы чисел
    # ТАКЖЕ И ЗДЕСЬ, НАЙТИ СУММУ БЕЗ ЭТОЙ ФУНКЦИИ (SUM)
    average = total / len(numbers)   # ? Вычисление среднего значения
    maximum = max(numbers)  # ? Нахождение максимального значения
    # НАЙТИ МАКСИМАЛЬНОЕ ЗНАЧЕНИЕ НЕ ИСПОЛЬЗУЯ ФУНКЦИЮ MAX, НЕ SORT
    

    print(f"Сумма: {total}")  # ? Вывод суммы
    print(f"Среднее: {average}")  # ? Вывод среднего значения
    print(f"Максимальное значение: {maximum}")  # ? Вывод максимального значения

read_numbers_and_calculate()  # ! Читает числа и выполняет вычисления
