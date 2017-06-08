# -*- coding: utf-8 -*-
# 作者说，from now on ,写下你犯过的错误，也决定把有用的common question记下来
# A variable wouldn't have the single-quotes around it.
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow' # sonw 不是变量，it is just a string with the word snow
print "And everywhere that Mary went."
print "." * 10 # what'd that do?  # 点乘以10，意思是打印十遍“.”

# python 中单引号和双引号效果一样，But typically ,single-quotes for any short strings like 'a' or 'snow'.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
# 如果移出逗号(comma)，最后两个print会输出两行，如果想输出一行，则加逗号。
# 加逗号前提是两行加起来不超过80个字符
print end1 + end2 + end3 + end4 + end5 + end6, # 字符串相连，没有空格，两个print之间会有空格.
print end7 + end8 + end9 + end10 + end11 + end12
