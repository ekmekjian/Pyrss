import feedparser
import time
import sys

filename = "source.txt"
class NODE:
  def __init__(self,title=None,link=None,pubDate=None,desc=None,id=None,next=None):
    self.title = title
    self.link=link
    self.pubDate = pubDate
    self.desc = desc
    self.id = id
    self.next = next
  def FillNode(self,eedArticle):
    self.title = feedArticle.title
    self.link = feedArticle.link
    self.pubDate = feedArticle.published
    self.desc = feedArticle.summary
    self.id = feedArticle.id
    self.next = None

# Functions:
def checkList(list,article):
  while(list.next != None):
    if(list.id == articl.id):
      return False
  return True

def addToList(item,list):
  while(list.next != None):
    list = list.next
  list.next = item

# Read sources from txt file
def gatherSources():
  source =[]
  with open(filename,"r") as f:
     for line in f:
        source.append(line)
  return source     



# Go through each source to fill feed
def createFeed():
  start = NODE()
  add = NODE()
  sources = gatherSources()
  if start == None:
    #start list    
    for k in sources:
      e = feedparser.parse(k)
      for e in range(len(k.entries)):
         start.FillNode(k.entries[e])
  else:
    for k in sources:
      e = feedparser.parse(k)
      for i in range(len(e.entries)):
    # go through list check for existing articles
        found=checkList(start,e.entries[i]) 
    # if article is not in list add to list
        if(found==False):
          add.FillNode(e.entries[i])
          addToList(add,start) 
  return start



def displayFeed():
    display = NODE()
    display = createFeed()
    # display list format: title:desc:pubdate  
    while display.next != None:
        for i in range(len(display.entries)):
            print display.title
            print display.desc
            print display.pubDate
            display = display.next
         
  
if len(sys.argv) >1:
   writer = open(filename,"w")
   writer.write(sys.argv[1])
   writer.close()
    
 
 
displayFeed()
  
