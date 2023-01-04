# Snake Water Gun or Rock paper Scissor Game

import random

def gamewin(comp, you):
    
    if comp== you:
        return None
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp == 'w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True
randNo= random.randint(1,3)
print(randNo)

if randNo == 1:
    comp= 's'
elif randNo == 2:
    comp= 'w'
elif randNo == 3:
    comp= 'g'

print('Comp Turn:Snake(s)Water(w) or Gun(g)?')

you=input("player's Turn:Snake(s)Water(w) or Gun(g)?") 

a= gamewin(comp, you)

print(f'Computer Chose: {comp}')
print(f'You Chose: {you}')
if a == None:
        print('The game is a tie!')
elif a:
    print('You Win...!!!')
else : 
    print('You Lose...!!!')