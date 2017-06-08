# -*- coding: utf-8 -*-
# Lists: a container of things that are organized in order from first to last. 
# In python 2.x, range returns a list. In 3.x, it returns an iterable range object.
# 例子1: python2.7
# >>>elements =  range(0, 6)
# >>> elements
# [0, 1, 2, 3, 4, 5]
# 例子2: python3.6
# >>> elements =  range(0, 6)
# >>> elements
# range(0, 6)

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count % d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# range(start, stop[, step])
# If the step argument is omitted, it defaults to 1. If the start argument is omitted, it defaults to 0.
# then use the range function to do 5 counts， # 让代码块执行固定次数
# The range() function only does numbers from the first to the last, not including the last.
# elements = range(0, 6)
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)   # It simply appends to the end of the list.

# now we can prints them out too
for i in elements:
    print "Element was: %d" % i

# How do you make a 2-dimensional (2D) list?  That's a list in a list like this: [[1,2,3],[4,5,6]]
# Why is a for-loop able to use a variable that isn't defined yet?
# The variable is defined by the for-loop when it starts, initializing it to the current element of the loop iteration, each time through.
