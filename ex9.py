# -*- coding: utf-8 -*-
# Here's some new strange stuff, remrember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" # \n是换行键

print "Here are the days: ", days
print "Here are the months: ",months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

# triple-quotes 三引号 可以任意输出 ,引号之间不加空格
# \n newlines not work when use %r :
# %r it prints it the way you wrote it (or close to it). It's the "raw" format for debugging.
