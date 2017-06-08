# -*- coding: utf-8 -*-
# Functions do three things: 函数
# keep thinking "mini-script" when I say "function" and keep playing with them.
# They name pieces of code the way variables name strings and numbers.
# They take arguments the way your scripts take argv.
# Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands."

# this one is like your scripts with argv
# def for "define".and give the function a name
def print_two(*args):     #  Then we tell it we want *args which is a lot like your argv parameter but for functions.
    arg1,arg2 = args        # : colon, and start indenting. indented four spaces
    print "arg1: %r, arg2: %r" % (arg1, arg2)
#  In Python we can skip the whole unpacking arguments and just use the names we want right inside ().like print_two_again
# *args  tells Python to take all the arguments to the function and then put them in args as a list.

def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one arguments
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
# in Python those "commands" are just functions.
# This means you can make your own commands and use them in your scripts too.
# "To 'run,' 'call,' or 'use' a function all mean the same thing."
