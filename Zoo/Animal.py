class Animal:

    def __init__(self, name, species, age, is_endangered=None,password=None):
        self.name = name
        self.species = species
        self.age = age
        self.is_endangered = is_endangered or False
        self.__passwprd = "admin@adminov"
        self._half_secret = "adminov"


    def make_sound(self):
        pass
        # print(f"{self.name} - {self.species} - MAKES THIS SOUND {sound}")

    def eat (self):
        pass
        # print(f"{self.species} - is eating {food}")

    def sleep (self):
        pass
        # print(f"{self.name} - {self.species} is sleeping")
        # return True



class Lion (Animal):

    def __init__(self, name, species, age, is_endangered=None ):
        super().__init__(name, species, age,  is_endangered)
        self.speed = 80

    def make_sound(self):
        print(f"{self.name} - {self.species} - MAKES THIS SOUND RRRR")

    def hunting(self):
        print(f"{self.species} with name {self.name} is hunting")

    def __str__(self):
        return f"{self.name}, {self.species}, {self.age}"

class Zebra (Animal):
    def __init__(self, name, species, age, is_endangered=None):
        super().__init__(name, species, age, is_endangered)
        self.has_stripes = True

    def make_sound(self):
        print(f"{self.name} - {self.species} - MAKES THIS SOUND feeeeaaarrrr")

    def run_from_lion (self, lion_obj: Lion):
        print(f"{self.species} - {self.name} is running from {lion_obj.name}")
        lion_obj.hunting()

class Giraffe(Animal):
    def __init__(self, name, species, age, is_endangered=None):
        super().__init__(name, species, age, is_endangered)
        self.neck_length = 2

    def make_sound(self):
        print(f"{self.name} - {self.species} - MAKES THIS SOUND dfdfsfadf")

    def cures_animals (self, animal: Animal):
        print(f"{self.name} is curing - {animal.name} the {animal.species} ")
        animal.make_sound()


animal_object = Animal ("Test Animal name", "Animal species", 10)

test_lion_obj1 = Lion("Alex","Lion", 5)
test_lion_obj2 = Lion("Simba","Lion", 3, True)

test_lion_obj1.make_sound()
test_lion_obj2.make_sound()

test_lion_obj1.hunting()
test_lion_obj2.hunting()

test_zebra_object = Zebra ("Martin","Zebra", 4)
test_zebra_object.run_from_lion(test_lion_obj1)
test_zebra_object.make_sound()


test_giraffe_object = Giraffe("Melmon","Giraffe",6)
test_giraffe_object.cures_animals(test_lion_obj2)
test_giraffe_object.cures_animals(test_zebra_object)
test_giraffe_object.cures_animals(animal_object)


class Exhibit:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.animals_list = []

    def add_animal (self, animal_obj):
        self.animals_list.append(animal_obj)
        print(f"{animal_obj.species} with name  - {animal_obj.name} is added to Exhibit  {self.name} ")

    def remove_animal (self, animal_obj):
        if animal_obj in self.animals_list:
            self.animals_list.remove(animal_obj)
            print(f"{animal_obj.name} is removed from Exhibit")
        else:
            print(f"{animal_obj}  ---> No such animals found ! ")

    def show_animal (self):
        print(f"The list of animals in Exhibit")
        for animal in self.animals_list:
            print(animal)


exhibit_for_lions = Exhibit("Lions exh", "Gogol str 1")
exhibit_for_lions.show_animal()
exhibit_for_lions.add_animal(test_lion_obj1)
exhibit_for_lions.show_animal()
exhibit_for_lions.add_animal(test_lion_obj2)
exhibit_for_lions.show_animal()

exhibit_for_lions.remove_animal(test_lion_obj1)
exhibit_for_lions.show_animal()


exhibit_for_lions.remove_animal("Test Error")
exhibit_for_lions.show_animal()





