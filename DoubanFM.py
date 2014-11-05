#!/usr/bin/env python
#coding=utf8


import json
import urllib2
import urllib
import subprocess
import time


url='http://www.douban.com/j/app/login'
post_data = {
'app_name' : 'radio_desktop_win',
'version' : 100,
'email' : 'lituobuaa@126.com',
'password' : '35022426abcd',
}
# create Post Data.

post_data = urllib.urlencode(post_data)
req = urllib2.Request(url, post_data)
result = urllib2.urlopen(req)
text = result.read()

jsdata = json.loads(text)

token = jsdata['token']
user_id = jsdata['user_id']
expire = jsdata['expire']

#x = [token,user_id,expire]


For_song = {
'app_name' : 'radio_desktop_win',
'version' : '100',
'user_id': user_id,
'token':token,
'expire' :expire,
'channel':'-3',
'type':'n',
    }

url = 'http://www.douban.com/j/app/radio/people'
post_data = urllib.urlencode(For_song)
url = url +'?'+ post_data
req = urllib2.Request(url)

result = urllib2.urlopen(req)
text = result.read()

jsdata = json.loads(text)

#print jsdata['err']
#print jsdata['song']  

content=jsdata['song']  
playlist = ''

for s in content:
        playlist = playlist  + s['url']+ "\n"
#print "字符串长度：",len(content) 
fp=open("song.txt","w")  

fp.write(playlist)  
fp.close()


Player = subprocess.Popen(['mpg123','-C','-@',"song.txt"],stdout= subprocess.PIPE)
Radio = subprocess.Popen(['sudo','PiFM/pifm','-','88.9','22050'],stdin = Player.stdout)
#Player = subprocess.Popen(['mpg123','-C','-@',"song.txt"])
time.sleep(content[0]['length'])
Player.kill()
Radio.kill()


