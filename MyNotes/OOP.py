class Employess:
    def __init__(self, name, position, base_salary):
        self.name = name
        self.position = position
        self.base_salary = base_salary

    def introduce (self):
        return f"Hello, my name is {self.name}, my position is {self.position} and my salary = {self.base_salary}"


class Manager(Employess):
    def __init__(self, name, position, base_salary, bonus):
        super().__init__(name, position, base_salary)
        self.bonus = bonus

    def total_salary (self):
        return self.base_salary+self.bonus

    def introduce(self):
        return f"Hello, My name is {self.name}, my position is {self.position} and my salary {self.total_salary()} "


class Developer(Employess):
    def __init__(self, name, position, base_salary, award):
        super().__init__(name, position, base_salary)
        self.award = award

    def total_salary(self):
        return self.base_salary + self.award

    def introduce(self):
        return f"Hello, My name is {self.name}, my position is {self.position} and my salary {self.total_salary()} "



empl1 = Employess("Aidar", "Lawyer", 75000)
print(empl1.introduce())


manager1 = Manager("Lolita", "HR manager", 95000,14999)
print(manager1.introduce())

developer1 = Developer("Botakoz", "QA", 175000,24999)
print(developer1.introduce())