import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,base64,datetime


#Global Constants
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

def CATEGORIES():
        addDir('FilmOn Without Epg','http://www.filmon.com/',1,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('FilmOn With Epg Main Channels','http://www.filmon.com/tvguide/',2,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')



def filmon_noepg(url):
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
            addDir(name,url,3,iconimage,'')
            xbmcplugin.setContent(int(sys.argv[1]), 'movies')
            xbmc.executebuiltin("Container.SetViewMode(503)")
            
def filmon_epg(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', USER_AGENT)
    response = urllib2.urlopen(req)
    link1=response.read()
    response.close()  
    link=str(link1).replace('\n','')      
    match=re.compile('<h3>(.+?)</h3>.+?</a>.+?<a  class="tooltipped"  href=".+?" >                <img src="(.+?)" />            </a>                            <div class="tooltip">.+?</div>                                                <h4>(.+?)</h4>            <div class="description">(.+?)</div>            <div class="channel-footer">                <a href="(.+?)">Watch now</a>').findall(link)
    for name, iconimage,  showname, description, url1 in match:
        cleandesc=str(description).replace('",','').replace('                ','').replace('<a class="read-more" href="/tvguide/','').replace('">Read more... &rarr;</a>','')
        description = '[B]%s [/B]\n\n%s' % (showname,cleandesc)
        url = 'http://www.filmon.com'+str(url1)
        addDir(name,url,3,iconimage,description)
        xbmcplugin.setContent(int(sys.argv[1]), 'movies')
        xbmc.executebuiltin("Container.SetViewMode(503)")

                      
def FilmOn(url,iconimage,description):
        req = urllib2.Request(url)
        req.add_header('User-Agent', USER_AGENT)
        response = urllib2.urlopen(req)
        link1=response.read()
        response.close()  
        link=str(link1).replace('\n','')      
        match=re.compile('"name":"(.+?)".+?"quality":"(.+?)".+?"url":"(.+?)}').findall(link)
        for playPath, name, a in match:
            url1=str(a).replace('\\','')
            url2=str(a).replace('\\','').replace('"','')
            regex = re.compile('rtmp://(.+?)/(.+?)/(.+?)id=([a-f0-9]*?)"')
            match1 = regex.search(url1)
            app = '%s/%sid=%s' %(match1.group(2), match1.group(3),match1.group(4))
            tcUrl=str(url2)
            swfUrl= 'http://www.filmon.com/tv/modules/FilmOnTV/files/flashapp/filmon/FilmonPlayer.swf'
            pageUrl = 'http://www.filmon.com/'
            url= str(url2)+' playpath='+str(playPath)+' app='+str(app)+' swfUrl='+str(swfUrl)+' tcUrl='+str(tcUrl)+' pageurl='+str(pageUrl)
            xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
            addLink(name,url,playPath,app,pageUrl,swfUrl,tcUrl)
            xbmcplugin.setContent(int(sys.argv[1]), 'movies')
            xbmc.executebuiltin("Container.SetViewMode(503)")
 
 
    
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

        
def addDir(name,url,mode,iconimage,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description} )
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
description=None

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
try:        
        description=int(params["description"])
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
        filmon_noepg(url)
        
elif mode==2:
        print ""+url
        filmon_epg(url)

elif mode==3:
        print ""+url
        FilmOn(url,iconimage,description)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
