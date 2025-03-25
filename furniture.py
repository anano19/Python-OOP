class Furniture:
    def __init__(self):
        self.type_of_furniture = "Teakwood"


class Chair(Furniture):
    def __init__(self):
        super().__init__()
        self.__number_of_legs = 4

    def changed_furniture(self):
        print("This chair is made of {} and has {} legs.".format(self.type_of_furniture, self._Chair__number_of_legs))
        self.changed = input("What would you like to change the furniture type to? ")
        print("This chair is made of {} and has {} legs.".format(self.changed, self._Chair__number_of_legs))


chair = Chair()
chair.changed_furniture()



