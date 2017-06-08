# -*- coding: utf-8 -*-
# Here's the list of commands
# close -- Closes the file. Like File->Save.. in your editor.
# read -- Reads the contents of the file. You can assign the result to a variable.
# readline -- Reads just one line of a text file.
# truncate -- Empties the file. Watch out if you care about the file.
# write('stuff') -- Writes "stuff" to the file. write takes a parameter of a string you want to write to the file.

from sys import argv

scripts, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') # we open the file, creating it if it doesn't exist and truncating it to 0 bytes if it does.
# Hint: open tries to be safe by making you explicitly say you want to write a file.
# print "Truncating the file.  Goodbye!"
# truncate()
# If you use 'w' then you're saying "open this file in 'write' mode,"
# There's also 'r' for "read," 'a' for append, and modifiers on these.

print "Now I'm going to ask you for three lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# target.write("\n".join(line1,line2,line3) + "\n")
# target.write( "%s\n%s\n%s\n" % (line1, line2, line3))
target.write (line1 + '\n' + line2 + '\n' + line3) # 最简单

print "And finally, we close it."
target.close()

# With truncate(), you can declare how much of the file you want to remove,
# based on where you're currently at in the file.  Without parameters, truncate() acts like w
# You can do 'w+', 'r+', and 'a+'. This will open the file in both read and write mode
# 'r' (read) mode default for the open() function.
# r for reading
# w for writing
# r+ opens for reading and writing (cannot truncate a file)
# w+ for writing and reading (can truncate a file)
# rb+ reading or writing a binary file
# wb+ writing a binary file
# a+ opens for appending
