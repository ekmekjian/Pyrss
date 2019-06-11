!#./usr/bin/env python

# Next steps:
# 1) Create a main loop for the program - done
# 2) Utilize the time function to update feed - done
# 3) Test with more sources - done
# 4) Create check methods to allow for more arguments-done
#    A) Allow the ability to add sources through argument - to be tested-done
# Project marked completed 6/10/2019

import feedparser
import time
import sys
import os
import colorama
from colorama import Style,Back,Fore
filename = "source.txt"
#adding one or more source to source.txt
def enterSource(argu):
  f = open(filename,"a+")
  if len(argu)>2:
    
    for i in range(1,len(argu)):
      f.write(argu[i]+"\n")
  else:
    f.write(argu[1]+"\n")
# Read sources from txt file
def gatherSources():
  source =[]
  with open(filename,"r") as f:
     for line in f:
       source.append(line.rstrip())
  return source     

def displayFeed(sources):
  for url in sources:
    e  = feedparser.parse(url)
    for article in range(len(e)):
      print Fore.WHITE+Style.NORMAL+e.entries[article].title
      print "--"
      print Fore.BLUE+Style.NORMAL+e.entries[article].description
      print "--"
      print Style.DIM+e.entries[article].published
      print "--"
      print e.entries[article].link
      print "--------------------------------------------------------------------------------"
  
if len(sys.argv) >1:
  enterSource(sys.argv)    
feed = gatherSources()
 
def mainLoop(): 
  while True:
    print("\n"*25)
    print(" "*50+"|")
    print(" "*50+"v")
    print("\n"+" "*45+"Scroll Down")
    print("\n"*10)
    os.system('clear')
    displayFeed(feed)
    time.sleep(360)
mainLoop()