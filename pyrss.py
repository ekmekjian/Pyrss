#!/usr/bin/env python

# Main steps:
# 1) Create a main loop for the program - done
# 2) Utilize the time function to update feed - done
# 3) Test with more sources - done
# 4) Create check methods to allow for more arguments-done
#    A) Allow the ability to add sources through argument - to be tested-done
# Project marked completed 6/10/2019
# Next steps:
#pressing 's' to search for titles for keywords
import threading
import sys
import os
import feedparser,colorama
import feeds
filename = "source.txt"

flag=''
if len(sys.argv) >1:
  flag = sys.argv[1]
  if(flag=='-s'):
     keyword=sys.argv[2:]
  if(flag=='-a'):
    feeds.enterSource(sys.argv[2],filename)    

feed =feeds.gatherSources(filename)
 
 #Redo main loop
def mainLoop():
  feeds.feedloop(flag,)
mainLoop()

