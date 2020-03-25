# -*- coding:utf-8 -*-
##import thread
import threading
from time import sleep,ctime

'''This is a test of the thread.'''

'''
def loop0():
    print 'start loop 0 at:',ctime()
   # sleep(4)
    print 'loop 0 done at:',ctime()

def loop1():
    print 'start loop 1 at:',ctime()
   # sleep(2)
    print 'loop 1 done at:',ctime()  

def main():
    print 'Starting at:',ctime()
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
   # sleep(6)
    print 'all DONE at:',ctime()
'''
'''****************************************************'''
'''这次用锁来替换之前代码中的sleep函数'''
loops = [4,2]

def loop(nloop,nsec):
    print 'Start loop',nloop,'at:',ctime()
    sleep(nsec)
    print 'loop',nloop,'done at:',ctime()
    #lock.release()

def main():
    print 'starting at:',ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        #lock = thread.allocate_lock()
        #lock.acquire()
        #locks.append(lock)
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)

    for i in nloops:   #start threads
        threads[i].start()

    for i in nloops:   #wait for all
        threads[i].join() #threads to finish
    
    print 'all DONE at:',ctime()



if __name__ == '__main__':
    main()