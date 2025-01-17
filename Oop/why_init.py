# === Что такое __init__ и зачем он нужен ===

# Представь, что ты создаешь своего друга, например, "Иван".
# Ты хочешь, чтобы у него было имя и возраст. Но что, если ты захочешь создавать таких друзей много, с разными именами и возрастами?

# Например, ты бы написал так:
class Person:
    name = ""  # Пустое имя по умолчанию
    age = 0     # Пустой возраст по умолчанию

# Теперь, если ты захочешь создать человека с конкретным именем и возрастом, ты бы мог написать:
friend1 = Person()  # Создаём человека без имени и возраста
friend1.name = "Иван"  # Даём имя
friend1.age = 25       # Даём возраст

friend2 = Person()  # Создаём ещё одного человека
friend2.name = "Мария"
friend2.age = 30

print(friend1)
print(friend1.name)
print(friend1.age)
# Это работает, но представь, если бы тебе нужно было каждый раз отдельно ставить имя и возраст каждому человеку.
# Это неудобно, особенно если людей много, и каждый раз ты бы вручную прописывал эти значения.

# **Вот почему нам нужен __init__**:
# `__init__` — это как конструктор. Он автоматически запускается, когда ты создаешь нового человека (объект).
# Это позволяет сразу в момент создания объекта передавать необходимые данные (например, имя и возраст) и не делать это вручную позже.

# `__init__` — это как конструктор. Он автоматически запускается, когда ты создаешь нового человека (объект).
# Это позволяет сразу в момент создания объекта передавать необходимые данные (например, имя и возраст) и не делать это вручную позже.

# Мы можем написать так:
class Person:
    def __init__(self, name: str, age: int):
        # Здесь мы сразу при создании человека передаём его имя и возраст
        self.name = name
        self.age = age

    # def get_email(self):
    #     return self.email

    def add_one_to_age(self):
        self.age = self.age + 1
        return self.age                

# Теперь, когда ты создаешь человека, ты сразу можешь передать имя и возраст:
person1 = Person("Иван", 25)  # И теперь друг "Иван" сразу с нужными данными
person1.add_one_to_age()
print(person1.age)

Person('bekzat', 22).add_one_to_age()

# Ты больше не обязан вручную прописывать имя и возраст после создания объекта, всё делается сразу.

# print(friend2.name)  # Выведет: Мария
# print(friend2.age)   # Выведет: 30
# print(friend2.email)   # Выведет: 30