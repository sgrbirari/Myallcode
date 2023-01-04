'''
FizzBuzz
here there will be 2 number fizz and buzz 
if nth number is divide by fizz then print Fizz
if nth number is divide by buzz print Buzz
and if by both print FizzBuzz 
else print number

example
Fizz = 2
Buzz = 3
n = 20

ans :
1
Fizz
Buzz
Fizz
5
FizzBuzz
7
Fizz
Buzz
Fizz
11
FizzBuzz
# 13
# Fizz
# Buzz
# Fizz
# 17
# FizzBuzz
# 19
# '''
n=20
fizz=2
buzz=3
for i in range(1,n):
    if i%2==0 and i%3==0:
        print('fizzbuzz')
    elif i%2== 0:
        print('fizz')
    elif i%3== 0:
        print('buzz')
    else:
        print(i)    

    


