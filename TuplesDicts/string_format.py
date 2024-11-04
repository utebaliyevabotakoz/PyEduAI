name = "Иван"
age = 30
message = "Меня зовут " + name + ", и мне " + str(age) + " лет."
print(message)  # Вывод: Меня зовут Иван, и мне 30 лет.

name = "Иван"
age = 30
message = "Меня зовут {}, и мне {} лет.".format(name, age)
print(message)  # Вывод: Меня зовут Иван, и мне 30 лет.

name = "Иван"
age = 30
message = f"Меня зовут {name}, и мне {age} лет."
print(message)  # Вывод: Меня зовут Иван, и мне 30 лет.

username = "Алексей"
score = 150
print(f"Поздравляем, {username.upper}! Вы набрали {score} очков!")  
# Вывод: Поздравляем, Алексей! Вы набрали 150 очков!
