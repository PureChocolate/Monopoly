from Board import Board
from Player import Player
from Dice import Dice


def runTurn(cBoard,cPlayer):
    i = ""
    while i != "done":
        i = input("What do you wish to do [Buy Houses(buy), Sell Houses/Properties(sell), Player Stats(stats)]: ")
        if i == "buy":
            if len(cPlayer.properties) > 0:
                print("Which property would you like to buy houses on")
                counter = 0
                for a in cPlayer.properties:
                    print(str(counter) + ". " + a.name)
                i = input("Enter the property number: ")
                cProp = cPlayer.properties[int(i)]
                print("Each house is $" + str(cBoard.rent[-2]))
                i = input("How many houses (1-4):- ")
                if i in ["1","2","3","4"]:
                    if cPlayer.money >= int(i) * cBoard.rent[-2]:
                        cPlayer.money -= int(i) * cBoard.rent[-2]
                        cProp.houses = int(i)
                    else: print("Not enough money.")
                else: print("Invalid number intered please enter a valid number 1 through 4")
        elif i == "sell":
            if len(cPlayer.properties) > 0:
                print("Which property would you like to sell (Note: you must sell the houses on it first for half the price)")
                counter = 0
                for a in cPlayer.properties:
                    print(str(counter) + ". " + a.name)
                i = input("Enter the property number: ")
                cProp = cPlayer.properties[int(i)]
                if cProp.houses > 0:
                    i = input("There are " + str(cProp.houses) + " on this property, enter the number for how many you would like to sell: ")
                    inc = int(i) * (cProp.price/2)
                    cProp.houses -= int(i)
                    print("You got $" + str(inc) +", and your total money is: $" + str(cPlayer.money))
                    cPlayer.money += inc
                    i = input("Would you still like to sell your house? (y/n): ")
                    if i == "y": print("Done.")
                    else: continue
                inc = cProp.price/2
                cPlayer += inc
                cProp.owner = "None"
            else: print("No properties to sell!")
        elif i == "stats":
            print("|---" + cPlayer.name + "---|")
            print("|---" + str(cPlayer.money) + "---|")
            for a in cPlayer.properties:
                print("|---" + a.name + "---|")
        elif i == "done": break
                


                    


def main():
    board = Board()
    board.fillSpaces()

    players = []
    c = input("Enter number of players").strip()
    c = int(c)
    while c > 0:
        n = input("Enter your name: ")
        p = Player(n,[],0,1500)
        players.append(p)
        board.spaces[0].occupiers.append(p)
        c -= 1

    board.showBoard()

    cTurn = 0
    while True:
        nextA = input("Player " + str(c) +" enter your action: ")
        roll = (0,0)
        if nextA in ["exit", "q"]: break
        elif nextA == "roll":

            dice = Dice(6)
            roll = dice.roll()
            cPlayer = players[c]
            ps = board.spaces[cPlayer.position].occupiers
            i = 0
            for a in ps:
                if a == cPlayer: board.spaces[cPlayer.position].occupiers.pop(i)
                i += 1
            cPlayer.position = (cPlayer.position + roll[0] + roll[1]) % len(board.spaces)
            board.spaces[cPlayer.position].occupiers.append(cPlayer)
            cBoard = board.spaces[cPlayer.position]
            
            board.showBoard()    
            print("Rolled", roll)
            if(cBoard.owner == "None" and cBoard.price > 0):
                i = input("Would you like to buy this property for" + str(cBoard.price) + "? (y/n) ")
                if i == "y":
                    if cPlayer.money >= cBoard.price:
                        cPlayer.money -= cBoard.price
                        cBoard.owner = cPlayer.name
                        cPlayer.properties.append(cBoard)
                    else: print("Not enough money! Others can bid on this property now.")
        runTurn(cBoard,cPlayer)
        c += 1
        if c >= len(players): c = 0

main()
