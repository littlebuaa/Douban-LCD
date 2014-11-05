#!/usr/bin/env python
#coding=utf8


import json
import urllib2
import urllib
import subprocess
import time

class Douban(object):


        def __init__(self,email,psword):
                '''Create the login object'''
                
                self.url='http://www.douban.com/j/app/login' 
                self.post_data = {
                        'app_name' : 'radio_desktop_win',
                        'version' : 100,
                        'email' : email, #'lituobuaa@126.com'
                        'password' : psword  #'35022426abcd',
                                }
                self.resLogin={}
        # create Post Data.
        def login(self):
                
                post_data = urllib.urlencode(self.post_data)
                req = urllib2.Request(self.url, post_data)
                result = urllib2.urlopen(req)
                text = result.read()
                jsdata = json.loads(text)

                self.resLogin ={
                          'token': jsdata['token'],
                        'user_id':jsdata['user_id'],
                        'expire' :jsdata['expire']
                        }
                print jsdata['user_id']
                print "Get the Token"

        #x = [token,user_id,expire]

        def getSong(self,nbChannel,listype):                

                # nbChannel is No. of FM Channel,eg, -3 is personel channel.
                # listype is a char, eg 'n' represents a new list

                For_song = {
                'app_name' : 'radio_desktop_win',
                'version' : '100',
                'channel': nbChannel,
                'type': listype
                }
                newPost = self.resLogin.copy()
                newPost.update(For_song)
                
                url = 'http://www.douban.com/j/app/radio/people'
                post_data = urllib.urlencode(newPost)
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

                return content 


#Player = subprocess.Popen(['mpg123','-C','-@',"song.txt"],stdout= subprocess.PIPE)
#Radio = subprocess.Popen(['sudo','PiFM/pifm','-','88.9','22050'],stdin = Player.stdout)
#Player = subprocess.Popen(['mpg123','-C','-@',"song.txt"])
#time.sleep(content[0]['length'])
#Player.kill()
#Radio.kill()


