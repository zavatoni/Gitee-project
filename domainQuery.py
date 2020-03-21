#!/usr/bin/python3
import urllib.request
req = urllib.request.urlopen('http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=doucube.com')
# print(req.read().decode())
with open("request.log","a") as code:
    code.write(req.read().decode())

with open("request.log","r") as brows:
    for brs in brows.readline():
        print(brs)
req_bd = urllib.request.urlopen('http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=baidu.com')
print(req_bd.read().decode())
