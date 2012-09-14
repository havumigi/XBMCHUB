import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,base64,datetime


#Global Constants
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

def CATEGORIES():
        url= 'http://www.filmon.com/'        
        req = urllib2.Request(url)
        req.add_header('User-Agent', USER_AGENT)
        response = urllib2.urlopen(req)
        link1=response.read()
        response.close()  
        link=str(link1).replace('\n','')      
        match=re.compile('alt="(.+?)" src=".+?" class=".+?" /><strong class=".+?" style="text-overflow: ellipsis"><a href="/channel/(.+?)"').findall(link)
        for iconimage, name in match:
            iconimage = str(iconimage).replace('logo.png','big_logo.png')
            url = 'http://www.filmon.com/channel/'+name
            addDir(name,url,1,iconimage)
        
            
            
                      
def FilmOn(url,iconimage,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', USER_AGENT)
        response = urllib2.urlopen(req)
        link1=response.read()
        response.close()  
        link=str(link1).replace('\n','')      
        match=re.compile('"name":"(.+?)".+?"quality":"360p".+?"url":"(.+?)}]').findall(link)
        for playPath, a in match:
            url1=str(a).replace('\\','')
            url2=str(a).replace('\\','').replace('"','')
            regex = re.compile('rtmp://(.+?)/(.+?)/(.+?)id=([a-f0-9]*?)"')
            match1 = regex.search(url1)
            app = '%s/%sid=%s' %(match1.group(2), match1.group(3),match1.group(4))
            tcUrl=str(url2)
            swfUrl= 'http://www.filmon.com/tv/modules/FilmOnTV/files/flashapp/filmon/FilmonPlayer.swf'
            pageUrl = 'http://www.filmon.com/'
            url= str(url2)+' playpath='+str(playPath)+' app='+str(app)+' swfUrl='+str(swfUrl)+' tcUrl='+str(tcUrl)+' pageurl='+str(pageUrl)
            print playPath
            print 'hello this below is the app'         
            print app
            print 'hello this below is the tcurl'         
            print tcUrl          
            addLink(name,url,playPath,app,pageUrl,swfUrl,tcUrl)
                                                                
 
 
    
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

        
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name} )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
                
def addLink(name,url,playPath,app,pageUrl,swfUrl,tcUrl):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable","true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok 
                      
               
params=get_params()
url=None
name=None
mode=None
iconimage=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
                   

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
   
        

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        print ""+url
        FilmOn(url,iconimage,name)
        

       
xbmcplugin.endOfDirectory(int(sys.argv[1]))
