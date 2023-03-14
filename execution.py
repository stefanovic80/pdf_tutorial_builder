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

fileName = "latexScriptsToIncude_images/picture_" + base + ".tex"

f = open(fileName, "w")

text1 = '\\begin{figure}[h!]\t\t\n\t\\centering\n   \t\\includegraphics[width=8.0in]{pictures/picture_'
text3 = '.png}\n  \t\\caption{Software}\n   \t\\label{fig:graficoST_unAcce}\n\\end{figure}'

totalText = text1 + base + text3

u = f.write(totalText)

f.close()