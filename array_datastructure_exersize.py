##############problem 1##############################
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190


# month_exp=[2200,2350,2600,2130,2190]
'''
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''
# 1 ans 
# extra_dollers_spent_in_Feb=month_exp[1]-month_exp[0]
# print(extra_dollers_spent_in_Feb)

# 2 ans
# def Sum_first_quarter():
#     sum=month_exp[0]+month_exp[1]+month_exp[2]
#     print(sum)
# s1= Sum_first_quarter()

# 3 ans
# for i in month_exp:
#     if i== 2000:
#         print('the index of this value is:',i)
#     else:
#         print('no any value is equal to 2000')

#4 ans
# month_exp.append(1980)
# print(month_exp)

# #5 ans
# print('the actual list before correction:', month_exp)
# correction_in_april= int(month_exp[3])-200
# month_exp.remove(month_exp[3])
# month_exp.insert(3, correction_in_april)
# print('the list after correction:', month_exp)
#########################################
# class Node:
#     def __init__(self, val):
#         self.childleft= None
#         self.childright= None
#         self.nodedata= val

# root= Node(1)
# root.childleft=Node(2)
# root.childright=Node(3)
# root.childleft.childleft=Node(4)
# root.childleft.childright=Node(5)

# def InOrd(root):
#     if root:
#         InOrd(root.childleft)
#         print(root.nodedata)
#         InOrd(root.childright)
# InOrd(root)
#####################################
# def Bs(lst1):
#     length1=len(lst1)-1
#     for elements in range(length1):
#         for y in range(length1-elements):
#             if lst1[y]>lst1[y+1]:
#                 lst1[y],lst1[y+1]=lst1[y+1],lst1[y]
#     return lst1
# lst1=[3,4,7,2,1,9,6,8,5]
# Bs(lst1)
# print(lst1)
###########################################
# def Isort(a):
#     for x in range(1, len(a)):
#         k=a[x] #element present at a index no. 1
#         j=x-1
#         while j >= 0 and k < a[j]:  #if  you want descending order, type- 'k > a[j]'
#             a[j+1] = a[j]
#             j -= 1
#         a[j+1] = k
# a = [14,52,11,20,3,18,5]
# Isort(a)
# print(a)
#############################################
# Selection sort
# def selsort(myarray, i):
#     for x in range(i):
#         minimum = x
#         for y in range (x+1, i) :
#             if myarray[y] < myarray[minimum]:
#                 minimum= y
#         (myarray[x],myarray[minimum]) = (myarray[minimum],myarray[x])
# mylist=[85,41,63,52,69,21]
# i= len(mylist)
# selsort(mylist,i)
# print(mylist)
########################################## 
# lin search
# def Linsearch(myarray, n , key):
#     for x in range(0,n):
#         if (myarray[x]==key):
#             return x
#     return -1
# myarray=[12,4,5,35,17]
# key= 17  
# n= len(myarray)
# matched=Linsearch(myarray,n, key)
# if (matched== -1):
#     print('key is not present')
# else:
#     print('key is present in given list at index:', matched)
##############################################
