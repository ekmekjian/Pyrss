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
import threading,sys,os,time,feedparser,colorama
import feeds
filename = "source.txt"
keyword = None
flag=''
if len(sys.argv) >1:
  flag = sys.argv[1]
  if(flag=='-s'):
     keyword=sys.argv[2:]
  if(flag=='-a'):
    feeds.enterSource(sys.argv[2],filename)    

feed =feeds.gatherSources(filename)
choice = ''
 #Redo main loop
def mainLoop():
  choice=''
  while choice !='q':
    if(keyword == None):
       fthread=threading.Thread(target=feeds.feedloop,args=(flag,feed,))
       fthread.daemon=True
       fthread.start()
    else:
       fthread=threading.Thread(target=feeds.feedloop,args=(flag,feed,keyword,))
       fthread.daemon=True
       fthread.start()
    time.sleep(1)
    choice=input('>')
mainLoop()

