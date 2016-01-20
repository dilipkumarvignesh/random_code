import scheduled_feed


folk_mumbai={'page_id':'821610684579349','album_id':'956517104422039',
             'token':'CAACEdEose0cBAF4CRQGsTCFHksZBRN5cnYJEuCCO2r4YGHlEeZByijwZA3QyygDf0iZBPGRewIZBxhy8i3omNcOJOLofjmjvOO5rRurpVmImZCpU593VtHd9ILSLJZAuziNp3VC5vjyL1wYC2z4VTdy5BbpNZCZBZCLuRRZCZAH1S4iEWaKRs838nBOPBDY53HCHz1nqVLBGQliaNwZDZD'}
hkm_mumbai={'page_id':'1518083865176416','album_id':'1518137061837763',
            'token':'CAACEdEose0cBAO7V96vcKuotZB5cZAQH0CQNbcdBAxXSmfGK1Dg5B3QvfjhKbDUOMF5uW0lPJnsRwZBUZAZBXsQ2p0KTPTbx9zpHZAUI5i1DZCQmmpNr9mcXcZCCYgr0xOPpFZCjkoWZBboDCd0EABgZB7pZCsWYDPfefl8q1Eus6FuGnLnpPbsqbrZB80Pv529bPB7tqpZCeS6OzbtQZDZD'}



scheduled_feed.init(hkm_mumbai['token'])
scheduled_feed.publish_image(hkm_mumbai['album_id'],'deities/IMG-20151022-WA0009')
