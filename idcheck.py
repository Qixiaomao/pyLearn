# -*- coding:utf-8 -*-

'''This is about the id check .You can use it check the string whether is the string or keywords.'''

import string
import keyword

alphas = string.letters + ''
nums = string.digits


print'Welcome to the Identifier Checker v1.0.'
print'Testees must be at least 2 chars long.'
myInput = raw_input('Indetifier to test? >>')



if len(myInput) > 1 or myInput == keyword.kwlist:
    print 'Sorry,%s is the keywords.' % myInput

    if myInput[0] not in alphas:
        print '''invalid: first symbol must be alphabetic'''
    else:
        for otherChar in myInput[1:]:

            if otherChar not in alphas + nums:
                print '''invalid: remaining symbols must be alphanumeric'''
                break
        else:
            print 'okay as an identifier'
elif len(myInput) == 1:

    print'This is a only 1 character.'


