# -*- coding: utf-8 -*-
# echo to make a file, and cat to show the file?
from sys import argv
from os.path import exists  # This returns True if a file exists, returns False if not.

scripts, from_file, to_file = argv

print "Coping from %s to %s" % (from_file, to_file)

# we could do these two on one line,how?
in_file = open(from_file)
indata = in_file.read()
# indata = open(from_file).read()
# like this ,这样就不需要 .close() 了
print "The input file is %d bytes long" % len(indata)
# It gets the length of the string that you pass to it then returns that as a number.
print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTR-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
# A closed file cannot be read or written any more. Any operation,
# which requires that the file be opened will raise a ValueError after the file has been closed.
