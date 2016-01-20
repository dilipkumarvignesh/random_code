import class_scheduled
import glob
import os
import time
import logging
import re
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')


folk_mumbai={'page_id':'821610684579349','album_id':'956517104422039',
             'token':'CAACEdEose0cBAF4CRQGsTCFHksZBRN5cnYJEuCCO2r4YGHlEeZByijwZA3QyygDf0iZBPGRewIZBxhy8i3omNcOJOLofjmjvOO5rRurpVmImZCpU593VtHd9ILSLJZAuziNp3VC5vjyL1wYC2z4VTdy5BbpNZCZBZCLuRRZCZAH1S4iEWaKRs838nBOPBDY53HCHz1nqVLBGQliaNwZDZD'}
hkm_mumbai={'page_id':'1518083865176416','album_id':'1518137061837763',
            'token':'CAACEdEose0cBAO7V96vcKuotZB5cZAQH0CQNbcdBAxXSmfGK1Dg5B3QvfjhKbDUOMF5uW0lPJnsRwZBUZAZBXsQ2p0KTPTbx9zpHZAUI5i1DZCQmmpNr9mcXcZCCYgr0xOPpFZCjkoWZBboDCd0EABgZB7pZCsWYDPfefl8q1Eus6FuGnLnpPbsqbrZB80Pv529bPB7tqpZCeS6OzbtQZDZD'}

testing={'token':'CAACEdEose0cBAFSyVYumkHtjIXauin4KLFe6yh439Uyu7yukjA37gr3lFNC85FznWAxZC9ZA3f38IAVEqj0tFenyiWywcAD9rfbAFqHyBwxVB0rFrv4bZAnULTOikPZCC9bnuuTApQdnZCqgKX9GIdteZC9PLWaGUveqV13FsDzuEZByo2IR0Tx2AVZCoFiEkcQZD'
         ,'album_id':'213424558991389'}

folk_instance=class_scheduled.fb_auto(folk_mumbai['token'])

test_instance=class_scheduled.fb_auto(testing['token'])

hkm_instance=class_scheduled.fb_auto(hkm_mumbai['token'])

##result=folk_instance.publish_image(folk_mumbai['album_id'],'C:\\Users\\I308830\\Documents\\darshan_pic.jpg',message="Today\'s darshan of Sri Sri Radha Krishna Chandra at ISKCON Bangalore")

##result=hkm_instance.publish_image(hkm_mumbai['album_id'],'C:\\Users\\I308830\\Documents\\darshan_pic.jpg',message="Today\'s darshan of Sri Sri Radha Krishna Chandra at ISKCON Bangalore")
##print(result)

def full_publish(get_time):
    images = glob.glob("C:\\Users\\I308830\\Desktop\\deity\\HKM-VRI1\\*.jpg")
    send_time=get_time   
    
    for image in images:
        
        result=hkm_instance.publish_image(hkm_mumbai['album_id'],image,published="false",scheduled_publish_time=str(send_time))
        print(result)
        send_time+=86400
        
def publish_videos(get_time):
    p=re.compile('[^0-9]')
    
    videos=glob.glob("C:\\Users\\I308830\\Desktop\\AAP\\*.mp4")
    time_send=get_time
    for video in videos:
        videos_name=video.split("\\")[5]
        video_final_name=videos_name.split("-")[0]
        video_extracted = " ".join(re.findall("[a-zA-Z]+", video_final_name))        
        logging.debug(video_extracted)
        result=folk_instance.publish_video(folk_mumbai['page_id'],video,description=video_extracted,title=video_extracted,published="false",scheduled_publish_time=str(time_send))        
        time_send=time_send+86400
        logging.info(result)
    

publish_videos(1453260600)
