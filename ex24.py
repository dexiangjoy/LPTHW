# -*- coding: utf-8 -*-
print "Let's practise everything."
print 'You\'d need to know escape sequences about \\ that do \n newlines and \t tabs.'

poem = """
The lovely world with logic so firmly planted
\tcannot discern \n\t the needs of love
\tnor comprehend passion from intuition
\tand requires an explanation
\n\twhere there is none.
"""

print "------&--------"
print poem
print "------&--------"


five = 5
print "This should be five: %s" % five

# inside the function the variable is temporary. When you return it then it can be assigned to a variable for later.  
def secret_formula(started):
    jelly_beans = started * five
    jars = jelly_beans / 100
    crates = jars / 10
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

end_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(end_point)
