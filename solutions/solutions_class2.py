#1

def contains_a(string):
    return 'a' in string

#2

def max(a,b):
    if a > b:
        return a
    else:
        return b

#3

import math

def perimeter(r):
    return 2*math.pi*r

#4

def square():
    for i in range(5):
        print("#"*5)

#5

def sum_product(a, b):
    if a*b > 1000:
        return a*b
    else:
        return a+b

#6

import math

def quadratic_formula(a,b,c):
    solution1 = (-b + math.sqrt(b**2-4*a*c))/2*a
    solution2 = (-b - math.sqrt(b**2-4*a*c))/2*a
    
    return solution1, solution2

#7

def divisors(n):
    for k in range(1,n+1):
        if n%k==0:
            print(k)

#8

def fibonnaci(i):
    if i == 1:
        return 1
    elif i == 2:
        return 1
    else:
        return fibonnaci(i-1)+fibonnaci(i-2)

#9

def fizzbuzz():
    for i in range(1,51):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)

#10

def check_velocity(speed):
    points = (speed-70)/5
    if speed < 70:
        print("ok")
    elif points > 12:
        print("carta de condução suspensa")
    else:
        print(points)