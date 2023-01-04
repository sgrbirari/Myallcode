# Python program to interchange first and last elements in a list
# def swaplist(newlist):
#     size=len(newlist)
    
#     temp=newlist[0]
#     newlist[0]=newlist[size-1]
#     newlist[size-1]=temp
    
#     return newlist

# newlist=[51,22,45,36,78,10,96]

# print(swaplist(newlist))
###################################
# Python | Ways to find length of list
# Method 1: Naive Method
# ls1=[1,4,7,8,5,2,3,6,9,8,7,4,5,1,2,3,6]
# print('the list is: '+ str(ls1))
# counter=0
# for i in ls1:
#     counter=counter+1
# print('length of list using naive method is:'+ str(counter))

# Method 2 : Using len()

# a= []
# a.append("Hello")
# a.append("Geeks")
# a.append("For")
# a.append("Geeks")
# print("The length of list is: ", len(a))


# Python program to demonstrate working
# of len()
# n = len([10, 20, 30])
# print("The length of list is: ", n)

# Method 3 : Using length_hint()

# # Python code to demonstrate
# # length of list
# # using len() and length_hint
# from operator import length_hint
 
# # Initializing list
# test_list = [5,8,9,6,4,1,2,3,1]
 
# # Printing test_list
# print ("The list is : " + str(test_list))
 
# # Finding length of list
# # using len()
# list_len = len(test_list)
 
# # Finding length of list
# # using length_hint()
# list_len_hint = length_hint(test_list)
 
# # Printing length of list
# print ("Length of list using len() is : " + str(list_len))
# print ("Length of list using length_hint() is : " + str(list_len_hint))
#########################################
# Python | Count occurrences of an element in a list

# def countx(lst, x):
#     count=0
#     for i in lst:
#         if i==x:
#             count=count+1
#     return count
# lst=[1,4,5,7,8,9,5,4,6,1,2,3,6,0,1,2,4,5,8,75]
# x=6

# print('{} has occurred {} times'.format(x, countx(lst, x)))

# Method 2 (Using count()) 

# def countx(lst,x):
#     return lst.count(x)
# lst=[1,2,4,7,8,4,5,1,2,3,6,5,6,8,9,97,7,4,4,5,1,2,3,6,5,4,1,2,2,3,3,3,1,14]
# x=7
# print(f'{x} is occured {countx(lst,x)} times')
##########################################

# Find sum and average of List in Python
# l=[10,20,30,40,50]
# count=0
# for i in l:
#     count=count+i
# avg=count/len(l)
# print(f'sum of numbers is: {count} and the avarage is: {avg}')