
class AnimalClass:
    # Class variable, shared by all instances
    species = "Animal"

    def __init__(self, name, age):
        # Instance variables, unique to each instance
        self.name = name
        self.age = age

    # Instance method
    def speak(self):
        return f"{self.name} makes a noise."

    # Class method, can be called on the class itself
    @classmethod
    def is_animal(cls):
        return f"This is a {cls.species}."

    # Static method, doesn't need class or instance reference
    @staticmethod
    def kingdom():
        return "Animalia"

    # Representation method, defines how the object is printed
    def __repr__(self):
        return f"Animal(name={self.name}, age={self.age})"

animal = AnimalClass("lion", 5)
print(animal)  # Uses the __repr__ method of the Animal class
print(animal.speak())  # Calls the speak method of the Animal class
print(AnimalClass.is_animal())  # Calls the class method of the Animal class
print(AnimalClass.kingdom())  # Calls the static method of the Animal class
