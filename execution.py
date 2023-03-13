# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pyscreenshot

path = 'pictures/'
os.chdir(path)
os.listdir()

a = [1360, 0, 3300, 1100]
pic = pyscreenshot.grab(a)
pic.show()

base = '000'

#for number in range(20):#number = 1
def exists(var):
     return var in globals()

 
firstRunCheck = exists("number")

print(firstRunCheck)

if firstRunCheck:
    number += 1
else:
    number = 0


print(number)
"""
print(number)

    
strNum = str(number)
t = len(strNum)

#listBase[-1] = str(number)
base = ''.join([base[:-t], strNum])

print(base)

name = 'picture_' #+ str(number)

pic.save(name + ".png")
"""