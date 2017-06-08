# -*- coding: utf-8 -*-
# object oriented programming
# 面向对象程序设计，指一种程序设计范型，同时也是一种程序开发的方法。对象指的是类的集合。
#它将对象作为程序的基本单元，将程序和数据封装其中，以提高软件的重用性、灵活性和扩展性。
# 面向对象程序设计可以看作一种在程序中包含各种独立而又互相调用的对象的思想，这与传统的思想刚好相反：
# 传统的程序设计主张将程序看作一系列函数的集合，或者直接就是一系列对电脑下达的指令。
# 面向对象程序设计中的每一个对象都应该能够接受数据、处理数据并将数据传达给其它对象，
# 因此它们都可以被看作一个小型的“机器”，即对象。
# 面向对象程序设计推广了程序的灵活性和可维护性，并且在大型项目设计中广为应用。

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10  thing in that list. Let's fix that."

stuff = ten_things.split(' ')  # split(ten_things, ' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

for i in range(10):  # 虽然可以运行，可是觉得写的恶习
    if len(stuff) > 10:
        break
    else:
        next_one = more_stuff.pop()
        stuff.append(next_one)
#while len(stuff) != 10:
#    next_one = more_stuff.pop()
#    print "Adding: ", next_one
#    stuff.append(next_one)  # append(stuff, next_one)
#    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()   # pop(more_stuff)
print '.'.join(stuff) # join(stuff, .)
print '#'.join(stuff[3:5])


# python ex38_sample.py
