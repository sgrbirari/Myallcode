# first and last digit of number
# n=int(input('enter a number:'))
# a=n[0]
# b=n[-1]
# last=n%10
# while n>0:
#     b=n%10
#     n=int(n/10)
# print(f'first digit is: {b} and last digit is: {last}')
########################
# muliti of digit in numbers
# n=int(input('enter a number:'))
# m=1
# print(f'multiplication of digits in {n} is:')
# while n>1:
#     x=n%10
#     m=m*x
#     n=int(n/10)
# print(m)
##########################
# s='today is good day'
# l=s.split()
# n=len(l)-1
# l1=[]
# for i in range(n,-1,-1):
#     l1.append(l[i])
# print(l1)
# final_reverse_string=' '.join(l1)
# print(final_reverse_string)    
####################
# s='today is good day'
# l=s.split()
# l1=[]
# i=0
# while  i<len(l):
#     l1.append(l[i][::-1])
#     i=i+1
# print(l1)
# final_reverse_string=' '.join(l1)
# print(final_reverse_string) 
##############################
# s='hello'
# L=[]
# for i in range(len(s)):
#     print(s[i])
# for i in s:
#     if i not in L:
#         L.append(i)
#     else:
#         L.remove(i)
# final=''.join(L)
# print(final)
#################################
# s='AC*wv12n/:#e123we2.45oin (fwoi6n#a98nfwb+qwi'
# x=" ".split(s)
# print(x)

################################
# import json
# python_data = {'name': 'Sonam', 'roll':101 }
# json_data = json.dumps(python_data)
# print(json_data)

# import json
# python_data = {name': 'Sonam', 'roll':101 }
# json_data = json.dumps(python_data)
# print(json_data)
##################################
# cjhecking if two words are anagrams
# from collections import Counter
# from itertools import count
# def is_anagram(str1, str2):
#     return Counter(str1)==Counter(str2)
# print(is_anagram('geek', 'peek'))
# print(is_anagram('geek', 'keeg'))
####################################
# Ways to remove i’th character from string in Python
str='SagarSubhashBirari'
print('the Original String:'+ str)
New_str='' 
for i in range(len(str)):
    if i!=2:
        New_str=New_str + str[i]
print('The NEw Srtring:'+ New_str)
##################################
