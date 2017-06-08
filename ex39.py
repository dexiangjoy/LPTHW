# -*- coding: utf-8 -*-
# create a mapping of state to abbreviation
# states 的值是cities 的键
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

# create a basic set of states and some cities/in them
# 州包含城市
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():       # items()方法返回键-值对
    print "%s is abbreviated %s" % (state, abbrev) # state 和 abbrev 分别储存 states 的键和值

# # print every city abbreviation
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])      # 这里绕了一下，abbrev 是 states 的值，对应着cities 的键

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')  # 没有改键，下面的 if 语句才可以执行

if not state:
    print "Sorry, no Texas." # states里没有Texas, 所以 if 语句执行

# get a city with a default value
# city 当cities 里没有TX 键返回给定的值
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
print cities

china_city = cities.setdefault('Hefei', 'I live in Hefei')
print china_city
print cities

# .get() 和 setdefault() 的区别：
# 二者都传入两个参数，使用get() 时，cities 字典不更新。使用 setdefault() ,cities 字典更新
# python ex39.py

# What is the difference between a list and a dictionary?
# A list is for an ordered list of items. A dictionary (or dict) is for matching some items (called "keys") to other items (called "values").

# What would I use a dictionary for?
# When you have to take one value and "look up" another value. In fact you could call dictionaries "look up tables."

# What would I use a list for?
# Use a list for any sequence of things that need to be in order, and you only need to look them up by a numeric index.
