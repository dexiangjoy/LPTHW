# -*- coding: utf-8 -*-
# > character (called the prompt)
# 第一步import ex25 不要加后缀  .py
# sentence = "All good things come to those who wait." ,变量sentence 被赋值了一个字符串
# 函数break_words调用sentence,返回一个列表['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']并赋值给words
# sorted(words) 和 words.sore() 都对words列表排序
# first word 和 last word ,返回该值的同时也删除该值。并对删除值后的列表进行排序

# join()方法针对字符串调用，传入一个列表值，返回字符串。join() is called on a string value and is passed a list value.
# split()则相反，针对字符串调用，返回一个字符串列表。It’s called on a string value and returns a list of strings.
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ') # 效果同 split()
    return words

# sort()与sorted()的不同是用法差异一个是li = sorted(words),另一个是words.sort()。都对列表排序
# sorted(words)将words从小到大排序,不影响words本身结构。sorted(words)为新列表
# words.sort()将words从小到大排序,影响words本身结构 ，将原位重新排列
# 二者均需要传入列表
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# 这函数名字起的有误导性，返回该值是为了提醒删除的是哪个元素。
# pop(0)就是删除第0个，pop()默认删除最后一个，效果等同于pop(-1)
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)  # 这里调用第一个函数break_words,目的是把字符串变成列表，然后让sort()排序
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
# 调用print_first_and_last时，先break_words把sentence变为列表，这时打印首位字母，是原来的排序
# 调用print_first_and_last_sorted时，先sort_sentence，把排序后的列表赋值给words，这时打印首位字母，是排序后的结果

# 本.py文件只写函数，执行时在终端打开Python环境，import ex25
# 要执行某个函数时，使用ex25.break_words(stuff) 。即ex25.加某个函数名，并可以把return的值再赋值
# help(ex25) 会显示所有#后面的内容，只不过是乱码，以及 """ 之间的内容
# help(ex25.break_words)，会显示单个函数的 """ 的内容，"""被称为documentation comments
# ex25 集成了许多函数，就像一个库一样，可以使用其中某个单独的模块。
# 像这样 from ex25 import break_words ,使用时 words = break_words(sentence)
# How can the words.pop function change the words variable?
# In this case words is a list, and because of that you can give it commands and it'll retain the results of those commands.
# This is similar to how files and many other things worked when you were working with them.
#When should I print instead of return in a function?
#The return from a function gives the line of code that called the function a result. You can think of a function as taking input through its arguments,
# and returning output through return. The print is completely unrelated to this, and only deals with printing output to the terminal.
