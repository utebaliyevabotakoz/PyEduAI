
#* Tuples - кортежи - НЕИЗМЕНЯЕМЫЙ список данных. 
#* Создается с помощью обычных скобок () и элементы внутри чередуются с запятыми


ticket_info = ("Алексей", "Ряд 3", "Место 12", ())
#? Как только билет выдан, место закреплено, и никто не может изменить его случайно.

#! КАКИЕ ПРЕИМУЩЕСТВА НАД СПИСКАМИ: 
#? 1) Скорость: Из-за того что кортежи неизменяемы, они обрабатываются быстрее, чем списки.
#? 2) Меньше памяти (экономия ресурсов):Кортежи 
#? 3) Занимают меньше места в памяти по сравнению со списками, так как им не нужно резервировать место для добавления новых элементов.

#* Dictionary - словари - КЛЮЧ + ЗНАЧЕНИЕ 
#* Создается с помощью фигурных скобок {} и состоят из ПАРЫ данныз {'ключ': 'значение'}


phone_book = {
    'Bekzat': '+77053876883',
    'Bobik': '+gav-gavgavgav-gavgavgavgavgavgav',
    'Oleg': {'home': '209385920834', 'work': '028340928', 'gender':('male')},
}


#! Зачем? Чтобы мы могли связывать ключ с его значением и могли легко находить данные
#! Вообще на понятии КЛЮЧ+ЗНАЧЕНИЕ построен например... Excel
#! У каждой ячейки есть своё имя (координаты), например А1, как только вы вводите туда значение, она привязывается к А1

excel_sheet = {
    'A1': 333,
    'A2': 444,
}

#! ЕСТЕСТВЕННО: Двух одинаковых ключей НЕ МОЖЕТ быть, но а вот значения могут

#* КАК ссылаться к значениям? С помошью их КЛЮЧЕЙ
number_bekzat = phone_book['Bekzat']

#* Добавляем новый контакт
phone_book['Alex'] = '+1234567890'
print(phone_book)

#* Обновляем существующий контакт
phone_book['Bekzat'] = '+77051234567'
print(phone_book)

# Удаляем по ключу
del phone_book['Bobik']
print(phone_book)

# #? Если ключа нет, можно избежать ошибки с помощью метода get:
number = phone_book.get('Oleg', 'Key Not found')
print(number)  # 'Key Not found'

#? Ты можешь пройтись по всем ключам и значениям в словаре:
for name, number in phone_book.items():
    print(f'This is the name of our contact {name}')
    print(f'This is the phone number of our contact {str(number)}')
    print(f"{name}: {number}")

#? Методы словарей:
# items() — возвращает ПАРЫ ключ и значения
print(phone_book.items()) 

# keys() — только ключи.
print(phone_book.keys())
list_of_keys = list(phone_book.keys()) # ['Bekzat', 'bobik', 'oleg']
print(list_of_keys[0])
print(list_of_keys[2])

# values() — только значения.
print(phone_book.values())
list_of_values = list(phone_book.values())
print(list_of_values)

print(list(list_of_values[2].values()))

# pop(key) — удаляет элемент по ключу и возвращает его значение.
#! Обязательно указать ключ

removed_number = phone_book.pop('Bobik')
print(phone_book)
print(removed_number)  


# clear() — очищает весь словарь.
phone_book.clear()
print(phone_book)  
# Вывод: {}


