# Rock-paper-scissors-lizard-Spock template
import random 
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
# helper functions
def name_to_number(name):
    # delete the following pass statement and fill in your code below    
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        number = 0
    elif name == "spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4     
        
    return number 
def number_to_name(number):
    # delete the following pass statement and fill in your code below        
    # convert number to a name using if/elif/else
    # don't forget to return the result! 
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
        
    return name
def rpsls(player_choice): 
    number = random.randint(0, 4)    
    computer = number_to_name(number)  
    # delete the following pass statement and fill in your code below       
    # print a blank line to separate consecutive games
    print "player choose", player_choice
    # print out the message for the player's choice
    print "computer choose", computer      
    # convert the player's choice to player_number using the function name_to_number()
    # compute random guess for comp_number using random.randrange()
    # convert comp_number to comp_choice using the function number_to_name()    
    # print out the message for computer's choice
    # compute difference of comp_number and player_number modulo five
    # use if/elif/else to determine winner, print winner message
    #player choose rock
    if player_choice == "rock" and computer == "lizard":
        print "player wins!!!\n"
    if player_choice == "rock" and computer == "scissors":
        print "player wins!!!\n"                
    if player_choice == "rock" and computer == "paper":
        print "computer wins!!!\n"
    if player_choice == "rock" and computer == "spock":
        print "computer wins!!!\n"
    if player_choice == "rock" and computer == "rock":
        print "player and computer lie!!!\n"    
        
    #player choose spock
    if player_choice == "spock" and computer == "rock":
        print "player wins!!!\n"
    if player_choice == "spock" and computer == "scissors":
        print "player wins!!!\n"                
    if player_choice == "spock" and computer == "paper":
        print "computer wins!!!\n"
    if player_choice == "spock" and computer == "lizard":
        print "computer wins!!!\n"
    if player_choice == "spock" and computer == "spock":
        print "player and computer lie!!!\n" 
        
    #player choose paper
    if player_choice == "paper" and computer == "rock":
        print "player wins!!!\n"
    if player_choice == "paper" and computer == "spock":
        print "player wins!!!\n"                
    if player_choice == "paper" and computer == "scissors":
        print "computer wins!!!\n"
    if player_choice == "paper" and computer == "lizard":
        print "computer wins!!!\n"
    if player_choice == "paper" and computer == "paper":
        print "player and computer lie!!!\n" 

    #player choose lizard
    if player_choice == "lizard" and computer == "spock":
        print "player wins!!!\n"
    if player_choice == "lizard" and computer == "paper":
        print "player wins!!!\n"                
    if player_choice == "lizard" and computer == "rock":
        print "computer wins!!!\n"
    if player_choice == "lizard" and computer == "scissors":
        print "computer wins!!!\n"
    if player_choice == "lizard" and computer == "lizard":
        print "player and computer lie!!!\n" 
        
    #player choose scissors
    if player_choice == "scissors" and computer == "paper":
        print "player wins!!!\n"
    if player_choice == "scissors" and computer == "lizard":
        print "player wins!!!\n"                
    if player_choice == "scissors" and computer == "rock":
        print "computer wins!!!\n"
    if player_choice == "scissors" and computer == "spock":
        print "computer wins!!!\n"
    if player_choice == "scissors" and computer == "scissors":
        print "player and computer lie!!!\n" 
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
# always remember to check your completed program against the grading rubric