# add new pair in dictionary
dict1={'name': 'Sagar', 'surname':'Birari'}
dict1['mobile no']=879646413 # new key value pair adding {'mobile no':879646413} in dictionary
print(dict1)
##################################
# Access Dictionary elements (key & value both)
x = dict1.items() # we get tuple of all key value pairs present in dictionary
print(x)
###################################
# A)print unique numbers 
# B) print duplicate numbers
l1=[1,2,2,3,3,4,5,5] # given
l2=[]
l3=[]
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        l3.append(i)
print(l2) # unique numbers list
print(l3) # duplicate numbers list
#####################################
# to print square of the elements of given list in another list by using lambda function
list1=[1,2,3,4,5] # given

s=list(map(lambda x: x*x , list1))
print(s)

# if in Eployee table, from salary column, display the salary from50000 to 100000?
'''
select * from Employee
where salary between 50000 and 100000;
'''
# if in Eployee table, from name column, display the name starts with 'S'?
'''
select name from Employee
WHERE Employee_name LIKE 'a%';
'''