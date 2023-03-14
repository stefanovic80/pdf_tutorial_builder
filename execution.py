# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#set "1" as content of ini.txt file
import os
import pyscreenshot


path = 'pictures/' 
number = len( os.listdir(path) )#number of pictures
strNum = str(number) #number of pictures in string format

a = [1360, 0, 3300, 1100] # size of the screenshot window
pic = pyscreenshot.grab(a) #grab a screenshot
#pic.show() #show a screenshot if "#" removed

base = '000' #name and number of the screenshot file

t = len(strNum) 
base = ''.join([base[:-t], strNum]) #name and number of the screenshot file

number =  int(strNum) + 1 # increase number of the screenshot file
strNum = str(number )

print(base)

Path = path + 'picture_' + base + '.png'
pic.save(Path)