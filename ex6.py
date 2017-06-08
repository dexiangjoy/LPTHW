# -*- coding: utf-8 -*-
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %  (binary, do_not)  #这里 两处

# 作者爱扯犊子，说什么string is put inside a string 有几处。答案是就四处

print x # 在字符串的外面加上% 10 ，则会替换%d
print y # binary 和 don't 会替换字符串里的两个%s

print "I said: %r." % x # 这里一处
print "I also said: '%s'." % y # 这里一处
# %r displays the "raw" data of the variable ，原x有"",故不需要另加
# %s displaying to users ,需要另加 ‘’ ，才能在结果里显示单引号
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious # joke_evaluation 后面的%r用hilarious替换

joke_evaluation = "Isn't that joke so funny?! {}"

print joke_evaluation.format(hilarious) # format用法，更易懂

w = "This is the left side of..."
e = "a string with a right side."

print w + e # 字符串相连
# 加号用在字符串是连接，用在数字则是相加
