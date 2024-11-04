# def my_function():
#     print("Hello from my function")
#     x='October'
#     print (x)
#
#
#
#
# name = 'Bota'
# print (name,4+3)
# my_function()
# print ("end function")
#
#
#
# def my_function1(y):
#     print (y)
#
#
#
#
# y=10
# print ('start2')
# my_function1(y)
# print ("end function2")



# def add(a,b):
#     return a+b
# a=4
# b=10
# print (add (a,b))
#


# def my_func (*kids):
#     print ("The youngest of my_func " + kids [1])
#
# my_func ("Misha","Leo","Dasha")
#
#
#
# def my_funct (a,b,c):
#     print("The value a is = " + a)
#     print("The value b is = " + b)
#     print("The value c is = " + c)
#
# my_funct (a="windows", b="Linux", c="Mac")
#
#
#
#
# def calculate (a,b):
#     return a+b, a-b, a*b
#
# sum, diff, mul =calculate(5,3)
# print (sum, diff, mul)
#

#
#
# def factorial (n):
#     if n==1:
#         return 1
#
#     else:
#         return n*factorial(n-1)
# print(factorial(5))
#
#


# def square (x):
#     return x*x
# print (square( 5))
#
#


# def power (base, exponenta):
#     return base ** exponenta
#
# print (power(3,2))
# print (power(exponenta=3,base=2))



def add (j,k):
    return j+k

def minus (j,k):
    return j-k

def operate (func, c,d):
    print ('this is func', func)
    return func (c,d)

print (operate ( add, 3,4),operate ( minus, 3,4))




x=lambda a, b: a+b+10
print (x(5,6))