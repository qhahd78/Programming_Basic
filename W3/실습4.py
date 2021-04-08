import tweepy
import time
import urllib

# 트위피 라이브러리를 사용하여 트위터에 메세지 전송하는 함수

print("의용메카트로닉스공학과 20195277 하유민")
text= "하유민 20195277"


def send_to_twitter(msg):
    CONSUMER_KEY = 'tlHsPFW8ifNQwNLnZbima2A7Q'
    CONSUMER_SECRET = '7qguxqu0n15B3ww9DwA8FpRoFAoMhLL8q7oCgAbkhcMtsMG3fq'
    ACCESS_KEY = '1375338044438454275-AibAPxMFSZBaCUzzYrY8ZzsP1yVK7w'
    ACCESS_SECRET = '6YROC0hu4w2TDij58guJtgs5SxRiLfbQ2BgcOZSi1ni71'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(msg)


def get_price():
    return (text)


price_now = input("Do you want to see the price now (Y/N)? ")

if price_now == "Y":
    msg = text
    send_to_twitter(msg)
else:
    msg = text
    send_to_twitter(msg)
