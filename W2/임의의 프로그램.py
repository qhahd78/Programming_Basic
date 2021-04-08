# 의용메카트로닉스공학과 20195277 하유민

print("의용메카트로닉스공학과 20195277 하유민")

import urllib.request

page = urllib.request.urlopen("https://www.yonhapnewstv.co.kr/news/MYH20210325005200038")
text= page.read().decode("utf8")

name = text.find("연합뉴스TV")
s = name
e = s + 1000
ff = text[s:e]

print(ff)
