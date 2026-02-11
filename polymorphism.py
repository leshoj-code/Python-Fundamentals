#Refers to the many forms a method can take.
from curses.textpad import rectangle


class Rectangle:
    def draw(self):
        print("Drawing a rectangle")

class Rhombus:
    def draw(self):
        print("Drawing a rhombus")

class Parallelogram:
    def draw(self):
        print("Drawing a parallelogram")

r = Rectangle()
rh = Rhombus()
p = Parallelogram()

for x in r,rh,p:
    x.draw()