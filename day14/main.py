import random
from art import logo,vs
from game_data import data



def higher_lower():
    print(logo)
    current_score=0
    should_continue=True

    while should_continue:
        dict1 = random.choice(data)
        dict2 = random.choice(data)

        person_1= dict1['follower_count']
        person_2=dict2['follower_count']


        print("Compare A:", dict1['name'], ",", dict1['description'], ",", "from", dict1['country'])
        print(vs)
        print("Against B:", dict2['name'], ",", dict2['description'], ",", "from", dict2['country'])

        user_choice = input("Who has more followers? Type 'A' or 'B': ")
        if user_choice=="A":
            if person_1>person_2:
                current_score+=1
                print(f"You are right! Current score: {current_score}")
            else:
                print(f"Sorry, that's wrong. Final score: {current_score}")
                should_continue=False


        elif user_choice == "B":
            if person_1 < person_2:
                current_score += 1
                print(f"You are right! Current score: {current_score}")
            else:
                print(f"Sorry, that's wrong. Final score: {current_score}")
                should_continue = False

higher_lower()