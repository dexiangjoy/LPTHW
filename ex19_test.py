def pen_pineapple_apple_pen(var):
    print "I have %s pen, I have %s apple." % (var, var)
    print "eng, %s apple-pen" % var
    print "I have %s pen, I have %s pineapple." % (var, var)
    print "eng, %s pen-pineapple-apple-pen" %(var)

print "A song"
pen_pineapple_apple_pen(1)

print "Song again"
var = 1
pen_pineapple_apple_pen(var)

print "How many pen do you have?"
var = raw_input('>')
pen_pineapple_apple_pen(var)
# python ex19_test.py
# What if I want to ask the user for the numbers of cheese and crackers?
# You need to use int() to convert what you get from raw_input().
# def的print 里的%s 如果换成 %d 就要使用int() 转换一下
