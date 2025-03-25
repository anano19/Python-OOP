class Car:
    number_of_wheels = 4
    _color = "black"
    __year = 1017

class BMW(Car):
    def __init__(self):
        print(self._color)

car = Car()
print(car.number_of_wheels)
bmw = BMW()
print(car._Car__year)