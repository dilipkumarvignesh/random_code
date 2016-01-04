import facebook
import requests
import urllib
import json
import codecs
graph = facebook.GraphAPI("")
images=graph.get_object('')
i=0

##with open('2.json') as data_file:
##    images=json.load(data_file)
#data = json.load(codecs.open('2.json', 'r', 'utf-8-sig'))
##json_data = open('9.json','r')
##data = json.load(json_data)
##print(data)
##response=urllib.request.urlopen("https://graph.facebook.com/v2.0/713365788733305/photos?access_token=CAACEdEose0cBAOCOsf4UVzbzEIrxkIHZBZCsnf3m8aFYLbfNONmdikd9NGKhqHB5IVCZCNdCotPVYGjpMaW91e8XAc2uZCyEjHLCkPRZApqznhtmzpeWCvVFQrH8OalUPnCxUSKPPntZCXOHU2WDKC0LTxZBtfXZCKcf0QXPbcPlkViUop7ckZCCCjPyvqaKeOvMokpASGfZAcKIZAtIG3Ek6Cd&limit=1&after=OTM1NjcwMzI5ODM2MTgy")
##json_data = json.loads(response.read().decode('utf-8'))
##images=response.read()
##print(json_data)
print(images["paging"]['next'])


#print(next.read())
for image in images["data"]:
    url=image["images"][0]["source"]
    
    response=urllib.request.urlopen(url)
    data=response.read()
    
    i=i+1
    
    filename=str(i)+".jpg"
    f=open(filename,'wb')
    f.write(data)
   if i%100 = 0:
        next=urllib.request.urlopen(images['paging']['next'])
        data=next.read().decode("utf-8")
        images=json.loads(data)
    
    
##print(images["data"]["paging"])
      
