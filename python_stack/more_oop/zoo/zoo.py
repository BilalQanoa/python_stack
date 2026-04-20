# Zoo class
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def display_animals(self):
        print(f"Animals in {self.name} Zoo:")
        for animal in self.animals:
            animal.display_info()
            print("")

# --------------------------------------------------------------------------------

# parent class
class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness


    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10

# --------------------------------------------------------------------------------

# child class
class Lion(Animal):
    def __init__(self, name, age, health, happiness, roar_strength):
        super().__init__(name, age, health, happiness)
        self.roar_strength = roar_strength

    def feed(self):
        self.health += 10
        return super().feed()
    
    def display_info(self):
        super().display_info()
        print(f"Roar Strength: {self.roar_strength}")

# --------------------------------------------------------------------------------

# child class
class Tiger(Animal):
    def __init__(self, name, age, health, happiness, num_stripes):
        super().__init__(name, age, health, happiness)
        self.num_stripes = num_stripes 

    def display_info(self):
        super().display_info()
        print(f"Number of Stripes: {self.num_stripes}")