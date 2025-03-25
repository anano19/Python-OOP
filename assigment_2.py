class Stones:
    stones = []
    def __init__(self, name):
        self.name = name
        if len(Stones.stones) >= 5:
            Stones.stones.pop(0)
        Stones.stones.append(self)
    @staticmethod
    def print_stones():
        print([stone.name for stone in Stones.stones])


ruby = Stones("RUby")
garnet = Stones("Garnet")
saphire = Stones("Saphire")
amethist = Stones("Amethist")
pearl = Stones("Pearl")

Stones.print_stones()

diamond = Stones("Diamond")

Stones.print_stones()
