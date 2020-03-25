# -*- coding:utf-8 -*-

'''This is a  use a list as a stack.'''

stack = []



def pushit():
    stack.append(raw_input('Enter New string:').strip())

def popit():
    if len(stack) == 0:
        print 'Cannot pop from an empty stack!'
    else:
        print'Removed [','stack.pop()',']'

def viewstack():
    print stack       #calls str() internally

CMDs = {'u':pushit,'o':popit,'v':viewstack}

def showmenu():
    pr="""
p(U)sh
p(o)p
(V)iew
(Q)uit

Enter choice: """

while True:
    while True:
         try:
             choice = raw_input().strip()[0].lower()
         except  (EOFError,KeyboardInterrupt,IndexError):
             choice ='q'

         print '/nYou picked: [%s]' % choice
         if choice not in 'uovq':
            print 'Invalid option, try again'
         else:
            break 
    if  choice == 'q':
        break
    CMDs[choice] ()

if __name__ == '__main__':
    showmenu()

