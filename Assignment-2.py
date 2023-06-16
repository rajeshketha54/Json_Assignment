class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def get_info(self):
        print(f"Coat Color: {self.coat_color}")

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def bark(self):
        print("Jack Russell Terrier is barking!")

    def hunt(self):
        print("Jack Russell Terrier is hunting!")

class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def bark(self):
        print("Bulldog is barking!")

    def guard(self):
        print("Bulldog is guarding!")

dog1 = Dog("Trixy", 2, "Black and White")
dog1.description()
dog1.get_info()
print("\n")

terrier = JackRussellTerrier("Snoopy", 2, "White")
terrier.description()
terrier.get_info()
terrier.bark()
terrier.hunt()
print("\n")

bulldog = Bulldog("Spike", 4, "Black")
bulldog.description()
bulldog.get_info()
bulldog.bark()
bulldog.guard()
