def greet():
    print("Hello world")
greet()



def greet (name):
    print(f"Hello  {name} ! ")

greet("Botakoz")



def add (a,b):
    return a+b

result_of_sum = add (5,3)
print (result_of_sum)


chislo9 = 9
print (result_of_sum == chislo9)

print (add(5,10))


import math

def calc_square_root (num):
    return math.sqrt (num)


def calc_square_of_circle (radius):
    return math.pi*(radius**2)

sqrt = calc_square_root (16)
print (f" sqrt = {sqrt} ")


square = calc_square_of_circle (5)
print (f" sqr = {square} ")


def round_num (num):
   return round(num,2)

rounded_num  = round_num (1.7)
print (f" round 1.7 = {rounded_num} ")


def round_to_floor (num):
    return math.floor(num)


print (f" round_to_floor 1.7 = {round_to_floor (1.7)} ")


def round_to_ceil (num):
    return math.ceil(num)

print (f" round_to_ceil 1.7 = {round_to_ceil (1.7)} ")



import geometry

from geometry import *
from geometry import reactangle_area

rect_height = 10
rect_width = 14

rect_square = geometry.reactangle_area.rect_area (rect_height, rect_width)


