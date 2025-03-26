from abc import ABCMeta, abstractmethod



class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    side = 4
    def area(self):
        print(self.side * self.side)


class Rectangle(Shape):
    width = 5
    lenght = 10
    def area(self):
        print(self.width *self.lenght)

square = Square()
rectangle = Rectangle()
square.area()
rectangle.area()