from threading import Timer
from hashlib import md5
import urllib2
import re
import json

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'


user='mikenike@hotmail.co.uk'
password = md5("miniskirt").hexdigest()
nothin =''
keep_alive='http://www.filmon.com/api/keep-alive?session_key='
url= 'http://www.filmon.com/api/init/'
req = urllib2.Request(url)
req.add_header('User-Agent', USER_AGENT)
response = urllib2.urlopen(req)
link=response.read()
match= re.compile('"session_key":"(.+?)"').findall (link)
ses=match[0]
print 'THIS IS MD5'
print password


print nothin
print nothin
print 'THIS IS SESSION ID'
print ses
print nothin
print nothin

res='http://www.filmon.com/api/login?session_key=%s&login=%s&password=%s' % (ses,user,password)
req = urllib2.Request(res)
req.add_header('User-Agent', USER_AGENT)
response = urllib2.urlopen(req)
link=response.read()

print nothin
print nothin
print 'THIS IS GROUPS'
grp='http://www.filmon.com/api/groups?session_key=%s' % (ses)
req = urllib2.Request(grp)
req.add_header('User-Agent', USER_AGENT)
response = urllib2.urlopen(req)
link=response.read()
data = json.loads(link)
for field in data:
    print field["group_id"]


description='37'

print nothin
print nothin
print 'THIS IS Channels'
grp='http://www.filmon.com/api/group/%s?session_key=%s' % (description,ses)
req = urllib2.Request(grp)
req.add_header('User-Agent', USER_AGENT)
response = urllib2.urlopen(req)
link=response.read()
data = json.loads(link)
for field in data:
    print field["id"]
    print field["title"]
    print field["logo"]    


