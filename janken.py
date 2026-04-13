import random

human = input("Input S for stone,K for knife and P for paper: ").capitalize()
computer = random.randint(0,2)

if human == "K" and computer == 1:
    print("Stone blunts Knife. Computer wins!!")
elif human == "S" and computer == 0:
    print("Stone blunts Knife. Player wins!!")
elif human == "K" and computer == 2:
    print("Knife cuts paper. Player wins!!")
elif human == "P" and computer == 1:
    print("Knife cuts paper. Computer wins!!")
elif human == "P" and computer == 0:
    print("Paper covers stone. Player wins")
elif human == "S" and computer == 2:
    print("Paper covers stone. Computer wins")
elif (human == "S" and computer == 0) or (human == "K" and computer == 1) or (human == "P" and computer == 2):
    print("draw!!!. no one wins!!")
