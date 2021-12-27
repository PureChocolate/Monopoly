class Player:
    def __init__(self,name,properties,position,money) -> None:
        self.name = name
        self.properties = properties
        self.position = position
        self.money = money
    
    def showPlayer(self):
        print(self.name, "Owned properties: ", self.properties,"Currently At: ", self.position)
    
    def __eq__(self, __o: object) -> bool:
        return (self.name == __o.name and self.money == __o.money and self.position == __o.position)