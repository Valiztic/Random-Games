from random import randint

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

t = ("Rock", "Paper", "Scissors")

computer = t[randint (0,2)]

counter = 0

wins = 0

rounds = int(input("How many rounds would you like to play: 1-10?: "))
while rounds <= 0 or rounds >= 11:
    rounds = int(input("Please input a valid number: 1-10?: "))

while rounds > counter:
     
    computer = t[randint (0,2)]
    
    print(color.BOLD + 'Round:' + color.END)
    print(counter + 1)
    print(color.BOLD + 'Wins:' + color.END)
    print(wins)
    
    player = input(color.BOLD + "Rock, Paper, Scissors?: " + color.END)
    print()
    if player == computer:
        print("Tie\n")
        
    elif player == "Rock":
        if computer == "Paper":
            print("YOU LOSE NERD! Paper covers Rock up\n")
        else:
            print ("You win! Rock crushes Scissors\n")
            wins = wins + 1
            
    elif player == "Paper":
        if computer == "Scissors":
            print("YOU LOSE NERD! Scissors cuts right through Paper\n")
        else:
            print("You win! Paper covers Rock up\n")
            wins = wins + 1
            
    elif player == "Scissors":
        if computer == "Rock":
            print("YOU LOSE NERD! Rock crushes Scissors\n")
        else:
            print("You win! Scissors cuts right through Paper\n")
            wins = wins + 1
            
    else:
        print("I cannot understand you! Please ensure that you have proper capitalization!\n")
        counter = counter - 1
        
    counter = counter + 1


    print(color.BOLD + "Total Wins:" + color.END)
    print(wins, "\n")
    while counter == rounds:
        print("Would you like to play again? If so, type Yes.")
        
        again = input(color.BOLD + "Yes, No: " + color.END)
        
        if again == "Yes":
            wins = 0
            counter = 0
            rounds = int(input("How many rounds would you like to play: 1-10?: "))
        elif again == "No":
            print("guess not :(")
            break
        else:
            print("Sorry I didn't understand what you wrote\n")
