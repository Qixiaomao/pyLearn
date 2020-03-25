# -*- coding: utf-8 -*-

'''
This is a test that makefile and read .
'''

import os
ls = os.linesep
all = []

fname = "G:\\pythonLearn\\test.txt"


print "==================================================\n"
print"+        welcome to my first test version1.0      + \n"
print"+   1.input                       2.cat           + \n"
print"===================================================\n"

#get the nums
def InputFile():

 while True:
     entry = raw_input('input>>')
     if entry =='.':
            break
     else:
           all.append(entry)

#read the file
def ReaadFile():
fname = raw_input('Enter filename:')



try:
	fobj = open(fname,'r')
except IOError, e:
	print "*** file open eror:",e
else:
	#display contents to the screen
    for eachline in fobj:
	   print eachline,
fobj.close()

#main function
if ( __name__=="__main__"):
	ipt = raw_input("%d")
while True:
	if ipt == 1:
		def InputFile()
	elif ipt == 2:
		def ReadFile()
    else:
		break
