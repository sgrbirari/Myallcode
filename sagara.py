# l=5*[[]]
# print(l)

# a= (1,2,3)
# b= (4,5,6)
# print(a+b)


# ▼
# ▼
# ▼
# ▼
# ▼
# ▼
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.")
#   elif age >= 45 and age <= 55:
#     print("Everything is going to be ok. Have a free ride on us!")
#   else:
#     bill = 12
#     print("Adult tickets are $12.")
  
#   wants_photo = input("Do you want a photo taken? Y or N. ")
#   if wants_photo == "Y":
#     bill += 3
  
#   print(f"Your final bill is ${bill}")

# else:
#   print("Sorry, you have to grow taller before you can ride.")
'''
love calcuclator
input
name1= input('enter your name:\n')
name2= input('enter their name:\n')
combine_str = name1 + name2
# lowering the letters
Lower_comb_str=combine_str.lower()


t =Lower_comb_str.count('t')
r =Lower_comb_str.count('r')
u =Lower_comb_str.count('u')
e =Lower_comb_str.count('e')

l =Lower_comb_str.count('l')
o =Lower_comb_str.count('o')
v =Lower_comb_str.count('v')
# e already counted in above word

# addition of count in love
love=l+o+v+e
# addition of count in true
true=t+r+u+e


# concatanation of both digits
calc=str(true) + str(love)
calc_int=int(calc)

# result
if calc_int >=90 or calc_int<=10:
    print(f"Your score is {calc_int}, you go together like coke and mentos.")   
elif 40 <= calc_int <= 50 :
    print(f"Your score is {calc_int}, you are alright together.")
else:
    print(f"Your score is {calc_int}.")  
'''

'''
# Import the random module here
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
list_len= len(names)
random_choice= random.randint(0,list_len-1)
who_will_pay= names[random_choice]
print(f'{who_will_pay} is going to buy the meal today!')
'''
