class Dog:
    def __init__(self, name, breed,hasFur):
        self.name = name
        self.breed = breed
        self.hasFur = hasFur

    def bark(self):
        print("Woof!! Woof!!")

    def locomotive(self):
        print("Dog is walking")

dog1 = Dog("JJ","Rotweiler",True)
print(dog1.name,dog1.breed,"He got fur:",dog1.hasFur)
dog1.bark()
print()

dog2 = Dog("Topaz","chihuahua",True)
print(dog2.name, dog2.breed, "He got fur:" ,dog2.hasFur)
dog2.locomotive()
print()

dog3 = Dog("Potter","German shepherd",True)
print(dog3.name, dog3.breed, "He got fur:" ,dog3.hasFur)



