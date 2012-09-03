import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,base64
import settings
from urlparse import urlparse

ADDON = settings.addon()
tvfs = settings.TV_FILESIZE()
mvfs = settings.MOVIE_FILESIZE()
tvfn = settings.TV_FILENAME()
mvfn = settings.MOVIE_FILENAME()
boost = settings.BOOST()
IMDBTV_WATCHLIST = settings.imdbtv_watchlist_url()


def CATEGORIES():
        addDir('Search Easy News','url',1,'','','','','')
        addDir('Movies','url',4,'','','','','')
        addDir('TV','url',5,'','','','','')
        addDir('Music','url',15,'','','','','')
        addDir('My IMDB Watch List','url',8,'','','','','')
        setView('movies', 'default-view') 
           
def MOVIE_CATEGORIES():
        addDir('Search Movies','url',6,'','','','','')
        addDir('New DVD Releases','http://www.lovefilm.com/browse/film/dvd/new-releases/films/?sort_by=release_date&rows=50',14,'','','','','')
        addDir('In Theatres','http://www.themoviedb.org/movie/now-playing',2,'','','','','')
        addDir('Top Movies','http://www.lovefilm.com/browse/film/dvd/films/?rows=50',14,'','','','','')
        addDir('Genres','url',21,'','','','','')
        addDir('<< Return To Main Menu','','','','','','','')    
        setView('movies', 'default-view')
            
def TOP_CATEGORIES():
        addDir('Action','http://www.lovefilm.com/browse/film/films/dvd/action/p1/?rows=50',14,'','','','','')
        addDir('Animated','http://www.lovefilm.com/browse/film/films/dvd/animated/p1/?rows=50',14,'','','','','')
        addDir('BollyWood','http://www.lovefilm.com/browse/film/films/dvd/bollywood/p1/?rows=50',14,'','','','','')
        addDir('Children','http://www.lovefilm.com/browse/film/films/dvd/childrens/p1/?rows=50',14,'','','','','')
        addDir('Comedy','http://www.lovefilm.com/browse/film/films/dvd/comedy/p1/?rows=50',14,'','','','','')
        addDir('Crime','http://www.lovefilm.com/browse/film/films/dvd/action/crime/p1/?rows=50',14,'','','','','')
        addDir('Drama','http://www.lovefilm.com/browse/film/films/dvd/drama/p1/?rows=50',14,'','','','','')
        addDir('Family','http://www.lovefilm.com/browse/film/films/dvd/family/p1/?rows=50',14,'','','','','')
        addDir('Historical','http://www.lovefilm.com/browse/film/films/dvd/action/historical/p1/?rows=50',14,'','','','','')
        addDir('Horror','http://www.lovefilm.com/browse/film/films/dvd/horror/p1/?rows=50',14,'','','','','')
        addDir('Musical','http://www.lovefilm.com/browse/film/films/dvd/music/p1/?rows=50',14,'','','','','')
        addDir('Romance','http://www.lovefilm.com/browse/film/films/dvd/romance/p1/?rows=50',14,'','','','','')
        addDir('Sci-Fi','http://www.lovefilm.com/browse/film/films/dvd/sci-fi/p1/?rows=50',14,'','','','','')
        addDir('Super Heroes','http://www.lovefilm.com/browse/film/films/dvd/music/p1/?rows=50',14,'','','','','')
        addDir('Thriller','http://www.lovefilm.com/browse/film/films/dvd/thriller/p1/?rows=50',14,'','','','','')
        addDir('War','http://www.lovefilm.com/browse/film/films/dvd/action/war/p1/?rows=50',14,'','','','','')
        addDir('<< Return To Movie Menu','url',4,'','','','','')    
        setView('movies', 'default-view')    
        
def TV_CATEGORIES():
        addDir('Search Tv Shows','url',12,'','','','','')
        addDir('Current Popular','http://www.imdb.com/search/title?num_votes=5000,&sort=moviemeter&title_type=tv_series',9,'','','','','')
        addDir('All Time Popular','http://www.imdb.com/search/title?num_votes=5000,&sort=user_rating&title_type=tv_series',9,'','','','','')
        addDir('A to Z','http://www.imdb.com/search/title?num_votes=5000,&sort=alpha,asc&start=&title_type=tv_series',9,'','','','','')
        addDir('<< Return To Main Menu','','','','','','','')    
        setView('movies', 'default-view')
        
def MUSIC_CATEGORIES():
        addDir('Search Music','url',16,'','','','','')
        addDir('BillBoard Album Charts','http://www.billboard.com/#/charts',22,'','','','','')
        addDir('HMV Best Selling','http://hmv.com/hmvweb/directQuery.do?pagingOptionSelect=%2Fhmvweb%2FdirectQuery.do%3FNo%3D0%26pagingOptionSelect%3D192%26N%3D1573%26adultFlag%3Dfalse%26rid%3D1394ED72CCC4',19,'','','','','')
        addDir('iTunes Charts','http://musicchartfeeds.com/itunes-rss/',17,'','','','','')
        addDir('<< Return To Main Menu','','','','','','','')    
        setView('movies', 'default-view') 
           
def SEARCH(url):
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, 'Search EasyNews...XBMCHUB.COM')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText() .replace(' ','+')  # sometimes you need to replace spaces with + or %20#
            if search_entered == None:
                return False          
        theurl = 'http://members-beta.easynews.com/global5/search.html?&gps='+search_entered+'&fex=&pby=1000&pno=1&s1=nsubject&s1d=-&s2=nrfile&s2d=-&s3=dsize&s3d=-&sS=5&d1t=&d2t=&b1t=&b2t=&px1t=&px2t=&fps1t=&fps2t=&bps1t=&bps2t=&hz1t=&hz2t=&rn1t=&rn2t=&fty[]=VIDEO&spamf=1&u=1&st=adv&safeO=0&boost=1&sb=1'
        username = ADDON.getSetting('easy_user')
        password = ADDON.getSetting('easy_pass')
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, theurl, username, password)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
        pagehandle = urllib2.urlopen(theurl)
        link= pagehandle.read()    
        match=re.compile('url="http://.+?-(.+?)" length="(.+?)" type="application/octet-stream" />\n<link>http.+?com/news/.+?/.+?/.+?/.+?/(.+?)</link>').findall(link)
        eng=''
        ger=''
        fre=''
        tur=''
        jap=''
        spa=''
        chi=''
        li=len(match)
        if re.search('alt=&#34;English', link, re.IGNORECASE):
                eng= ' English,'    
        if not re.search('alt=&#34;English', link, re.IGNORECASE):
                eng= ''          
        if re.search('alt=&#34;German', link, re.IGNORECASE):
                ger= 'German,' 
        if not re.search('alt=&#34;German', link, re.IGNORECASE):
                ger= ''          
        if re.search('alt=&#34;French', link, re.IGNORECASE):
                fre= 'French,'
        if not re.search('alt=&#34;French', link, re.IGNORECASE):
                fre= ''     
        if re.search('alt=&#34;Turkish', link, re.IGNORECASE):
                tur= 'Turkish,'
        if not re.search('alt=&#34;Turkish', link, re.IGNORECASE):
                tur= '' 
        if re.search('alt=&#34;Japanese', link, re.IGNORECASE):
                jap= 'Japanese,'
        if not re.search('alt=&#34;Japanese', link, re.IGNORECASE):
                jap= ''     
        if re.search('alt=&#34;Spanish', link, re.IGNORECASE):
                spa= 'Spanish,'
        if not re.search('alt=&#34;Spanish', link, re.IGNORECASE):
                spa= '' 
        if re.search('alt=&#34;Chinese', link, re.IGNORECASE):
                chi= 'Chinese,'
        if not re.search('alt=&#34;Chinese', link, re.IGNORECASE):
                chi= ''         
        all= '%s %s %s %s\n%s %s %s' % (eng,ger,chi,fre,jap,spa,tur)
        found='[B]%s  LINKS FOUND[/B]' % (li)
        xbmcgui.Dialog().ok(found,str(all))
        for url1 ,filesize, name in match:
            regex = re.compile("downloads.members.easynews.com/news/(.+?)/(.+?)/(.+?)/(.+?)/(.+?)")
            match = regex.search(url1)
            output = "downloads.members.easynews.com/news/%s/%s/%s/pr-%s/pr-%s" %(match.group(1), match.group(2), match.group(3), match.group(4), match.group(5))
            mkv=''
            avi=''
            vob=''
            mov=''
            mp4=''
            iso=''
            m4v=''
            if re.search('.mkv', name, re.IGNORECASE):
                    mkv= 'MKV'    
            if not re.search('.mkv', name, re.IGNORECASE):
                    mkv= ''          
            if re.search('.avi', name, re.IGNORECASE):
                    avi= 'AVI' 
            if not re.search('.avi', name, re.IGNORECASE):
                    avi= ''          
            if re.search('.vob', name, re.IGNORECASE):
                    vob= 'VOB'
            if not re.search('.vob', name, re.IGNORECASE):
                    vob= ''     
            if re.search('.mov', name, re.IGNORECASE):
                    mov= 'MOV'
            if not re.search('.mov', name, re.IGNORECASE):
                    mov= '' 
            if re.search('.mp4', name, re.IGNORECASE):
                    mp4= 'MP4'
            if not re.search('.mp4', name, re.IGNORECASE):
                    mp4= '' 
            if re.search('.iso', name, re.IGNORECASE):
                    iso= 'ISO'
            if not re.search('.iso', name, re.IGNORECASE):
                    iso= ''
            if re.search('.m4v', name, re.IGNORECASE):
                    iso= 'M4V'
            if not re.search('.iso', name, re.IGNORECASE):
                    iso= ''  
            all=str(mkv)+str(avi)+str(vob)+str(mov)+str(mp4)+str(iso)+str(m4v)
            name = '[[B]%s %s[/B]]' % (filesize,all)+'  '+str(name).replace('%20',' ').replace('%28','(').replace('%29',')').replace('.mkv','').replace('.avi','').replace('.iso','').replace('.mov','').replace('.mp4','').replace('.m4v','').replace('.vob','').replace('%5B','').replace('%5C','').replace('%5A','')
            changeboost4 = 'http://'+username+':'+password+'@' +boost
            url = str(changeboost4)+str(url1)
            iconimage = str(changeboost4)+str(output).replace('.avi','.jpg').replace('.mkv','.jpg') .replace('.wmv','.jpg').replace('.mov','.jpg').replace('.mpg', '.jpg').replace('.asf', '.jpg').replace('.mp4', '.jpg') .replace('.iso', '.jpg').replace('.rm', '.jpg').replace('.flv', '.jpg') 
            xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
            addLink(name,url,iconimage,fanart,series,description,rating)        
            setView('movies', 'easy-view')     
            
def IMDB_SEARCH(name, iconimage):
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, 'Search EasyNews...XBMCHUB.COM')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText() .replace(' ','+')  # sometimes you need to replace spaces with + or %20#
            if search_entered == None:
                return False   
        url= 'http://www.themoviedb.org/search/movie?query=%s&movie_page=&movie_collection_page=&person_page=&company_page=&keyword_page=&active=0'% (search_entered)           
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()      
        match=re.compile('title="(.+?)"><img class=".+?" src="(.+?)" width=".+?" height=".+?" /></a>').findall(link)
        for name, iconimage in match:
            name= str(name).replace('-',' ')
            iconimage= str(iconimage).replace('w92','original')
            addDir(name,url,3,iconimage,fanart,series,description,rating)
            setView('movies', 'movies-view')
                                                                
def TMDB(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('<img src="(.+?)" width=".+?" /></a>\n      </div>\n\n      <div class="info">\n        <h4><a href="(.+?)">(.+?)</a>').findall(link)
        nextp=re.compile(' <a href="(.+?)">Next').findall(link)
        try:
                nextp1=nextp[0]
        except:
                pass
        for iconimage, url1, name in match:
            url=url1
            name = str(name).replace('&hellip;','')
            iconimage = str(iconimage).replace('w92','original')
            addDir(name,url,3,iconimage,fanart,series,description,rating)
            setView('movies', 'default-view') 
        try:
                url=str(nextp1)
                name= 'Next Page >>'
                addDir(name,url,2,'','','','','')    
                setView('movies', 'movies-view') 
        except:
                pass
        addDir('<< Return To Movies Menu','url',4,'','','','','')    
        setView('movies', 'movies-view') 
             
def ONDVD(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link1=str(link).replace('\n','').replace('\t','')
        match=re.compile('<img ref=".+?" src="(.+?)".+?<div class="fl_detail_info"><h2><a href=".+?"title=".+?">(.+?)</a>.+?<div class="read_more">(.+?)<').findall(link1)
        nextp=re.compile('\n\n\n\n<li><a href="(.+?)"  >Next &gt;</a></li>\n\n\n\n\n\n\n').findall(link)
        try:
                nextp1=nextp[0]
        except:
                pass
        for iconimage, name, description in match:
            name = str(name).replace('/','').replace('-','').replace("'","").replace(",","").replace(",","").replace(" Extended Version","")
            iconimage = str(iconimage).replace('77x109.gif','lrg2.gif').replace('77x109','large')
            addDir(name,url,3,iconimage,fanart,series,description,rating)
            setView('movies', 'movies-view')
        try:
                url=str(nextp1)
                name= 'Next Page >>'
                addDir(name,url,14,'','','','','')    
                setView('movies', 'movies-view') 
        except:
                pass
        addDir('<< Return To Movies Menu','url',4,'','','','','')    
        setView('movies', 'movies-view') 
            
def ITUNES_MOVIES_CATEGORIES(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('src="(.+?)" width="113" height="170" alt=".+?"></a><h3><a href=".+?">(.+?)</a>').findall(link)
        for iconimage, name in match:
            iconimage=str(iconimage).replace('170x170','600x600')
            addDir(name,url,3,iconimage,fanart,series,description,rating)    
            setView('movies', 'default-view')    
            
                                              
def EasySearch(name,iconimage):
        search_entered = str(name).replace('.','').replace(', ','+').replace(' ','+') .replace(':','').replace('[','').replace(']',' ').replace('(The)','').replace('(','') .replace(')','') .replace('-','+').replace("'",'') .replace("&",'and').replace("!",'')      
        dialog = xbmcgui.Dialog()
        if dialog.yesno("Search Options", "Choose your required quality?", "Custom: Use your custom settings", "Any: Returns any available quality", mvfn, "Any"):
                theurl = 'http://members-beta.easynews.com/global5/search.html?&gps='+search_entered+'&fex=&pby=1000&pno=1&s1=nsubject&s1d=-&s2=nrfile&s2d=-&s3=dsize&s3d=-&sS=5&d1t=&d2t=&b1t='+mvfs+'&b2t=&px1t=&px2t=&fps1t=&fps2t=&bps1t=&bps2t=&hz1t=&hz2t=&rn1t=&rn2t=&fty[]=VIDEO&spamf=1&u=1&st=adv&safeO=0&boost=1&sb=1'
        else:
                theurl = 'http://members-beta.easynews.com/global5/search.html?&gps='+search_entered+'&fex='+mvfn+'&pby=1000&pno=1&s1=nsubject&s1d=-&s2=nrfile&s2d=-&s3=dsize&s3d=-&sS=5&d1t=&d2t=&b1t='+mvfs+'&b2t=&px1t=&px2t=&fps1t=&fps2t=&bps1t=&bps2t=&hz1t=&hz2t=&rn1t=&rn2t=&fty[]=VIDEO&spamf=1&u=1&st=adv&safeO=0&boost=1&sb=1'
        username = ADDON.getSetting('easy_user')
        password = ADDON.getSetting('easy_pass')
        print theurl
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, theurl, username, password)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
        pagehandle = urllib2.urlopen(theurl)
        link= pagehandle.read()      
        match=re.compile('url="http://.+?-(.+?)" length="(.+?)" type="application/octet-stream" />\n<link>http.+?com/news/.+?/.+?/.+?/.+?/(.+?)</link>').findall(link)
        eng=''
        ger=''
        fre=''
        tur=''
        jap=''
        spa=''
        chi=''
        li=len(match)
        if re.search('alt=&#34;English', link, re.IGNORECASE):
                eng= 'English,'    
        if not re.search('alt=&#34;English', link, re.IGNORECASE):
                eng= ''          
        if re.search('alt=&#34;German', link, re.IGNORECASE):
                ger= 'German,' 
        if not re.search('alt=&#34;German', link, re.IGNORECASE):
                ger= ''          
        if re.search('alt=&#34;French', link, re.IGNORECASE):
                fre= 'French,'
        if not re.search('alt=&#34;French', link, re.IGNORECASE):
                fre= ''     
        if re.search('alt=&#34;Turkish', link, re.IGNORECASE):
                tur= 'Turkish,'
        if not re.search('alt=&#34;Turkish', link, re.IGNORECASE):
                tur= '' 
        if re.search('alt=&#34;Japanese', link, re.IGNORECASE):
                jap= 'Japanese,'
        if not re.search('alt=&#34;Japanese', link, re.IGNORECASE):
                jap= ''     
        if re.search('alt=&#34;Spanish', link, re.IGNORECASE):
                spa= 'Spanish,'
        if not re.search('alt=&#34;Spanish', link, re.IGNORECASE):
                spa= '' 
        if re.search('alt=&#34;Chinese', link, re.IGNORECASE):
                chi= 'Chinese,'
        if not re.search('alt=&#34;Chinese', link, re.IGNORECASE):
                chi= ''         
        all= '%s %s %s %s\n%s %s %s' % (eng,ger,chi,fre,jap,spa,tur)
        found='[B]%s  LINKS FOUND[/B]' % (li)
        xbmcgui.Dialog().ok(found,str(all))
        for url1 ,filesize, name in match:
            regex = re.compile("downloads.members.easynews.com/news/(.+?)/(.+?)/(.+?)/(.+?)/(.+?)")
            match = regex.search(url1)
            output = "downloads.members.easynews.com/news/%s/%s/%s/pr-%s/pr-%s" %(match.group(1), match.group(2), match.group(3), match.group(4), match.group(5))
            mkv=''
            avi=''
            vob=''
            mov=''
            mp4=''
            iso=''
            m4v=''
            if re.search('.mkv', name, re.IGNORECASE):
                    mkv= 'MKV'    
            if not re.search('.mkv', name, re.IGNORECASE):
                    mkv= ''          
            if re.search('.avi', name, re.IGNORECASE):
                    avi= 'AVI' 
            if not re.search('.avi', name, re.IGNORECASE):
                    avi= ''          
            if re.search('.vob', name, re.IGNORECASE):
                    vob= 'VOB'
            if not re.search('.vob', name, re.IGNORECASE):
                    vob= ''     
            if re.search('.mov', name, re.IGNORECASE):
                    mov= 'MOV'
            if not re.search('.mov', name, re.IGNORECASE):
                    mov= '' 
            if re.search('.mp4', name, re.IGNORECASE):
                    mp4= 'MP4'
            if not re.search('.mp4', name, re.IGNORECASE):
                    mp4= '' 
            if re.search('.iso', name, re.IGNORECASE):
                    iso= 'ISO'
            if not re.search('.iso', name, re.IGNORECASE):
                    iso= ''
            if re.search('.m4v', name, re.IGNORECASE):
                    iso= 'M4V'
            if not re.search('.iso', name, re.IGNORECASE):
                    iso= ''  
            all=str(mkv)+str(avi)+str(vob)+str(mov)+str(mp4)+str(iso)+str(m4v)
            name = '[[B]%s %s[/B]]' % (filesize,all)+'  '+str(name).replace('%20',' ').replace('%28','(').replace('%29',')').replace('.mkv','').replace('.avi','').replace('.iso','').replace('.mov','').replace('.mp4','').replace('.m4v','').replace('.vob','').replace('%5B','').replace('%5C','').replace('%5A','')
            changeboost4 = 'http://'+username+':'+password+'@' +boost
            url = str(changeboost4)+str(url1)
            iconimage = str(changeboost4)+str(output).replace('.avi','.jpg').replace('.mkv','.jpg') .replace('.wmv','.jpg').replace('.mov','.jpg').replace('.mpg', '.jpg').replace('.asf', '.jpg').replace('.mp4', '.jpg') .replace('.iso', '.jpg').replace('.rm', '.jpg').replace('.flv', '.jpg') 
            xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
            addLink(name,url,iconimage,fanart,series,description,rating)  
            setView('movies', 'easy-view') 
    
def TV_POPULAR(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('<img src="(.+?)" height="74" width="54" alt=".+?" title=".+?"></a>\n  </td>\n  <td class="title">\n    \n\n<span class="wlb_wrapper" data-tconst="(.+?)" data-size="small" data-caller-name="search"></span>\n\n    <a href=".+?">(.+?)</a>\n    <span class="year_type">.+?</span><br>\n<div class="user_rating">\n\n\n<div class="rating rating-list" data-auth=".+?" id=".+?" data-ga-identifier="advsearch"\n title=".+?click stars to rate">\n<span class="rating-bg">&nbsp;</span>\n<span class="rating-imdb" style="width.+?">&nbsp;</span>\n<span class="rating-stars">\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>1</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>2</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>3</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>4</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>5</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>6</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>7</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>8</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>9</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>10</span></a>\n</span>\n<span class="rating-rating"><span class="value">.+?</span><span class="grey">/</span><span class="grey">10</span></span>\n<span class="rating-cancel"><a href=".+?" title="Delete" rel="nofollow"><span>X</span></a></span>\n&nbsp;</div>\n\n</div>\n<span class="outline">(.+?)</span>').findall(link)
        nextp=re.compile('<a href="(.+?)">Next&nbsp;').findall(link)
        try:      
                nextp1=nextp[0]
        except:
                pass       
        for iconimage, url, name, description in match:
            name = str(name).replace('&#xB7;','').replace('&#x27;','').replace('&#x26;','And').replace('&#x26;','And')
            iconimage1 = iconimage
            url = 'http://www.imdb.com/title/'+str(url)+'/'
            series = str(name).replace('&#xB7','').replace('&#x27;','').replace('&#x26;','And').replace('&#x26;','And')
            regex=re.compile('(.+?)_V1.+?.jpg')
            regex1=re.compile('(.+?).gif')
            try:
                    match = regex.search(iconimage1)
                    iconimage= '%s_V1_.SX593_SY799_.jpg'%(match.group(1))
            except:
                    pass
            try:    
                    match= regex1.search(iconimage1)
                    iconimage= '%s.gif'%(match.group(1))
            except:
                    pass
                    addDir(name,url,10,iconimage,fanart,series,description,rating)   
                    setView('movies', 'tvshows-view') 
        try:
                url='http://www.imdb.com'+str(nextp1)
                name= 'Next Page >>'
                addDir(name,url,9,'','','','','')
                setView('movies', 'tvshows-view') 
        except:
                pass
        addDir('<< Return To Movies Menu','url',5,'','','','','')    
        setView('movies', 'tvshows-view') 
             
def TV_SEASON(url,iconimage,series):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('.+?/rg/tt-episodes/season.+?/images/.+?season.+?     href="(.+?)"    >(.+?)</a>').findall(link)
        url2= str(url)
        for url1, name in match:
            url = str(url2)+str(url1)
            name = 'Season '+str(name)
            xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
            addDir(name,url,11,iconimage,fanart,series,description,rating) 
            setView('movies', 'seasons-view') 
            
def TV_EPISODE(url,iconimage,series):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('src="(.+?)">\n<div>(.+?)</div>\n</div>\n</a>  </div>\n  <div class="info" itemprop="episodes" itemscope itemtype="http://schema.org/TVEpisode">\n    <meta itemprop="episodeNumber" content=".+?"/>\n    <div class="airdate">\n.+?\n    </div>\n    <strong><a\nonclick=".+?src=.+?\nhref=".+?"\ntitle=".+?"\nitemprop="name">(.+?)</a></strong>\n    <div class="item_description" itemprop="description">(.+?)</div>').findall(link)
        series1=series
        for iconimage, episode, name, description in match:
            description= str(description).replace('&#700;','')
            iconimage1= iconimage
            episode='['+str(episode).replace('26,','26').replace('25,','25').replace('24,','24').replace('23,','23').replace('22,','22').replace('21,','21').replace('20,','20').replace('19,','19').replace('18,','18').replace('17,','17').replace('16,','16').replace('15,','15').replace('14,','14').replace('13,','13').replace('12,','12').replace('11,','11').replace('10,','10').replace('9,','09').replace('8,','08').replace('7,','07').replace('6,','06').replace('5,','05').replace('4,','04').replace('3,','03').replace('2,','02').replace('1,','01').replace('p26','26').replace('p25','25').replace('p24','24').replace('p23','23').replace('p22','22').replace('p21','p21').replace('p20','20').replace('p19','19').replace('p18','18').replace('p17','17').replace('p16','16').replace('p15','15').replace('p14','14').replace('p13','13').replace('p12','12').replace('p11','11').replace('p10','10').replace('p9','09').replace('p8','08').replace('p7','07').replace('p6','06').replace('p5','05').replace('p4','04').replace('p3','03').replace('p2','02').replace('p1','01')+']'
            name= str(episode)+' '+str(name).replace('&#xB7;','').replace('&#x27;','').replace('&#x26;','And')
            series = str(episode)+' '+str(series1)
            regex=re.compile('(.+?)_V1.+?.jpg')
            regex1=re.compile('(.+?).gif')
            try:
                    match = regex.search(iconimage1)
                    iconimage= '%s_V1_.SX593_SY799_.jpg'%(match.group(1))
            except:
                    pass
            try:    
                    match= regex1.search(iconimage1)
                    iconimage= '%s.gif'%(match.group(1))
            except:
                    pass
                    addDir(name,url,13,iconimage,fanart,series,description,rating)                
                    setView('movies', 'episodes-view') 
            
                             
def TV_SEARCH(name, iconimage):
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, 'Search EasyNews...XBMCHUB.COM')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText() .replace(' ','+')  # sometimes you need to replace spaces with + or %20#
            if search_entered == None:
                return False   
        url= 'http://www.imdb.com/find?q=%s&s=tt'% (search_entered)           
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()      
        match=re.compile('b>Popular Titles</b>.+?<table><tr> <td valign="top"><a href=".+?" onClick=".+?src=.+?link=.+?\';"><img src="(.+?)" width="23" height="32" border="0"></a>&nbsp;</td><td align="right" valign="top"><img src="/images/b.gif" width="1" height="6"><br>.+?</td><td valign="top"><img src="/images/b.gif" width="1" height="6"><br><a href=".+?" onclick=".+?src=.+?link=(.+?)\';">&#x22;(.+?)&#x22;').findall(link)
        for iconimage, url, name in match:
            iconimage1 = iconimage
            url = 'http://www.imdb.com'+str(url).replace("'",'')
            name= str(name).replace('-',' ')
            series = name
            regex=re.compile('(.+?)_V1.+?.jpg')
            match = regex.search(iconimage1)
            iconimage= '%s_V1_.SX593_SY799_.jpg'%(match.group(1))
            addDir(name,url,10,iconimage,fanart,series,description,rating)   
            setView('movies', 'seasons-view')
                  
def TV_EASY_SEARCH(series):
        search_entered = str(series).replace('.','').replace(' ','+') .replace(':','') .replace(',','').replace('[','').replace(']','')   
        dialog = xbmcgui.Dialog()
        if dialog.yesno("Search Options", "Choose your required quality?", "Custom: Use your custom settings", "Any: Returns any available quality", tvfn, "Any"):
                theurl = 'http://members-beta.easynews.com/global5/search.html?&gps='+search_entered+'&fex=&pby=1000&pno=1&s1=nsubject&s1d=-&s2=nrfile&s2d=-&s3=dsize&s3d=-&sS=5&d1t=&d2t=&b1t='+tvfs+'&b2t=&px1t=&px2t=&fps1t=&fps2t=&bps1t=&bps2t=&hz1t=&hz2t=&rn1t=&rn2t=&fty[]=VIDEO&spamf=1&u=1&st=adv&safeO=0&boost=1&sb=1'
                print theurl
        else:
                theurl = 'http://members-beta.easynews.com/global5/search.html?&gps='+search_entered+'&fex='+tvfn+'&pby=1000&pno=1&s1=nsubject&s1d=-&s2=nrfile&s2d=-&s3=dsize&s3d=-&sS=5&d1t=&d2t=&b1t='+tvfs+'&b2t=&px1t=&px2t=&fps1t=&fps2t=&bps1t=&bps2t=&hz1t=&hz2t=&rn1t=&rn2t=&fty[]=VIDEO&spamf=1&u=1&st=adv&safeO=0&boost=1&sb=1'
                print theurl
        username = ADDON.getSetting('easy_user')
        password = ADDON.getSetting('easy_pass')
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, theurl, username, password)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
        pagehandle = urllib2.urlopen(theurl)
        link= pagehandle.read()      
        match=re.compile('url="http://.+?-(.+?)" length="(.+?)" type="application/octet-stream" />\n<link>http.+?com/news/.+?/.+?/.+?/.+?/(.+?)</link>').findall(link)
        eng=''
        ger=''
        fre=''
        tur=''
        jap=''
        spa=''
        chi=''
        li=len(match)
        if re.search('alt=&#34;English', link, re.IGNORECASE):
                eng= 'English,'    
        if not re.search('alt=&#34;English', link, re.IGNORECASE):
                eng= ''          
        if re.search('alt=&#34;German', link, re.IGNORECASE):
                ger= 'German,' 
        if not re.search('alt=&#34;German', link, re.IGNORECASE):
                ger= ''          
        if re.search('alt=&#34;French', link, re.IGNORECASE):
                fre= 'French,'
        if not re.search('alt=&#34;French', link, re.IGNORECASE):
                fre= ''     
        if re.search('alt=&#34;Turkish', link, re.IGNORECASE):
                tur= 'Turkish,'
        if not re.search('alt=&#34;Turkish', link, re.IGNORECASE):
                tur= '' 
        if re.search('alt=&#34;Japanese', link, re.IGNORECASE):
                jap= 'Japanese,'
        if not re.search('alt=&#34;Japanese', link, re.IGNORECASE):
                jap= ''     
        if re.search('alt=&#34;Spanish', link, re.IGNORECASE):
                spa= 'Spanish,'
        if not re.search('alt=&#34;Spanish', link, re.IGNORECASE):
                spa= '' 
        if re.search('alt=&#34;Chinese', link, re.IGNORECASE):
                chi= 'Chinese,'
        if not re.search('alt=&#34;Chinese', link, re.IGNORECASE):
                chi= ''         
        all= '%s %s %s %s\n%s %s %s' % (eng,ger,chi,fre,jap,spa,tur)
        found='[B]%s  LINKS FOUND[/B]' % (li)
        xbmcgui.Dialog().ok(found,str(all))
        for url1 ,filesize, name in match:
            regex = re.compile("downloads.members.easynews.com/news/(.+?)/(.+?)/(.+?)/(.+?)/(.+?)")
            match = regex.search(url1)
            output = "downloads.members.easynews.com/news/%s/%s/%s/pr-%s/pr-%s" %(match.group(1), match.group(2), match.group(3), match.group(4), match.group(5))
            mkv=''
            avi=''
            vob=''
            mov=''
            mp4=''
            iso=''
            m4v=''
            if re.search('.mkv', name, re.IGNORECASE):
                    mkv= 'MKV'    
            if not re.search('.mkv', name, re.IGNORECASE):
                    mkv= ''          
            if re.search('.avi', name, re.IGNORECASE):
                    avi= 'AVI' 
            if not re.search('.avi', name, re.IGNORECASE):
                    avi= ''          
            if re.search('.vob', name, re.IGNORECASE):
                    vob= 'VOB'
            if not re.search('.vob', name, re.IGNORECASE):
                    vob= ''     
            if re.search('.mov', name, re.IGNORECASE):
                    mov= 'MOV'
            if not re.search('.mov', name, re.IGNORECASE):
                    mov= '' 
            if re.search('.mp4', name, re.IGNORECASE):
                    mp4= 'MP4'
            if not re.search('.mp4', name, re.IGNORECASE):
                    mp4= '' 
            if re.search('.iso', name, re.IGNORECASE):
                    iso= 'ISO'
            if not re.search('.iso', name, re.IGNORECASE):
                    iso= ''
            if re.search('.m4v', name, re.IGNORECASE):
                    iso= 'M4V'
            if not re.search('.iso', name, re.IGNORECASE):
                    iso= ''  
            all=str(mkv)+str(avi)+str(vob)+str(mov)+str(mp4)+str(iso)+str(m4v)
            name = '[[B]%s %s[/B]]' % (filesize,all)+'  '+str(name).replace('%20',' ').replace('%28','(').replace('%29',')').replace('.mkv','').replace('.avi','').replace('.iso','').replace('.mov','').replace('.mp4','').replace('.m4v','').replace('.vob','').replace('%5B','').replace('%5C','').replace('%5A','')
            changeboost4 = 'http://'+username+':'+password+'@' +boost
            url = str(changeboost4)+str(url1)
            iconimage = str(changeboost4)+str(output).replace('.avi','.jpg').replace('.mkv','.jpg') .replace('.wmv','.jpg').replace('.mov','.jpg').replace('.mpg', '.jpg').replace('.asf', '.jpg').replace('.mp4', '.jpg') .replace('.iso', '.jpg').replace('.rm', '.jpg').replace('.flv', '.jpg') 
            xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
            addLink(name,url,iconimage,fanart,series,description,rating)  
            setView('movies', 'easy-view')
            
def MUSIC_SEARCH(url):
        xbmc.PlayList(0).clear()
        artist = ''
        keyboard = xbmc.Keyboard(artist, 'Artist Name')
        keyboard.doModal()
        if keyboard.isConfirmed():
            artist = keyboard.getText() .replace(' ','+')  # sometimes you need to replace spaces with + or %20#
            if artist == None:
                return False
        album = ''
        keyboard = xbmc.Keyboard(album, 'Album Name')
        keyboard.doModal()
        if keyboard.isConfirmed():
            album = keyboard.getText() .replace(' ','+')  # sometimes you need to replace spaces with + or %20#
            if album == None:
                return False 
        dialog = xbmcgui.Dialog()
        if dialog.yesno("Add Album To Playlist", "     If Any Music Is Found Would You Like To", "       Add All The Songs To Your PlayList ?"):
                theurl = 'http://members-beta.easynews.com/global5/search.html?&gps='+artist+'+'+album+'&pby=20&pno=1&s1=dtime&s1d=-&s2=nrfile&s2d=-&s3=dsize&s3d=-&sS=5&d1t=&d2t=&b1t=&b2t=10&px1t=&px2t=&fps1t=&fps2t=&bps1t=&bps2t=&hz1t=&hz2t=&rn1t=&rn2t=&fty[]=AUDIO&u=1&st=adv&safeO=0&boost=1&sb=1'
                username = ADDON.getSetting('easy_user')
                password = ADDON.getSetting('easy_pass')
                passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
                passman.add_password(None, theurl, username, password)
                authhandler = urllib2.HTTPBasicAuthHandler(passman)
                opener = urllib2.build_opener(authhandler)
                urllib2.install_opener(opener)
                pagehandle = urllib2.urlopen(theurl)
                link= pagehandle.read()      
                match=re.compile('downloads.members.easynews.com/news/(.+?)/(.+?)/(.+?)/(.+?)/(.+?).mp3" length=".+?"').findall(link)
                try:
                        thumb = 'http://www.htbackdrops.com/v2/thumbnails.php?search=%s&submit=search&album=search&title=checked&caption=checked&keywords=checked&type=AND' % str(artist).replace(", ","+").replace("(The)","").replace(" ","+")
                        req2 = urllib2.Request(thumb)
                        req2.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                        response2 = urllib2.urlopen(req2)
                        link2=response2.read()
                        response2.close()
                except:
                        pass
                try:    
                        icon = re.compile('<img src="(.+?)" class="image" width=".+?" height=".+?" border="0" alt=".+?" title="Filename=.+?\r\nFilesize=.+?KiB\r\nDimensions=1.+?x.+?0').findall(link2)
                        normal = icon[0]
                except:
                        pass
                try:    
                        iconimage = 'http://www.htbackdrops.com/v2/%s' % str(normal).replace('thumb','normal')
                except:
                            iconimage= ''
                try:
                        fanart = 'http://www.htbackdrops.com/v2/%s' % str(normal).replace('thumb_','')
                except:
                            fanart = ''
                uniques= []
                for url1,url2, url3, url4, name in match:
                        if name[:2] not in uniques:
                            uniques.append(name[:2])
                            changeboost4 = 'http://'+username+':'+password+'@' +boost
                            url = str(changeboost4)+'downloads.members.easynews.com/news/'+str(url1)+'/'+str(url2)+'/'+str(url3)+'/'+str(url4)+'/'+str(name)+'.mp3'
                            name = str(name).replace('%20',' ').replace('%28','').replace('%29','').replace('-',' ').replace('_',' ').replace('%5B','').replace('%2C','').replace('%27','').replace('%26','')
                            xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
                            addLink1(name,url,iconimage,fanart)        
                            setView('movies', 'easy-view') 
        else:
                theurl = 'http://members-beta.easynews.com/global5/search.html?&gps='+artist+'+'+album+'&pby=20&pno=1&s1=dtime&s1d=-&s2=nrfile&s2d=-&s3=dsize&s3d=-&sS=5&d1t=&d2t=&b1t=&b2t=10&px1t=&px2t=&fps1t=&fps2t=&bps1t=&bps2t=&hz1t=&hz2t=&rn1t=&rn2t=&fty[]=AUDIO&u=1&st=adv&safeO=0&boost=1&sb=1'
                username = ADDON.getSetting('easy_user')
                password = ADDON.getSetting('easy_pass')
                passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
                passman.add_password(None, theurl, username, password)
                authhandler = urllib2.HTTPBasicAuthHandler(passman)
                opener = urllib2.build_opener(authhandler)
                urllib2.install_opener(opener)
                pagehandle = urllib2.urlopen(theurl)
                link= pagehandle.read()      
                match=re.compile('downloads.members.easynews.com/news/(.+?)/(.+?)/(.+?)/(.+?)/(.+?).mp3" length=".+?"').findall(link)
                try:
                        thumb = 'http://www.htbackdrops.com/v2/thumbnails.php?search=%s&submit=search&album=search&title=checked&caption=checked&keywords=checked&type=AND' % str(artist).replace(", ","+").replace("(The)","").replace(" ","+")
                        req2 = urllib2.Request(thumb)
                        req2.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                        response2 = urllib2.urlopen(req2)
                        link2=response2.read()
                        response2.close()
                except:
                        pass
                try:    
                        icon = re.compile('<img src="(.+?)" class="image" width=".+?" height=".+?" border="0" alt=".+?" title="Filename=.+?\r\nFilesize=.+?KiB\r\nDimensions=1.+?x.+?0').findall(link2)
                        normal = icon[0]
                except:
                        pass
                try:    
                        iconimage = 'http://www.htbackdrops.com/v2/%s' % str(normal).replace('thumb','normal')
                except:
                            iconimage= ''
                try:
                        fanart = 'http://www.htbackdrops.com/v2/%s' % str(normal).replace('thumb_','')
                except:
                            fanart = ''    
                uniques= []
                for url1,url2, url3, url4, name in match:
                        if name[:2] not in uniques:
                            uniques.append(name[:2])
                            changeboost4 = 'http://'+username+':'+password+'@' +boost
                            url = str(changeboost4)+'downloads.members.easynews.com/news/'+str(url1)+'/'+str(url2)+'/'+str(url3)+'/'+str(url4)+'/'+str(name)+'.mp3'
                            name = str(name).replace('%20',' ').replace('%28','').replace('%29','').replace('-',' ').replace('_',' ').replace('%5B','').replace('%2C','').replace('%27','').replace('%26','')
                            xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
                            addLink2(name,url,iconimage,fanart)        
                            setView('movies', 'easy-view')     
           
            
def ITUNES_LIST(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('href="(.+?)">(.+?) RSS Feed').findall(link)
        for url, name in match:
            xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)    
            addDir(name,url,20,iconimage,fanart,series,description,rating)    
            setView('movies', 'music-view')
            
def ITUNES_RSS(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('<img border="0" src="(.+?)" /></a></td>\n\t\t\t\t\t<td width="10"><img alt="" width="10" height="1" src="http://r.mzstatic.com/images/spacer.gif" /></td>\n\t\t\t\t\t<td width="95%"><B><a href=".+?">(.+?)</a></B><br>\n\t\t\t\t\t\t<a href=".+?">(.+?)</a>').findall(link)
        for iconimage, url, name in match:
            url=str(url).replace('+','plus').replace('Deluxe','').replace('deluxe','').replace('Version','').replace('version','').replace('(','').replace(')','').replace('&amp;','and').replace('Edition','').replace('edition','')
            name=str(name).replace('&amp;','and').replace('&#039;','').replace("\'","")
            iconimage=str(iconimage).replace('100x100','600x600')
            xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
            addDir(name,url,18,iconimage,fanart,series,description,rating)    
            setView('movies', 'music-view')    
            
            
def MUSIC_LIST_SEARCH(name, url):
        xbmc.PlayList(0).clear()
        dialog = xbmcgui.Dialog()
        if dialog.yesno("Add Album To Playlist", "     If Any Music Is Found Would You Like To", "       Add All The Songs To Your PlayList ?"):
                        theurl = 'http://members-beta.easynews.com/global5/search.html?&gps='+str(name).replace(' ','+')+'+'+str(url).replace(' ','+')+'&pby=20&pno=1&s1=dtime&s1d=-&s2=nrfile&s2d=-&s3=dsize&s3d=-&sS=5&d1t=&d2t=&b1t=&b2t=10&px1t=&px2t=&fps1t=&fps2t=&bps1t=&bps2t=&hz1t=&hz2t=&rn1t=&rn2t=&fty[]=AUDIO&u=1&st=adv&safeO=0&boost=1&sb=1'
                        username = ADDON.getSetting('easy_user')
                        password = ADDON.getSetting('easy_pass')
                        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
                        passman.add_password(None, theurl, username, password)
                        authhandler = urllib2.HTTPBasicAuthHandler(passman)
                        opener = urllib2.build_opener(authhandler)
                        urllib2.install_opener(opener)
                        pagehandle = urllib2.urlopen(theurl)
                        link= pagehandle.read()      
                        match=re.compile('downloads.members.easynews.com/news/(.+?)/(.+?)/(.+?)/(.+?)/(.+?).mp3" length=".+?"').findall(link)
                        try:
                                thumb = 'http://www.htbackdrops.com/v2/thumbnails.php?search=%s&submit=search&album=search&title=checked&caption=checked&keywords=checked&type=AND' % str(name).replace(", ","+").replace("(The)","").replace(" ","+")
                                req2 = urllib2.Request(thumb)
                                req2.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                                response2 = urllib2.urlopen(req2)
                                link2=response2.read()
                                response2.close()
                        except:
                                pass
                        try:    
                                icon = re.compile('<img src="(.+?)" class="image" width=".+?" height=".+?" border="0" alt=".+?" title="Filename=.+?\r\nFilesize=.+?KiB\r\nDimensions=1.+?x.+?0').findall(link2)
                                normal = icon[0]
                        except:
                                pass
                        try:
                                fanart = 'http://www.htbackdrops.com/v2/%s' % str(normal).replace('thumb_','')
                        except:
                                    fanart = ''
                        uniques= []     
                        for url1,url2, url3, url4, name in match:
                            if name[:2] not in uniques:
                                    uniques.append(name[:2])
                                    changeboost4 = 'http://'+username+':'+password+'@' +boost
                                    url = str(changeboost4)+'downloads.members.easynews.com/news/'+str(url1)+'/'+str(url2)+'/'+str(url3)+'/'+str(url4)+'/'+str(name)+'.mp3'
                                    name = str(name).replace(str(url),'').replace('%20',' ').replace('%28','').replace('%29','').replace('-',' ').replace('_',' ').replace('%5B','').replace('%2C','').replace('%27','').replace('%26','')
                                    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
                                    addLink1(name,url,iconimage,fanart)        
                                    setView('movies', 'easy-view') 

        else:
                        theurl = 'http://members-beta.easynews.com/global5/search.html?&gps='+str(name).replace(' ','+')+'+'+str(url).replace(' ','+')+'&pby=20&pno=1&s1=dtime&s1d=-&s2=nrfile&s2d=-&s3=dsize&s3d=-&sS=5&d1t=&d2t=&b1t=&b2t=10&px1t=&px2t=&fps1t=&fps2t=&bps1t=&bps2t=&hz1t=&hz2t=&rn1t=&rn2t=&fty[]=AUDIO&u=1&st=adv&safeO=0&boost=1&sb=1'
                        username = ADDON.getSetting('easy_user')
                        password = ADDON.getSetting('easy_pass')
                        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
                        passman.add_password(None, theurl, username, password)
                        authhandler = urllib2.HTTPBasicAuthHandler(passman)
                        opener = urllib2.build_opener(authhandler)
                        urllib2.install_opener(opener)
                        pagehandle = urllib2.urlopen(theurl)
                        link= pagehandle.read()      
                        match=re.compile('downloads.members.easynews.com/news/(.+?)/(.+?)/(.+?)/(.+?)/(.+?).mp3" length=".+?"').findall(link)
                        try:
                                thumb = 'http://www.htbackdrops.com/v2/thumbnails.php?search=%s&submit=search&album=search&title=checked&caption=checked&keywords=checked&type=AND' % str(name).replace(", ","+").replace("(The)","").replace(" ","+")
                                req2 = urllib2.Request(thumb)
                                req2.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                                response2 = urllib2.urlopen(req2)
                                link2=response2.read()
                                response2.close()
                        except:
                                pass
                        try:    
                                icon = re.compile('<img src="(.+?)" class="image" width=".+?" height=".+?" border="0" alt=".+?" title="Filename=.+?\r\nFilesize=.+?KiB\r\nDimensions=1.+?x.+?0').findall(link2)
                                normal = icon[0]
                        except:
                                pass
                        try:
                                fanart = 'http://www.htbackdrops.com/v2/%s' % str(normal).replace('thumb_','')
                        except:
                                    fanart = ''
                        uniques= []     
                        for url1,url2, url3, url4, name in match:
                            if name[:2] not in uniques:
                                    uniques.append(name[:2])
                                    changeboost4 = 'http://'+username+':'+password+'@' +boost
                                    url = str(changeboost4)+'downloads.members.easynews.com/news/'+str(url1)+'/'+str(url2)+'/'+str(url3)+'/'+str(url4)+'/'+str(name)+'.mp3'
                                    name = str(name).replace('%20',' ').replace('%28','').replace('%29','').replace('-',' ').replace('_',' ').replace('%5B','').replace('%2C','').replace('%27','').replace('%26','')
                                    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
                                    addLink2(name,url,iconimage,fanart)        
                                    setView('movies', 'easy-view')     
            
def HMV_SEARCH(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('src="(.+?)" alt="Picture of - (.+?)&nbsp;(.+?)"').findall(link)
        nextp=re.compile('<a class="next" href="(.+?)">next</a></li>').findall(link)
        try:
                nextp1=nextp[0]
        except:
                pass
        for iconimage, name, url in match:
            url=str(url).replace('Hmv.com Exclusive','').replace('+','').replace('Deluxe','').replace('deluxe','').replace('Version','').replace('version','').replace('(','').replace(')','').replace('&amp;','and').replace('Edition','').replace('edition','').replace(':','').replace('2cd','').replace('Artcards','')
            name=str(name).replace('&amp;','and').replace('&#039;','').replace('Va','Various Artists').replace(':','')
            addDir(name,url,18,iconimage,fanart,series,description,rating)    
        try:
                url='http://hmv.com'+str(nextp1)
                name= 'Next Page >>'
                addDir(name,url,19,'','','','','')    
        except:
                pass
        addDir('<< Return To Music Menu','url',15,'','','','','')    
        setView('movies', 'music-view') 
        
        
def BILLBOARD_MAIN_LIST(url):
        addDir('BillBoard 200','http://www.billboard.com/charts/billboard-200#/charts/billboard-200',7,'','','','','')
        addDir('Country Albums','http://www.billboard.com/charts/country-albums#/charts/country-albums',7,'','','','','')
        addDir('HeatSeeker Albums','http://www.billboard.com/charts/heatseekers-albums#/charts/heatseekers-albums',7,'','','','','')
        addDir('Independent Albums','http://www.billboard.com/charts/independent-albums#/charts/independent-albums',7,'','','','','')
        addDir('Catalogue Albums','http://www.billboard.com/charts/catalog-albums#/charts/catalog-albums',7,'','','','','')
        addDir('Folk Albums','http://www.billboard.com/charts/folk-albums#/charts/folk-albums',7,'','','','','')
        addDir('Digital Albums','http://www.billboard.com/charts/digital-albums#/charts/digital-albums',7,'','','','','')
        addDir('<< Return To Music Menu','url',15,'','','','','')    
        
def BILLBOARD_ALBUM_LISTS(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('"title" : "(.+?)"\r\n        ,"artist" : "(.+?)"\r\n        ,"image" : "(.+?)"\r\n').findall(link)
        for url, name, iconimage in match:
            addDir(name,url,18,iconimage,fanart,series,description,rating)    
            setView('movies', 'default-view')  
        addDir('<< Return To Billboard Menu','url',22,'','','','','')    
        setView('movies', 'music-view') 
           
def WATCH_TV_LIST(url):
        url=IMDBTV_WATCHLIST
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link=str(link).replace('\n','').replace('\t','')
        match = re.compile('data-const=".+?"><img src="(.+?)" height="209" width="140" alt=".+?" class="zero-z-index"></div></a></div>.+?href="/title/(.+?)/"    >(.+?)</a>    <span class="year_type">.+?</span>.+?<div class="item_description">(.+?)<span>').findall(link)
        for iconimage, url, name, description in match:
            iconimage1 = iconimage
            regex=re.compile('(.+?)_V1.+?.jpg')
            regex1=re.compile('(.+?).gif')
            try:
                    match = regex.search(iconimage1)
                    iconimage= '%s_V1_.SX593_SY799_.jpg'%(match.group(1))
            except:
                    pass
            try:    
                    match= regex1.search(iconimage1)
                    iconimage= '%s.gif'%(match.group(1))
            except:
                    pass
                    url = 'http://www.imdb.com/title/'+str(url)+'/'
                    name = str(name).replace('&#xB7;','').replace('&#x27;','').replace('&#x26;','And')
                    addDir(name,url,24,iconimage,fanart,series,description,rating)   
                    setView('movies', 'movies-view') 
                        
def WATCH_LIST_SEARCH(name,url,iconimage,description):
        series = str(name)
        dialog = xbmcgui.Dialog()
        if dialog.yesno("Please Select", "Please Select Type", "", '', "MOVIE", "TV"): 
		        req = urllib2.Request(url)
		        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		        response = urllib2.urlopen(req)
		        link=response.read()
		        response.close()
		        match = re.compile('.+?/rg/tt-episodes/season.+?/images/.+?season.+?     href="(.+?)"    >(.+?)</a>').findall(link)
		        url2= str(url)
		        for url1, name in match:
		            url = str(url2)+str(url1)
		            name = 'Season '+str(name)
		            xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
		            addDir(name,url,11,iconimage,fanart,series,description,rating) 
		            setView('movies', 'seasons-view') 
        else:
		        search_entered = str(name).replace('.','').replace(', ','+').replace(' ','+') .replace(':','').replace('[','').replace(']',' ').replace('(The)','').replace('(','') .replace(')','') .replace('-','+').replace("'",'') .replace("&",'and').replace("!",'')      
		        dialog = xbmcgui.Dialog()
		        if dialog.yesno("Search Options", "Choose your required quality?", "Custom: Use your custom settings", "Any: Returns any available quality", mvfn, "Any"):
		                theurl = 'http://members-beta.easynews.com/global5/search.html?&gps='+search_entered+'&fex=&pby=1000&pno=1&s1=nsubject&s1d=-&s2=nrfile&s2d=-&s3=dsize&s3d=-&sS=5&d1t=&d2t=&b1t='+mvfs+'&b2t=&px1t=&px2t=&fps1t=&fps2t=&bps1t=&bps2t=&hz1t=&hz2t=&rn1t=&rn2t=&fty[]=VIDEO&spamf=1&u=1&st=adv&safeO=0&boost=1&sb=1'
		        else:
		                theurl = 'http://members-beta.easynews.com/global5/search.html?&gps='+search_entered+'&fex='+mvfn+'&pby=1000&pno=1&s1=nsubject&s1d=-&s2=nrfile&s2d=-&s3=dsize&s3d=-&sS=5&d1t=&d2t=&b1t='+mvfs+'&b2t=&px1t=&px2t=&fps1t=&fps2t=&bps1t=&bps2t=&hz1t=&hz2t=&rn1t=&rn2t=&fty[]=VIDEO&spamf=1&u=1&st=adv&safeO=0&boost=1&sb=1'
		        username = ADDON.getSetting('easy_user')
		        password = ADDON.getSetting('easy_pass')
		        print theurl
		        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
		        passman.add_password(None, theurl, username, password)
		        authhandler = urllib2.HTTPBasicAuthHandler(passman)
		        opener = urllib2.build_opener(authhandler)
		        urllib2.install_opener(opener)
		        pagehandle = urllib2.urlopen(theurl)
		        link= pagehandle.read()      
		        match=re.compile('url="http://.+?-(.+?)" length="(.+?)" type="application/octet-stream" />\n<link>http.+?com/news/.+?/.+?/.+?/.+?/(.+?)</link>').findall(link)
		        eng=''
		        ger=''
		        fre=''
		        tur=''
		        jap=''
		        spa=''
		        chi=''
		        li=len(match)
		        if re.search('alt=&#34;English', link, re.IGNORECASE):
		                eng= 'English,'    
		        if not re.search('alt=&#34;English', link, re.IGNORECASE):
		                eng= ''          
		        if re.search('alt=&#34;German', link, re.IGNORECASE):
		                ger= 'German,' 
		        if not re.search('alt=&#34;German', link, re.IGNORECASE):
		                ger= ''          
		        if re.search('alt=&#34;French', link, re.IGNORECASE):
		                fre= 'French,'
		        if not re.search('alt=&#34;French', link, re.IGNORECASE):
		                fre= ''     
		        if re.search('alt=&#34;Turkish', link, re.IGNORECASE):
		                tur= 'Turkish,'
		        if not re.search('alt=&#34;Turkish', link, re.IGNORECASE):
		                tur= '' 
		        if re.search('alt=&#34;Japanese', link, re.IGNORECASE):
		                jap= 'Japanese,'
		        if not re.search('alt=&#34;Japanese', link, re.IGNORECASE):
		                jap= ''     
		        if re.search('alt=&#34;Spanish', link, re.IGNORECASE):
		                spa= 'Spanish,'
		        if not re.search('alt=&#34;Spanish', link, re.IGNORECASE):
		                spa= '' 
		        if re.search('alt=&#34;Chinese', link, re.IGNORECASE):
		                chi= 'Chinese,'
		        if not re.search('alt=&#34;Chinese', link, re.IGNORECASE):
		                chi= ''         
		        all= '%s %s %s %s\n%s %s %s' % (eng,ger,chi,fre,jap,spa,tur)
		        found='[B]%s  LINKS FOUND[/B]' % (li)
		        xbmcgui.Dialog().ok(found,str(all))
		        for url1 ,filesize, name in match:
		            regex = re.compile("downloads.members.easynews.com/news/(.+?)/(.+?)/(.+?)/(.+?)/(.+?)")
		            match = regex.search(url1)
		            output = "downloads.members.easynews.com/news/%s/%s/%s/pr-%s/pr-%s" %(match.group(1), match.group(2), match.group(3), match.group(4), match.group(5))
		            mkv=''
		            avi=''
		            vob=''
		            mov=''
		            mp4=''
		            iso=''
		            m4v=''
		            if re.search('.mkv', name, re.IGNORECASE):
		                    mkv= 'MKV'    
		            if not re.search('.mkv', name, re.IGNORECASE):
		                    mkv= ''          
		            if re.search('.avi', name, re.IGNORECASE):
		                    avi= 'AVI' 
		            if not re.search('.avi', name, re.IGNORECASE):
		                    avi= ''          
		            if re.search('.vob', name, re.IGNORECASE):
		                    vob= 'VOB'
		            if not re.search('.vob', name, re.IGNORECASE):
		                    vob= ''     
		            if re.search('.mov', name, re.IGNORECASE):
		                    mov= 'MOV'
		            if not re.search('.mov', name, re.IGNORECASE):
		                    mov= '' 
		            if re.search('.mp4', name, re.IGNORECASE):
		                    mp4= 'MP4'
		            if not re.search('.mp4', name, re.IGNORECASE):
		                    mp4= '' 
		            if re.search('.iso', name, re.IGNORECASE):
		                    iso= 'ISO'
		            if not re.search('.iso', name, re.IGNORECASE):
		                    iso= ''
		            if re.search('.m4v', name, re.IGNORECASE):
		                    iso= 'M4V'
		            if not re.search('.iso', name, re.IGNORECASE):
		                    iso= ''  
		            all=str(mkv)+str(avi)+str(vob)+str(mov)+str(mp4)+str(iso)+str(m4v)
		            name = '[[B]%s %s[/B]]' % (filesize,all)+'  '+str(name).replace('%20',' ').replace('%28','(').replace('%29',')').replace('.mkv','').replace('.avi','').replace('.iso','').replace('.mov','').replace('.mp4','').replace('.m4v','').replace('.vob','').replace('%5B','').replace('%5C','').replace('%5A','')
		            changeboost4 = 'http://'+username+':'+password+'@' +boost
		            url = str(changeboost4)+str(url1)
		            iconimage = str(changeboost4)+str(output).replace('.avi','.jpg').replace('.mkv','.jpg') .replace('.wmv','.jpg').replace('.mov','.jpg').replace('.mpg', '.jpg').replace('.asf', '.jpg').replace('.mp4', '.jpg') .replace('.iso', '.jpg').replace('.rm', '.jpg').replace('.flv', '.jpg') 
		            xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
		            addLink(name,url,iconimage,fanart,series,description,rating)  
		            setView('movies', 'easy-view') 
 
    
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

        
def addDir(name,url,mode,iconimage,fanart,series,description,rating):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&series="+urllib.quote_plus(series)+"&description="+urllib.quote_plus(description)+"&rating="+urllib.quote_plus(rating)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name,"Plot":description,"Rating":rating  } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
                
def addLink(name,url,iconimage,fanart,series,description,rating):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name,"Plot":description  } )
        liz.setProperty("IsPlayable","true")
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok 
                      
def addLink1(name,url,iconimage,fanart):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={ "Title": name})
        liz.setProperty('mimetype', 'audio/mpeg')
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        pl=xbmc.PlayList(0)
        pl.add(url, liz)
        xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(pl)
        return ok
        
        
def addLink2(name,url,iconimage,fanart):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={ "Title": name})
        liz.setProperty('mimetype', 'audio/mpeg')
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok
        
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
series=None
description=None
rating=None



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
        series=urllib.unquote_plus(params["series"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass   
        
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass 
        
try:        
        rating=urllib.unquote_plus(params["rating"])
except:
        pass                      

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
print "Series: "+str(series)


def setView(content, viewType):
        # set content type so library shows more views and info
        if content:
                xbmcplugin.setContent(int(sys.argv[1]), content)
        if ADDON.getSetting('auto-view') == 'true':
                xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )

       
        

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        print ""+url
        SEARCH(url)
        
elif mode==2:
        print ""+url
        TMDB(url)       

elif mode==3:
        print ""+name+iconimage
        EasySearch(name,iconimage)    
        
elif mode==4:
        print ""+name+iconimage
        MOVIE_CATEGORIES()  
        
elif mode==5:
        print ""+name+iconimage
        TV_CATEGORIES()    
        
elif mode==6:
        print ""+name+iconimage
        IMDB_SEARCH(name,iconimage)   
        
elif mode==7:
        print ""+url
        BILLBOARD_ALBUM_LISTS(url) 
        
elif mode==8:
        print ""+url
        WATCH_TV_LIST(url)  
        
elif mode==9:
        print ""+url
        TV_POPULAR(url)  
        
elif mode==10:
        print ""+url +iconimage +series
        TV_SEASON(url,iconimage, series) 
        
elif mode==11:
        print ""+url +iconimage +series
        TV_EPISODE(url,iconimage, series)

elif mode==12:
        print ""+url +iconimage 
        TV_SEARCH(url,iconimage)     
        
elif mode==13:
        print ""+series
        TV_EASY_SEARCH(series) 
        
elif mode==14:
        print ""+url
        ONDVD(url)
        
elif mode==15:
        print ""
        MUSIC_CATEGORIES()
        
elif mode==16:
        print ""+url
        MUSIC_SEARCH(url) 
        
elif mode==17:
        print ""+url
        ITUNES_LIST(url)           

elif mode==18:
        print ""+name +url
        MUSIC_LIST_SEARCH(name, url) 
        
elif mode==19:
        print ""+url
        HMV_SEARCH(url)         
                         
elif mode==20:
        print ""+url
        ITUNES_RSS(url) 
        
elif mode==21:
        print ""+url
        TOP_CATEGORIES() 
        
elif mode==22:
        print ""+url
        BILLBOARD_MAIN_LIST(url) 
        
elif mode==23:
        print ""+url
        ITUNES_MOVIES_CATEGORIES(url) 
        
elif mode==24:
        print ""+url
        WATCH_LIST_SEARCH(name,url,iconimage,description)  
        
                                                       
xbmcplugin.endOfDirectory(int(sys.argv[1]))
