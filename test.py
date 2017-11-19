import http.client
import urllib.parse
import json
import random

url = "localhost:8080" #The URL and port to test.
users = 400 #Total users to create on this thread.
repeats = 10000 #Total number of updates per user to send.

def openConnection(url):
    c = http.client.HTTPConnection(url)
    c.request("GET", "/connect")
    content = str(c.getresponse().read())
    content = content[31:-16]
    c.close()
    return content
    
def doRandomMove(token, url):
    params = urllib.parse.urlencode({'token': token, 'motion': random.randint(-10, 10)})
    c = http.client.HTTPConnection(url)
    c.request("POST", "/inform", params)
    content = str(c.getresponse().read())
    if("success" in content):
        print("YES: " + token)
    else:
        print("NO: " + token)
    c.close()
    return content
    

tokens = []

for i in range(users):
    tokens.append(openConnection(url))

while repeats>0:
    for token in tokens:
        doRandomMove(token, url)
    repeats-=1