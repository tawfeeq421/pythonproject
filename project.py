import random
user_choice=int(input("Enter Your Choice : Type of 0 for Rock,1 for Paper, 2 for Seissors  :"))
if user_choice >= 3 or user_choice <=0:
    print("Your Entred Invalid Number, You lose")
else:
    computer_choice = random.randint(0,2)
    print("computer chose")
    print(computer_choice)
    if computer_choice == user_choice:
        print("it's Draw")
    elif computer_choice ==0 and user_choice ==2:
        print("You Lose")
    elif user_choice ==0 and computer_choice == 2:
        print("You Wins")
    # elif user_choice ==0 and computer_choice ==2:
    #     print("You Wins")
    elif computer_choice > user_choice:
        print("You Lose")
    elif user_choice > computer_choice:
        print("You Wins")

