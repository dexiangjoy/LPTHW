# -*- coding: utf-8 -*-
# We can give it straight numbers. We can give it variables. We can give it math. We can even combine math and variables.
# In a way, the arguments to a function are kind of like our = character when we make a variable.
# In fact, if you can use = to name something, you can usually pass it to a function as an argument.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers of directly:"
cheese_and_crackers(20, 30)
# 分别给cheese_count和boxes_of_crackers赋值20和30

print "OR, we can use variables from our script:"
amount_of_cheese = 10  # 避免全局变量的名字(global variables)和函数变量(function variables)的名字相同
amount_of_crackers = 50 # 好像也可以叫局部变量 (function variables)
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# 先给变量赋值，再在函数里调用变量。

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
# 只是做一个简单的加法运算

print "And we can combine the two,variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# 再一次调用变量，而且还给变量做运算

# 强调：什么最重要？ 里面的数字最重要
# Is there a limit to the number of arguments a function can have?
# he practical limit though is about five arguments before the function becomes annoying to use.
