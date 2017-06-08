# -*- coding: utf-8 -*-
i = 0
numbers = []

for i in range(0, 6, 1):
    print "At the top i is %d" % i
    numbers.append(i)
#     i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

# 这个练习对于SD5， Write it to use for-loops and range.
#  Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?
# i = i + 1 如果去掉，numbers.append(i)将不起作用，这时在range() 括号里再加一个数字表示增量
