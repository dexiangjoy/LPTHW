# -*- coding: utf-8 -*-
# The return statement causes your function to exit and hand back a value to its caller. --stack overflow
# add a and b then return them.Python adds the two numbers. Then when the function ends,
# any line that runs it will be able to assign this a + b result to a variable. like age = add(3, 5)
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


print "Let's do some math with just function!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ; %d" % (age, height, weight, iq)


# A puzzle for the extra credit (学习单元) , type it in anyway.
print "Here is a puzzle."

# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
what = age + height - weight * iq / 3
print "That becomes: ", what, "Can you do it by hand?"

# What you should do is try to figure out the normal formula that would recreate this same set of operations.
# what = age + (height - (weight *(iq / 2)))
# what = age + height - weight * iq / 2
# 我写了一个简单的练习
# Why does Python print the formula or the functions "backward"?
# It's not really backward, it's "inside out." When you start breaking down the function into separate formulas and function calls you'll see how it works.
# Try to understand what I mean by "inside out" rather than "backward."
# 我已经理解了inside out 的意思，Python 会从里到外的打印所有公式 formula ,而不是backward ,最先运算的公式最先打印。
# 当使用raw_input(), 整数使用int(raw_input()) ,浮点数使用float(raw_input())
