# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#type "number = 1" before running code
import os
import pyscreenshot


a = [1360, 0, 3300, 1100]
pic = pyscreenshot.grab(a)
pic.show()

base = '000'

#number = 1

with open('ini.txt', 'r') as f:
     strNum = f.read()


#strNum = str(number)
#print(number)   
    
#strNum = str(1)
base = ''.join([base[:-1], strNum])

number =  int(strNum) + 1
strNum = str(number )
with open('ini.txt', 'w') as f:
    f.write(strNum)

print(base)

path = 'pictures/' + 'picture_' + base + '.png'

pic.save(path)
