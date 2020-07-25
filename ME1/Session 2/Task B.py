import random
#task B conditional flow
#task B1
'''playerX = input("Input player X's name:")
playerY = input("Input player Y's name:")

diceX = int(random.random()*6 + 1)
diceY = int(random.random()*6 + 1)

print(playerX, "rolls", diceX)
print(playerY, "rolls", diceY)

if diceX > diceY:
    print(playerX, "beats", playerY)
else:
    print(playerY, "beats" , playerX)'''

#task B2
'''playerX = input("Input player X's name:")
playerY = input("Input player Y's name:")
playerXwins = []
playerYwins = []
R = range(1, int(input("input N times here"))+1)
for i in R:
    diceX = int(random.random()*6 + 1)
    diceY = int(random.random()*6 + 1)

    print(playerX, "rolls", diceX)
    print(playerY, "rolls", diceY)

    if diceX > diceY:
        print(playerX, "beats", playerY)
        playerXwins = playerXwins + [1]
    else:
        print(playerY, "beats" , playerX)
        playerYwins = playerYwins + [1]

print(playerX, "won", sum(playerXwins), "games")
print(playerY, "won", sum(playerYwins), "games")'''


#task B3
UserInput = input("Rock(R), Paper(P) or Scissors(S)?")
if UserInput == "R":
    print("You chose rock!")
if UserInput == "P":
    print("You chose paper!")
if UserInput == "S":
    print("You chose scissors!")

Computer = int(random.random()*3 + 1)
if Computer == 1:
    print("Computer chose rock!")
if Computer == 2:
    print("Computer chose paper!")
if Computer == 3:
    print("Computer chose scissors!")

if Computer == 1 and UserInput == "S":
    print("Computer Wins")
if Computer == 2 and UserInput == "R":
    print("Computer Wins")
if Computer == 2 and UserInput == "P":
    print("Computer Wins")
if UserInput == "R" and Computer == 3:
    print("You Win!")
if UserInput == "P" and Computer == 1: 
    print("You Win!")
if UserInput == "S" and Computer == 2:
    print("You Win!")
if Computer == UserInput:
    print("It's a tie!")