from Board import Board
from Player import Player
from Dice import Dice


def runTurn(cBoard,cPlayer,rentS):
    colorP = {"brown" : 2, "cyan": 3, "purple": 3, "orange": 3, "red": 3, "yellow": 3, "blue": 2}
    i = ""
    while i != "done" or rentS:
        print("---------------")
        if rentS: print("Note; you are in debt, you must sell enough to pay up, or sell everything.")
        i = input("What do you wish to do [Buy Houses(buy), Sell Houses/Properties(sell), Player Stats(stats), Go back to roll(roll), Done with the options here (done)]: ")
        if i == "buy":
            if len(cPlayer.properties) > 0:
                print("Which property would you like to buy houses on")
                counter = 0
                for a in cPlayer.properties:
                    print(str(counter) + ". " + a.name)
                i = input("Enter the property number: ")
                if int(i) < len(cPlayer.properties):
                    cProp = cPlayer.properties[int(i)]
                    cCount = 0 #colorP[cProp.color]
                    for a in cPlayer.properties:
                        if a.color == cProp.color: cCount += 1
                    if colorP[cProp.color] == cCount:
                        print("Each house is $" + str(cBoard.rent[-2]))
                        i = input("How many houses (1-4):- ")
                        if i in ["1","2","3","4"]:
                            if cPlayer.money >= int(i) * cBoard.rent[-2]:
                                cPlayer.money -= int(i) * cBoard.rent[-2]
                                cProp.houses = int(i)
                            else: print("Not enough money.")
                        else: print("Invalid number intered please enter a valid number 1 through 4")
                    else: print("You do not own all the properties in the color group, no purchase of house allowed.")
                else: print("Invalid number intered please enter a valid number from the list shown.")
        elif i == "sell":
            if len(cPlayer.properties) > 0:
                print("Which property would you like to sell (Note: you must sell the houses on it first for half the price)")
                counter = 0
                for a in cPlayer.properties:
                    print(str(counter) + ". " + a.name)
                i = input("Enter the property number: ")
                if int(i) < len(cPlayer.properties):
                    cProp = cPlayer.properties[int(i)]
                    if cProp.houses > 0:
                        i = input("There are " + str(cProp.houses) + " on this property, enter the number for how many you would like to sell: ")
                        i = int(i)
                        inc = i * int(cProp.price/2)
                        while i > 0:
                            for a in cPlayer.properties:
                                if a.color == cProp.color: 
                                    a.houses -= 1
                                    i -= 1
                        cProp.houses -= i
                        cPlayer.money += inc
                        print("You got $" + str(inc) +", and your total money is: $" + str(cPlayer.money))
                        if(cProp.houses == 0):
                            i = input("Would you still like to sell your house? (y/n): ")
                            if i == "y": print("Done.")
                            else: continue
                        else: print("You have " + str(cProp.houses) + " left on " + cProp.name)
                    inc = int(cProp.price/2)
                    cPlayer.money += inc
                    cProp.owner = "None"
                else: print("Invalid number intered please enter a valid number from list shown")
            else: 
                print("No properties to sell!")
                if rentS: return 1
        elif i == "stats":
            print("|---" + cPlayer.name + "---|")
            print("|---" + str(cPlayer.money) + "---|")
            for a in cPlayer.properties:
                print("|---" + a.name + "---|")
        elif i == "roll": return 0
        elif i == "done": return 0

def main():
    board = Board()
    board.fillSpaces()

    players = []
    c = ""
    try:
        c = int(input("Enter number of players: ").strip())
        if c <= 0: 
            print("Wrong number of players")
            return 0
    except: 
        print("Not a valid number of players")
        return 0 
    while c > 0:
        n = input("Enter your name: ")
        p = Player(n,[],0,1500)
        players.append(p)
        board.spaces[0].occupiers.append(p)
        c -= 1

    board.showBoard()

    c = 0
    while True:
        if len(players) <= 0: break
        print("---------------")        
        cPlayer = players[c]
        if cPlayer.jail:
            if cPlayer.jailTime > 3: 
                print("You didnt pay up before 3 turns, you are bankrupt!")
                players.pop(c)
            else:
                i = input("You are in jail, its been "  + str(cPlayer.jailTime) + "turns (Max: 3), would you like to pay $50 to get out next turn? (y/n): ")
                if i == "y":
                    if cPlayer.money >= 50: 
                        cPlayer.money -= 50
                        cPlayer.jail = False
                        cPlayer.jailTime = 1
                    else: 
                        print("You don't have enough money")
                        while True:
                            print("You must sell any properties/houses you have to pay up: ")
                            runTurn(cBoard,cPlayer,True)
                            if cPlayer.money >= 50: 
                                cPlayer.money -= 50
                                cPlayer.jail = False
                                cPlayer.jailTime = 1
                                break
                            else:
                                if len(cPlayer.properties) > 0: continue
                                print("You are bankrupt!")
                                players.pop(c)
                                break
                else:
                    cPlayer.jailTime += 1
        else:
            nextA = input("Player " + cPlayer.name +" enter your action [roll, options]: ")
            roll = (0,0)
            cBoard = []
            cBoard = board.spaces[cPlayer.position]
            if nextA in ["exit", "q"]: break
            elif nextA == "roll":

                dice = Dice(6)
                roll = dice.roll()
                ps = board.spaces[cPlayer.position].occupiers
                i = 0
                for a in ps:
                    if a == cPlayer: board.spaces[cPlayer.position].occupiers.pop(i)
                    i += 1
                prev = cPlayer.position
                cPlayer.position = (cPlayer.position + roll[0] + roll[1]) % len(board.spaces)
                if cPlayer.position < prev: cPlayer.money += 200
                board.spaces[cPlayer.position].occupiers.append(cPlayer)
                cBoard = board.spaces[cPlayer.position]
                
                board.showBoard()    
                print("Rolled", roll, "Landed on " + cBoard.name + " Color: " + cBoard.color + " Owner: " + cBoard.owner)
                if(cBoard.owner == "None" and cBoard.price > 0):
                    i = input("Would you like to buy " + cBoard.name + " for " + str(cBoard.price) + "? (y/n) ")
                    if i == "y":
                        if cPlayer.money >= cBoard.price:
                            cPlayer.money -= cBoard.price
                            cBoard.owner = cPlayer.name
                            cPlayer.properties.append(cBoard)
                        else: print("Not enough money! Others can bid on this property now.")
                elif cBoard.owner == "None" and cBoard.price < 0 and cBoard.name != "Goto Jail":
                    if cPlayer.money >= (-1 * cBoard.price): 
                        cPlayer.money += cBoard.price
                        print("You paid $" + str(cBoard.price) +", money left: $" + str(cPlayer.money))
                    else:
                        pay = cBoard.price
                        while True:
                            print("You must sell any properties/houses you have to pay up: ")
                            runTurn(cBoard,cPlayer,True)
                            if cPlayer.money >= pay: 
                                cPlayer.money -= pay
                                break
                            else:
                                if len(cPlayer.properties) > 0: continue
                                print("You are bankrupt!")
                                players.pop(c)
                                break
                elif cBoard.name == "Goto Jail":
                    ps = board.spaces[cPlayer.position].occupiers
                    i = 0
                    for a in ps:
                        if a == cPlayer: board.spaces[cPlayer.position].occupiers.pop(i)
                        i += 1
                    cPlayer.position = 10
                    board.spaces[cPlayer.position].occupiers.append(cPlayer)
                    cPlayer.jail = True
                    
                else:
                    if type(cBoard.owner) != type(""):
                        if cBoard.owner != cPlayer.name:
                            pay = cBoard.rent[cBoard.houses]
                            if cPlayer.money >= pay: 
                                cPlayer.money -= pay
                                print("You paid to someone $" + str(pay) +", money left: $" + str(cPlayer.money))
                                cBoard.printer()
                            else:
                                while True:
                                    print("You must sell any properties/houses you have to pay the rent: ")
                                    runTurn(cBoard,cPlayer,True)
                                    if cPlayer.money >= pay: 
                                        cPlayer.money -= pay
                                        break
                                    else:
                                        if len(cPlayer.properties) > 0: continue
                                        print("You are bankrupt!")
                                        players.pop(c)
                                        break
            elif nextA == "options":
                if runTurn(cBoard,cPlayer,False) == 0: continue
            else: 
                print("Please enter a valid actions")
                continue
        c += 1
        if c >= len(players): c = 0

main()
