# Importing random package 
import random

# Printing the Game Title and Game Rules
print("Rock-Paper-Scissors Game \n")
print("Rules of the Game: \n * Rock VS Paper ----> Paper WINS \n * Rock VS Scissors----> Rock WINS \n * Paper VS Scissors ----> Scissors WINS \n")

# Setting Condition for replaying
is_running = True 

while is_running:

    # TO indicate the round of the game
    round = 1

    # A full function of the program that can be itrated
    def repeatGame() :
        
        # user selecting choice
        uchoice = input("Enter choice \n R for Rock, \n P for Paper, and \n S for Scissor \n Type you Choice: ")[0]
        userChoice = uchoice.upper()
        
        # Picking CPU choice at Random
        cpuChoice = random.choice(['R','P','S'])
        # Matching CPU choice with value
        if cpuChoice == 'R':
            cpuChoiceName = 'Rock'
        elif cpuChoice == 'P':
            cpuChoiceName = 'Paper'
        else:
            cpuChoiceName = 'Scissors'
        
        # Matching users choice with Title
        if userChoice == 'R':
            userChoiceName = 'Rock'
            print("\n***** Round",round,"*****\nPlayer (",userChoiceName,") : CPU (",cpuChoiceName,")\n")
        elif userChoice == 'P':
            userChoiceName = 'Paper'
            print("\n***** Round",round,"*****\nPlayer (",userChoiceName,") : CPU (",cpuChoiceName,")\n")
        elif userChoice == 'S':
            userChoiceName = 'Scissors'
            print("\n***** Round",round,"*****\nPlayer (",userChoiceName,") : CPU (",cpuChoiceName,")\n")
        else:
            print("Choice ou of range, type in the first letter of your choice.....\n")


        # Setting condition for winning
        if((userChoice == 'R' and cpuChoice == "P") or
        (userChoice == 'P' and cpuChoice =='R' )):
            result = "Paper"
            repeatGame.isWin = True
            # Printing our either computer or user wins
            if result == userChoiceName:
                repeatGame.toPrint = "Player WINS via "+ result +"\n***************"
            else:
                repeatGame.toPrint = "Computer WINS via "+ result+"\n***************"

        elif((userChoice == 'R' and cpuChoice == 'S') or
            (userChoice == 'S' and cpuChoice == 'R')):
            result = "Rock"
            repeatGame.isWin = True
            # Printing our either computer or user wins
            if result == userChoiceName:
                repeatGame.toPrint = "Player WINS via "+ result + "\n***************"
            else:
                repeatGame.toPrint = "Computer WINS via "+ result+"\n***************"    
        
        elif((userChoice == 'S' and cpuChoice == 'P') or
            (userChoice == 'P' and cpuChoice == 'S')):
            result = "Scissors"
            repeatGame.isWin = True
            # Printing our either computer or user wins
            if result == userChoiceName:
                repeatGame.toPrint = "Player WINS via "+ result +"\n***************"
            else:
                repeatGame.toPrint = "Computer WINS via "+ result+"\n***************"
        
        elif(userChoice == cpuChoice):
            repeatGame.isWin = False
    
    # Calling the funing so that if run
    repeatGame()

    # Condition to repeat the game until a win is acheived
    while repeatGame.isWin == False:
        round +=1
        print("*****NO WINNER*****\nThe Game is A Tie\n***************")
        repeatGame()
    else:    
        # Terminate the game
        print("*****GAME OVER*****\n",repeatGame.toPrint)
        
               
    # Requesting for either a replay or ternimation of program
    runingChoice = input("Press any key to play again and [n or N] to Terminate:") 
    if runingChoice == "n" or runingChoice == "N":
        is_running = False 
        # This is the same thing as a break.

print("Thanks for Playing, See you Soon...")