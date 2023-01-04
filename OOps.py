#inside constructor by using self variable
'''
we can declare instance variable inside a constructor by using self keyword,
once we create object, automatically these variables added to the object.
'''
class Employee:
    def __init__(self):
        self.eno=100
        self.ename='Sagar'
        self.esal='100000'
e=Employee()
print(e.__dict__)

#Inside Instance method by using self variable
'''
if any instance variable declared inside instance method, 
that instance variable will be added once we call that method
'''
class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
        
t=Test()
t.m1()
print(t.__dict__)    

#outside of the class by using object reference variable:
'''
we can also add instance variable outside of a class to a particular object
'''
class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
t=Test()
t.m1()
t.d=40
print(t.__dict__) 

#how to accaes instance variavbles:
'''
we can access instancde variables with in the class 
by using self variable and outside of the class by using object reference
'''
class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def display(self):
        print(self.a)
        print(self.b)
t=Test()
t.display()
print(t.a,t.b)

#how todelete instance variables from the object
'''
del self .variablename #  Delete within class

del objectreference.variablename # delete outside of class
'''
class Test:
    def __init__(self):
        
        self.a=10
        self.b=20
        self.c=30
        self.d=40
    def m1(self):
        del self.d
t=Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
del t.c
print(t.__dict__)