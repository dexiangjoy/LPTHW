# -*- coding: utf-8 -*-
# One more input method , Well the ex13.py part of the command is called an "argument."
# What we'll do now is write a script that also accepts arguments.
from sys import argv  # add modules to your script from the Python feature set
#The argv is the "argument variable"  This variable holds the arguments you pass to your Python script when you run it.
script, first, second = argv  # "unpacks" argv , rather than holding all the arguments, it gets assigned  variables on the left in order.
name = raw_input("What's your name? ")
age = int(raw_input("How old are you? "))
print "So you're %s, and you're %d years old" %(name, age)
print "The script is called:", script
print "You first variable is:", first
print "Your second variable is:", second

# when run code,你必须这样输入 ：python ex13.py first 2nd 3rd
# 输出：The script is called: ex13.py
#             Your first variable is: apple
#             Your second variable is: orange
#             Your third variable is: grapefruit

# ValueError: need more than 3 values to unpack
# This happens when you do not put enough arguments on the command when you run it
# 报的错取决你输了几个数，只输入ex13.py就显示more 1 values
# python3 的报错ValueError: not enough values to unpack (expected 4, got 3) 更人性化有没有

# 没有区分的必要
# What's the difference between argv and raw_input()?
# The difference has to do with where the user is required to give input.
# If they give your script inputs on the command line, then you use argv.
# If you want them to input using the keyboard while the script is running, then use raw_input().
# 在需要区分时就加以说明：“函数声明中的参数”和“调用函数时传入的参数” 即parameter、argument
# What is the difference between an argument and a parameter?
# 引数和参数有何区别？
# While defining method, variables passed in the method are called parameters.
# 当定义方法时，传递到方法中的变量称为参数.
# While using those methods, values passed to those variables are called arguments.
# 当使用方法时，传给变量的值称为引数.
