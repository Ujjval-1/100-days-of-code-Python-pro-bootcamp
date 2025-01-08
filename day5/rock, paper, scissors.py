import random
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
game = [rock,paper,scissors]
user_input = int(input("Enter 0 for rock, 1 for paper, 2 for scissors\n"))
if user_input not in [0, 1, 2]:
    print("Wrong input")
else:
    if user_input==0:
        print(f"you chose rock {rock}")
    elif user_input==1:
        print(f"You chose paper {paper}")
    elif user_input==2:
        print(f"You chose scissors {scissors}")


    computer_choice = random.randint(0,2)
    print(f"computer chose {game[computer_choice]}")

    if user_input==computer_choice:
        print("It's a draw")
    elif user_input==0 and computer_choice==1:
        print("You lost! try again")
    elif user_input==0 and computer_choice==2:
        print("You won")
    elif user_input==1 and computer_choice==0:
        print("You won")
    elif user_input==1 and computer_choice==2:
        print("You lost! try again")
    elif user_input==2 and computer_choice==0:
        print("You lost! try again")
    elif user_input==2 and computer_choice==1:
        print("You won")



