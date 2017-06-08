# -*- coding: utf-8 -*-
# Learning if-statements
people = 20
cats = 20
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"

if people >cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people >dogs:
    print "The world is dry!"


dogs += 5
if people >= dogs:
    print "People are greater than or equal to dogs."
if people <= dogs:
    print "People are less than or equal to dogs."
if people == dogs:
    print "People are dogs"
if not(people >= cats):
    print "Just a try!"
#What do you think the if does to the code under it?
# if 做判断，是就执行，不是就忽略
#Why does the code under the if need to be indented four spaces?
# 是的，要缩进四个空格
#What happens if it isn't indented?
# 不缩进 ：IndentationError: expected an indented block
#Can you put other boolean expressions from Exercise 27 in the if-statement? Try it.
#看第二十七和第二十八行
#What happens if you change the initial values for people, cats, and dogs?
# 会显示name 'dog' is not define
