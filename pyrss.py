import feedparser
import time
import sys

filename = "source.txt"
sources = []
class NODE:
   def __init__(self, title, link, pubDate, desc):
    self.title = title
    self.link = link
    self.pubDate = pubDate
    self.desc = desc
    self.lifeT = 
    self.next = None
      
class feed:
  def __init__(self):
    self.head = None
# Functions:
# Read sources from txt file
with open(filename,"r") as f:
   for line in f:
      sources.append(line)     
# Go through each source to fill feed
# Check periodically for old articles
def displayFeed():
  start = feed()
  if start.head == None:
    #start list
  else:
    # go through list check for existing articles
    # if article is not in list add to list
    # display list format: title:desc:pubdate  
  
if len(sys.argv) >1:
   writer = open(filename,"w")
   writer.write(sys.argv[1])
   # add link to list
   
while uInput !='q':
  displayFeed()
  
  
