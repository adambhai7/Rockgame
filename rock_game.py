#ROCK PAPER SECISIOR GAME 
import random
# print() use for spaceing
print("\nWELCOME TO ROCK,PAPER,SECISIOR GAME.")
#print() use for spaceing
try:
    user_input = int(input("\nEnter 1 for rock, 2 for paper, 3 for secisior : "))
except EnvironmentError as e:
        print(f"press only 1,2 or 3.",e)
if (user_input<=3):
     print(f"YOU CHOOSE : {user_input}")   
else:
    print(f"sorry press only 1,2 or 3.")
    exit()
computer = [1,2,3]
computer_user = random.choice(computer)
print(f"COMPUTER CHOOSE : {computer_user}")
if (user_input == computer_user):
    print("YOUR MATCH IS DRAW.")

elif (user_input == 1) and (computer_user == 3):
     print("YOU ARE WIN.")

elif (user_input == 2) and (computer_user == 1):
     print("YOU ARE WIN.")

elif (user_input == 3) and (computer_user == 2):
     print("YOU ARE WIN.")

elif (user_input == 1) and (computer_user == 2):
     print("YOU ARE LOSE.")

elif (user_input == 2) and (computer_user == 3):
     print("YOU ARE LOSE.")

elif (user_input == 3) and (computer_user == 1):
     print("YOU ARE LOSE.")
else:
    print("something wrong ???.")
