import random

game = ["rock", "paper", "scissors"]
diff = ["y", "n"]
pl_scr = 0
co_scr = 0
hard = input("Do you want to play on hard mode? y or n: ")
while hard.lower() not in diff:
    hard = input("Invalid input. Please try again: ")

while hard.lower() == "n":
    player = input(f"Insert one of {game}: ")
    comp = random.choice(game)

    while player.lower() not in game:
        player = input("Invalid input, please try again: ")

    if player == comp:
        print(f"Human and computer players have both chosen {comp}. This round is a tie.")
    elif player == "rock":
        if comp == "paper":
            co_scr += 1
            print(f"The computer player wins this round with {comp}.")
        else:
            pl_scr += 1
            print(f"The human player wins this round with {player}.")
    elif player == "paper":
        if comp == "scissors":
            co_scr += 1
            print(f"The computer player wins this round with {comp}.")
        else:
            pl_scr += 1
            print(f"The human player wins this round with {player}.")
    elif player == "scissors":
        if comp == "rock":
            co_scr += 1
            print(f"The computer player wins this round with {comp}.")
        else:
            pl_scr += 1
            print(f"The human player wins this round with {player}.")
    
    if pl_scr == co_scr:
        print(f"The score is tied at {pl_scr}")
    elif pl_scr > co_scr:
        print(f"The score is {pl_scr} to {co_scr} in favor of the human player.")
    else:
        print(f"The score is {co_scr} to {pl_scr} in favor of the computer player.")
    print("")
    
while hard.lower() == "y":
    player = input(f"Insert one of {game}: ")
    comp = random.choice(game)

    while player.lower() not in game:
        player = input("Invalid input, please try again: ")

    if random.random() < 0.4:
        if player == "rock":
            comp = "paper"
        elif player == "paper":
            comp = "scissors"
        else:
            comp = "rock"
            
    if player == comp:
        print(f"Human and computer players have both chosen {comp}. This round is a tie.")
    elif player == "rock":
        if comp == "paper":
            co_scr += 1
            print(f"The computer player wins this round with {comp}.")
        else:
            pl_scr += 1
            print(f"The human player wins this round with {player}.")
    elif player == "paper":
        if comp == "scissors":
            co_scr += 1
            print(f"The computer player wins this round with {comp}.")
        else:
            pl_scr += 1
            print(f"The human player wins this round with {player}.")
    elif player == "scissors":
        if comp == "rock":
            co_scr += 1
            print(f"The computer player wins this round with {comp}.")
        else:
            pl_scr += 1
            print(f"The human player wins this round with {player}.")
    
    if pl_scr == co_scr:
        print(f"The score is tied at {pl_scr}")
    elif pl_scr > co_scr:
        print(f"The score is {pl_scr} to {co_scr} in favor of the human player.")
    else:
        print(f"The score is {co_scr} to {pl_scr} in favor of the computer player.")
    print("")


                

