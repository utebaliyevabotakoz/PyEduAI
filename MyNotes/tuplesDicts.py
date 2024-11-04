# ticket_info = ("Bota","Место 5", "Ряд 10", (1, 5,3))  #Tuples - кортежи, редко используются


phone_book = {
    "Bota": "+77014561234",
    "number": 3,
    "Oleg":{"home":"15 avenue", "gender":"male"}
}
print(phone_book)


number_Bota = phone_book["Bota"]

phone_book["Lolita"]="+713468913" #insert
print(phone_book)

phone_book["Bota"]="+7 777 6324152" #update

del phone_book["number"]
print(phone_book)

number = phone_book.get ("Ivan","Key is not found")
print(number)


for name, number  in phone_book.items():
    print(f"{name} : {number} ")


print(phone_book.items()) #dict_items([('Bota', '+7 777 6324152'), ('Oleg', {'home': '15 avenue', 'gender': 'male'}), ('Lolita', '+713468913')])

print(phone_book.keys())
list_of_keys = list (phone_book.keys())

print(list_of_keys)

print(list_of_keys[2])

print(phone_book.values())
list_of_values = list(phone_book.values())
print(list_of_values)


print(phone_book)
removed_number = phone_book.pop("Bota")
print(removed_number)
print(phone_book)


print("Clearing")
phone_book.clear()
print(phone_book)

