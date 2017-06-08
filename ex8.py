# -*- coding: utf-8 -*-
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True) # 布尔值不加双引号
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",   # 这行输出后，仍然是双引号，原因是字符串里面用了单引号
    "So I said goodnight."
)
# 除开特例外，双引号会输出成单引号。问：why？
# Python is going to print the strings in the most efficient way it can, not replicate exactly the way you wrote them.
#  only use %r for getting debugging information about something
# Chinese (or some other non-ASCII characters) into these strings, but %r prints out weird symbols.
# Use %s to print that instead and it'll work.
