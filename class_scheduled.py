import requests
import json
import facebook
import time
global token,graph
import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
class fb_auto:
      
      def __init__(self,app_token):
            self.token=app_token

         
      def scheduled_post_feed(self,message,page_id,time):
           data={'message':message,'access_token':self.token,'published':'false','scheduled_publish_time':time}
           r=requests.post("https://graph.facebook.com/v2.5/"+str(page_id)+"/feed",data=data)
           print(r.content)

      def publish_image(self,album_id,pic_name,**kwargs):
              send_data={'access_token':self.token}
              if kwargs is not None:
                send_data.update(kwargs)
                print(send_data)
              r=requests.post("https://graph.facebook.com/v2.5/"+str(album_id)+"/photos",files={'source':open(str(pic_name),'rb')},
                          data=send_data)
              
              return r.content
      def publish_video(self,page_id,video_name,**kwargs):
          logging.debug(video_name)
          send_data={'access_token':self.token}
          if kwargs is not None:
                send_data.update(kwargs)
          logging.debug(send_data)
          r=requests.post("https://graph.facebook.com/v2.5/"+str(page_id)+"/videos",files={'source':open(str(video_name),'rb')},
                          data=send_data)
          
          return r.content


