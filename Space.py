class Space:
    def __init__(self,name,rent,houses,hotels,occupiers,owner,color) -> None:
        self.name = name
        self.rent = rent # Dict to give rent value based on houses
        self.houses = houses
        self.hotels = hotels
        self.occupiers = occupiers
        self.owner = owner # Player object or string name?
        self.color = color
        self.price = rent[-1]

    def printer(self):
        print(self.name, self.price, self.color, self.rent, self.hotels, self.houses, self.occupiers, self.owner)
