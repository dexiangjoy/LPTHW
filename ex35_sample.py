# -*- coding: utf-8 -*-
# 顺序调整易懂版
from sys import exit

def dead(why):    # 本游戏提前退出的结局，死亡
    print why, "Good job!"
    exit(0)

def start():       # 游戏从start() 开始
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()        # 选左，跳到 bear_room
    elif choice == "right":
        cthulhu_room()    # 选右，跳到 cthulhu_room
    else:      # 两个都不选，等着饿死吧
        dead("You stumble around the room until you starve.")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:    # makes an infinite loop
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True    # 嘲讽一下熊，熊就走了
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews you leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()    # 第一个elif 执行后顺着执行下来，我原以为会直接结束
        else:
            print "I got no idea what that means."

def gold_room():
    print "This room is full of gold.  How much do you take?"

    how_much = int(raw_input("> "))

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()    # 逃跑就回到一开始
    elif "head" in choice:     # 被吃就挂掉
        dead("Well that was tasty!")
    else:    # 都不选就原地打转，直到你选为止
        middle()

def middle():
    dead("If you choice middle, you must go die!")

start()
# What does exit(0) do?
# On many operating systems a program can abort with exit(0), and the number passed in will indicate an error or not.
#  If you do exit(1) then it will be an error, but exit(0) will be a good exit.
# The reason it's backward from normal boolean logic (with 0==False) is that you can use different numbers to indicate different error results.
#You can do exit(100) for a different error result than exit(2) or exit(1).

# exit(0) means a clean exit without any errors / problems
# exit(1) means there was some issue / error / problem and that is why the program is exiting.
