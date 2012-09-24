import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,base64,datetime,os
import settings

from t0mm0.common.net import Net
from t0mm0.common.addon import Addon
net = Net()
ADDON = xbmcaddon.Addon(id='plugin.video.FilmOn')

#Global Constants
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
channel= 'http://www.filmon.com/channel/'
logo = 'http://static.filmon.com/couch/channels/'
res= settings.res()
addon = Addon('plugin.video.FilmOn', sys.argv)
datapath = addon.get_profile()
cookie_path = os.path.join(datapath, 'cookies')
net=Net()
loginurl = 'http://www.filmon.com/ajax/login'
email    =ADDON.getSetting('user')
password =ADDON.getSetting('pass')
data     = {'password': password,
                    'email': email,
                    'remember': 1}
headers  = {'Host':'www.filmon.com',
                    'Origin':'http://www.filmon.com',
                    'Referer':'http://www.filmon.com/user/login',
                        'X-Requested-With':'XMLHttpRequest'}
html = net.http_POST(loginurl, data, headers)
cookie_jar = os.path.join(cookie_path, "FilmOn.lwp")
if os.path.exists(cookie_path) == False:
    os.makedirs(cookie_path)
net.save_cookies(cookie_jar)

        
def CATEGORIES():
        if ADDON.getSetting('message') == 'false':
                xbmcgui.Dialog().ok('EasyNews Information','            For Full Support For This Plugin Please Visit','                    [COLOR yellow][B]WWW.XBMCHUB.COM[/B][/COLOR]','Please Turn Off Message in Addon Settings')
                xbmc.executebuiltin("XBMC.Container.Update(path,replace)")
                xbmc.executebuiltin("XBMC.ActivateWindow(Home)")
        addDir('My Recordings','http://www.filmon.com/my/recordings',5,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Live Now Epg Main Channels','http://www.filmon.com/tvguide/',1,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        url='http://www.filmon.com'
        req = urllib2.Request(url)
        req.add_header('User-Agent', USER_AGENT)
        response = urllib2.urlopen(req)
        link1=response.read()
        response.close()  
        link=str(link1).replace('\n','')      
        match=re.compile('class="header channel_group searchable" tags="(.+?)"><strong>(.+?)</strong></div>').findall(link)
        for url,  name in match:
            iconimage='http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png'
            addDir(name,url,3,iconimage,'')
            setView('movies', 'default') 
        
def Channels(url):
        url1= 'http://www.filmon.com'
        r='tags="%s (.+?)" id=".+?" ><img alt="(.+?)".+?<a href="(.+?)"'% str(url)
        req = urllib2.Request(url1)
        req.add_header('User-Agent', USER_AGENT)
        response = urllib2.urlopen(req)
        link1=response.read()
        response.close()  
        link=str(link1).replace('\n','')      
        match=re.compile(r).findall(link)
        for name, iconimage, url2 in match:
            iconimage = str(iconimage).replace('logo','big_logo')
            url = 'http://www.filmon.com'+str(url2)
            addDir(name,url,2,iconimage,'')
            xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
            setView('movies', 'default') 
            
            
     
def filmon_epg(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', USER_AGENT)
    response = urllib2.urlopen(req)
    link1=response.read()
    response.close()  
    link=str(link1).replace('\n','')      
    match=re.compile('bottom">(.+?)</h3>.+?href="(.+?)" >                <img src="(.+?)".+?.+?div class="title">.+?</div>.+?h4>(.+?)/h4>.+?"description">(.+?)/div>').findall(link)
    for name,  url1, iconimage, showname, description in match:
        cleandesc=str(description).replace('",','').replace('                ','').replace('<a class="read-more" href="/tvguide/','').replace('">Read more... &rarr;</a>','').replace('\xc3','').replace('\xa2','').replace('\xe2','').replace('\x82','').replace('\xac','').replace('\x84','').replace('\xa2s','').replace('\xc2','').replace('\x9d','').replace('<','')
        showname = str(showname).replace('<','')
        description = '[B]%s [/B]\n\n%s' % (showname,cleandesc)
        url = 'http://www.filmon.com'+str(url1)
        addDir(name,url,2,iconimage,description)
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
        setView('movies', 'epg') 
                      
def FilmOn(url,iconimage,description):
        dialog = xbmcgui.Dialog()
        if dialog.yesno("Tv Guide", "", "[B]Would You Like To See The Tv Guide?[/B]", '[B]Or Just Watch You Can Watch At Any Point In EPG[/B]', "WATCH", "GUIDE"): 
	        url= str(iconimage).replace('static.','').replace('couch/','').replace('channels/','tvguide/').replace('big_logo.png','')
	        req = urllib2.Request(url)
	        req.add_header('User-Agent', USER_AGENT)
	        response = urllib2.urlopen(req)
	        link1=response.read()
	        response.close()  
	        link=str(link1).replace('\n','').replace('\r','')       
	        match=re.compile('<div class="info">                        <h3>(.+?)</h3>                        <p>(.+?)/p>                    </div>                </li>                            <li class="clearfix">                                    <span class="time">                        Start:<br />                        (.+?)                        <br /><br />                        End:                        <br />                        (.+?)                    </span>').findall(link)
	        print match
	        for name, description,a,b in match:
	            a=str(a).replace('01:','1:').replace('02:','2:').replace('03:','3:').replace('04:','4:').replace('05:','5:').replace('06:','6:').replace('07:','7:').replace('08:','8:').replace('09:','9:')
	            a=str(a).replace('01:','1:').replace('02:','2:').replace('03:','3:').replace('04:','4:').replace('05:','5:').replace('06:','6:').replace('07:','7:').replace('08:','8:').replace('09:','9:')
	            description=str(description).replace('<','')
	            name='[%s-%s] %s' %(a,b,name)
	            url =str(url).replace('/tvguide/','/channel/')
	            addDir(name,url,2,iconimage,description)
	            setView('movies', 'epg') 
        else:
	        net.set_cookies(cookie_jar)
	        html = net.http_GET(url).content
	        link1 = html.encode('ascii', 'ignore')
	        link=str(link1).replace('\n','')
	        if ADDON.getSetting('res') == '1':
	                match=re.compile('"name":"(.+?)".+?"quality":".+?".+?"url":"(.+?)}').findall(link)
	                playPath=match[1][0]
	                a=match[1][1]
	                url1=str(a).replace('\\','')
	                url2=str(a).replace('\\','').replace('"','')
	                regex = re.compile('rtmp://(.+?)/(.+?)/(.+?)id=([a-f0-9]*?)"')
	                match1 = regex.search(url1)
	                iconimage=str(iconimage)
	                name ='360p'
	                app = '%s/%sid=%s' %(match1.group(2), match1.group(3),match1.group(4))
	                tcUrl=str(url2)
	                swfUrl= 'http://www.filmon.com/tv/modules/FilmOnTV/files/flashapp/filmon/FilmonPlayer.swf'
	                pageUrl = 'http://www.filmon.com/'
	                url= str(url2)+' playpath='+str(playPath)+' app='+str(app)+' swfUrl='+str(swfUrl)+' tcUrl='+str(tcUrl)+' pageurl='+str(pageUrl) 
	                xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(url)
	                xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
	                addLink(name,url,iconimage,playPath,app,pageUrl,swfUrl,tcUrl,description)
	                setView('movies', 'default') 
	        if ADDON.getSetting('res') == '2':
	                match=re.compile('"name":"(.+?)".+?"quality":"480p".+?"url":"(.+?)}').findall(link)
	                for playPath, a in match:
	                    url1=str(a).replace('\\','')
	                    url2=str(a).replace('\\','').replace('"','')
	                    regex = re.compile('rtmp://(.+?)/(.+?)/(.+?)id=([a-f0-9]*?)"')
	                    match1 = regex.search(url1)
	                    iconimage=str(iconimage)
	                    name ='480p'
	                    app = '%s/%sid=%s' %(match1.group(2), match1.group(3),match1.group(4))
	                    tcUrl=str(url2)
	                    swfUrl= 'http://www.filmon.com/tv/modules/FilmOnTV/files/flashapp/filmon/FilmonPlayer.swf'
	                    pageUrl = 'http://www.filmon.com/'
	                    url= str(url2)+' playpath='+str(playPath)+' app='+str(app)+' swfUrl='+str(swfUrl)+' tcUrl='+str(tcUrl)+' pageurl='+str(pageUrl)
	                    xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(url)
	                    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
	                    addLink(name,url,iconimage,playPath,app,pageUrl,swfUrl,tcUrl,description)
	                    setView('movies', 'default') 
	        if ADDON.getSetting('res') == '0':
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
	                    addLink(name,url,iconimage,playPath,app,pageUrl,swfUrl,tcUrl,description)
	                    setView('movies', 'default') 
                    
                    
def MyRecordings(url):
        net.set_cookies(cookie_jar)
        url='http://www.filmon.com/my/recordings'
        html = net.http_GET(url).content
        link = html.encode('ascii', 'ignore')
        match=re.compile('title":"(.+?)","id":".+?","channel_id":"(.+?)".+?"description":"(.+?)".+?"stream_name":"(.+?)","stream_url":"(.+?)}').findall(link)
        for name, channel, description, playPath, a in match:
            url1=str(a).replace('\\','')
            url2=str(a).replace('\\','').replace('"','')
            regex = re.compile('rtmp://(.+?)/(.+?)/(.+?)/(.+?)/(.+?)/(.+?)/(.+?)"')
            match1 = regex.search(url1)
            try:
	            app = '%s/%s/%s/%s/%s/%s' %(match1.group(2), match1.group(3),match1.group(4),match1.group(5),match1.group(6),match1.group(7))
            except:
            	pass
            tcUrl=str(url2)
            iconimage='https://static.filmon.com/couch/channels/%s/big_logo.png' % str(channel)
            swfUrl= 'http://www.filmon.com/tv/modules/FilmOnTV/files/flashapp/filmon/FilmonPlayer.swf'
            pageUrl = 'http://www.filmon.com/my/recordings'
            url= str(url2)+' playpath='+str(playPath)+' app='+str(app)+' swfUrl='+str(swfUrl)+' tcUrl='+str(tcUrl)+' pageurl='+str(pageUrl)
            xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
            addLink(name,url,iconimage,playPath,app,pageUrl,swfUrl,tcUrl,description)
            setView('movies', 'epg') 
    
        
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
                
def addLink(name,url,iconimage,playPath,app,pageUrl,swfUrl,tcUrl,description):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty("IsPlayable","true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok 
        
def setView(content, viewType):
        # set content type so library shows more views and info
        if content:
                xbmcplugin.setContent(int(sys.argv[1]), content)
        if ADDON.getSetting('auto-view') == 'true':
                xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )
                
        
                   

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
        filmon_epg(url)

elif mode==2:
        print ""+url
        FilmOn(url,iconimage,description)
        
elif mode==3:
        print ""+url
        Channels(url)
        
elif mode==4:
        print ""+url
        Channel_Lists(url)
        

        
elif mode==5:
        print ""+url
        MyRecordings(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
