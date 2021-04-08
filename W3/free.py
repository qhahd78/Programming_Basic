import twitter 

CONSUMER_KEY = 'tlHsPFW8ifNQwNLnZbima2A7Q'
CONSUMER_SECRET = '7qguxqu0n15B3ww9DwA8FpRoFAoMhLL8q7oCgAbkhcMtsMG3fq'
ACCESS_KEY = '1375338044438454275-AibAPxMFSZBaCUzzYrY8ZzsP1yVK7w'
ACCESS_SECRET = '6YROC0hu4w2TDij58guJtgs5SxRiLfbQ2BgcOZSi1ni71'

twitter_api = twitter.Api(consumer_key=CONSUMER_KEY,
                            consumer_secret=CONSUMER_SECRET,
                            access_token_key=ACCESS_KEY,
                            access_token_secret=ACCESS_SECRET)
                    
account = "@BTS_twt"
statuses = twitter_api.GetUserTimeline(screen_name=account, count= 10, include_rts=False, exclude_replies=False)

for status in statuses: 
    print(status.text)