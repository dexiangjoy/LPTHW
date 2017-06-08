# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv  # 脚本名字和txt文件的名字，要在命令行输入

txt = open(filename) # it takes a parameter and returns a value you can set to your own variable.
# You just opened a file. 先打开这个txt文件
print "Here's your file %r:" % filename
print txt.read()
# You give a file a command by using the . (dot), the name of the command(方法), and parameters.
# 读取这个txt文件，打印出来

# If you are not sure ask someone for help or search online.
# Many times searching for "python THING" will find answers to what that THING does in Python.
# Try searching for "python open."\
# I used the word "commands" here, but commands are also called "functions" and "methods."
# txt = open(filename) don't return the contents of the file ,It actually makes something called a "file object."
# "file object." like DVD player. the DVD player is not the DVD the same way the file object is not the file's contents.
# What does from sys import argv mean?
# For now just understand that sys is a package, and this phrase just says to get the argv feature from that package.
# open the file twice? Python will not restrict you from opening a file more than once and sometimes this is necessary.
