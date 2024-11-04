
#* Открытие файла для чтения с помощью with
def open_file_read_with():
    """ Открывает файл для чтения. Файл должен существовать. """
    with open("example.txt", "r") as file:  # ? Открытие файла для чтения (r)
        content = file.read()  # Чтение содержимого файла
        print(content) # ? Вывод содержимого файла
# open_file_read_with()  # ! Прочитает содержимое существующего файла

def open_file_write_with():
    """ Открывает файл для записи. Создаёт файл, если он не существует. """
    with open("example.txt", "w") as file:  # * Открытие файла для записи (w)
        file.write("NEW write method, write style.\n")  # ? Запись данных в файл

# open_file_write_with()  # ! Создаст новый файл или очистит существующий

def open_file_append_with():
    """ Открывает файл для добавления. Создаёт файл, если он не существует. """
    with open("example.txt", "a") as file:  # * Открытие файла для добавления (a)
        file.write("Добавлено новое содержимое.\n")  # ? Добавление данных в файл

# open_file_append_with()  # ! Добавит новое содержимое в файл

def open_file_read_write_with():
    """ Открывает файл для чтения и записи. Файл должен существовать. """
    with open("example.txt", "r+") as file:  # * Открытие файла для чтения и записи (r+)
        content = file.read()  # Чтение содержимого файла
        print("Содержимое файла перед записью:", content)  # ? Вывод содержимого файла
        file.write("Записано новое содержимое.\n")  # ? Запись данных в файл

# open_file_read_write_with()  # ! Прочитает и запишет новое содержимое в файл

#? TXT, CSV, BIN, JSON




