# -*- coding: utf-8 -*-
print "Type the filename :"
filename = raw_input("> ")
# 可再次输入txt文件名，也可打开其他的txt
txt = open(filename)

print txt.read()

# 最后两步重复
# 问？ 这个和ex15.py哪个get the filename好？我觉得这个好，方便。
# In Python shell
# >>>filename = raw_input()
# ex15.txt
# >>>txt = open(filename)
# >>>print txt.read() 或者直接输入txt.read()
# >>>txt.close()
# >>>txt.read()
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ValueError: I/O operation on closed file

#  txt = open(ex15.txt) it doesn't work
# You don't put the names of files in, you let Python put the name in.
