rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

comp_selection = random.randint(1,4)

rockID = 1
paperID = 2
scissorID = 3

def getCompSelection(comp_selection):
    if comp_selection == 1:
        return "rock"
    elif comp_selection == 2:
        return "paper"
    elif comp_selection == 3:
        return "scissors"

usr_selection = int(input("Select from the following options:\n1=Rock\n2=Paper\n3=Scissors\n"))

if usr_selection < 1 or usr_selection > 3:
    print("Error")
else:
    if usr_selection == 1:
        print("You have selected rock")
        print(rock)
        if getCompSelection(comp_selection) == "rock":
            print("They selected rock")
            print(rock)
            print("Draw!")
        elif getCompSelection(comp_selection) == "paper":
            print("They selected paper")
            print(paper)
            print("Computer Wins!")
        elif getCompSelection(comp_selection) == "scissors":
            print("They selected scissors")
            print(scissors)
            print("User Wins!")
    elif usr_selection == 2:
        print("You have selected paper")
        print(paper)
        if getCompSelection(comp_selection) == "rock":
            print("They selected rock")
            print(rock)
            print("User Wins!")
        elif getCompSelection(comp_selection) == "paper":
            print("They selected paper")
            print(paper)
            print("Draw!")
        elif getCompSelection(comp_selection) == "scissors":
            print("They selected scissors")
            print(scissors)
            print("Computer Wins Wins!")
    elif usr_selection == 3:
        print("You have selected scissors")
        print(scissors)
        if getCompSelection(comp_selection) == "rock":
            print("They selected rock")
            print(rock)
            print("Computer Wins!")
        elif getCompSelection(comp_selection) == "paper":
            print("They selected paper")
            print(paper)
            print("User Wins!")
        elif getCompSelection(comp_selection) == "scissors":
            print("They selected scissors")
            print(scissors)
            print("Draw!")
    else:
        print("Error")
