#!/usr/bin/env python

# Main steps:
# 1) Create a main loop for the program - done
# 2) Utilize the time function to update feed - done
# 3) Test with more sources - done
# 4) Create check methods to allow for more arguments-done
#    A) Allow the ability to add sources through argument - to be tested-done
# Project marked completed 6/10/2019
# Next steps:
# 1) Allow for user intput while program runs for the following;
#      pressing 'q' for quitting
#      pressing 's' to search for titles for keywords
#      pressing 'r' to reload feed
import threading
import sys
import os
import feeds
filename = "source.txt"
#adding one or more source to source.txt

def userinput(choice):
    choice = input('>')
    return choice    

 #Check for tags from argument
 #if S iniate search feed
     #searches for title that matches keyword
if len(sys.argv) >1:
  feeds.enterSource(sys.argv,filename)    

feed = gatherSources(filename)
 
 #Redo main loop
def mainLoop():
    #check for userinput during script running
    #if s initate searchloop
    #if r refresh feed
    #if q quit the program
    choice=''
    while choice != 'q':
        if(choice=='s'):
            feeds.search(input('Enter keyword: '),filename)
        inputthread=thread.start_new_thread(target=userinput,(choice,))
        inputthread.daemon=True 
        feedloop()
        inputthread.start()
    sys.exit()
mainLoop()
