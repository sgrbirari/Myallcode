'''
Find out dublicate element in list
'''
X= [1,0,1,0,2,4,2,0,1,2,4,0,1,1] 
Z=[]
for i in X:
    if i not in Z:
        Z.append(i)
print(Z)

####################################
A=[1,2,3,4,8,5,7,9] 
B=[4,7,8,4,5,6,1,4,7,8,9]
'''
combine the 
both list A & B and sort the elements in ascending order, and 
don’t use any method like sort, append, etc
'''
A.extend(B)
print(A)
new=[]
while A:
    min= A[0]
    for i in A:
        if i < min:
            min = i
    new.append(min)
    A.remove(min)
print(new)