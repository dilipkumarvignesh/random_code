import requests
import json
import facebook
import time
global token,graph

def init(app_token):
      global token
      token = app_token
   


def scheduled_post_feed(message,page_id,time):
     data={'message':message,'access_token':token,'published':'false','scheduled_publish_time':time}
     r=requests.post("https://graph.facebook.com/v2.5/"+str(page_id)+"/feed",data=data)
     print(r.content)

def publish_image(album_id,pic_name,**kwargs):
        send_data={'access_token':token}
        if kwargs is not None:
          send_data.update(kwargs)
           
        r=requests.post("https://graph.facebook.com/v2.5/"+str(album_id)+"/photos",files={'source':open(str(pic_name)+'.jpg','rb')},
                    data=send_data)
        return r.content
def publish_video(page_id,video_name,**kwargs):
    
    send_data={'access_token':token}
    if kwargs is not None:
          send_data.update(kwargs)
    r=requests.post("https://graph.facebook.com/v2.5/"+str(page_id)+"/videos",files={'source':open(str(video_name)+'.mp4','rb')},
                    data=send_data)
    
def get_time():
    print(time.time())

def get_arg(**kwargs):
      data={'com':'sap'}
      data.update(kwargs)
      print(data)
      if kwargs is not None:
            for key,value in kwargs.items():
                  print(key,value)
##get_time()

##init("CAACEdEose0cBAG11vHJclM9zL0g4uJOCs2RvvbHiYF3bKFfO9rZAyaDb3bSAyHZBgP3d1V9WjN12Ct07YNoZBKLAC7KaL4ZC76sr9lZBw0273DpbCRWKWziXEbRGJXYAUcxJYMqKNQYW8HxFCsCPVkF5zGeCwZCcAMazFeMhgQCI3niMUGpDW9sQNsuuyyChkZD")
##publish_video("212576309076214")
##init("CAACEdEose0cBAJRqgz1PWw7cG1P9Mp1yK1RENEX0WXQ6VA38j9XLxTGOkk3yI79maDpOxJNYqvMFlljT4LAU7fZC6HI1HZBzGfhoudZAF3YJQODCQieL8d9ZCx1iYhKAYEBdRIJuU3ZAexn2L3wkZAol5j2o9yJdJR7cgowVPOm5ZCsYZBCYUfnVxoPrLH5Vn5489Ow1pZBvTWAZDZD")
##scheduled_post_feed("hello world12345",
##          "212576309076214","1451649999")
##publish_image("956517104422039","1451608200")


