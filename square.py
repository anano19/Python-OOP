class Square:
    def __init__(self, side):
        self.side = side

    def __pow__(square_one, square_two):
       return (square_one.side ** square_two.side)
    
square_one = Square(2)
square_two = Square(4)
print(square_one ** square_two)

        








