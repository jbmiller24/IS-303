class PetClass:
    hunger = 5
    happiness = 0
    sleep = 0

    def __init__(self, pet_name, pet_type): #Constructor

        self.name = pet_name #attribute
        self.type = pet_type #attribute

    def play_time(self, amount):
        self.happiness += amount

    def eat_time(self, amount):
        self.hunger += amount

    def sleep_time(self, amount):
        self.sleep += amount

pet1 = PetClass("Berry", "Bear")  
pet2 = PetClass("Jeff", "Cat")  
pet3 = PetClass("Bluey", "Bird")

print(pet1.name)
print(pet1.type)

print(pet2.name)
print(pet2.type)

print(pet3.name)
print(pet3.type)