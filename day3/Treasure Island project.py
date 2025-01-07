print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Type L for left direction and type R to go in right direction:\n")
if direction=="L":
    print("You fell into the hole, game over! try again.")
elif direction=="R":
    wants_to = input("Type S for swimming and W for waiting for a boat:\n")
    if wants_to == "S":
        print("Whales attacked you, game over! try again.")
    elif wants_to =="W":
        boat =input("choose the correct door! blue(type B) / yellow(type Y) / red(type R)\n")
        if boat=="B":
            print("Attacked by sharks! game over,try again")
        elif boat =="Y":
            print("Boat broken! game over,try again")
        elif boat=="R":
            print("Congratulations, mission completed")
        else:
            print("wrong door chosen, game over! try again")

    else:
        print("Wrong option chosen, game over! try again")
else:
    print("You have chosen wrong direction,game over! try again")