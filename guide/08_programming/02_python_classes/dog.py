
from animal import AnimalClass

class DogClass(AnimalClass):
    # Class variable, specific to the Dog class
    species = "Dog"

    def __init__(self, name, age, breed):
        # Call the constructor of the base class
        super().__init__(name, age)
        # Additional instance variable for the Dog class
        self.breed = breed

    # Overriding the speak method from the base class
    def speak(self):
        return f"{self.name} barks."

    # Additional method specific to the Dog class
    def fetch(self, item):
        return f"{self.name} fetches the {item}."

    # Representation method, defines how the object is printed
    def __repr__(self):
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"
    
dog = DogClass("Rex", 3, "Golden Retriever")
print(dog)  # Uses the __repr__ method of the Dog class
print(dog.speak())  # Calls the overridden speak method of the Dog class
print(dog.fetch("ball"))  # Calls the fetch method of the Dog class
print(DogClass.is_animal())  # Calls the inherited class method of the Animal class
print(DogClass.kingdom())  # Calls the inherited static method of the Animal class
