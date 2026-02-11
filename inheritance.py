#Parent class/Super class/Base class
class Animal:
    isMammal = True

    def speak(self):
        print("Animal is speaking")

#Child class/Sub class/Derived class
class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

    def climb(self):
        print("Cat is climbing a tree")

class Donkey(Animal):
    hasTail = True

    def move(self):
        print("Donkey is moving")


a = Animal()

c = Cat()

d = Donkey()
