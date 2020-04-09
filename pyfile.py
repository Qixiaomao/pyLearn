
'''
    for eachline in fline:
        eachline.strip()
        if not eachline.startswith("#"):
            print eachline 
 This is other way of other person.       
'''

def printfile():
    fline = open('G:\\pythonLearn\\test.txt','r+')
  
    allLines = fline.readlines()
    for eachline in allLines:
        if eachline[0] != "#":
            print eachline     

    fline.close()

printfile() 