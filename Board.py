from Space import Space
from collections import defaultdict
class Board:
    def __init__(self) -> None:
        self.spaces = [] #enter space(every slot on board)info for the board

    def fillSpaces(self):
        rent = defaultdict(lambda: 0)        
        self.spaces.append(Space("GO", rent,0,0,[],"None", "No color"))
        rent[-1] = 60
        rent[0] = 2
        rent[1] = 10
        rent[2] = 30
        rent[3] = 90
        rent[4] = 160
        rent[5] = 250
        rent[-2] = 50
        self.spaces.append(Space("Mediterranean Ave", rent,0,0,[],"None","Brown"))
        rent = defaultdict(lambda: 0)
        self.spaces.append(Space("Community Chest", rent,0,0,[],"None","No Color"))
        rent[-1] = 60
        rent[0] = 4
        rent[1] = 20
        rent[2] = 60
        rent[3] = 180
        rent[4] = 320
        rent[5] = 450
        rent[-2] = 50
        self.spaces.append(Space("Baltic Avenue", rent,0,0,[],"None", "Brown"))
        #------4 spaces done 
        rent = defaultdict(lambda: 0)    
        rent[-1] = -200
        self.spaces.append(Space("Income Tax",rent,0,0,[],"None", "No color"))
        rent = defaultdict(lambda: 0)    
        rent[-1] = 200
        self.spaces.append(Space("Reading Railroad",rent,0,0,[],"None","Brown"))
        rent[-1] = 100
        rent[0] = 6
        rent[1] = 30
        rent[2] = 90
        rent[3] = 270
        rent[4] = 400
        rent[5] = 550
        rent[-2] = 50
        self.spaces.append(Space("Oriental Avenue",rent,0,0,[],"None","Cyan"))
        rent = defaultdict(lambda: 0)
        self.spaces.append(Space("Chance", rent,0,0,[],"None", "No color"))
        #------4 spaces done
        rent[-1] = 100
        rent[0] = 6
        rent[1] = 30
        rent[2] = 90
        rent[3] = 270
        rent[4] = 400
        rent[5] = 550
        rent[-2] = 50
        self.spaces.append(Space("Vermount Ave",rent,0,0,[],"None", "Cyan"))
        rent[-1] = 120
        rent[0] = 8
        rent[1] = 40
        rent[2] = 100
        rent[3] = 300
        rent[4] = 450
        rent[5] = 600
        rent[-2] = 50
        self.spaces.append(Space("Connecticut Ave", rent,0,0,[],"None","Cyan"))
        rent = defaultdict(lambda: 0)
        self.spaces.append(Space("Jail",rent,0,0,[],"None","No Color"))
        rent[-1] = 140
        rent[0] = 10
        rent[1] = 50
        rent[2] = 150
        rent[3] = 450
        rent[4] = 625
        rent[5] = 750
        rent[-2] = 100
        self.spaces.append(Space("ST. Charles Place", rent,0,0,[],"None", "Purple"))
        # #------4 spaces done
        rent = defaultdict(lambda: 0)
        rent[-1] = 200
        self.spaces.append(Space("Electric Company",rent,0,0,[],"None", "No color"))
        rent[-1] = 140
        rent[0] = 10
        rent[1] = 50
        rent[2] = 150
        rent[3] = 450
        rent[4] = 625
        rent[5] = 750
        rent[-2] = 100
        self.spaces.append(Space("States Ave", rent,0,0,[],"None","Purple"))
        rent[-1] = 160
        rent[0] = 12
        rent[1] = 60
        rent[2] = 180
        rent[3] = 500
        rent[4] = 700
        rent[5] = 900
        rent[-2] = 100
        self.spaces.append(Space("Virginia Avenue", rent,0,0,[],"None", "Purple"))
        # #------4 spaces done
        rent = defaultdict(lambda: 0)
        self.spaces.append(Space("Pennsylvania Railroad",rent,0,0,[],"None", "No color"))
        rent[-1] = 180
        rent[0] = 14
        rent[1] = 70
        rent[2] = 200
        rent[3] = 550
        rent[4] = 750
        rent[5] = 950
        rent[-2] = 100
        self.spaces.append(Space("ST. James Place", rent,0,0,[],"None","Orange"))
        rent = defaultdict(lambda: 0)
        self.spaces.append(Space("Community Chest", rent,0,0,[],"None","No Color"))
        rent[-1] = 180
        rent[0] = 14
        rent[1] = 70
        rent[2] = 200
        rent[3] = 550
        rent[4] = 750
        rent[5] = 950
        rent[-2] = 100
        self.spaces.append(Space("Tennessee Avenue", rent,0,0,[],"None", "Orange"))
        # #------4 spaces done 
        rent[-1] = 200
        rent[0] = 16
        rent[1] = 80
        rent[2] = 220
        rent[3] = 600
        rent[4] = 800
        rent[5] = 1000
        rent[-2] = 100
        self.spaces.append(Space("New York Avenue",rent,0,0,[],"None", "Orange"))
        rent = defaultdict(lambda: 0)
        self.spaces.append(Space("Free Parking", rent,0,0,[],"None","No Color"))
        rent[-1] = 220
        rent[0] = 18
        rent[1] = 90
        rent[2] = 250
        rent[3] = 700
        rent[4] = 875
        rent[5] = 1050
        rent[-2] = 150
        self.spaces.append(Space("Kentucy Avenue", rent,0,0,[],"None","Red"))
        rent = defaultdict(lambda: 0)
        self.spaces.append(Space("Chance", rent,0,0,[],"None", "No color"))
        # #------4 spaces done 
        rent[-1] = 220
        rent[0] = 18
        rent[1] = 90
        rent[2] = 250
        rent[3] = 700
        rent[4] = 875
        rent[5] = 1050
        rent[-2] = 150
        self.spaces.append(Space("Indiana Avenue",rent,0,0,[],"None", "Red"))
        rent[-1] = 240
        rent[0] = 20
        rent[1] = 100
        rent[2] = 300
        rent[3] = 750
        rent[4] = 925
        rent[5] = 1100
        rent[-2] = 150
        self.spaces.append(Space("Illinois Ave", rent,0,0,[],"None","Red"))
        rent = defaultdict(lambda: 0)
        self.spaces.append(Space("B & O Railroad",rent,0,0,[],"None","No color"))
        rent[-1] = 260
        rent[0] = 22
        rent[1] = 110
        rent[2] = 330
        rent[3] = 800
        rent[4] = 975
        rent[5] = 1150
        rent[-2] = 150
        self.spaces.append(Space("Atlantic Avenue", rent,0,0,[],"None", "Yellow"))
        # #------4 spaces done
        rent[-1] = 260
        rent[0] = 22
        rent[1] = 110
        rent[2] = 330
        rent[3] = 800
        rent[4] = 975
        rent[5] = 1150
        rent[-2] = 150
        self.spaces.append(Space("Ventnor Ave",rent,0,0,[],"None", "Yellow"))
        rent = defaultdict(lambda: 0)
        self.spaces.append(Space("Water Work", rent,0,0,[],"None","Brown"))
        rent[-1] = 280
        rent[0] = 24
        rent[1] = 120
        rent[2] = 360
        rent[3] = 850
        rent[4] = 1025
        rent[5] = 1200
        rent[-2] = 150
        self.spaces.append(Space("Marvin Gardens", rent,0,0,[],"None","Yellow"))
        rent = defaultdict(lambda: 0)
        rent[-1] = -50
        self.spaces.append(Space("Goto Jail", rent,0,0,[],"None", "No color"))
        # #------4 spaces done
        rent[-1] = 300
        rent[0] = 26
        rent[1] = 130
        rent[2] = 390
        rent[3] = 900
        rent[4] = 1100
        rent[5] = 1275
        rent[-2] = 200
        self.spaces.append(Space("Pacific Avenue",rent,0,0,[],"None", "Green"))
        rent[-1] = 300
        rent[0] = 26
        rent[1] = 130
        rent[2] = 390
        rent[3] = 900
        rent[4] = 1100
        rent[5] = 1275
        rent[-2] = 200
        self.spaces.append(Space("North Carolina Ave", rent,0,0,[],"None","Green"))
        rent = defaultdict(lambda: 0)
        self.spaces.append(Space("Community Chest", rent,0,0,[],"None","No Color"))
        rent[-1] = 320
        rent[0] = 28
        rent[1] = 150
        rent[2] = 450
        rent[3] = 1000
        rent[4] = 1200
        rent[5] = 1400
        rent[-2] = 200
        self.spaces.append(Space("Pennsylvania Ave", rent,0,0,[],"None", "Green"))
        #----------4 Spaces done
        rent = defaultdict(lambda: 0)
        self.spaces.append(Space("Short Line",rent,0,0,[],"None","No color"))
        rent = defaultdict(lambda: 0)
        self.spaces.append(Space("Chance",rent,0,0,[],"None","No color"))
        rent[-1] = 350
        rent[0] = 35
        rent[1] = 175
        rent[2] = 500
        rent[3] = 1100
        rent[4] = 1300
        rent[5] = 1500
        rent[-2] = 200
        self.spaces.append(Space("Park Place", rent,0,0,[],"None", "Blue"))
        rent = defaultdict(lambda: 0)
        rent[-1] = -100
        self.spaces.append(Space("Luxury Tax", rent,0,0,[],"None", "No color"))
        rent[-1] = 400
        rent[0] = 50
        rent[1] = 200
        rent[2] = 600
        rent[3] = 1400
        rent[4] = 1700
        rent[5] = 2000
        rent[-2] = 200
        self.spaces.append(Space("Boardwalk",rent,0,0,[],"None","Blue"))

    def showBoard(self):
        counter = 0
        strings0 = []
        temp = []
        for a in self.spaces:
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
            if counter % 5 == 0 or a == self.spaces[-1]:
                temp.append(card)
                strings0.append(temp)
                temp = []
            else: temp.append(card)
            counter +=1
            # print("")
        for a in strings0:
            strings = a
            print(*[''.join(x) for x in zip(*[[x.ljust(len(max(s.split('\n'), key=len))) for x in s.split('\n')] for s in strings])], sep='\n')
            print("\n\n\n\n")
        # art = [f.split("\n") for f in fir10]
        # zipper = zip(*art)
        # for a in zipper:
        #     print("".join(a))
        # print(sec10)
        # print(thir10)
        # print(four10)