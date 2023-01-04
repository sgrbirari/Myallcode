# # # emp= employees.objects.update('id'=101)
# # # x= employeess.objects.fil
# # lst=[]
# # for n in range(6):
# #     n=int(input('enter a number:'))
# #     lst.append(n)
# # print('original list:', lst)
# # lst.sort()
# # print('sorted list:', lst)
# # print('second largest element from list is:', lst[-2])

# # calculator for groceries
# sum=0
# while (True):
#     user_input= (input('enter the item price or press \'q\' to quit: \n'))
#     if user_input!='q':
#         sum= sum + int(user_input)
#         print(f'order total so far:{sum}')
#     else:
#         print(f'your bill total is:{sum}. thanks for shoppijng with us!!')
#         break
######################################
# lst=[]
# print('summary of bill:')
# for user_input in lst:
#     lst.append(user_input)
# print(lst)
# class A :
#     def __init__(s):
#         self.s=s
            
#     def print():
#         pass
# a=A('john')
# a.print()
############################
# def add(a,b):
#     assert(a>b)
#     assert(b>a)
#     print(a/b)
# add(4,0)

#########################
# lst1=[]
# N=int ( input('enter a total number to be added in the list:'))
# for i in range(N):
#     num=int(input('enter a numbers:'))
#     lst1.append(num)
# print(lst1)
# print('Mininum Number in the List:', min(lst1))
##############
# def numbers(n):
#     for i in n:
#         yield i**2
# cubes= numbers([2,6,1,9,5])
# print(list(sorted(cubes)))
###########
# def num (x):
#     n=0
#     while n<=x:
#         yield n
#         n+=1
# S=sum(num(10))
# print(S)
####
# lis=['a','d','s']
# print(lis[10:])
###########


# class Rectangle(object):
#     def __init__(self,w,h):
#         self.w=w
#         self.h=h
#     def area(self):
#         return self.w*self.h

#     def __str__(self):
#         return '(Rectangle: %s , %s)' %(self.w, self.h)
    
# r1=Rectangle(17,24)
# print(r1)
###################
# L1=[2,'s',4]
# L2=['m', '1',10]
# print(L1+L2*2**2)
############
# def task (p,i):
#     i=iter(i)
#     for x in i:
#         if not p(x):
#             yield x
#             break
#     for x in i:
#         yield x
# a= task(lambda x:x<5,[4,-2,0,1,3,-1,10,33])
# for i in range(2):
#     print(next(a),end=' ')
#########################
# class parent(object):
#     x=1

# class child1(parent):
#     pass

# class child2(parent):
#     pass

# print(parent.x,child1.x, child2.x)

# child1.x=2
# print(parent.x,child1.x, child2.x)

# parent.x=3
# print(parent.x,child1.x, child2.x)
############
# def program(func):
#     def test(*args,**kwargs):
#         value= func(*args,**kwargs)
#         return value
#     return test
# @program
# def Cal(x,y):
#     return x+y
# x,y=2,3
# print(x,y)