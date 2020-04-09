# -*- coding:utf-8 -*-

import os

'''
创建一个文件
'''
for tmpdir in ('\temp',r'G:\pythonLearn'):
    if os.path.isdir(tmpdir):
        break
else:
    print 'no temp direcctory available'
    tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print '*** creating temporary directory'
    print cwd

    print '*** creating example directory...'
    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print '*** new working directory:'
    print cwd
    print '*** original directory listing:'
    print os.listdir(cwd)

    print '*** creating test file...'
    fobj = open('test','w')
    fobj.write('foo\n')
    fobj.write('test\n')
    fobj.close()
    print '*** updated directory listing:'
    print os.listdir(cwd)

    print "*** renaming 'test' to 'filetest.txt' "
    os.rename('test','filetest.txt')
    print '*** updated directory listing:'
    print os.listdir(cwd)

    path = os.path.join(cwd,os.listdir(cwd)[0])
    print '*** full file pathname'
    print path
    print '*** (filename, extension) =='
    print os.path.splitext(os.path.basename(path))


    print '*** displaying file contents'
    fobj = open(path)
    for eachline in fobj:
        print eachline,
    fobj.close()

    print '*** deleting test file'
    os.remove(path)
    print '*** updated direcory listing:'
    print os.listdir(cwd)
    os.chdir(os.path)
    print '*** deleting test directory'
    os.rmdir('example')
    print '*** DONE'
