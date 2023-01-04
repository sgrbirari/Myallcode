#shift all zeros to the end
x=[12,0,23,0,26,0,67,0,34]
y=[]

for i in x:
    if i ==0:
        y.append(i)
        x.remove(i)
x.extend(y)
print(x)