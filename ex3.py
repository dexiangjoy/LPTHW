# -*- coding: utf-8 -*- 
print "I will now count my chickens:"

print "Hens", 25 + 30.0 / 6.0 #python2的除法必须用浮点数
print "Roosters", 100 - 25 * 3 % 4 #75除以4得18余3，%这个符号是求余数

print "Now I will count the eggs:"

print 3 + 2 + 1 -5 + 4 % 2 -1.0 /4.0 + 6 #同理，除法用浮点数

print "Is it true that 3 + 2 < 5 -7?" #运算在括号内，可以算做字符串

print 3 + 2 < 5 -7 #没有引号，就会做布尔运算，True or False 大小写敏感，这里计算为False

print "what is 3 +2?", 3 + 2 #先打印字符串，再做运算
print "what is 5 - 7?", 5-7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2  #先打印字符串，然后同样做布尔值运算
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal", 5 <= -2
