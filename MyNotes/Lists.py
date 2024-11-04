from ReviewSessionInfo.data_types_ZcHV5aE import number

tasks = ['проснуться в 6 утра']

# tasks.append ('пойти в зал в 6/30') # добавление в КОНЕЦ списка
# print(tasks)
#
#
# tasks.insert (1, 'выпить кофе в 6/10') # добавление в КОНЕЦ списка
# print(tasks)
#
#
# name = "Botakoz"
# print ("Utebaliyeva " + name) #Utebaliyeva Botakoz
# print (f"Utebaliyeva {name}" ) #Utebaliyeva Botakoz
#
#
# message = "Я учусья прогяраммироватья"
# print(message[2:7]) #учусь
#
# print (message [4:7].upper()) #Я УЧУСЬ ПРОГРАММИРОВАТЬ
# print (message.lower()) #я учусь программировать
# print (message.capitalize()) #Я учусь программировать
# print (message.title()) #Я Учусь Программировать
# print (message.replace("Я","мы")) #Я Учусь Программировать
# print (message.replace("я","мы",2)) #Я Учусь Программировать
#
#
# print(len("Hello my World!"))
# print(str(31121991))
# print(int(31121991.8))
# print(float("31121991"))
#
# # number1 = int (input("type your message "))
#
#
# # email = input("input your email:")
# # print(email.lower())

# tasksr = ["Проснуть в 6 утра", 123, [1,3,5]]
# otdelnii_spisok = tasksr[2][1]
# print (otdelnii_spisok)

# my_name = input("enter your name ")
# tassks =["good morning", "have a breakfast dear", my_name ]
# print(tassks)


tasksst= ["Проснутья в 6 утра"]
print(tasksst)

tasksst.append("пойти на треню в 6/30") #Добавление элемента в конец списка
print(tasksst)

tasksst.insert(1,"позавтракать в 6/10") #Добавление элемента в указанную позицию списка
print(tasksst)

tasksst.insert(5,"гулять в обед") #Добавление элемента в указанную позицию списка
print(tasksst)

tasksst.append(input("type your next element "))
print(tasksst)

print(len(tasksst))

print(tasksst[1])

tasksst.extend(["PAROVOZ1","PAROVOZ22", "gtfred"])
print (tasksst)



books =[]
while len(books)<3:
    books.append(input ("input your next book "))
print(books)


tasksst.extend(books)
print (tasksst)


book = ["Harry Potter"]
tasksst.insert(0,book)
print (tasksst)

tasksst.remove("пойти на треню в 6/30") #? Удаление элементов: удаление элемента из списка по его названию.
print (tasksst)


print("pop tasksst ")
tasksst.pop() #? Удаление последнего элемента
print (tasksst)


del tasksst[0]
print (tasksst)



print("Clearing of tasksst on next row ")
tasksst.clear()
print(tasksst) #[]


numbers = [5,2,6,5,4,21,879]
print(numbers)
numbers.sort()
print(numbers) #[2, 4, 5, 5, 6, 21, 879]

letters = [" ","a", 'ff', '/','.','ytrds','A','X']
letters.sort() #[' ', '.', '/', 'A', 'X', 'a', 'ff', 'ytrds']
print(letters)


unsorted_tasks = ["обедать","завтракать", "вставать с кровати", "пойти спать"]
sorted_tasks = sorted (unsorted_tasks)
print (sorted_tasks)


movies = ['nnn','aaa', 'bbb']

for movie in movies:
    if movie[0] == 'nnn':
        movie += " was not published"
    movie += ' This book '
    print(movie)



movie=''
for element in range (0, len(movies)):
    movie=movies[element]
    print(movie)


text = 'apple, banana, cherry'
print(text.split(", "))


list_of_fruits = ['apple', 'banana', 'cherry']
string_of_fruits = ', '.join(list_of_fruits)
print(string_of_fruits)


salaries = [500,100,984,321]
print(max(salaries))
print(min(salaries))

