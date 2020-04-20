# -*- coding:utf-8 -*-
myseq = (123, 45.67, -6.2e8, 999999999L)
def convert (func, seq):

    return [func (eachNum) for eachNum in seq]


print convert(int, myseq)
print convert(long, myseq)
print convert(float, myseq)
