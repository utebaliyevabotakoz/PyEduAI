
#* === Тема: Четыре закона ООП и зачем они нужны ===

#? В ООП существует четыре основных закона, которые помогают нам правильно строить объекты и работать с ними.
#? Они обеспечивают гибкость, упорядоченность и безопасность данных, делая код более удобным и понятным.

# * === 1. Инкапсуляция ===
#? Инкапсуляция — это процесс скрытия деталей реализации объекта и предоставления только необходимых данных и действий.
#? Это похоже на то, как ты не видишь, что происходит внутри коробки, но знаешь, как с ней работать (например, кнопка на телефоне).
#? В ООП инкапсуляция позволяет скрыть внутреннюю логику работы объектов, чтобы она не мешала пользователю.

# Например, метод "introduce" не должен знать о внутренних переменных, его задача — просто выполнить действие:
class Person:
    def __init__(self, name, age):
        self.name = name  # Атрибут: имя
        self.age = age    # Атрибут: возраст

    def introduce(self):  # Это метод, который действует на данные внутри объекта
        return f"Привет, меня зовут {self.name} и мне {self.age} лет!"

#? Инкапсуляция помогает нам избежать изменения данных объекта напрямую и предоставлять только нужную информацию через методы:
#? Вызываем метод для получения данных, вместо того чтобы напрямую обращаться к атрибутам
# dad = Person("Джон", 45)
# print(dad.introduce())  # Вместо того, чтобы делать print(dad.name), мы используем метод

# * === 2. Наследование ===
#? Наследование позволяет создать новый объект, который будет обладать всеми характеристиками (данными и методами) родительского объекта,
#? а также добавлять или изменять что-то своё. Это похоже на то, как у тебя есть родитель, а ты получаешь от него что-то, но можешь быть уникальным.
#? Например, ты можешь создать нового человека, но с дополнительными возможностями.

#! Создаём класс "Дочери" на основе класса "Человек" (наследуем все его характеристики и добавляем что-то новое):
class Daughter(Person):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)  # Вызываем родительский конструктор
        self.hobby = hobby          # Дополнительный атрибут: хобби

    def introduce(self):
        return f"Привет, меня зовут {self.name}, мне {self.age} лет, и моё хобби — {self.hobby}. Я себя необычно знакомлю"

#! Создаем объект дочери с дополнительной характеристикой "хобби"
# daughter1 = Daughter("Анна", 20, "рисование")
# print(daughter1.introduce())  # Вывод: Привет, меня зовут Анна, мне 20 лет, и моё хобби — рисование

# Наследование позволяет создавать новые объекты, которые имеют все возможности старых объектов, но с дополнительными функциями или изменениями.

# * === 3. Полиморфизм ===
#? Полиморфизм позволяет объектам разных типов реагировать на одни и те же сообщения (методы) по-своему.
#? Это как если бы ты говорил одному другу "Пойдём гулять", а другому "Давай в кафе" — оба понимают твои слова, но каждый делает что-то своё.

#? Пример: оба объекта "Человек" и "Дочь" могут использовать метод "introduce", но он будет работать по-разному, потому что каждый объект — уникален:
dad = Person("Джон", 45)
daughter = Daughter("Анна", 20, "рисование")

#? В зависимости от типа объекта метод будет вести себя по-разному:
print(dad.introduce())      # Привет, меня зовут Джон и мне 45 лет!
print(daughter.introduce()) # Привет, меня зовут Анна, мне 20 лет, и моё хобби — рисование

# Полиморфизм помогает работать с разными объектами одинаково, но каждый объект будет "реагировать" по-своему.

# * === 4. Абстракция ===
#? Абстракция — это процесс скрытия лишних деталей и представление только самой необходимой информации.
#? Это как когда ты едешь на машине: тебе не нужно знать, как работает двигатель, ты просто нажимаешь на педаль газа и едешь.
#? В ООП абстракция помогает создавать простые интерфейсы для взаимодействия с объектами, скрывая все сложные детали внутри.

# Например, если у нас есть объект "Человек", нам не нужно знать, как работает его метод "introduce". Мы просто вызываем этот метод:
person = Person("Джон", 45)
print(person.introduce())  # Привет, меня зовут Джон и мне 45 лет!

# Мы не думаем, как именно работает метод, мы просто используем его, что облегчает взаимодействие с объектами.

#! === Заключение ===
#! Все эти четыре закона — инкапсуляция, наследование, полиморфизм и абстракция — помогают нам создавать более понятные,
#! гибкие и масштабируемые программы. Они позволяют организовать код так, чтобы объекты выполняли только те задачи, которые им предназначены,
#! и работали с минимальным вмешательством человека.