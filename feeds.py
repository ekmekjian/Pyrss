import feedparser
import time
import sys
import os
import colorama
from colorama import Style,Back,Fore


def enterSource(argu,filename):
  f = open(filename,"a+")
  if len(argu)>2:
    
    for i in range(1,len(argu)):
      f.write(argu[i]+"\n")
  else:
    f.write(argu[1]+"\n")
# Read sources from txt file
def gatherSources(filename):
  source =[]
  with open(filename,"r") as f:
     for line in f:
       source.append(line.rstrip())
  return source     


def search(keyword,sources):
  print("\n"*25)
  print(" "*50+"|")
  print(" "*50+"v")
  print("\n"+" "*45+"Scroll Down")
  print("\n"*10)
  os.system('clear')
  for url in sources:
    e  = feedparser.parse(url)
  for article in range(len(e)):
    if(e.entries[article].title.lower().find(keyword)!=-1):
          print (Fore.WHITE+Style.NORMAL,e.entries[article].title)
          print ("--")
          print (Fore.BLUE+Style.NORMAL,e.entries[article].description)
          print ("--")
          print (Style.DIM,e.entries[article].published)
          print ("--")
          print (e.entries[article].link)
          print ("--------------------------------------------------------------------------------")
  print("End of results")
def displayloop(sources):
  print("\n"*25)
  print(" "*50+"|")
  print(" "*50+"v")
  print("\n"+" "*45+"Scroll Down")
  print("\n"*10)
  for url in sources:
    e  = feedparser.parse(url)
    os.system('clear')
    for article in range(len(e)):
      print (Fore.WHITE+Style.NORMAL,e.entries[article].title)
      print ("--")
      print (Fore.BLUE+Style.NORMAL,e.entries[article].description)
      print ("--")
      print (Style.DIM,e.entries[article].published)
      print ("--")
      print (e.entries[article].link)
      print ("--------------------------------------------------------------------------------")
def feedloop(flag,feed,keyword=None):
  if keyword == None:
    displayloop(feed)
  else:
    search(keyword,feed)
 
