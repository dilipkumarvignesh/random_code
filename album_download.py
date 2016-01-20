import facebook
import requests
import urllib
import json
import codecs
import logging
import re
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
##graph = facebook.GraphAPI("CAACEdEose0cBADHsEfZAG3KUj7R9mSgtMk1bZCcsYD13TuGYS6mYPom5pGNC3r0LWtLw9eOZBIqXa07BFfvZCa5aGSZCk0hMv5j62HZACUCZAHdZC0canPqpbCEe8MZCtgYoorW3gQyPBqZBmJUDh7ouwsqt6JnroVsfN4E8XwCxQ3ZAqSSTuEfyL4iMaa8xbHHhsWpNYb5o0N6ahSOf1H85KAB")
##images=graph.get_object('253316558119988')
i=0

##with open('2.json') as data_file:
##    images=json.load(data_file)
#data = json.load(codecs.open('2.json', 'r', 'utf-8-sig'))
##json_data = open('9.json','r')
##data = json.load(json_data)
##print(data)

album=urllib.request.urlopen("https://graph.facebook.com/v2.5/143920112308030/albums?limit=100&access_token=CAACEdEose0cBAOFwcTAwlPb8ZALlCoZCGiY1XL5RgZBw4M86hrNlE4VGTlTfIZAoseBdGbZAIZB2izZCGIq0yUKylLat4ODIgTgHuCozWZAwj0PXH0oo4F1tPm9cNtj0ZCJ8vHhDXe8APbArujwnrcf18IEfuHRgFevUZCPqq0HT1yZAEWO6WvWhWBETPDol5aKNva7fucwnOiDjs5C6ZCDXkVkE")
json_album=json.loads(album.read().decode('utf-8'))
print(json_album)
alb_cnt=0
for album in json_album['data']:
      
          alb_cnt+=1
          if re.search('Darshan',album['name']) is not None:
            logging.debug((album['name']))
            response=urllib.request.urlopen("https://graph.facebook.com/v2.5/"+album['id']+"/photos?fields=images&limit=100&access_token=CAACEdEose0cBAOFwcTAwlPb8ZALlCoZCGiY1XL5RgZBw4M86hrNlE4VGTlTfIZAoseBdGbZAIZB2izZCGIq0yUKylLat4ODIgTgHuCozWZAwj0PXH0oo4F1tPm9cNtj0ZCJ8vHhDXe8APbArujwnrcf18IEfuHRgFevUZCPqq0HT1yZAEWO6WvWhWBETPDol5aKNva7fucwnOiDjs5C6ZCDXkVkE")
            json_data = json.loads(response.read().decode('utf-8'))
            images=response.read()
            images=json_data

           

            for image in images["data"]:
                url=image["images"][0]["source"]
                
                response=urllib.request.urlopen(url)
                data=response.read()
                
                i=i+1   
                
                filename=str(i)+".jpg"
                f=open("C:\\Users\\I308830\\HKM-ISK1\\ISK1"+filename,'wb')
                f.write(data)
                if i%100 == 0:
                    next1=urllib.request.urlopen(images['paging']['next'])
                    data=next1.read().decode("utf-8")
                    images=json.loads(data)
          if alb_cnt%25 == 0:
                next1=urllib.request.urlopen(json_album["paging"]["next"])
                logging.debug(next1)    
                data=next1.read().decode("utf-8")
                json_album=json.loads(data)
    
##print(images["data"]["paging"])
##      
