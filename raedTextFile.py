# -*- coding: utf-8 -*-

'readTextFile.py -- read and display text file'



fname = 'G:\\pythonLearn\\test.txt'
#get filename

fname = raw_input('Enter filename:')

print

# attempt to open file for reading
try:
	fobj = open(fname,'r')
except IOError, e:
	print "*** file open eror:",e
else:
	#display contents to the screen
    for eachline in fobj:
	    print eachline,
fobj.close()
