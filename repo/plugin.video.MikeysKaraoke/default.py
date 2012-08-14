import urllib,urllib2,re,sys,xbmcplugin,xbmcgui,xbmcaddon
import settings

ADDON = settings.addon()



def CATEGORIES():
        addDir('Search Mikeys Karaoke','url',3,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Search.png')
        addDir('Browse Artist','http://www.sunflykaraoke.com/',1,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Artist.png')
        addDir('Browse Tracks','http://www.sunflykaraoke.com/',2,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Title.png')
        addDir('Genre','http://www.sunflykaraoke.com/',8,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Genre.png')
        setView('movies', 'MAIN')

def AtoZArtist(url):
        addDir1('0-9','http://www.lyricsmania.com/lyrics/num.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/0-9.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
        addDir1('A','http://www.lyricsmania.com/lyrics/A.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/A.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
        addDir1('B','http://www.lyricsmania.com/lyrics/B.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/B.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg') 
        addDir1('C','http://www.lyricsmania.com/lyrics/C.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/C.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
        addDir1('D','http://www.lyricsmania.com/lyrics/D.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/D.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')        
        addDir1('E','http://www.lyricsmania.com/lyrics/E.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/E.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
        addDir1('F','http://www.lyricsmania.com/lyrics/F.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/F.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg') 
        addDir1('G','http://www.lyricsmania.com/lyrics/G.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/G.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
        addDir1('H','http://www.lyricsmania.com/lyrics/H.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/H.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
        addDir1('I','http://www.lyricsmania.com/lyrics/I.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/I.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
        addDir1('J','http://www.lyricsmania.com/lyrics/J.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/J.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg') 
        addDir1('K','http://www.lyricsmania.com/lyrics/K.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/K.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
        addDir1('L','http://www.lyricsmania.com/lyrics/L.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/L.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')        
        addDir1('M','http://www.lyricsmania.com/lyrics/M.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/M.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
        addDir1('N','http://www.lyricsmania.com/lyrics/N.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/N.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg') 
        addDir1('O','http://www.lyricsmania.com/lyrics/O.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/O.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
        addDir1('P','http://www.lyricsmania.com/lyrics/P.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/P.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg') 
        addDir1('Q','http://www.lyricsmania.com/lyrics/Q.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/Q.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
        addDir1('R','http://www.lyricsmania.com/lyrics/R.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/R.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg') 
        addDir1('S','http://www.lyricsmania.com/lyrics/S.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/S.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
        addDir1('T','http://www.lyricsmania.com/lyrics/T.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/T.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')        
        addDir1('U','http://www.lyricsmania.com/lyrics/U.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/U.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
        addDir1('V','http://www.lyricsmania.com/lyrics/V.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/V.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg') 
        addDir1('W','http://www.lyricsmania.com/lyrics/W.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/W.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
        addDir1('X','http://www.lyricsmania.com/lyrics/X.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/X.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
        addDir1('Y','http://www.lyricsmania.com/lyrics/Y.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/Y.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
        addDir1('Z','http://www.lyricsmania.com/lyrics/Z.html',4,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/Z.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')     
        setView('movies', 'A-Z')
        
def AtoZTracks(url):
        addDir1('A','http://www.sunflykaraoke.com/browse/tracks/a?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/A.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')
        addDir1('B','http://www.sunflykaraoke.com/browse/tracks/b?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/B.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg') 
        addDir1('C','http://www.sunflykaraoke.com/browse/tracks/c?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/C.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')
        addDir1('D','http://www.sunflykaraoke.com/browse/tracks/d?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/D.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')        
        addDir1('E','http://www.sunflykaraoke.com/browse/tracks/e?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/E.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')
        addDir1('F','http://www.sunflykaraoke.com/browse/tracks/f?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/F.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg') 
        addDir1('G','http://www.sunflykaraoke.com/browse/tracks/g?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/G.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')
        addDir1('H','http://www.sunflykaraoke.com/browse/tracks/h?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/H.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')
        addDir1('I','http://www.sunflykaraoke.com/browse/tracks/i?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/I.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')
        addDir1('J','http://www.sunflykaraoke.com/browse/tracks/j?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/J.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg') 
        addDir1('K','http://www.sunflykaraoke.com/browse/tracks/k?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/K.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')
        addDir1('L','http://www.sunflykaraoke.com/browse/tracks/l?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/L.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')        
        addDir1('M','http://www.sunflykaraoke.com/browse/tracks/m?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/M.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')
        addDir1('N','http://www.sunflykaraoke.com/browse/tracks/n?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/N.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg') 
        addDir1('O','http://www.sunflykaraoke.com/browse/tracks/o?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/O.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')
        addDir1('P','http://www.sunflykaraoke.com/browse/tracks/p?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/P.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg') 
        addDir1('Q','http://www.sunflykaraoke.com/browse/tracks/q?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/Q.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')
        addDir1('R','http://www.sunflykaraoke.com/browse/tracks/r?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/R.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg') 
        addDir1('S','http://www.sunflykaraoke.com/browse/tracks/s?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/S.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')
        addDir1('T','http://www.sunflykaraoke.com/browse/tracks/t?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/T.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')        
        addDir1('U','http://www.sunflykaraoke.com/browse/tracks/u?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/U.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')
        addDir1('V','http://www.sunflykaraoke.com/browse/tracks/v?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/V.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg') 
        addDir1('W','http://www.sunflykaraoke.com/browse/tracks/w?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/W.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')
        addDir1('X','http://www.sunflykaraoke.com/browse/tracks/x?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/X.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')
        addDir1('Y','http://www.sunflykaraoke.com/browse/tracks/y?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/Y.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')
        addDir1('Z','http://www.sunflykaraoke.com/browse/tracks/z?pgBrowseTracksAll=&show_BrowseTracksAll=1000',7,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/AtoZ/Z.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg') 
        setView('movies', 'A-Z')
        
def GENRE(url):
        addDir1('40s/50s','http://www.sunflykaraoke.com/search/genre/40-s-and-50-s-pop/song-titles,albums,artists/3429190/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/4050POP.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('60s','http://www.sunflykaraoke.com/search/genre/60-s-pop/song-titles,albums,artists/3429191/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/60POP.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg') 
        addDir1('70s','http://www.sunflykaraoke.com/search/genre/70-s-pop/song-titles,albums,artists/3429192/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/70POP.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('80s','http://www.sunflykaraoke.com/search/genre/80-s-pop/song-titles,albums,artists/3429193/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/80POP.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('90s','http://www.sunflykaraoke.com/search/genre/90-s-pop/song-titles,albums,artists/3429194/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/90POP.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('2000s','http://www.sunflykaraoke.com/search/genre/00-s-pop/song-titles,albums,artists/3429189/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/2000sPOP.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg') 
        addDir1('2010s','http://www.sunflykaraoke.com/search/genre/10-s-pop/song-titles,albums,artists/3429195/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/2010sPOP.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Boybands','http://www.sunflykaraoke.com/search/genre/boybands/song-titles,albums,artists/3429196/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Boybands.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('R&B','http://www.sunflykaraoke.com/search/genre/r-n-b/song-titles,albums,artists/3429220/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/RnB.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Brit Pop','http://www.sunflykaraoke.com/search/genre/brit-pop/song-titles,albums,artists/3429229/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Britpop.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Broadway','http://www.sunflykaraoke.com/search/genre/broadway/song-titles,albums,artists/3429197/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Broadway.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg') 
        addDir1('Elvis','http://www.sunflykaraoke.com/search/genre/elvis/song-titles,albums,artists/3429204/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Elvis.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Childrens','http://www.sunflykaraoke.com/search/genre/children-s/song-titles,albums,artists/3429198/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Childrens.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')        
        addDir1('Christmas','http://www.sunflykaraoke.com/search/genre/christmas/song-titles,albums,artists/3429199/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Christmas.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Comedy','http://www.sunflykaraoke.com/search/genre/comedy/song-titles,albums,artists/3429200/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Comedy.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg') 
        addDir1('Country','http://www.sunflykaraoke.com/search/genre/country/song-titles,albums,artists/3429201/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Country.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Dance','http://www.sunflykaraoke.com/search/genre/dance/song-titles,albums,artists/3429202/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Dance.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg') 
        addDir1('Duets','http://www.sunflykaraoke.com/search/genre/duets/song-titles,albums,artists/3429203/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Duets.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Male Superstars','http://www.sunflykaraoke.com/search/genre/male-superstars/song-titles,albums,artists/3429213/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Male.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Female Superstars','http://www.sunflykaraoke.com/search/genre/female-superstars/song-titles,albums,artists/3429205/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Female.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg') 
        addDir1('Folk','http://www.sunflykaraoke.com/search/genre/folk/song-titles,albums,artists/3429230/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Folk.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Football Anthems','http://www.sunflykaraoke.com/search/genre/football-anthems/song-titles,albums,artists/3429228/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Football.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')        
        addDir1('Foreign','http://www.sunflykaraoke.com/search/genre/foreign/song-titles,albums,artists/3429206/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Foreign.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Funk','http://www.sunflykaraoke.com/search/genre/funk/song-titles,albums,artists/3429231/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Funk.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg') 
        addDir1('Girlbands','http://www.sunflykaraoke.com/search/genre/girlbands/song-titles,albums,artists/3429207/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Girlbands.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Glee','http://www.sunflykaraoke.com/search/genre/glee/song-titles,albums,artists/14196105/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/GAYCUNTS.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Grunge','http://www.sunflykaraoke.com/search/genre/grunge-post-grunge/song-titles,albums,artists/18813424/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Grunge.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Halloween','http://www.sunflykaraoke.com/search/genre/halloween/song-titles,albums,artists/3429208/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Halloween.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg') 
        addDir1('Heavy Metal','http://www.sunflykaraoke.com/search/genre/heavy-metal-alt-metal/song-titles,albums,artists/3429209/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Metal.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Jazz/Blues','http://www.sunflykaraoke.com/search/genre/jazz-blues/song-titles,albums,artists/3429212/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/JazzBlues.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg') 
        addDir1('Indie','http://www.sunflykaraoke.com/search/genre/indie/song-titles,albums,artists/3429210/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Indie.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Irish','http://www.sunflykaraoke.com/search/genre/irish/song-titles,albums,artists/3429211/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Irish.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Medleys','http://www.sunflykaraoke.com/search/genre/medley-s/song-titles,albums,artists/3429214/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Medleys.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Movies & TV','http://www.sunflykaraoke.com/search/genre/movie-s-and-tv/song-titles,albums,artists/3429215/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Movies.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg') 
        addDir1('Multiplex','http://www.sunflykaraoke.com/search/genre/multiplex/song-titles,albums,artists/3429216/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Multiplex.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Punk Rock','http://www.sunflykaraoke.com/search/genre/punk-rock/song-titles,albums,artists/3429217/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/PunkRock.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')        
        addDir1('Rap/Hip-Hop','http://www.sunflykaraoke.com/search/genre/rap-hip-hop/song-titles,albums,artists/3429218/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/HipHop.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg') 
        addDir1('Reggae','http://www.sunflykaraoke.com/search/genre/reggae/song-titles,albums,artists/3429219/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Reggae.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Religious/Gospel','http://www.sunflykaraoke.com/search/genre/religious-gospel/song-titles,albums,artists/3429227/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/GODFREAKS.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Rock','http://www.sunflykaraoke.com/search/genre/rock/song-titles,albums,artists/3429221/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Rock.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Rock & Roll/Disco','http://www.sunflykaraoke.com/search/genre/rock-and-roll-disco/song-titles,albums,artists/3429222/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/RnR.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg') 
        addDir1('Sea Shanties','http://www.sunflykaraoke.com/search/genre/sea-shanties/song-titles,albums,artists/30174405/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Shanties.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg') 
        addDir1('Sing A Long','http://www.sunflykaraoke.com/search/genre/sing-a-long/song-titles,albums,artists/3429223/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Sing.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Skate/Soft Rock','http://www.sunflykaraoke.com/search/genre/skate-soft-rock/song-titles,albums,artists/3429224/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Skate.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg') 
        addDir1('Soul/Motown','http://www.sunflykaraoke.com/search/genre/soul-motown/song-titles,albums,artists/3429225/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Soul.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
        addDir1('Swing/Standards','http://www.sunflykaraoke.com/search/genre/swing-standards/song-titles,albums,artists/3429226/?pg_Song%20Titles=&show_Song%20Titles=500&sort_Song%20Titles=popularity-desc',10,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Genre/Swing.png','http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg') 
        setView('movies', 'GENRE')

def SEARCH(url):
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, 'Search Mikeys Karaoke...XBMCHUB.COM')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText() .replace(' ','+')  # sometimes you need to replace spaces with + or %20#
            if search_entered == None:
                return False
            ADDON.setSetting('history_10', ADDON.getSetting('history_9'))
            ADDON.setSetting('history_9', ADDON.getSetting('history_8'))
            ADDON.setSetting('history_8', ADDON.getSetting('history_7'))
            ADDON.setSetting('history_7', ADDON.getSetting('history_6'))
            ADDON.setSetting('history_6', ADDON.getSetting('history_5'))
            ADDON.setSetting('history_5', ADDON.getSetting('history_4'))
            ADDON.setSetting('history_4', ADDON.getSetting('history_3'))
            ADDON.setSetting('history_3', ADDON.getSetting('history_2'))
            ADDON.setSetting('history_2', ADDON.getSetting('history_1'))
            ADDON.setSetting('history_1', search_entered)               
        url = 'http://m.youtube.com/results?gl=GB&client=mv-google&hl=en-GB&q=%s+karaoke&submit=Search' % (search_entered)        
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('&amp;v=(.+?)">(.+?)\n').findall(link)
        for url, name in match:
            name = str(name).replace("&#39;","'") .replace("&amp;","and") .replace("&#252;","u") .replace("&quot;","")
            iconimage = 'http://i.ytimg.com/vi/%s/0.jpg' % url
            url = 'plugin://plugin.video.youtube/?path=root/video&action=play_video&videoid=%s' % url
            addLink(name,url,iconimage)        
            setView('movies', 'VIDEO')
                                                                     
def ARTIST_INDEX(url, iconimage):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('<li><a href="(.+?)" title="(.+?)">.+?</a></li>').findall(link)
        for url, name in match:
            url = 'http://www.lyricsmania.com'+url   
            name = str(name).replace("lyrics","")
            addDir1(name,url,5,iconimage,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg')
            setView('tvshows', 'DEFAULT')


def ARTIST_SONG_INDEX(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('<a href="(.+?)">.+? in alphabetical order</a></b><br>').findall(link)
        url1 = 'http://www.lyricsmania.com'+match[0]
        req1 = urllib2.Request(url1)
        req1.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response1 = urllib2.urlopen(req1)
        link1=response1.read()
        response1.close()
        match1 = re.compile('<a href=".+?_lyrics_(.+?).html" title="(.+?) lyrics">').findall(link1)
        try:
                thumb = 'http://www.htbackdrops.com/v2/thumbnails.php?search=%s&submit=search&album=search&title=checked&caption=checked&keywords=checked&type=AND' % str(name).replace(", ","+").replace("(The)","").replace(" ","+")
                print thumb
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
        	    iconimage= 'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Artist.png'
        try:
                fanart = 'http://www.htbackdrops.com/v2/%s' % str(normal).replace('thumb_','')
        except:
        	    fanart = 'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_A.jpg'
        print iconimage
        print fanart	    
        for url, name, in match1:
            name = str(name).replace("&Agrave;","A").replace('&eacute;','e').replace('&ecirc;','e').replace('&egrave;','e').replace("&agrave;","A")
            addDir1(name,url,6,iconimage,fanart)
            setView('tvshow', 'DEFAULT')
            
def TRACK_INDEX(url, iconimage):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('target="_self">(.+?)</a></td><td class="listing-col-artist"><a href=".+?" target="_self">(.+?)</a>').findall(link)
        uniques = []
        for name, url, in match:
            if name not in uniques and url not in uniques:
                uniques.append(name)
                uniques.append(url)
                name = str(name).replace("&#39;","'") .replace("&amp;","and") .replace("&#252;","u") .replace("&quot;","")  
                url = str(url).replace("&#39;","'") .replace("&amp;","and") .replace("&#252;","u") .replace("&quot;","") 
                name = name+ '   ('+ url+')'
                addDir1(name,url,9,iconimage,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_T.jpg')
                setView('tvshows', 'DEFAULT')
                
def GENRE_INDEX(url, iconimage):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('target="_self">(.+?)</a></td><td class="listing-col-artist"><a href=".+?" target="_self">(.+?)</a>').findall(link)
        for name, url, in match:
	        name = str(name).replace("&#39;","'") .replace("&amp;","and") .replace("&#252;","u") .replace("&quot;","")  
	        url = str(url).replace("&#39;","'") .replace("&amp;","and") .replace("&#252;","u") .replace("&quot;","") 
	        name = name+ '   ('+ url+')'
	        addDir1(name,url,9,iconimage,'http://live-tv-stream.googlecode.com/svn/Karaoke%20Icons/Main/Fanart_G.jpg')
	        setView('tvshows', 'DEFAULT')

def YOUTUBE_SONG_INDEX(name, url, iconimage, fanart):
        url = str(url).replace(' ','+').replace('_','+')  
        name = str(name).replace(' ','+') 
        url = 'http://m.youtube.com/results?gl=GB&client=mv-google&hl=en-GB&q=%s+%s+karaoke&submit=Search' % (name, url) 
        print url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('&amp;v=(.+?)">(.+?)\n').findall(link)
        for url, name in match:
            iconimage = 'http://i.ytimg.com/vi/%s/0.jpg' % url
            name = str(name).replace("&amp;#39;","'").replace("&#252;","u") .replace('&amp;quot;','"').replace("&amp;amp;","&")
            url = 'plugin://plugin.video.youtube/?path=root/video&action=play_video&videoid=%s' % url
            addLink1(name,url,iconimage,fanart)        
            setView('movies', 'VIDEO')
            
def TITLE_ORDERS_YOUTUBE(name, url,fanart):
        name = str(name).replace('   (','+') .replace(' ','+') .replace(')','')
        url = 'http://m.youtube.com/results?gl=GB&client=mv-google&hl=en-GB&q=%s+karaoke&submit=Search' % (name) 
        print url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('&amp;v=(.+?)">(.+?)\n').findall(link)
        for url, name in match:
            iconimage = 'http://i.ytimg.com/vi/%s/0.jpg' % url
            name = str(name).replace("&amp;#39;","'").replace("&#252;","u") .replace('&amp;quot;','"').replace("&amp;amp;","&")
            url = 'plugin://plugin.video.youtube/?path=root/video&action=play_video&videoid=%s' % url
            addLink1(name,url,iconimage,fanart)        
            setView('movies', 'VIDEO')
            
            
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
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
def addDir1(name,url,mode,iconimage,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty( "Fanart_Image", fanart )
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
def addLink(name,url,iconimage):
                ok=True
                liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
                liz.setInfo( type="Video", infoLabels={ "Title": name } )
                liz.setProperty("IsPlayable","true")
                ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
                return ok 
                
def addLink1(name,url,iconimage, fanart):
                u=sys.argv[0]+"&fanart="+urllib.quote_plus(fanart)
                ok=True
                liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
                liz.setInfo( type="Video", infoLabels={ "Title": name } )
                liz.setProperty("IsPlayable","true")
                liz.setProperty("Fanart_Image", fanart )
                ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
                return ok 
                      
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
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
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
                
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
print "FanartImage: "+str(fanart)


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
        AtoZArtist(url)
        
elif mode==2:
        print ""+url
        AtoZTracks(url)

elif mode==3:
        print ""+url
        SEARCH(url)
        
elif mode==4:
        print ""+url +iconimage
        ARTIST_INDEX(url, iconimage) 
        
elif mode==5:
        print ""+url+name
        ARTIST_SONG_INDEX(url,name)
        
elif mode==6:
        print ""+name +url
        YOUTUBE_SONG_INDEX(name, url, iconimage, fanart)
                                                             
elif mode==7:
        print ""+url +iconimage
        TRACK_INDEX(url, iconimage)
        
elif mode==8:
        print ""+url
        GENRE(url)   
        
elif mode==9:
        print ""+name, url, fanart
        TITLE_ORDERS_YOUTUBE(name, url, fanart)   
        
elif mode==10:
        print ""+url +iconimage
        GENRE_INDEX(url, iconimage)              
              
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
