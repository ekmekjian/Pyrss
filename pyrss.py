import feedparser
import time
import sys

filename = "source.txt"
class NODE:
  def FillNode(feedArticle):
    self.title = title
    self.link = link
    self.pubDate = pubDate
    self.desc = desc
    self.next = None
      
# Functions:
# Read sources from txt file
def gatherSources(source):
  with open(filename,"r") as f:
     for line in f:
        source.append(line)
  return sour     
# Go through each source to fill feed
def createFeed(sources,head):
  start = NODE()
  if start.head == None:
    #start list    
    for k in sources:
      e = feedparser.parse(k)
      for e in range(len(k.entries)):
         start.FillNode(k.entries[e])
         
 # else:
    # go through list check for existing articles
    # if article is not in list add to list
    # display list format: title:desc:pubdate  
  
# Check periodically for old articles
def displayFeed(head):
    display = head
    createFeed(filename,display)
    while display.next != Null:
        for i in range(len(display.entries)):
            print display.title
            print display.desc
            print display.pubDate
            display = display.next
         
  
if len(sys.argv) >1:
   writer = open(filename,"w")
   writer.write(sys.argv[1])
   writer.close()
    
uInput = 'a'
start = NODE()
while uInput !='q':
  displayFeed(start)
  uInput = input()    
  
