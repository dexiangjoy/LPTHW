# -*- coding: utf-8 -*-
def numbers(num, increment):
    i = 0
    numbers = []

    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

# SD1：照搬，只要把 i < 6 ,改成 i < num
# python ex33_sample.py
numbers(10000, 1000)
