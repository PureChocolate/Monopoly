class Space:
    def __init__(self,name,rent,houses,hotels,occupiers,owner,color) -> None:
        self.name = name
        self.rent = rent # Dict to give rent value based on houses
        self.houses = houses
        self.hotels = hotels
        self.occupiers = occupiers
        self.owner = owner # Player object or string name?
        self.color = color.lower()
        self.price = rent[-1]

    def printer(self):
        a = self
        card = "|--Color: " + a.color + "----|\n"
        card += "|" + a.name
        sp = 23 - len(a.name)
        add = (" " * (sp-1))
        card += add + "\n"
        card += "|Buy:" + str(str(a.price)) + " Owner: " + a.owner + (" " * (8 - len(a.owner))) + "\n"
        card += "|Houses:" + str(a.houses) + " Hotels: " + str(a.hotels) + "     \n"
        ps = a.occupiers
        for x in ps:
            card += "|Player: " + x.name + (" " * (15 - len(a.owner))) + "\n"
        print(card)
