from zoo import Zoo, Lion, Tiger

my_zoo = Zoo("park")
lion1 = Lion("Simba", 5, 80, 90, "Loud")
tiger1 = Tiger("Shere Khan", 7, 70, 85, 100)    
my_zoo.add_animal(lion1)
my_zoo.add_animal(tiger1)   

print("--- Before Feeding ---")
my_zoo.display_animals()

print("--- After Feeding ---")
lion1.feed()
tiger1.feed()
my_zoo.display_animals()