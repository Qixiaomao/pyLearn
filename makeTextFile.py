

# -*- coding: utf-8 -*-

# makeTextFile.py -- create text File.

import os
ls = os.linesep

fname = 'G:\\pythonLearn\\test.txt'

# get filename
'''
while True:
   if os.path.exists(fname):
        print"ERROR:'%s' already exists" % fname
   else:
    	break
'''
# get file content (text)lines

all = []
#print"\nEnter lines('.'by itself to quit).\n"
print "==================================================\n"
print"+        welcome to my first test version1.0      + \n"
print"+   1.input                       2.cat           + \n"
print"===================================================\n"

#loop until user terminates input
while True:
 entry = raw_input('input>>')
 if entry =='.':
     break
 else:
    all.append(entry)

#write lines to file with proper line-ending
fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print "DONE!"
