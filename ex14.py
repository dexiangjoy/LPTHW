# -*- coding: utf-8 -*-
from sys import argv

script, user_name, age = argv # 有几个argv，在命令行执行时就要填入几个参数
prompt = '--- '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few question."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about likng me.
You live in %r. Not sure where that is.
You are %s years old.
And you have a %r computer. Nice.
""" % (likes, lives, age, computer)
