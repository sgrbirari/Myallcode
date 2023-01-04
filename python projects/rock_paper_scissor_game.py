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

#Write your code below this line 👇
import random

choice=[rock, paper, scissors]
lst_len = len(choice)
you=int(input('enter the choice among "rock" as 0, "paper" as 1 & "scissors" as 2:\n')) 
print('You chose:\n', choice[you])

if you>2 and you<0:
    print('You have entered invalid keys, You lose..!!')
    
comp= random.randint(0,2)
print( "computer chose:\n",choice[comp])

'''
Rock wins against scissors. 0 & 2,  0 wins
Scissors win against paper. 2 & 1,  2 wins
Paper wins against rock.    1 & 0,  1 wins
'''
#0 0
if you==0 and comp==0:
    print('draw')
#0 1
if you==0 and comp==1:
    print('You lose')
#0 2    
if you==0 and comp==2:
    print('You won')
#1 0  
if you==1 and comp==0:
    print('you won')
#1 1
if you==1 and comp==1:
    print('draw')
#1 2
if you==1 and comp==2:
    print('You lose')
#2 0
if you==2 and comp==0:
    print('You lose')
#2 1
if you==2 and comp==1:
    print('you won')
#2 2
if you==2 and comp==2:
    print('draw')
