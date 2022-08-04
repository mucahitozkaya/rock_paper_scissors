import random

# 1 = Rock -- 2 = Paper -- 3 = Scissors
list = [1,2,3]

print("\n1 - Rock\n2 - Paper\n3 - Scissors")
user_score, computer_score = 0, 0

for _ in list:
    
    computer = random.choice(list)
    user = int(input("Choose one of 1,2,3 = "))

    if user == 1:
        if computer == 1:
            print("Rock and Rock. Equal!")
        elif computer == 2:
            print("Paper and Rock. You LOSE!")
            computer_score += 1
        elif computer == 3:
            print("Scissors and Rock. You WIN!")
            user_score += 1
        
    elif user == 2:
        if computer == 1:
            print("Rock and Paper. You WIN!")
            user_score += 1
        elif computer == 2:
            print("Paper and Paper. Equal!")
        elif computer == 3:
            print("Scissors and Paper. You LOSE!")
            computer_score += 1

    elif user == 3:
        if computer == 1:
            print("Rock and Scissors. You LOSE!")
            computer_score += 1
        elif computer == 2:
            print("Paper and Scissors. You WIN!")
            user_score += 1
        elif computer == 3:
            print("Scissors and Scissors. Equal!")
    
    else:
        print("Invalid Choice")       
   
print("\nYour Score: {}\nComputer's Score: {}".format(user_score, computer_score))
