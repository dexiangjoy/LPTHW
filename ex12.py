# -*- coding: utf-8 -*-
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# Remember %r is for debugging and is "raw representation" while %s is for display.
# python -m pydoc
# raw_input open, file, os, and sys
# 参数-p <port> 在当前主机启用HTTP服务，使用指定的端口。
# C:\>python -m pydoc -p 53241  然后打开 http://localhost:53241/
