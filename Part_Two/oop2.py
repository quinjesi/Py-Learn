class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
       
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Point(10, 20)
point1.move()
point1.draw()



class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Hi, my name is", self.name)

    def walk(self):
        print("Walk")


person1 = Person("John")
person1.talk()
person1.walk()


# Inheritance example

class Mammal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")

    def eat(self):
        print(f"{self.name} is eating") 


class Dog(Mammal):
    def bark(self):
        print(f"{self.name} is barking")


class Cat(Mammal):
    def meow(self):
        print(f"{self.name} is meowing")
        

dog = Dog("Buddy")
dog.walk()
dog.eat()
dog.bark()

cat = Cat("Whiskers")
cat.walk()
cat.eat()
cat.meow()