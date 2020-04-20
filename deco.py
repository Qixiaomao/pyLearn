from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print '[%s]  %s()' % (ctime(), func.__name__)
		return func()
	return wrappedFunc

@tsfunc
def foo():
	pass

foo()
sleep(4)

for i in range(2):
	sleep(1)
	foo()
