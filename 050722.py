# def multi(a,b):
#     return a*b

# def show():
#     print('the multiplication is:',)
    
# display=show(multi)
# display()

#Write a Program to match a string that has the letter ‘a’ followed by 4 t 8 'b’s.
# string = "abbabbbbbcccabbbb"    

# string = "abbabbbbbcccabbbb" 
# for i in string:
#     if count(b)<=4:
# def multi(func):
#     print('multi is:')
# ############################################
# a = {'x':100, 'y':200}
# b = list(a.items())
# print(b)
############################
# LCM of 2 numbers
# n1=int(input('enter a first number:'))
# n2=int(input('enter a second number:'))
# i=1
# while i>=1:
#     if i%n1==0 and i%n2==0:
#         print('LCM of {} and {} is {}'.format(n1,n2,i))
#         break
#     i+=1
################################
# HCF of two numbers
# n1=int(input('enter a first number:'))
# n2=int(input('enter a second number:'))
# m=1
# for i in range(1,n1+1):
#     if n1%i==0 and n2%i==0:
#         m=i
# print('HCF of {} and {} is {}'.format(n1,n2,m))
####################################
# Pythagoras theorem
# n1=int(input('enter a first number:'))
# n2=int(input('enter a second number:'))
# n3=((n1*n1)+(n2*n2))**0.5
# print(f'third side of tringle is:{n3}')
#############################
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hello my name is " + self.name)

# p1 = Person('sagar', 26)
# p1.myfunc()
###############################
# class Phone:
#     def make_calls(self):
#         print('Making phone calls')
    
#     def play_games(self):
#         print('playing games')

# p1=Phone()
# p1.make_calls()
# p1.play_games()
##################################
from scipy import constants
print(constants.pi)

print(dir(constants))
print(constants.gibi)
# Mass
print(constants.gram)
print(constants.lb)
# angle
print(constants.degree)
print(constants.arcmin)
# time
print(constants.minute)
print(constants.hour)
# length
print(constants.yard)
print(constants.nautical_mile)
#pressure
print(constants.atm)
print(constants.bar)
# area
print(constants.acre)
print(constants.hectare)
# volume
print(constants.liter)
print(constants.gallon)
# speed
print(constants.mach)
print(constants.knot)
# temprature
print(constants.zero_Celsius)
print(constants.degree_Fahrenheit)
# energy
print(constants.calorie)
# power
print(1260/(1000/constants.hp))
# force
print(constants.dyn)
print(constants.kilo)
'''
Optimizers in SciPy-
Optimizers are a set of procedures defined in SciPy 
that either find the minimum value of a function, 
or the root of an equation.
'''
'''
Optimizing Functions-
Essentially, all of the algorithms in Machine Learning 
are nothing more than a complex equation 
that needs to be minimized with the help of given data.
'''
'''
Roots of an Equation
NumPy is capable of finding roots for polynomials and linear equations, 
but it can not find roots for non linear equations, like this one:

x + cos(x)

For that you can use SciPy's optimze.root function.
This function takes two required arguments:

fun - a function representing an equation.
x0 - an initial guess for the root.

The function returns an object with information regarding the solution.
'''
from scipy.optimize import root
from math import cos

def eqn(x):
  return cos(x)

myroot = root(eqn, 0)

print(myroot)

'''
Minimizing a Function-
A function, in this context, represents a curve, curves have high points and low points.

High points are called maxima.

Low points are called minima.

The highest point in the whole curve is called global maxima, whereas the rest of them are called local maxima.

The lowest point in whole curve is called global minima, whereas the rest of them are called local minima.
'''
'''
Finding Minima-
We can use scipy.optimize.minimize() function to minimize the function.

The minimize() function takes the following arguments:

fun - a function representing an equation.

x0 - an initial guess for the root.

method - name of the method to use. Legal values:
    'CG'
    'BFGS'
    'Newton-CG'
    'L-BFGS-B'
    'TNC'
    'COBYLA'
    'SLSQP'

callback - function called after each iteration of optimization.

options - a dictionary defining extra params:

{
     "disp": boolean - print detailed description
     "gtol": number - the tolerance of the error
  }

'''
