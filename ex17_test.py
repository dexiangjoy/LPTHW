from sys import argv

open(argv[2], 'w').write( open(argv[1]).read())

# It should already be closed by Python once that one line runs.
# python ex17_test.py test.txt new_file.txt
