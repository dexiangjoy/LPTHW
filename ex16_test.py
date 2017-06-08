# -*- coding: utf-8 -*-

from sys import argv

scripts, filename = argv

test = open(filename)

print test.read()
