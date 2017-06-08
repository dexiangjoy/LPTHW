# -*- coding: utf-8 -*-
# We put a , (comma) at the end of each print line.
# This is so print doesn't end the line with a newline character and go to the next line.
print "What's your name?",
name = raw_input()
print  "How old are you?",
age = raw_input()
print "How tall are you?", # 单位inches，也就是6'2" ，当用%r输出'6\'2"'' 用%s 输出6'2"
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "Hi %r , you're %r years old, %r tall and %r heavy." % (
    name, age, height, weight)
# 传入raw_input的都是字符串，所以用%r,结果都带单引号，用%s则不带
# 为什么当用%r输出'6\'2"'' 用%s 输出6'2"     ？
# %r输出原生字符串，想打印出 6'2" ，得这么写 print '6\'2"' 。而%r只不过把它无保留的打印出来了
# It presents a prompt to the user (the optional arg of raw_input([arg])),
# gets input from the user and returns the data input by the user in a string.
# raw_input() returns a string, and input() tries to run the input as a Python expression.
# 即python2的input()判断输入是变量还是字符串，是变量就报错
# x = int(raw_input()) which gets the number as a string from raw_input()
#  then converts it to an integer using int()
# When my strings print out there's a u in front of them, as in u'35'.
# That's how Python tells you that the string is Unicode.
# Use a %s format instead and you'll see it printed like normal.
