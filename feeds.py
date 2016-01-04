import facebook
import urllib
import json
import re


def init(token):
    global graph
    graph=facebook.GraphAPI(token)

def get_feeds(id):
    id=str(id)
    id+="/feed?limit=100"
    feeds=graph.get_object(id)
    data=feeds["data"]
    feed_count = len(data)
    print(feed_count)
    i=0
    while i<feed_count:

            if 'message' in data[i]:
                story=data[i]["message"]
                if len(story)>100:
                    story=story.encode("utf-8",errors='replace')
                    story_name = story.decode().split("\n")[0]
                    story_name=re.sub('[^A-Za-z0-9 ]+', '', story_name)
                    if(len(story_name)>64):
                        story_name=story_name[0:63]
                    story_name+='.txt'    
                    print(story_name)
                
                    f=open(story_name,"wb")
                    f.write(story)
                    f.close()
                
            i=i+1   
           
            if i%100 == 0:

            
                    next = urllib.request.urlopen(feeds['paging']['next'])
 
                    feeds=next.read().decode("utf-8")
 
                    feeds=json.loads(feeds)
                    data=feeds["data"]
                    i=0
        
        


