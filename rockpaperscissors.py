# NAME: Eliyas Philip      
# EMAIL: eliyas.philip84@myhunter.cuny.edu



import random as rnd

cont = True
winner = ""

while cont:
    p = int(input("enter 1 for rock, 2 for paper, or 3 for scissors: "))
    c = rnd.randrange(1,3,1)

    if p == 0:
        cont = False
    elif p == c:
        print("computerMove:", c)
        winner = "draw"
        print("round finished and winner is:", winner)
    elif p == 1:
        print("computerMove:", c)
        if c == 2:
            winner = "computer"
            print("round finished and winner is:", winner)
        else:
            winner = "human"
            print("round finished and winner is:", winner)
    elif p == 2:
        print("computerMove:", c)
        if c == 1:
            winner = "human"
            print("round finished and winner is:", winner)
        else:
            winner = "computer"
            print("round finished and winner is:", winner)
    elif p == 3:
        print("computerMove:", c)
        if c == 1:
            winner = "computer"
            print("round finished and winner is:", winner)
        else:
            winner = "human"
            print("round finished and winner is:", winner)
    else:
        print("computerMove:", c)
        winner = "invalid"
        print("round finished and winner is:", winner)
    
print("game finished and winner is:", winner)