class Animal:       # Parent Class
    isAlive = True
    
    def eat(self):
        return "This animal is eating."
        
    def sleep(self):
        return "This animal is sleeping."
        
class Dog(Animal):  # Child Class
    def barks(self):
        return "This animal barks."
class Hawk(Animal): # Child Class
    def fly(self):
        return "This animal can fly."
class Cat(Animal):  # Child Class
    def legs(self):
        return "This animal has 4 legs."

dog = Dog()     # object
# print(dog.isAlive)
hawk = Hawk()   # object
cat = Cat()     # object

hawk.eat()
cat.sleep()
cat.legs()

print(f"All animals can be alive: {Animal.isAlive}, eat: {dog.eat()}, and sleep: {dog.sleep()}")

# Exercise 1: Basic Parent and Child Class
# Create a parent class called Vehicle with:

# An attribute type (e.g., "Car", "Bike", etc.).
# Methods start() and stop(), which print "Vehicle started" and "Vehicle stopped."
# Create two child classes, Car and Bike, that inherit from Vehicle.

# Add a method honk() in Car that prints "Car is honking!"
# Add a method ride() in Bike that prints "Bike is being ridden."
# Create objects of Car and Bike and call all their methods.

class Vehicle:
    def start(self):
        print("Vehicle started!")
    def stop(self):
        print("Vehicle stopped!")

class Car(Vehicle):
    def honk(self):
        print("Car is honking!")
class Bike(Vehicle):
    def ride(self):
        print("Bike is being ridden.")
    
# Creating an object of Car
car = Car()
car.start()
car.honk()
car.stop()

# Creating an object of Car
bike = Bike()
bike.start()
bike.ride()
bike.stop()

# Exercise 2: Overriding Methods
# Create a parent class called Appliance with:

# A method power() that prints "This appliance is powered on."
# Create two child classes:

# WashingMachine that overrides power() to print "Washing machine is powered on."
# Refrigerator that overrides power() to print "Refrigerator is powered on."
# Create objects for both child classes and call the power() method.
class Appliance:
    def power(self):
        print("This appliance is powered on.")
        
class WashingMachine(Appliance):
    def power(self):
        print("Washing machine is powered on.")
class Refrigerator(Appliance):
    def power(self):
        print("Refrigerator machine is powered on.")
    
# Create an object of WashingMachine
washingMachine = WashingMachine()
# Create an object of Refrigerator
refrigerator = Refrigerator()

# printing
washingMachine.power()
refrigerator.power()

# Exercise 3: Using Class Attributes
# Create a parent class called School with:

# A class attribute location = "City Center".
# A method info() that prints "This is a school."
# Create a child class called HighSchool that inherits from School.

# Add a method grade_levels() that prints "Grades 9 to 12."
# Access the location attribute from the parent class using the child class and its object.

class School:
    location = "City Center"
    def info(self):
        print("This is a school.")
class HighSchool(School):
    def grade_levels(self):
        print("Grades 9 to 12.")
    
highSchool = HighSchool()

print("Our school is located in {}".format(highSchool.location))
highSchool.info()
highSchool.grade_levels()

#Exercise 4: Adding Instance Attributes
# Create a parent class Animal with:

# An __init__() method to initialize the name and species of the animal.
# A method describe() that prints "This is a [species] named [name]."
# Create a child class Fish that inherits from Animal.

# Add an attribute water_type (e.g., "Freshwater" or "Saltwater").
# Add a method swim() that prints "This fish swims in [water_type]."
# Create an object of the Fish class, and call both describe() and swim().

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def describe(self):
        print(f"This is a, {self.species} named {self.name}.")

class Fish(Animal):
    def __init__(self, name, species, water_type):
        super().__init__(name, species)
        self.water_type = water_type
        
    water_type = "Freshwater"
    def swim(self):
        print(f"This fish swims in {self.water_type}.")
        
fish = Fish("Goldfish", "Fish", "Freshwater")
fish.describe()
fish.swim()