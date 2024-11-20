class Staff:


    def __init__(self, name, position, age):
        self.name = name
        self.position = position
        self.age = age

    def work(self):
        print(f"{self.name}  is {self.position} {self.age} years old is working")


class Zookeeper  (Staff):
    def __init__(self,name, age, gender = None):
        super().__init__(name, "Zookeeper",age)
        self.gender = gender or "Woman"

    def feed_animal(self, animal):
        print(f"{self.position}: {self.name}  is {self.gender},  {self.age} years old, feeds  {animal.name}  {animal.species}")


class Vet (Staff):
    def __init__(self, name, age, gender=None):
        super().__init__(name, "Vet", age)
        self.gender = gender or "Man"

    def check_health(self, animal):
        print(f"{self.position}: {self.name}  is {self.gender},  {self.age} years old, checks health  {animal.name}  {animal.species}")


# test_zookeeper_obj1 = Zookeeper ("Maria",23)
# test_vet_obj1 = Vet("Denis",34)
#
# test_zookeeper_obj1.feed_animal(test_lion_obj2)
# test_vet_obj1.check_health(test_zebra_object)