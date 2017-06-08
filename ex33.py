# -*- coding: utf-8 -*-
# A while-loop will keep executing the code block under it as long as a boolean expression is True.
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
# What's the difference between a for-loop and a while-loop?
# A for-loop can only iterate (loop) "over" collections of things.
# A while-loop can do any kind of iteration (looping) you want. However,
# while-loops are harder to get right and you normally can get many things done with for-loops.
# What they do is simply do a test like an if-statement, but instead of running the code block once,
# they jump back to the "top" where the while is, and repeat. A while-loop runs until the expression is False.

# Here's the problem with while-loops: Sometimes they do not stop. This is great if your intention is to just keep looping until the end of the universe.
# Otherwise you almost always want your loops to end eventually.
# To avoid these problems, there are some rules to follow:
# Make sure that you use while-loops sparingly. Usually a for-loop is better.
# Review your while statements and make sure that the boolean test will become False at some point.
# When in doubt, print out your test variable at the top and bottom of the while-loop to see what it's doing.
