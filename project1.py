# e='butter'
# def f(a): print(a)+ e
# f('bitter')
# import instaloader
# ig= instaloader.instaloader()
# dp= input('Enter insta username:')
# ig.download_profile(dp, profile_pic_only= True)
# time_until_midnight = '5'
# print('there are ' +time_until_Midnight+' hours until midnight')
# name= input('what is your name?')
# print('hello, '+ name)
# age=12
# print('you are'+ age + 'years old')
print('Welcome to the Tip Calculator!')
totalBill= int(input('What was the total bill?: Rs. '))
tip=int(input('what percentage tip would you lie to give? 12, 15, or 20 ?: '))
no_of_peopple=int(input('How many people to split the bill?'))
perhead=(totalBill * (1+(tip/100)))/ no_of_peopple
roundofperhead='{:.2f}'.format(perhead)
print(f'Each person should pay:Rs. {roundofperhead} ')
