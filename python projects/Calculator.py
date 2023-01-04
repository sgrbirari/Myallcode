def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def mul(p,q):
    return p*q
def div(p,q):
    return p/q

print('Please select the operation:')
print('a.   Add')
print('b.   Subtract')
print('c.   Multiply')
print('d.   Divide')

choice= input('Please enter choice- a / b / c / d:')

num_1= int(input('Please enter the first number: '))
num_2= int(input('Please enter the second number: '))

if choice == 'a':
    print(num_1, '+', num_2, '=', add(num_1,num_2))
elif choice == 'b':
    print(num_1, '-', num_2, '=', sub(num_1,num_2))
elif choice == 'c':
    print(num_1, 'x', num_2, '=', mul(num_1,num_2))
elif choice == 'd':
    print(num_1, '/', num_2, '=', div(num_1,num_2))
else:
    print('This is an invalid iput')