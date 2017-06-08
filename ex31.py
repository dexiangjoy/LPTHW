# -*- coding: utf-8 -*-
print "You enter a dark room with two doors. Do you go through door #1 or door #2 or door #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off.  Good job!"
    elif bear == "2":
        print "The bear eats your legs off.  Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "Now, you have two choice  "
    print "1. go back"
    print "2. go through the way until you meet a girl"

    choice =raw_input("> ")

    if choice == "1":
        print "Have a nice day!"
    elif choice == "2":
        print "Fuck that girl!"
    else:
        print "Poor guy, open the game again"

elif door == "3":
    print "There is nothing in here!"
else:
    print "You stumble around and fall on a knife and die.  Good job!"

# Can you replace elif with a sequence of if-else combinations?
# You can in some situations, but it depends on how each if/else is written.
# It also means that Python will check every if-else combination, rather than just the first false ones like it would with if-elif-else.
# How do I tell if a number is between a range of numbers?
# You have two options: Use 0 < x < 10 or 1 <= x < 10, which is classic notation, or use x in range(1, 10).
# What if I wanted more options in the if-elif-else blocks?
# Add more elif blocks for each possible choice.
