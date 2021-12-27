import random
class Dice:
    def __init__(self,sides) -> None:
        self.sides = sides

    def roll(self) -> int:
        return (random.randint(1,self.sides),random.randint(1,self.sides))