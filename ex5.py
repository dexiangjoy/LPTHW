# -*- coding: utf-8 -*-
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74/0.3937  # inches to centmeters
weight = 100/2.20462  # lbs to kilogram

eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
# % 和 .format() 的区别。 .format() 优于 % ，这两种用法都可在py2，py3 运行。
# 作者在 python2中教 % ，python3 中教 {} .format用法
# %d用于整数，使用round()无效，所以%d用%r代替
print "Let's talk about %s." % name
print "He's %s centmeters tall." % round(height, 1) # 取一位小数点
print "He's %s kilograms heavy." % round(weight, 1)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair) # 两个以上变量加括号，用元组tuple
print "He's got {} eyes and {} hair.".format(eyes, hair) # 通过在大括号里改数字而改顺序
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %s, and %s I get %s." % (
    age, round(height, 1), round(weight, 1), age + round(height, 1) + round(weight, 1))
# 这里age不用取小数，所以用%d。后面两个用%s和%r效果一样
print "my name is %s, I was %d years old, and I have %r eyes" %(name, age, eyes )
# %r 会输出完整的文本，print时变量有引号便会输出引号
# %s 会输出字符串，print时变量有引号便会去掉引号
# format() 可直接输出小数点
