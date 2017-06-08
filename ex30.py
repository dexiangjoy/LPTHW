# -*- coding: utf-8 -*-
# Study Drills.
# What do you think the if does to the code under it?
# An if-statement creates what is called a "branch" in the code. It's kind of like those choose your own adventure books where you are asked to turn to one page if you make one choice,
# and another if you go a different direction. The if-statement tells your script, "If this boolean expression is True, then run the code under it, otherwise skip it."
# Why does the code under the if need to be indented four spaces?
#A colon at the end of a line is how you tell Python you are going to create a new "block" of code,
# and then indenting four spaces tells Python what lines of code are in that block. This is exactly the same thing you did when you made functions in the first half of the book.
# What happens if it isn't indented?
# If it isn't indented, you will most likely create a Python error. Python expects you to indent something after you end a line with a : (colon).

people = 20
cars = 30
trucks = 20

if cars > people and trucks > cars :
    print "We should take the trucks"
elif trucks <= people :      # 否则如果，仅在前面的条件为False时才检查该条件。
    print "We have too many people"  # elif 语句是“许多”可能的子句中有一个被执行。
else:      # else语句不包含条件，只有在 if 和 elif 的条件为 False 时才会执行
    print "We do not going anywhere"

if trucks > cars :
    print "That's too many trucks."
elif trucks < cars or trucks > people:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

# What happens if multiple elif blocks are True?
# Python starts and the top runs the first block that is True, so it will run only the first one.
