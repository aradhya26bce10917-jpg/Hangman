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
choice1 =input('u/re at a crossroad ..where do u want to go?type "left" or "right" ')
if choice1 =="left":
    choice2= input('u hav come to a lake..there is an island in middle of lake.Type "wait" to wait for boat else "swim" to swim across.')
    if choice2 =="wait":
       choice3=input('u arrived unharmed to island.theres a house with three doors ..choose between "yellow" "red" "blue" .' )
       if choice3 =="yellow":
          print("itss a winnn..yayyy you wonnn.")
       elif choice3 =="blue":
          print("GAME OVER u got attacked by an angry trout..")
       elif choice3 =="red":
            print("GAME OVER....fire warningggg")
       else:
          print("u entered wrong room.GAME OVER..")
    else:
         print("you got attacked by crocodile in water.game is over.")
elif choice1 =="right":
   print("you fell into a hole.game over..")

