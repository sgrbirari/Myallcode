# treasure hunt game
# print("""

#                     ____...------------...____
#                _.-"` /o/__ ____ __ __  __ \o\_`"-._
#              .'     / /                    \ \     '.
#              |=====/o/======================\o\=====|
#              |____/_/________..____..________\_\____|
#              /   _/ \_     <_o#\__/#o_>     _/ \_   \
#              \_________\####/_________/
#               |===\!/========================\!/===|
#               |   |=|          .---.         |=|   |
#               |===|o|=========/     \========|o|===|
#               |   | |         \() ()/        | |   |
#               |===|o|======{'-.) A (.-'}=====|o|===|
#               | __/ \__     '-.\uuu/.-'    __/ \__ |
#               |==== .'.'^'.'.====|
#           jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
#               `""""-""""""""""""""""""""""""""-""""`
# """)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

q1 = input('You are at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()
if q1 == 'left':
    q2 = input('''You have come to a lake. There is an island in the middle of the lake. 
          Type "wait" to wait for a boat. Type "swim" to swim across.\n''').lower()
    if q2 == 'wait':
        q3 = input('''You arrive at the island unharmed. There is a house with 3 doors. 
         One red, one yellow and one blue. Which colour do you choose?\n''').lower()
        if q3 == 'red':
            print("It's a room full of fire. Game Over.")
        elif q3 == 'blue':
            print("You enter a room of beasts. Game Over.")
        elif q3 == 'yellow':
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")  
    else:
        print("You get attacked by an angry trout. Game Over.")  
else:
    print("You fell into a hole. Game Over.")

    
        