# class MathOp:
#     def Addition(a,b):
#         return a+b
    
# class DSM(MathOp):
#     def Multi():
        
#     def div():
        
#     def sub():
        
'''
inheritance- make one class and implement addition method and 
make another class which inheriting first class and 
implements the multiplication, substraction and division methods 
but one condition is that inherited class can not use any operator 
for functioning, it can only use parent class method.
'''
######################################
# to swap the first and last element of list

# lst=[4,7,8,9,6,4,1,2,3]
# def swaplist():
#     temp=lst[0]
#     lst[0]=lst[-1]
#     lst[-1]=temp
    
#     size=len(lst)
#     print('size of list:', size)
#     print(lst)
# x=swaplist()
######################################
# another way
# lst=[56,7,8,9,6,4,1,2,45]
# def swaplist(lst):
#     lst[0], lst[-1]=lst[-1], lst[0]
#     return lst
# print (swaplist(lst))
###############################
# to print even chr of string
# stre='how are you Sagar?'
# def evenchr():
#     for i in range (len(stre)):
#         if i%2==0:
#             print(stre[i],end=' ')
# x=evenchr()
#########################
# Python program to print even length words in a string
# n='baby you are sooo sexy'
# s=n.split(' ')
# for i in s:
#     if len(i)%2==0:
#         print(i,end=' ')
############################
# Reverse words in a given String in Python
s='baby I love you Baby'
x=s.split()[::-1]
l=[]
for n in x:
    l.append(n)
print(' '.join(l))
#################################
#  Count the Number of matching characters in a pair of string
str1 = 'abcdef'
str2 = 'defghia'
####################################
lst=[1,4,5,6,44,8]  
print(lst[-1])
