import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon, base64
import settings
from urlparse import urlparse

ADDON = settings.addon()
tvfs = settings.TV_FILESIZE()
mvfs = settings.MOVIE_FILESIZE()
tvfn = settings.TV_FILENAME()
mvfn = settings.MOVIE_FILENAME()



def CATEGORIES():
        addDir('Search Easy News','url',1,'','','','','')
        addDir('Movies','url',4,'','','','','')
        addDir('TV','url',5,'','','','','')
   
        
def MOVIE_CATEGORIES():
        addDir('Search Movies','url',6,'','','','','')
        addDir('Now Playing','http://www.themoviedb.org/movie/now-playing',2,'','','','','')
        addDir('Blu-ray & DVD Last Week','http://www.lovefilm.com/browse/film/new-releases/dvd/films/new-last-week/?sort_by=release_date&rows=50',14,'','','','','')
        addDir('Blu-ray & DVD 2 Weeks Ago','http://www.lovefilm.com/browse/film/new-releases/dvd/films/new-2-weeks/?sort_by=release_date&rows=50',14,'','','','','')
        addDir('Blu-ray & DVD 3 Weeks Ago','http://www.lovefilm.com/browse/film/new-releases/dvd/films/new-3-weeks/?sort_by=release_date&rows=50',14,'','','','','')
        addDir('Blu-ray & DVD 4 Weeks Ago','http://www.lovefilm.com/browse/film/new-releases/dvd/films/new-4-weeks/?sort_by=release_date&rows=50',14,'','','','','')
        addDir('Blu-ray & DVD 2 Months Ago','http://www.lovefilm.com/browse/film/new-releases/dvd/films/new-2-months/?sort_by=release_date&rows=50',14,'','','','','')
        addDir('Top Rated','http://www.themoviedb.org/movie/top-rated',2,'','','','','')
        addDir('Genres','http://www.imdb.com/genre',7,'','','','','')
        setView('movies', 'default-view')

def TV_CATEGORIES():
        addDir('Search Tv Shows','url',12,'','','','','')
        addDir('Most Popular','http://www.imdb.com/search/title?num_votes=5000,&sort=moviemeter&title_type=tv_series',9,'','','','','')
        addDir('Most Popular 2','http://www.imdb.com/search/title?num_votes=5000,&sort=moviemeter,asc&start=51&title_type=tv_series',9,'','','','','')
        addDir('Most Popular 3','http://www.imdb.com/search/title?num_votes=5000,&sort=moviemeter,asc&start=101&title_type=tv_series',9,'','','','','')
        addDir('Most Popular 4','http://www.imdb.com/search/title?num_votes=5000,&sort=moviemeter,asc&start=151&title_type=tv_series',9,'','','','','')
        addDir('Most Popular 5','http://www.imdb.com/search/title?num_votes=5000,&sort=moviemeter,asc&start=201&title_type=tv_series',9,'','','','','')
        setView('movies', 'default-view')

def SEARCH(url):
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, 'Search EasyNews...XBMCHUB.COM')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText() .replace(' ','+')  # sometimes you need to replace spaces with + or %20#
            if search_entered == None:
                return False          
        theurl = 'http://members.easynews.com/global5/index.html?&gps='+search_entered+'&sbj=&from=&ns=&fil=&fex=&vc=&ac=&fty%5B%5D=VIDEO&s1=nsubject&s1d=%2B&s2=nrfile&s2d=%2B&s3=dsize&s3d=%2B&pby=1000&spamf=1&u=1&svL=&d1=&d1t=&d2=&d2t=&b1=&b1t=&b2=&b2t=&px1=&px1t=&px2=&px2t=&fps1=&fps1t=&fps2=&fps2t=&bps1=&bps1t=&bps2=&bps2t=&hz1=&hz1t=&hz2=&hz2t=&rn1=&rn1t=&rn2=&rn2t=&fly=2&pno=1&sS=5'
        username = ADDON.getSetting('easy_user')
        password = ADDON.getSetting('easy_pass')
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, theurl, username, password)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
        pagehandle = urllib2.urlopen(theurl)
        link= pagehandle.read()      
        match=re.compile('url="(.+?)" length="(.+?)" type="application/octet-stream" />\n<link>http.+?com/news/.+?/.+?/.+?/.+?/(.+?)</link>').findall(link)
        eng=''
        ger=''
        fre=''
        tur=''
        jap=''
        spa=''
        if re.search('alt=&#34;English', link, re.IGNORECASE):
                eng= 'English'    
        if not re.search('alt=&#34;English', link, re.IGNORECASE):
                eng= ''          
        if re.search('alt=&#34;German', link, re.IGNORECASE):
                ger= 'German' 
        if not re.search('alt=&#34;German', link, re.IGNORECASE):
                ger= ''          
        if re.search('alt=&#34;French', link, re.IGNORECASE):
                fre= 'French'
        if not re.search('alt=&#34;French', link, re.IGNORECASE):
                fre= ''     
        if re.search('alt=&#34;Turkish', link, re.IGNORECASE):
                tur= 'Turkish'
        if not re.search('alt=&#34;Turkish', link, re.IGNORECASE):
                tur= '' 
        if re.search('alt=&#34;Japanese', link, re.IGNORECASE):
                jap= 'Japanese'
        if not re.search('alt=&#34;Japanese', link, re.IGNORECASE):
                jap= ''     
        if re.search('alt=&#34;Spanish', link, re.IGNORECASE):
                spa= 'Spanish'
        if not re.search('alt=&#34;Spanish', link, re.IGNORECASE):
                spa= '' 
        all= '%s\n%s %s %s\n%s %s %s' % ('',eng,ger,fre,tur,jap,spa)
        xbmcgui.Dialog().ok('Found These Languages',str(all))
        for url1 ,filesize, name in match:
            regex = re.compile("http://boost4-downloads.members.easynews.com/news/(.+?)/(.+?)/(.+?)/(.+?)/(.+?)")
            match = regex.search(url1)
            output = "http://boost4-downloads.members.easynews.com/news/%s/%s/%s/pr-%s/pr-%s" %(match.group(1), match.group(2), match.group(3), match.group(4), match.group(5))
            name = '['+str(filesize)+']   '+str(name).replace('%20',' ').replace('%28','(').replace('%29',')')
            changeboost4 = 'http://'+username+':'+password+'@'
            url = str(url1).replace('http://',str(changeboost4))
            iconimage = str(output).replace('http://',str(changeboost4)).replace('.avi','.jpg').replace('.mkv','.jpg') .replace('.wmv','.jpg').replace('.mov','.jpg').replace('.mpg', '.jpg').replace('.asf', '.jpg').replace('.mp4', '.jpg') .replace('.iso', '.jpg').replace('.rm', '.jpg').replace('.flv', '.jpg') 
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
        for iconimage, url1, name in match:
            url=url1
            name = str(name).replace('&hellip;','')
            iconimage = str(iconimage).replace('w92','original')
            fanart = iconimage
            addDir(name,url,3,iconimage,fanart,series,description,rating)
            setView('movies', 'default-view')   
             
def ONDVD(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match= re.compile('src="(.+?)" alt=".+?" .+?\n.+?</a>\n        </div>\n\n\n\n\t    <ul id=".+?" class=".+?">\n                <li class=".+?">\n        <a rel="nofollow" href=".+?" class=".+?" title=".+?" >\n\t\t.+?\n\t\t</a>\n    </li>\n\n</ul>\n</div> \n<div class=".+?">\n\t<h2><a href=".+?"title=".+?">.+?</a>\n\n\n        <span class="release_decade">(.+?)</span>\n    </h2>\n    \n\n<ul class=".+?">\n    \n\n        <li property=".+?" content="(.+?)">\n            \n        <div class=".+?" data-rating_id=".+?">\n            <span class=".+?" style=".+?"><em>.+?</em></span>\n            <span class=".+?" style=".+?"><em></em></span>\n            <a class=".+?" title=".+?" data-product_media=".+?" data-product_name="(.+?)" .+?=".+?" .+?=".+?" .+?=".+?"></a>\n    </div>\n    \n        </li>\n            <li><small property=".+?" content=".+?">\n.+?\n            </small></li>\n            \n\n</ul>\n\n\n\n\t<div.+?>(.+?)<').findall(link)
        for iconimage, year, rating, name, description in match:
            iconimage = str(iconimage).replace('77x109','large')
            addDir(name,url,3,iconimage,fanart,series,description,rating)
            setView('movies', 'movies-view')
            
                          
def TMDB_GENRES(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('<td><a href="(.+?)">(.+?)</a></td>').findall(link)
        for url, name in match:
            url = 'http://www.imdb.com/'+str(url)
            addDir(name,url,8,iconimage,fanart,series,description,rating)    
            setView('movies', 'default-view')            
           
def GENRE_LIST(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('<img src="(.+?)" height="74" width="54" alt=".+?" title=".+?"></a>\n  </td>\n  <td class="title">\n    \n\n<span class="wlb_wrapper" data-tconst="(.+?)" data-size="small" data-caller-name="search"></span>\n\n    <a href=".+?">(.+?)</a>\n    <span class="year_type">.+?</span><br>\n<div class="user_rating">\n\n\n<div class="rating rating-list" data-auth=".+?" id=".+?" data-ga-identifier="advsearch"\n title=".+?click stars to rate">\n<span class="rating-bg">&nbsp;</span>\n<span class="rating-imdb" style="width.+?">&nbsp;</span>\n<span class="rating-stars">\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>1</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>2</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>3</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>4</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>5</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>6</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>7</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>8</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>9</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>10</span></a>\n</span>\n<span class="rating-rating"><span class="value">.+?</span><span class="grey">/</span><span class="grey">10</span></span>\n<span class="rating-cancel"><a href=".+?" title="Delete" rel="nofollow"><span>X</span></a></span>\n&nbsp;</div>\n\n</div>\n<span class="outline">(.+?)</span>').findall(link)
        for iconimage, url, name, description in match:
            iconimage1 = iconimage
            regex=re.compile('(.+?)_V1.+?.jpg')
            regex1=re.compile('(.+?).gif')
            try:
                    match = regex.search(iconimage1)
                    iconimage= '%s_V1.jpg'%(match.group(1))
            except:
                    pass
            try:    
                    match= regex1.search(iconimage1)
                    iconimage= '%s.gif'%(match.group(1))
            except:
                    pass
                    fanart= iconimage
                    url = 'http://www.imdb.com/title/'+str(url)+'/'
                    name = str(name).replace('&#xB7;','').replace('&#x27;','').replace('&#x2;','And')
                    addDir(name,url,3,iconimage,fanart,series,description,rating)   
                    setView('movies', 'movies-view') 
                    
def EasySearch(name,iconimage,fanart):
        search_entered = str(name).replace(' ','+') .replace(':','') .replace(', ','+').replace(',','+').replace('[','').replace(']',' ').replace('(The)','').replace('(','') .replace(')','') .replace('-','+').replace("'",'+')       
        theurl = 'http://members.easynews.com/global5/index.html?&gps='+search_entered+'&sbj=&from=&ns=&fil=&fex='+mvfn+'&vc=&ac=&fty%5B%5D=VIDEO&s1=nsubject&s1d=%2B&s2=nrfile&s2d=%2B&s3=dsize&s3d=%2B&pby=1000&spamf=1&u=1&svL=&d1=&d1t=&d2=&d2t=&b1=&b1t='+mvfs+'&b2=&b2t=&px1=&px1t=&px2=&px2t=&fps1=&fps1t=&fps2=&fps2t=&bps1=&bps1t=&bps2=&bps2t=&hz1=&hz1t=&hz2=&hz2t=&rn1=&rn1t=&rn2=&rn2t=&fly=2&pno=1&sS=5'
        username = ADDON.getSetting('easy_user')
        password = ADDON.getSetting('easy_pass')
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, theurl, username, password)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
        pagehandle = urllib2.urlopen(theurl)
        link= pagehandle.read()      
        match=re.compile('url="(.+?)" length="(.+?)" type="application/octet-stream" />\n<link>http.+?com/news/.+?/.+?/.+?/.+?/(.+?)</link>').findall(link)
        eng=''
        ger=''
        fre=''
        tur=''
        jap=''
        spa=''
        if re.search('alt=&#34;English', link, re.IGNORECASE):
                eng= 'English'    
        if not re.search('alt=&#34;English', link, re.IGNORECASE):
                eng= ''          
        if re.search('alt=&#34;German', link, re.IGNORECASE):
                ger= 'German' 
        if not re.search('alt=&#34;German', link, re.IGNORECASE):
                ger= ''          
        if re.search('alt=&#34;French', link, re.IGNORECASE):
                fre= 'French'
        if not re.search('alt=&#34;French', link, re.IGNORECASE):
                fre= ''     
        if re.search('alt=&#34;Turkish', link, re.IGNORECASE):
                tur= 'Turkish'
        if not re.search('alt=&#34;Turkish', link, re.IGNORECASE):
                tur= '' 
        if re.search('alt=&#34;Japanese', link, re.IGNORECASE):
                jap= 'Japanese'
        if not re.search('alt=&#34;Japanese', link, re.IGNORECASE):
                jap= ''     
        if re.search('alt=&#34;Spanish', link, re.IGNORECASE):
                spa= 'Spanish'
        if not re.search('alt=&#34;Spanish', link, re.IGNORECASE):
                spa= '' 
        all= '%s\n%s %s %s\n%s %s %s' % ('',eng,ger,fre,tur,jap,spa)
        xbmcgui.Dialog().ok('Found These Languages',str(all))
        for url1 ,filesize, name in match:
            regex = re.compile("http://boost4-downloads.members.easynews.com/news/(.+?)/(.+?)/(.+?)/(.+?)/(.+?)")
            match = regex.search(url1)
            output = "http://boost4-downloads.members.easynews.com/news/%s/%s/%s/pr-%s/pr-%s" %(match.group(1), match.group(2), match.group(3), match.group(4), match.group(5))
            name = '['+str(filesize)+']   '+str(name).replace('%20',' ').replace('%28','(').replace('%29',')')
            changeboost4 = 'http://'+username+':'+password+'@'
            url = str(url1).replace('http://',str(changeboost4))
            iconimage = str(output).replace('http://',str(changeboost4)).replace('.avi','.jpg').replace('.mkv','.jpg') .replace('.wmv','.jpg').replace('.mov','.jpg').replace('.mpg', '.jpg').replace('.asf', '.jpg').replace('.mp4', '.jpg') .replace('.iso', '.jpg').replace('.rm', '.jpg').replace('.flv', '.jpg') 
            addLink(name,url,iconimage,fanart,series,description,rating)  
            setView('movies', 'easy-view') 
    
def TV_POPULAR(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('<img src="(.+?)" height="74" width="54" alt=".+?" title=".+?"></a>\n  </td>\n  <td class="title">\n    \n\n<span class="wlb_wrapper" data-tconst="(.+?)" data-size="small" data-caller-name="search"></span>\n\n    <a href=".+?">(.+?)</a>\n    <span class="year_type">.+?</span><br>\n<div class="user_rating">\n\n\n<div class="rating rating-list" data-auth=".+?" id=".+?" data-ga-identifier="advsearch"\n title=".+?click stars to rate">\n<span class="rating-bg">&nbsp;</span>\n<span class="rating-imdb" style="width.+?">&nbsp;</span>\n<span class="rating-stars">\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>1</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>2</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>3</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>4</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>5</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>6</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>7</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>8</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>9</span></a>\n<a href=".+?" title="Register or login to rate this title" rel="nofollow"><span>10</span></a>\n</span>\n<span class="rating-rating"><span class="value">.+?</span><span class="grey">/</span><span class="grey">10</span></span>\n<span class="rating-cancel"><a href=".+?" title="Delete" rel="nofollow"><span>X</span></a></span>\n&nbsp;</div>\n\n</div>\n<span class="outline">(.+?)</span>').findall(link)
        for iconimage, url, name, description in match:
            iconimage1 = iconimage
            url = 'http://www.imdb.com/title/'+str(url)+'/'
            series = str(name).replace('&#xB7','').replace('&#x27;','').replace('&#x2;','And')
            regex=re.compile('(.+?)_V1.+?.jpg')
            regex1=re.compile('(.+?).gif')
            try:
                    match = regex.search(iconimage1)
                    iconimage= '%s_V1.jpg'%(match.group(1))
            except:
                    pass
            try:    
                    match= regex1.search(iconimage1)
                    iconimage= '%s.gif'%(match.group(1))
            except:
                    pass
                    fanart= iconimage
                    addDir(name,url,10,iconimage,fanart,series,description,rating)   
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
            iconimage1= iconimage
            episode='['+str(episode).replace('26,','26').replace('25,','25').replace('24,','24').replace('23,','23').replace('22,','22').replace('21,','21').replace('20,','20').replace('19,','19').replace('18,','18').replace('17,','17').replace('16,','16').replace('15,','15').replace('14,','14').replace('13,','13').replace('12,','12').replace('11,','11').replace('10,','10').replace('9,','09').replace('8,','08').replace('7,','07').replace('6,','06').replace('5,','05').replace('4,','04').replace('3,','03').replace('2,','02').replace('1,','01').replace('p26','26').replace('p25','25').replace('p24','24').replace('p23','23').replace('p22','22').replace('p21','p21').replace('p20','20').replace('p19','19').replace('p18','18').replace('p17','17').replace('p16','16').replace('p15','15').replace('p14','14').replace('p13','13').replace('p12','12').replace('p11','11').replace('p10','10').replace('p9','09').replace('p8','08').replace('p7','07').replace('p6','06').replace('p5','05').replace('p4','04').replace('p3','03').replace('p2','02').replace('p1','01')+']'
            name= str(episode)+' '+str(name).replace('&#xB7;','').replace('&#x27;','').replace('&#x2;','And')
            series = str(episode)+' '+str(series1)
            regex=re.compile('(.+?)_V1.+?.jpg')
            regex1=re.compile('(.+?).gif')
            try:
                    match = regex.search(iconimage1)
                    iconimage= '%s_V1.jpg'%(match.group(1))
            except:
                    pass
            try:    
                    match= regex1.search(iconimage1)
                    iconimage= '%s.gif'%(match.group(1))
            except:
                    pass
                    fanart= iconimage
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
            iconimage= '%s_V1.jpg'%(match.group(1))
            addDir(name,url,10,iconimage,fanart,series,description,rating)   
            setView('movies', 'seasons-view')
                  
def TV_EASY_SEARCH(series):
        search_entered = str(series).replace(' ','+') .replace(':','') .replace(',','').replace('[','').replace(']','')     
        theurl = 'http://members.easynews.com/global5/index.html?&gps='+search_entered+'&sbj=&from=&ns=&fil=&fex='+tvfn+'&vc=&ac=&fty%5B%5D=VIDEO&s1=nsubject&s1d=%2B&s2=nrfile&s2d=%2B&s3=dsize&s3d=%2B&pby=1000&spamf=1&u=1&svL=&d1=&d1t=&d2=&d2t=&b1=&b1t='+tvfs+'&b2=&b2t=&px1=&px1t=&px2=&px2t=&fps1=&fps1t=&fps2=&fps2t=&bps1=&bps1t=&bps2=&bps2t=&hz1=&hz1t=&hz2=&hz2t=&rn1=&rn1t=&rn2=&rn2t=&fly=2&pno=1&sS=5'
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
        match=re.compile('url="(.+?)" length="(.+?)" type="application/octet-stream" />\n<link>http.+?com/news/.+?/.+?/.+?/.+?/(.+?)</link>').findall(link)
        eng=''
        ger=''
        fre=''
        tur=''
        jap=''
        spa=''
        if re.search('alt=&#34;English', link, re.IGNORECASE):
                eng= 'English'    
        if not re.search('alt=&#34;English', link, re.IGNORECASE):
                eng= ''          
        if re.search('alt=&#34;German', link, re.IGNORECASE):
                ger= 'German' 
        if not re.search('alt=&#34;German', link, re.IGNORECASE):
                ger= ''          
        if re.search('alt=&#34;French', link, re.IGNORECASE):
                fre= 'French'
        if not re.search('alt=&#34;French', link, re.IGNORECASE):
                fre= ''     
        if re.search('alt=&#34;Turkish', link, re.IGNORECASE):
                tur= 'Turkish'
        if not re.search('alt=&#34;Turkish', link, re.IGNORECASE):
                tur= '' 
        if re.search('alt=&#34;Japanese', link, re.IGNORECASE):
                jap= 'Japanese'
        if not re.search('alt=&#34;Japanese', link, re.IGNORECASE):
                jap= ''     
        if re.search('alt=&#34;Spanish', link, re.IGNORECASE):
                spa= 'Spanish'
        if not re.search('alt=&#34;Spanish', link, re.IGNORECASE):
                spa= '' 
        all= '%s\n%s %s %s\n%s %s %s' % ('',eng,ger,fre,tur,jap,spa)
        xbmcgui.Dialog().ok('Found These Languages',str(all))
        for url1 ,filesize, name in match:
            regex = re.compile("http://boost4-downloads.members.easynews.com/news/(.+?)/(.+?)/(.+?)/(.+?)/(.+?)")
            match = regex.search(url1)
            output = "http://boost4-downloads.members.easynews.com/news/%s/%s/%s/pr-%s/pr-%s" %(match.group(1), match.group(2), match.group(3), match.group(4), match.group(5))
            name = '['+str(filesize)+']   '+str(name).replace('%20',' ').replace('%28','(').replace('%29',')')
            changeboost4 = 'http://'+username+':'+password+'@'
            url = str(url1).replace('http://',str(changeboost4))
            iconimage = str(output).replace('http://',str(changeboost4)).replace('.avi','.jpg').replace('.mkv','.jpg') .replace('.wmv','.jpg').replace('.mov','.jpg').replace('.mpg', '.jpg').replace('.asf', '.jpg').replace('.mp4', '.jpg') .replace('.iso', '.jpg').replace('.rm', '.jpg').replace('.flv', '.jpg') 
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
        EasySearch(name,iconimage,fanart)    
        
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
        TMDB_GENRES(url) 
        
elif mode==8:
        print ""+url
        GENRE_LIST(url)  
        
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
                                                     
xbmcplugin.endOfDirectory(int(sys.argv[1]))
