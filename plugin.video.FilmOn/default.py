import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,base64,datetime


#Global Constants
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
ADDON = xbmcaddon.Addon(id='plugin.video.FilmOn')
channel= 'http://www.filmon.com/channel/'
logo = 'http://static.filmon.com/couch/channels/'

        
def CATEGORIES():
        addDir('FilmOn With Epg Main Channels','http://www.filmon.com/tvguide/',1,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('UK TV Channels','url',6,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Local Channels','url',3,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('SportsChannels','url',4,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Music Channels','url',5,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Premium Channels','url',7,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Comedy Channels','url',8,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Asian Channels','url',9,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Movie Channels','url',10,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Lifestyle Channels','url',11,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Kids Channels','url',12,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Education Channels','url',13,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Religious Channels','url',14,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Horror Channels','url',15,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('News Channels','url',16,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Bikini Channels','url',17,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Arabic Channels','url',18,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Galaxie Music Channels','url',19,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('German Channels','url',20,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Latin Channels','url',21,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Documentary Channels','url',22,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Italian Channels','url',23,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Mind Body And Spirit Channels','url',24,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Free Channels','url',25,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Shopping Channels','url',26,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Main Channels','url',27,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        addDir('Interactive Channels','url',28,'http://a3.mzstatic.com/us/r1000/065/Purple/a8/0d/f0/mzl.otgnsovy.png','')
        setView('movies', 'default') 
        
def LocalChannels(url):
        addDir('Filmon Live',channel+'live',2,logo+'689/big_logo.png','')
        addDir('CBS Palo Alto',channel+'cbs-palo-alto',2,logo+'967/big_logo.png','')
        addDir('ABC Palo Alto',channel+'abc-palo-alto',2,logo+'970/big_logo.png','')
        addDir('NBC Palo Alto',channel+'nbc-palo-alto',2,logo+'973/big_logo.png','')
        addDir('Fox Palo Alto',channel+'fox-palo-alto',2,logo+'976/big_logo.png','')
        addDir('TV5Monde Europe',channel+'tv5monde-europe',2,logo+'517/big_logo.png','')
        addDir('BLU',channel+'blu',2,logo+'448/big_logo.png','')
        addDir('Canal+ TV',channel+'canal',2,logo+'363/big_logo.png','')
        setView('movies', 'default') 
        
def SportsChannels(url):
        addDir('Filmon Football',channel+'filmon-football',2,logo+'374/big_logo.png','')
        addDir('Filmon Collage Basekitball',channel+'filmon-college-basketball',2,logo+'485/big_logo.png','')
        addDir('Filmon Collage Football',channel+'filmon-college-football',2,logo+'488/big_logo.png','')
        addDir('X-Treme Sports',channel+'x-treme-sports',2,logo+'326/big_logo.png','')
        addDir('Masked Republic AAA Lucha Libre',channel+'masked-republic-aaa-lucha-libre',2,logo+'802/big_logo.png','')
        addDir('UFC Next',channel+'ufc-next',2,logo+'713/big_logo.png','')
        addDir('Skiers World TV',channel+'skiers-world-tv',2,logo+'408/big_logo.png','')
        addDir('NWA Wrestling',channel+'nwa-wrestling',2,logo+'373/big_logo.png','')
        addDir('Thats Boating TV',channel+'thats-boating-tv',2,logo+'388/big_logo.png','')
        addDir('Eighteen Holes TV',channel+'eighteen-holes-tv',2,logo+'389/big_logo.png','')
        addDir('Badass Sports TV',channel+'badass-sports-tv',2,logo+'391/big_logo.png','')
        addDir('Pursuit Channel',channel+'pursuit-channel',2,logo+'349/big_logo.png','')
        addDir('Dubai Sports',channel+'dubai-sports',2,logo+'79/big_logo.png','')
        setView('movies', 'default') 
        
def MusicChannels(url):
        addDir('Filmon Jazz and Blues',channel+'filmon-jazz-and-blues',2,logo+'530/big_logo.png','')
        addDir('JCTV Music',channel+'jctv',2,logo+'400/big_logo.png','')
        addDir('The Noise Network',channel+'the-noise-network',2,logo+'385/big_logo.png','')
        addDir('Urban Music Network',channel+'urban-music-network',2,logo+'347/big_logo.png','')
        addDir('The Soundtrack Channel',channel+'the-soundtrack-channel',2,logo+'350/big_logo.png','')
        addDir('THe Country Network',channel+'the-country-network',2,logo+'342/big_logo.png','')
        addDir('Classic Arts Showcase',channel+'classic-arts-showcase',2,logo+'309/big_logo.png','')
        addDir('Filmon Rock TV',channel+'filmon-rock-tv',2,logo+'311/big_logo.png','')
        addDir('4 Music',channel+'4-music',2,logo+'95/big_logo.png','')
        addDir('Viva',channel+'viva',2,logo+'8/big_logo.png','')
        addDir('Film On Music Legends TV',channel+'filmon-music-legends-tv',2,logo+'257/big_logo.png','')
        setView('movies', 'default') 
        
def UkTvChannels(url):
        addDir('BBC One',channel+'bbc-one',2,logo+'14/big_logo.png','')
        addDir('BBC Two',channel+'bbc-two',2,logo+'25/big_logo.png','')
        addDir('ITV1',channel+'itv1',2,logo+'11/big_logo.png','')
        addDir('Channel 4',channel+'channel-4',2,logo+'2/big_logo.png','')
        addDir('Channel 5',channel+'channel-5',2,logo+'22/big_logo.png','')
        addDir('ITV2',channel+'itv2',2,logo+'67/big_logo.png','')
        addDir('ITV3',channel+'itv3',2,logo+'26/big_logo.png','')
        addDir('ITV4',channel+'itv4',2,logo+'101/big_logo.png','')
        addDir('E4',channel+'e4',2,logo+'65/big_logo.png','')
        addDir('More4',channel+'more4',2,logo+'97/big_logo.png','')
        addDir('5USA',channel+'5usa',2,logo+'845/big_logo.png','')
        addDir('5USA+1',channel+'5usa1',2,logo+'848/big_logo.png','')
        addDir('5*',channel+'5',2,logo+'851/big_logo.png','')
        addDir('5*+1',channel+'51',2,logo+'854/big_logo.png','')
        addDir('Channel5+1',channel+'channel51',2,logo+'857/big_logo.png','')
        addDir('Dave',channel+'dave',2,logo+'370/big_logo.png','')
        addDir('Pick TV',channel+'pick-tv',2,logo+'371/big_logo.png','')
        addDir('Really',channel+'really',2,logo+'372/big_logo.png','')
        addDir('BBC1 North Island',channel+'bbc-1-north-ireland',2,logo+'361/big_logo.png','')
        addDir('CBBC/BBC Three',channel+'cbbcbbc-three',2,logo+'113/big_logo.png','')
        addDir('CBEEBIES/BBC Four',channel+'cbeebiesbbc-four',2,logo+'103/big_logo.png','')
        addDir('BBC News',channel+'bbc-news',2,logo+'27/big_logo.png','')
        setView('movies', 'default') 
        
def PremiumChannels(url):
        addDir('World of Martial Arts Television',channel+'world-of-martial-arts-television',2,logo+'406/big_logo.png','')
        addDir('Ginx',channel+'ginx',2,logo+'796/big_logo.png','')
        addDir('Ebru',channel+'ebru',2,logo+'914/big_logo.png','')
        addDir('Halogen TV',channel+'halogen-tv',2,logo+'703/big_logo.png','')
        addDir('HRTV',channel+'hrtv',2,logo+'694/big_logo.png','')
        addDir('Clubbing TV',channel+'clubbing-tv',2,logo+'691/big_logo.png','')
        addDir('Sportskool',channel+'sportskool',2,logo+'686/big_logo.png','')
        addDir('The Ski Channel',channel+'the-ski-channel',2,logo+'265/big_logo.png','')
        addDir('Untamed Sports',channel+'untamed-sports',2,logo+'436/big_big_logo.png','')
        addDir('Parables TV',channel+'parables-tv',2,logo+'405/big_logo.png','')
        addDir('Wealth TV',channel+'wealth-tv',2,logo+'403/big_logo.png','')
        addDir('R&R Television',channel+'rr-television',2,logo+'402/big_logo.png','')
        addDir('WW Extreme',channel+'ww-extreme',2,logo+'394/big_logo.png','')
        addDir('Filmon Reels',channel+'filmon-reels',2,logo+'395/big_logo.png','')
        addDir('Wheels TV',channel+'wheels-tv',2,logo+'397/big_logo.png','')
        addDir('American Horrors',channel+'american-horrors',2,logo+'393/big_logo.png','')
        addDir('e Scapes HD TV',channel+'escapes-hd-tv',2,logo+'341/big_logo.png','')
        addDir('Havoc Television',channel+'havoc-television',2,logo+'335/big_logo.png','')
        addDir('My Family TV',channel+'my-family-tv',2,logo+'301/big_logo.png','')
        addDir('My Combat Channel',channel+'my-combat-channel',2,logo+'295/big_logo.png','')
        addDir('Fashion TV',channel+'fashion-tv',2,logo+'21/big_logo.png','')
        addDir('TVC Latino',channel+'tvc-latino',2,logo+'213/big_logo.png','')
        addDir('Filmon Breaking News',channel+'filmon-breaking-news',2,logo+'302/big_logo.png','')
        setView('movies', 'default')
         
def ComedyChannels(url):
        addDir('Filmon at the Improv',channel+'filmon-at-the-improv',2,logo+'407/big_logo.png','')
        addDir('Popcorn TV',channel+'popcorn-tv',2,logo+'716/big_logo.png','')
        addDir('Comedy Net',channel+'comedy-net',2,logo+'497/big_logo.png','')
        addDir('Kevin Spencer TV',channel+'kevin-spencer-tv',2,logo+'387/big_logo.png','')
        addDir('ComedyTime TV',channel+'comedytime-tv',2,logo+'344/big_logo.png','')
        setView('movies', 'default') 
        
def AsianChannels(url):
        addDir('Arirang TV',channel+'arirang-tv',2,logo+'932/big_logo.png','')
        setView('movies', 'default') 
        
def MovieChannels(url):
        addDir('MyFamily TV East',channel+'myfamily-tv-east',2,logo+'779/big_logo.png','')
        addDir('American Primetime Television',channel+'american-primetime-television',2,logo+'707/big_logo.png','')
        addDir('Filmon Martial Arts',channel+'filmon-martial-arts',2,logo+'10/big_logo.png','')
        addDir('Threshold',channel+'threshold',2,logo+'514/big_logo.png','')
        addDir('Filmon Stars',channel+'filmon-stars',2,logo+'494/big_logo.png','')
        addDir('Action Cinema',channel+'mbc-action',2,logo+'369/big_logo.png','')
        addDir('Inspirational Films',channel+'inspirational-films',2,logo+'503/big_logo.png','')
        addDir('Hollywoodland Channel',channel+'hollywoodland-channel',2,logo+'411/big_logo.png','')
        addDir('Sci-Fi Channel',channel+'sci-fi-telly',2,logo+'382/big_logo.png','')
        addDir('The Western Channel',channel+'the-western-channel',2,logo+'384/big_logo.png','')
        addDir('Cultra',channel+'cultra',2,logo+'336/big_logo.png','')
        addDir('Filmon Grab Bag TV',channel+'filmon-grab-bag-tv',2,logo+'310/big_logo.png','')
        addDir('Film 4',channel+'film-4',2,logo+'13/big_logo.png','')
        addDir('Filmon Classics',channel+'filmon-classics',2,logo+'206/big_logo.png','')
        setView('movies', 'default') 
        
def LifestyleChannels(url):
        addDir('Buzz TV',channel+'buzz-tv',2,logo+'782/big_logo.png','')
        addDir('Steel Dreams',channel+'steel-dreams',2,logo+'784/big_logo.png','')
        addDir('Distant Roads',channel+'distant-roads',2,logo+'787/big_logo.png','')
        addDir('Travel Channel+1',channel+'travel-channel1',2,logo+'842/big_logo.png','')
        addDir('AMG TV',channel+'amg-tv',2,logo+'902/big_logo.png','')
        addDir('Eye for an Eye',channel+'eye-for-an-eye',2,logo+'911/big_logo.png','')
        addDir('PopStop TV',channel+'popstop-tv',2,logo+'770/big_logo.png','')
        addDir('The Miki Show',channel+'the-miki-show',2,logo+'728/big_logo.png','')
        addDir('INSP',channel+'insp',2,logo+'700/big_logo.png','')
        addDir('Eco-Rico',channel+'eco-rico',2,logo+'710/big_logo.png','')
        addDir('Men7',channel+'men7',2,logo+'396/big_logo.png','')
        addDir('Veg TV',channel+'veg-tv',2,logo+'383/big_logo.png','')
        addDir('GeoBeats Travel',channel+'geobeats-travel',2,logo+'386/big_logo.png','')
        addDir('Legacy TV',channel+'legacy-tv',2,logo+'340/big_logo.png','')
        addDir('Jewish Life TV',channel+'jewish-life-tv',2,logo+'332/big_logo.png','')
        addDir('Time tv',channel+'time-tv',2,logo+'414/big_logo.png','')
        addDir('Unreliable Sources',channel+'unreliable-sources',2,logo+'239/big_logo.png','')
        addDir('Motorz',channel+'motorz',2,logo+'262/big_logo.png','')
        addDir('Wine',channel+'wine-channel-tv',2,logo+'263/big_logo.png','')
        setView('movies', 'default') 
        
def KidsChannels(url):
        addDir('Kartoon Klassics',channel+'kartoon-klassics',2,logo+'793/big_logo.png','')
        addDir('Animal Atlas',channel+'animal-atlas',2,logo+'799/big_logo.png','')
        addDir('Emba Kids',channel+'emba-kids',2,logo+'719/big_logo.png','')
        addDir('Smile of Child',channel+'smile-of-child',2,logo+'401/big_logo.png','')

def EducationChannels(url):
        addDir('UWTV',channel+'uwtv',2,logo+'808/big_logo.png','')
        addDir('The Florida Channel',channel+'the-florida-channel',2,logo+'305/big_logo.png','')

def ReligiousChannels(url):
        addDir('DayStar',channel+'daystar',2,logo+'833/big_logo.png','')
        addDir('TBN',channel+'tbn',2,logo+'398/big_logo.png','')
        addDir('The Church Channel',channel+'the-church-channel',2,logo+'399/big_logo.png','')
        setView('movies', 'default') 
        
def HorrorChannels(url):
        addDir('Horror Channel',channel+'horror-channel',2,logo+'836/big_logo.png','')
        addDir('ShockORama',channel+'shockorama',2,logo+'509/big_logo.png','')
        addDir('Braindamage TV',channel+'braindamage-tv',2,logo+'339/big_logo.png','')
        addDir('Macare Theatre',channel+'macabre-theatre',2,logo+'315/big_logo.png','')
        addDir('RSquared',channel+'rsquared',2,logo+'256/big_logo.png','')
        setView('movies', 'default')
         
def NewsChannels(url):
        addDir('CNBC',channel+'cnbc',2,logo+'860/big_logo.png','')
        addDir('DVIDs TV',channel+'dvids-tv',2,logo+'725/big_logo.png','')
        addDir('Free Speech TV',channel+'free-speech-tv',2,logo+'697/big_logo.png','')
        addDir('Biz TV',channel+'biztv',2,logo+'343/big_logo.png','')
        addDir('WeatherNation',channel+'weathernation',2,logo+'329/big_logo.png','')
        addDir('NASA HD',channel+'nasa-hd',2,logo+'330/big_logo.png','')
        addDir('The Pentagon',channel+'the-pentagon',2,logo+'333/big_logo.png','')
        addDir('France24',channel+'france24',2,logo+'298/big_logo.png','')
        addDir('Russia Today',channel+'russia-today-2',2,logo+'93/big_logo.png','')
        addDir('AL Jazeera',channel+'al-jazeera',2,logo+'4/big_logo.png','')
        addDir('Bloomberg',channel+'bloomberg',2,logo+'81/big_logo.png','')
        setView('movies', 'default')
         
def BikiniChannels(url):
        addDir('MiamiTV',channel+'miamitv',2,logo+'866/big_logo.png','')
        addDir('Bikini TeeVee',channel+'bikini-teevee',2,logo+'380/big_logo.png','')
        addDir('Party TeeVee',channel+'party-teevee',2,logo+'790/big_logo.png','')
        setView('movies', 'default') 
        
def ArabicChannels(url):
        addDir('iFilm',channel+'ifilm',2,logo+'908/big_logo.png','')
        addDir('MBC',channel+'mbc',2,logo+'367/big_logo.png','')
        addDir('MBC2',channel+'mbc2',2,logo+'368/big_logo.png','')
        addDir('MBC Action',channel+'mbc-action',2,logo+'369/big_logo.png','')
        setView('movies', 'default') 
        
def GalaxieMusicChannels(url):
        addDir('GALAXIE ADULT ALTERNATIVE',channel+'galaxie-adult-alternative',2,logo+'536/big_logo.png','')
        addDir('GALAXIE CLASSIC MASTERS',channel+'galaxie-classic-masters',2,logo+'539/big_logo.png','')
        addDir('GALAXIE CLASSIC ROCK',channel+'galaxie-classic-rock',2,logo+'542/big_logo.png','')
        addDir('GALAXIE COUNTRY CLASSICS',channel+'galaxie-country-classics',2,logo+'545/big_logo.png','')
        addDir('GALAXIE EASY LISTENING',channel+'galaxie-easy-listening',2,logo+'548/big_logo.png','')
        addDir('GALAXIE FLASHBACK 70S',channel+'galaxie-flashback-70s',2,logo+'551/big_logo.png','')
        addDir('GALAXIE FOLK ROOTS',channel+'galaxie-folk-roots',2,logo+'554/big_logo.png','')
        addDir('GALAXIE HIT LIST',channel+'galaxie-hit-list',2,logo+'557/big_logo.png','')
        addDir('GALAXIE HOT COUNTRY',channel+'galaxie-hot-country',2,logo+'560/big_logo.png','')
        addDir('GALAXIE JAMMIN',channel+'galaxie-jammin',2,logo+'563/big_logo.png','')
        addDir('GALAXIE JAZZ MASTERS',channel+'galaxie-jazz-masters',2,logo+'566/big_logo.png','')
        addDir('GALAXIE JUKEBOX OLDIES',channel+'galaxie-jukebox-oldies',2,logo+'569/big_logo.png','')
        addDir('GALAXIE KIDS STUFF',channel+'galaxie-kids-stuff',2,logo+'572/big_logo.png','')
        addDir('GALAXIE LATINO TROPICAL',channel+'galaxie-latino-tropical',2,logo+'575/big_logo.png','')
        addDir('GALAXIE POP ADULT',channel+'galaxie-pop-adult',2,logo+'578/big_logo.png','')
        addDir('GALAXIE POP CLASSICS',channel+'galaxie-pop-classics',2,logo+'581/big_logo.png','')
        addDir('GALAXIE EVERTHING 80S',channel+'galaxie-everything-80s',2,logo+'584/big_logo.png','')
        addDir('GALAXIE ROCK',channel+'galaxie-rock',2,logo+'587/big_logo.png','')
        addDir('GALAXIE ROCK ALTERNAIVE',channel+'galaxie-rock-alternative',2,logo+'590/big_logo.png','')
        addDir('GALAXIE SMOOTH JAZZ',channel+'galaxie-smooth-jazz',2,logo+'593/big_logo.png','')
        addDir('GALAXIE SOUL STORM',channel+'galaxie-soul-storm',2,logo+'596/big_logo.png','')
        addDir('GALAXIE STANDARDS',channel+'galaxie-standards',2,logo+'599/big_logo.png','')
        addDir('GALAXIE THE BLUES',channel+'galaxie-the-blues',2,logo+'602/big_logo.png','')
        addDir('GALAXIE THE LIGHT',channel+'galaxie-the-light',2,logo+'605/big_logo.png','')
        addDir('GALAXIE URBAN BEATS',channel+'galaxie-urban-beats',2,logo+'608/big_logo.png','')
        addDir('GALAXIE NOTHIN BUT THR 90`s',channel+'galaxie-nothin-but-90s',2,logo+'611/big_logo.png','')
        addDir('GALAXIE MAXIMIM PARTY',channel+'galaxie-maximum-party',2,logo+'614/big_logo.png','')
        addDir('GALAXIE DANCE CLUBBIN',channel+'galaxie-dance-clubbn',2,logo+'617/big_logo.png','')
        addDir('GALXAIE BLUEGRASS',channel+'galaxie-bluegrass',2,logo+'620/big_logo.png','')
        addDir('GALAXIE BIG BAND',channel+'galaxie-big-band',2,logo+'623/big_logo.png','')
        addDir('GALAXIE JAZZ NOW',channel+'galaxie-jazz-now',2,logo+'626/big_logo.png','')
        addDir('GALAXIE THE CHILL LOUNGE',channel+'galaxie-the-chill-lounge',2,logo+'629/big_logo.png','')
        addDir('GALAXIE THE SPA',channel+'galaxie-the-spa',2,logo+'632/big_logo.png','')
        addDir('GALAXIE BAROQUE',channel+'galaxie-baroque',2,logo+'635/big_logo.png','')
        addDir('GALAXIE OPERA PLUS',channel+'galaxie-opera-plus',2,logo+'638/big_logo.png','')
        addDir('GALAXIE CHAMBER MUSIC',channel+'galaxie-chamber-music',2,logo+'641/big_logo.png','')
        addDir('GALAXIE TODAYS LATIN POP',channel+'galaxie-todays-latin-pop',2,logo+'644/big_logo.png','')
        addDir('GALAXIE RETRO R&B',channel+'galaxie-retro-rb',2,logo+'647/big_logo.png','')
        addDir('GALAXIE NO FENCES',channel+'galaxie-no-fences',2,logo+'650/big_logo.png','')
        addDir('GALAXIE DANCE CLASSICS',channel+'galaxie-dance-classics',2,logo+'653/big_logo.png','')
        addDir('GALAXIE HOLIDAY HITS',channel+'galaxie-holiday-hits',2,logo+'656/big_logo.png','')
        addDir('GALAXIE HARD ROCK',channel+'galaxie-hard-rock',2,logo+'659/big_logo.png','')
        addDir('GALAXIE ALT ROCK CLASSICS',channel+'galaxie-alt-rock-classics',2,logo+'662/big_logo.png','')
        addDir('GALAXIE ROCK ALT-COUNTRY AMERICANA',channel+'galaxie-rock-alt-country-americana',2,logo+'665/big_logo.png','')
        addDir('GALAXIE GOSPEL',channel+'galaxie-gospel',2,logo+'668/big_logo.png','')
        addDir('GALAXIE CELTIC',channel+'galaxie-celtic',2,logo+'671/big_logo.png''')
        addDir('GALAXIE RETRO LATINO',channel+'galaxie-retro-latino',2,logo+'674/big_logo.png','')
        addDir('GALAXIE LATINO URBANA',channel+'galaxie-latino-urbana',2,logo+'677/big_logo.png','')
        addDir('GALAXIE LATINO TEJANO',channel+'galaxie-latino-tejano',2,logo+'680/big_logo.png','')
        addDir('GALAXIE REGIONAL MEXICAN',channel+'galaxie-regional-mexiana',2,logo+'683/big_logo.png','')
        setView('movies', 'default') 
        
def GermanChannels(url):
        addDir('ProSieben Austria',channel+'prosieben-austria',2,logo+'520/big_logo.png','')
        addDir('Eins Extra',channel+'eins-extra',2,logo+'415/big_logo.png','')
        addDir('Eins Plus',channel+'eins-plus',2,logo+'418/big_logo.png','')
        addDir('Eins Festival',channel+'eins-festival',2,logo+'421/big_logo.png','')
        addDir('QVC Deutschland',channel+'qvc-deutschland',2,logo+'354/big_logo.png','')
        addDir('QVC PLUS',channel+'qvc-plus',2,logo+'355/big_logo.png','')
        addDir('zdf.kultur',channel+'zdfkultur',2,logo+'359/big_logo.png','')
        addDir('ZDFneo',channel+'zdfneo',2,logo+'360/big_logo.png','')
        setView('movies', 'default') 
        
def LatinChannels(url):
        addDir('Andalucia TV',channel+'andalucia-tv',2,logo+'526/big_logo.png','')
        addDir('Telemadrid',channel+'telemadrid',2,logo+'529/big_logo.png','')
        addDir('RT Espanol',channel+'rt-espaaol',2,logo+'299/big_logo.png','')
        addDir('RTVE',channel+'rtve',2,logo+'23/big_logo.png','')
        addDir('RTpi America',channel+'rtpi-america',2,logo+'303/big_logo.png','')
        setView('movies', 'default') 
        
def DocumentaryChannels(url):
        addDir('War in Color',channel+'war-in-color',2,logo+'491/big_logo.png','')
        addDir('War and Crime',channel+'war-crime-network',2,logo+'381/big_logo.png','')
        setView('movies', 'default') 
        
def ItalianChannels(url):
        addDir('QVC Italia',channel+'qvc-italia',2,logo+'463/big_logo.png','')
        addDir('Canale Italia 84',channel+'canale-italia-84',2,logo+'442/big_logo.png','')
        addDir('Canale Italia',channel+'canale-italia',2,logo+'445/big_logo.png','')
        addDir('Studio Europa',channel+'studio-europa',2,logo+'451/big_logo.png','')
        addDir('Justice TV',channel+'justice-tv',2,logo+'454/big_logo.png','')
        addDir('RAI 1',channel+'rai-1',2,logo+'375/big_logo.png','')
        addDir('RAI 2',channel+'rai-2',2,logo+'376/big_logo.png','')
        addDir('RAI 3',channel+'rai-3',2,logo+'377/big_logo.png','')
        addDir('Camera dei Deputati',channel+'camera-dei-deputati',2,logo+'379/big_logo.png','')
        setView('movies', 'default') 
        
def MindBodyAndSpiritChannels(url):
        addDir('Fitness Lifestyle TV',channel+'fitness-lifestyle-tv',2,logo+'410/big_logo.png','')
        addDir('Cornerstone TV',channel+'cornerstone-tv',2,logo+'212/big_logo.png','')
        addDir('Supreme Master TV',channel+'supreme-master-tv',2,logo+'304/big_logo.png','')
        setView('movies', 'default') 
        
def FreeChannels(url):
        addDir('Linkct Network',channel+'linkct-network',2,logo+'390/big_logo.png','')
        setView('movies', 'default') 
        
def ShoppingChannels(url):
        addDir('QVC HD',channel+'qvc-hd',2,logo+'413/big_logo.png','')
        addDir('9021go TV',channel+'9021go-tv',2,logo+'214/big_logo.png','')
        addDir('Jewelry TV',channel+'jewelry-tv',2,logo+'306/big_logo.png','')
        setView('movies', 'default') 
        
def MainChannels(url):
        addDir('Phoenix',channel+'phoenix',2,logo+'424/big_logo.png','')
        setView('movies', 'default') 
        
def InteractiveChannels(url):
        addDir('Battlecam People',channel+'battlecam-people',2,logo+'324/big_logo.png','')
        addDir('PPV Celebrity Fight',channel+'ppv-celebrity-fight',2,logo+'412/big_logo.png','')
        addDir('Janice TV',channel+'janice-tv',2,logo+'460/big_logo.png','')
        addDir('Dave Live',channel+'davelive',2,logo+'733/big_logo.png','')
        addDir('Kato',channel+'kato',2,logo+'758/big_logo.png','')
        addDir('Situation',channel+'situation',2,logo+'761/big_logo.png','')
        addDir('Rampage',channel+'rampage',2,logo+'764/big_logo.png','')
        addDir('Andy Dick',channel+'andy-dick',2,logo+'767/big_logo.png','')
        addDir('Zola Live',channel+'zolar-live',2,logo+'899/big_logo.png','')
        setView('movies', 'default') 
        
     
def filmon_epg(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', USER_AGENT)
    response = urllib2.urlopen(req)
    link1=response.read()
    response.close()  
    link=str(link1).replace('\n','')      
    match=re.compile('<h3>(.+?)</h3>.+?</a>.+?<a  class="tooltipped"  href=".+?" >                <img src="(.+?)" />            </a>                            <div class="tooltip">.+?</div>                                                <h4>(.+?)/h4>            <div class="description">(.+?)</div>            <div class="channel-footer">                <a href="(.+?)">Watch now</a>').findall(link)
    for name, iconimage,  showname, description, url1 in match:
        cleandesc=str(description).replace('",','').replace('                ','').replace('<a class="read-more" href="/tvguide/','').replace('">Read more... &rarr;</a>','')
        showname = str(showname).replace('<','')
        description = '[B]%s [/B]\n\n%s' % (showname,cleandesc)
        url = 'http://www.filmon.com'+str(url1)
        addDir(name,url,2,iconimage,description)
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
        setView('movies', 'epg') 
                      
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
            setView('movies', 'default') 
 
    
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
        
def setView(content, viewType):
        # set content type so library shows more views and info
        if content:
                xbmcplugin.setContent(int(sys.argv[1]), content)
        if ADDON.getSetting('auto-view') == 'true':
                xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )
                
                   
if ADDON.getSetting('pass') == '':
        xbmcgui.Dialog().ok('Sinful iPhone Members','To use this plugin, sign up to [COLOR yellow][B]XBMCHUB.COM[/B][/COLOR] thank','Sinful admin,they do not give credit to the developers','that makes the plugins [COLOR yellow]Sinful Admin Contact My Email[/COLOR]')
        xbmcgui.Dialog().ok('Sinful iPhone Members','                 [COLOR yellow][B]mike@GOFUCKYOURSELF.COM[/B][/COLOR] ','                [COLOR green][B]SHOULDNT BAN ME SUPERBEE!!![/B][/COLOR]','please put xbmchub user and pass in addon settings')
        xbmc.executebuiltin("XBMC.Container.Update(path,replace)")
        xbmc.executebuiltin("XBMC.ActivateWindow(Home)")
        
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
        LocalChannels(url)
        
elif mode==4:
        print ""+url
        SportsChannels(url)
        
elif mode==5:
        print ""+url
        MusicChannels(url)

elif mode==6:
        print ""+url
        UkTvChannels(url)

elif mode==7:
        print ""+url
        PremiumChannels(url)

elif mode==8:
        print ""+url
        ComedyChannels(url)

elif mode==9:
        print ""+url
        AsianChannels(url)

elif mode==10:
        print ""+url
        MovieChannels(url)

elif mode==11:
        print ""+url
        LifestyleChannels(url)

elif mode==12:
        print ""+url
        KidsChannels(url)

elif mode==13:
        print ""+url
        EducationChannels(url)

elif mode==14:
        print ""+url
        ReligiousChannels(url)

elif mode==15:
        print ""+url
        HorrorChannels(url)

elif mode==16:
        print ""+url
        NewsChannels(url)

elif mode==17:
        print ""+url
        BikiniChannels(url)

elif mode==18:
        print ""+url
        ArabicChannels(url)

elif mode==19:
        print ""+url
        GalaxieMusicChannels(url)

elif mode==20:
        print ""+url
        GermanChannels(url)

elif mode==21:
        print ""+url
        LatinChannels(url)

elif mode==22:
        print ""+url
        DocumentaryChannels(url)

elif mode==23:
        print ""+url
        ItalianChannels(url)

elif mode==24:
        print ""+url
        MindBodyAndSpiritChannels(url)

elif mode==25:
        print ""+url
        FreeChannels(url)

elif mode==26:
        print ""+url
        ShoppingChannels(url)

elif mode==27:
        print ""+url
        MainChannels(url)

elif mode==28:
        print ""+url
        InteractiveChannels(url)
        
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
