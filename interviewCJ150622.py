
# newlist=[]
# for i in range(1,100):
#     if i%5==0 and i%3==0:
#         newlist.append(i)
# print(newlist)

# newlist=[x for x in range(1,100) if x%5==0 and x%3==0]
# print(newlist)

#  select * from Employee
#  where Salary= max(salary) from Employee
#  where not in select max(salary) from Employee

# x=[2,4,6,8,10,11,6,8,4]
# for i in x:
#     if i not in x:
#         i
#     else:
#         print(i)



# f=open('interview stats.txt') 



# ALPHA='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
# s1=[]       
# s='AC*wv12n/:#e123we2.45oin (fwoi6n#a98nfwb+qwi'
#############################################
# #multithreading
# t=threading.current_thread().getName()
# print(t)       
# from threading import *
# def display():
#     for i in range(1,3):
#         print('child thread')
# t=Thread(target=display)
# t.start()
# for i in range(1,3):
#     print('main thread')
    
##################

# creating thread without any class

# from threading import Thread
# def disp(a, b):
#      print('Thread Running:', a, b)
# t = Thread(target=disp, args=(10, 20))
# t.start()

# from curses.ascii import isdigit
# from threading import Thread
# def disp(a, b):
#      print('Thread Running:', a, b)
# for i in range(5):
#       t = Thread(target=disp, args=(10, 20))
#       t.start()
#####################################
# class Mythread(Thread):
#     def Run(self):
#         for i in range(10):
#             print('child thread')
# t=Mythread()
# t.start()
# for i in range(10):
#     print(' main thread')
################################

# creating thread without extending thread class
# from threading import *
# class Test:
#     def display(self):
#         for i in range(10):
#             print('child thread-2')
# obj=Test()
# t=Thread(target=obj.display) 
# t.start()
# t.join()
# for i in range(10):
#     print('main thred-2')       
#################################
# from threading import *
# import time
# def doubles(numbers):
#     for n in numbers:
#         time.sleep(2)
#         print('Double:', n*2)
# def Squares(numbers):
#     for n in numbers:
#         time.sleep(2)
#         print('Square:',n*n)

# numbers=[1,2,3,4,5]
# begintime=time.time()
# t1=Thread(target=doubles, args=(numbers,))
# t2=Thread(target=Squares, args=(numbers,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('the total time taken:',time.time()-begintime)
####################################
# get name() and Set name()
# print('########################')
# from threading import *
# print(current_thread().getName())
# current_thread().setName('Sagar')
# print(current_thread().getName())
# print(current_thread().name)

# print('########################')
############################################
# ident function
# from unicodedata import numeric



# s='AC*wv12n/:#e123we2.45oin (fwoi6n#a98nfwb+qwi'
# # print(' '.join(s))
# # print(s)
# s1=[]
# num_list=[int(x) for x in s if  s.split() if  x.isdigit()]
# print(num_list)
# for i in s:
#     if i.isdigit():
#         s1.append(int(i))   
# print(s1)