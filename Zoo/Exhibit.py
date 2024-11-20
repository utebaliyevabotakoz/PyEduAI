class Exhibit:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.animals_list = []

    def add_animal (self, animal_obj):
        self.animals_list.append(animal_obj)
        print(f"{animal_obj.species} with name {animal_obj.name} is added to Exhibit  {self.name}  {self.location}")

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



# exhibit_for_lions = Exhibit("Lions exh", "Gogol str 1")
# exhibit_for_lions.show_animal()
# exhibit_for_lions.add_animal(test_lion_obj1)
# exhibit_for_lions.show_animal()
# exhibit_for_lions.add_animal(test_lion_obj2)
# exhibit_for_lions.show_animal()
#
# exhibit_for_lions.remove_animal(test_lion_obj1)
# exhibit_for_lions.show_animal()
#
#
# exhibit_for_lions.remove_animal("Test Error")
# exhibit_for_lions.show_animal()