'''
sort list of students by there marks then 
find student with second highest score 
if there are two 2nd highest then follow alphabetic order 
[{"name":"ABC","marks":70},{"name":"PQR","marks":40},{"name":"ZYX","marks":60},{"name":"PCB","marks":50},{"name":"QST","marks":60}]
'''
lst=[{"name":"ABC","marks":70},{"name":"PQR","marks":40},{"name":"ZYX","marks":60},{"name":"PCB","marks":50},{"name":"QST","marks":60}]
x=[]
y=[]
for i in range(len(lst)):
    if lst[i]['marks'] not in x: 
        x.append(lst[i]['marks'])
        
# print(x)            #only marks list, no duplication
sorteed_marks= sorted(x)

# print(sorteed_marks)    # sorted marks list
# print(sorteed_marks[-2])    # second highest in marks

for i in range(len(lst)):
    if lst[i]['marks']==sorteed_marks[-2]:
        y.append((lst[i]))
        
# print(y)                # the ditionaries  of second highest marks
y= sorted(y, key=lambda d: d['name'])

# print(y)            # sorting alphabetically,
print(y[0])         # result printed.