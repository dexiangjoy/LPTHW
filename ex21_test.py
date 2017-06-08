# -*- coding: utf-8 -*-
#num = [(num1+num2)/(num1-num2)]*num3

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

n1 = add(10, 4)
n2 = subtract(8, 3)
n3 = multiply(6, 7)
n4 = divide(100.0, 7)

print "n1 = %d, n2 = %d, n3 = %d, n4 = %d" % (n1, n2, n3, n4)

print "num0 = n3 * (n2 - (n1+n4/7)"

num0 = multiply(n3, subtract(n2, add(n1, divide(n4, 7))))

print "num0:", num0

# python ex21_test.py
