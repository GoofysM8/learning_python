class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate a dog rolling over in responce to a command"""
        print(f"{self.name} rolled over!")


my_dog = Dog('Buster', 6)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} yoears old")

my_dog.sit()
my_dog.roll_over()


class Dashond(Dog):
    """Represent aspects of a dog, speecific to dashonds 'kind of'"""

    def __init__(self, name, age):
        """Initialize attributes of the parent class"""
        super().__init__(name, age)


your_dog = Dashond('Willie', 4)
print(f"Your dog's name is {your_dog.name}")
your_dog.roll_over()