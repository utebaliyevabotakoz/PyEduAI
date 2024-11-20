from Animal import Lion
from Animal import Zebra
from Exhibit import Exhibit
from Staff import Zookeeper
from Staff import Vet

def zoo():


    while True:
        print("\nНаш любимый Зоопарк")
        print("1. Добавить Льва")
        print("2. Добавить Льва в Вольер")
        print("3. Добавить Смотрителя")
        print("4. Посмотреть Вольеры")
        print("5. Добавить Зебру")
        print("6. Добавить Ветеринара")
        print("7. Удалить Льва из Вольера")
        print("8. Выход")

        choice = input("Введите ваш выбор: ")

        # Обработка выбора пользователя
        if choice == "1":
            name = input("Введите имя Льва: ")
            age = int(input("Введите возраст: "))
            lion = Lion(name,age)
            lion.make_sound()
            lion.hunting()


        elif choice == "2":
            name = input("Введите название вольера: ")
            location = input("Введите локацию (например, в конце зоопарка/возле пруда): ")
            exhibit = Exhibit (name, location)
            exhibit.add_animal(lion)

        elif choice == "3":
            name = input("Введите имя Смотрителя зоопарка: ")
            age = int(input("Введите возраст "))
            zookeeper = Zookeeper (name, age)
            zookeeper.feed_animal(lion)

        elif choice == "4":
            exhibit.show_animal()

        elif choice == "5":
            name = input("Введите имя Зебры: ")
            age = int(input("Введите возраст: "))
            zebra = Zebra(name,age)
            zebra.make_sound()
            zebra.run_from_lion(lion)

        elif choice == "6":
            name = input("Введите имя Ветеринара зоопарка: ")
            age = int(input("Введите возраст "))
            vet = Vet (name, age)
            vet.check_health(zebra)


        elif choice == "7":
            exhibit.remove_animal(lion)

        elif choice == "8":
            print("До свидания! Приходите к нам еще")
            break

        else:
            print("Неверный выбор, пожалуйста, попробуйте снова.")

# Запуск основной программы
# if __name__ == "__Zoo__":
zoo()
