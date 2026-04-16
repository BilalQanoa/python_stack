import zoo

my_zoo = zoo.Zoo("park")
lion1 = zoo.Lion("Simba", 5, 80, 90, "Loud")
tiger1 = zoo.Tiger("Shere Khan", 7, 70, 85, 100)    
my_zoo.add_animal(lion1)
my_zoo.add_animal(tiger1)   

print("--- Before Feeding ---")
my_zoo.display_animals()

print("--- After Feeding ---")
lion1.feed()
tiger1.feed()
my_zoo.display_animals()