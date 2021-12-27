from Board import Board
from Player import Player
from Dice import Dice
# def main():
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
                else: print("Not enough money! Others can bid on this property now.")
        if cBoard.owner == cPlayer.name:
            i = input("Do you wish to buy houses/hotels on your properties? Each house is $" + str(cBoard.rent[0])+ "(y/n) ")
            if i == "y":
                i = input("How many houses (1-4):- ")
                if i in ["1","2","3","4"]:
                    if cPlayer.money >= int(i) * cBoard.rent[0]:
                        cPlayer.money -= int(i) * cBoard.rent[0]
                        cBoard.houses = int(i)
                    else: print("Not enough money.")
                else: print("Invalid number intered please enter a valid number 1 through 4")

    c += 1
    if c >= len(players): c = 0


