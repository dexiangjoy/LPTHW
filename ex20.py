# -*- coding: utf-8 -*-
from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline() # f.readline() reads a single line from the file

current_file = open(input_file)
# 读之前先open ，不然就返回错误，input_fiel是自己新建的文件
print "First let's print the whole file:\n"

print_all(current_file)
# 用.read() 打印出新建的文件test.txt
print "Now let's rewind, kind of like a tape."

rewind(current_file)
# 这个函数在这里没卵用，只是打个酱油，说的就是seek
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)
# 有了 .readline() 函数，每次打印一行，三个print 就打印三行
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
# 调用函数时，用 current_line 替换 current_line，作者问 line_count 是怎么成为 current_line 的？不知道

# seek() 函数
# fileObject.seek(offset[, whence])
# offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
# whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；
# 0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
# f.read() 一次，就  If the end of the file has been reached, f.read() will return an empty string ("").
# 而 f.readline() 一次返回一行，当返回完后则同上，每次末尾都会有换行符Newline \n

# What is f in the print_all and other functions?
# The f is a variable, except this time it's a file. A file in Python is kind of like an old tape drive on a mainframe,
# or maybe a DVD player. It has a "read head," and you can "seek" this read head around the file to positions,
# then work with it there. Each time you do f.seek(0) you're moving to the start of the file.
# Each time you do f.readline() you're reading a line from the file, and moving the read head to right after the \n that ends that line.

# Why does seek(0) not set the current_line to 0?
# First, the seek() function is dealing in bytes, not lines. The code seek(0) moves the file to the 0 byte (first byte) in the file. Second,
#  current_line is just a variable and has no real connection to the file at all. We are manually incrementing it.

# How does readline() know where each line is?
# Inside readline() is code that scans each byte of the file until it finds a \n character, then stops reading the file to return what it found so far.
# The file f is responsible for maintaining the current position in the file after each readline() call, so that it will keep reading each line.

# Why are there empty lines between the lines in the file?
# The readline() function returns the \n that's in the file at the end of that line. Add a ,
# at the end of your print function calls to avoid adding double \n to every line.
