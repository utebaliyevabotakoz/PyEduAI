def open_file_read():
    # открывает файл для чтения. Файл должен существовать
    file = open ("examples.txt","r") #открытие файла для чтения
    content = file.read() #чтение содержимого файла
    print(content)
    file.close()

#"C:\\Users\\Administrator\\Downloads\\Утебалиева Ботакоз Дузелбаевна.pdf"    absolute path

#open_file_read()  #прочитает содержимого файла


# r read - чтение
# w write - запись
# a append - добавляет данные в конец файла
# r+ read + write - чтение и запись


def open_file_write():
    file = open("examples.txt", "w")  # открытие файла для чтения
    file.write ("Heelo worls.\n")   # запись данных в файл
    file.close()

# open_file_write()



def open_file_append(message):
    file = open("examples.txt", "a")  # открытие файла для чтения
    file.write (f" {message} \n")   # запись данных в файл
    file.close()

# open_file_append("new message")


def open_file_read_write():
    file = open ("examples.txt","r+") #открытие файла для чтения
    content = file.read() #чтение содержимого файла
    print("содержиммое перед записью \n", content)
    file.write ("New content R+ \n")
    file.close()

# open_file_read_write()




def open_file_read_with():
    # открывает файл для чтения. Файл должен существовать
    with open (" examples.txt","r") as file: #открытие файла для чтения
        content = file.read() #чтение содержимого файла
        print(content)


# open_file_read_with()
