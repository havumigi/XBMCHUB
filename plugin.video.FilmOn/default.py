import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,base64,datetime


#Global Constants
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

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
        
def LocalChannels(url):
        addDir('Filmon Live','http://www.filmon.com/channel/live',2,'http://static.filmon.com/couch/channels/689/big_logo.png','')
        addDir('CBS Palo Alto','http://www.filmon.com/channel/cbs-palo-alto',2,'http://static.filmon.com/couch/channels/967/big_logo.png','')
        addDir('ABC Palo Alto','http://www.filmon.com/channel/abc-palo-alto',2,'http://static.filmon.com/couch/channels/970/big_logo.png','')
        addDir('NBC Palo Alto','http://www.filmon.com/channel/nbc-palo-alto',2,'http://static.filmon.com/couch/channels/973/big_logo.png','')
        addDir('Fox Palo Alto','http://www.filmon.com/channel/fox-palo-alto',2,'http://static.filmon.com/couch/channels/976/big_logo.png','')
        addDir('TV5Monde Europe','http://www.filmon.com/channel/tv5monde-europe',2,'http://static.filmon.com/couch/channels/517/big_logo.png','')
        addDir('BLU','http://www.filmon.com/channel/blu',2,'http://static.filmon.com/couch/channels/448/big_logo.png','')
        addDir('Canal+ TV','http://www.filmon.com/channel/canal',2,'http://static.filmon.com/couch/channels/363/big_logo.png','')
        
def SportsChannels(url):
        addDir('Filmon Football','http://www.filmon.com/channel/filmon-football',2,'http://static.filmon.com/couch/channels/374/big_logo.png','')
        addDir('Filmon Collage Basekitball','http://www.filmon.com/channel/filmon-college-basketball',2,'http://static.filmon.com/couch/channels/485/big_logo.png','')
        addDir('Filmon Collage Football','http://www.filmon.com/channel/filmon-college-football',2,'http://static.filmon.com/couch/channels/488/big_logo.png','')
        addDir('X-Treme Sports','http://www.filmon.com/channel/x-treme-sports',2,'http://static.filmon.com/couch/channels/326/big_logo.png','')
        addDir('Masked Republic AAA Lucha Libre','http://www.filmon.com/channel/masked-republic-aaa-lucha-libre',2,'http://static.filmon.com/couch/channels/802/big_logo.png','')
        addDir('UFC Next','http://www.filmon.com/channel/ufc-next',2,'http://static.filmon.com/couch/channels/713/big_logo.png','')
        addDir('Skiers World TV','http://www.filmon.com/channel/skiers-world-tv',2,'http://static.filmon.com/couch/channels/408/big_logo.png','')
        addDir('NWA Wrestling','http://www.filmon.com/channel/nwa-wrestling',2,'http://static.filmon.com/couch/channels/373/big_logo.png','')
        addDir('Thats Boating TV','http://www.filmon.com/channel/thats-boating-tv',2,'http://static.filmon.com/couch/channels/388/big_logo.png','')
        addDir('Eighteen Holes TV','http://www.filmon.com/channel/eighteen-holes-tv',2,'http://static.filmon.com/couch/channels/389/big_logo.png','')
        addDir('Badass Sports TV','http://www.filmon.com/channel/badass-sports-tv',2,'http://static.filmon.com/couch/channels/391/big_logo.png','')
        addDir('Pursuit Channel','http://www.filmon.com/channel/pursuit-channel',2,'http://static.filmon.com/couch/channels/349/big_logo.png','')
        addDir('Dubai Sports','http://www.filmon.com/channel/dubai-sports',2,'http://static.filmon.com/couch/channels/79/big_logo.png','')

def MusicChannels(url):
        addDir('Filmon Jazz and Blues','http://www.filmon.com/channel/filmon-jazz-and-blues',2,'http://static.filmon.com/couch/channels/530/big_logo.png','')
        addDir('JCTV Music','http://www.filmon.com/channel/jctv',2,'http://static.filmon.com/couch/channels/400/big_logo.png','')
        addDir('The Noise Network','http://www.filmon.com/channel/the-noise-network',2,'http://static.filmon.com/couch/channels/385/big_logo.png','')
        addDir('Urban Music Network','http://www.filmon.com/channel/urban-music-network',2,'http://static.filmon.com/couch/channels/347/big_logo.png','')
        addDir('The Soundtrack Channel','http://www.filmon.com/channel/the-soundtrack-channel',2,'http://static.filmon.com/couch/channels/350/big_logo.png','')
        addDir('THe Country Network','http://www.filmon.com/channel/the-country-network',2,'http://static.filmon.com/couch/channels/342/big_logo.png','')
        addDir('Classic Arts Showcase','http://www.filmon.com/channel/classic-arts-showcase',2,'http://static.filmon.com/couch/channels/309/big_logo.png','')
        addDir('Filmon Rock TV','http://www.filmon.com/channel/filmon-rock-tv',2,'http://static.filmon.com/couch/channels/311/big_logo.png','')
        addDir('4 Music','http://www.filmon.com/channel/4-music',2,'http://static.filmon.com/couch/channels/95/big_logo.png','')
        addDir('Viva','http://www.filmon.com/channel/viva',2,'http://static.filmon.com/couch/channels/8/big_logo.png','')
        addDir('Film On Music Legends TV','http://www.filmon.com/channel/filmon-music-legends-tv',2,'http://static.filmon.com/couch/channels/257/big_logo.png','')

def UkTvChannels(url):
        addDir('BBC One','http://www.filmon.com/channel/bbc-one',2,'http://static.filmon.com/couch/channels/14/big_logo.png','')
        addDir('BBC Two','http://www.filmon.com/channel/bbc-two',2,'http://static.filmon.com/couch/channels/25/big_logo.png','')
        addDir('ITV1','http://www.filmon.com/channel/itv1',2,'http://static.filmon.com/couch/channels/11/big_logo.png','')
        addDir('Channel 4','http://www.filmon.com/channel/channel-4',2,'http://static.filmon.com/couch/channels/2/big_logo.png','')
        addDir('Channel 5','http://www.filmon.com/channel/channel-5',2,'http://static.filmon.com/couch/channels/22/big_logo.png','')
        addDir('ITV2','http://www.filmon.com/channel/itv2',2,'http://static.filmon.com/couch/channels/67/big_logo.png','')
        addDir('ITV3','http://www.filmon.com/channel/itv3',2,'http://static.filmon.com/couch/channels/26/big_logo.png','')
        addDir('ITV4','http://www.filmon.com/channel/itv4',2,'http://static.filmon.com/couch/channels/101/big_logo.png','')
        addDir('E4','http://www.filmon.com/channel/e4',2,'http://static.filmon.com/couch/channels/65/big_logo.png','')
        addDir('More4','http://www.filmon.com/channel/more4',2,'http://static.filmon.com/couch/channels/97/big_logo.png','')
        addDir('5USA','http://www.filmon.com/channel/5usa',2,'http://static.filmon.com/couch/channels/845/big_logo.png','')
        addDir('5USA+1','http://www.filmon.com/channel/5usa1',2,'http://static.filmon.com/couch/channels/848/big_logo.png','')
        addDir('5*','http://www.filmon.com/channel/5',2,'http://static.filmon.com/couch/channels/851/big_logo.png','')
        addDir('5*+1','http://www.filmon.com/channel/51',2,'http://static.filmon.com/couch/channels/854/big_logo.png','')
        addDir('Channel5+1','http://www.filmon.com/channel/channel51',2,'http://static.filmon.com/couch/channels/857/big_logo.png','')
        addDir('Dave','http://www.filmon.com/channel/dave',2,'http://static.filmon.com/couch/channels/370/big_logo.png','')
        addDir('Pick TV','http://www.filmon.com/channel/pick-tv',2,'http://static.filmon.com/couch/channels/371/big_logo.png','')
        addDir('Really','http://www.filmon.com/channel/really',2,'http://static.filmon.com/couch/channels/372/big_logo.png','')
        addDir('BBC1 North Island','http://www.filmon.com/channel/bbc-1-north-ireland',2,'http://static.filmon.com/couch/channels/361/big_logo.png','')
        addDir('CBBC/BBC Three','http://www.filmon.com/channel/cbbcbbc-three',2,'http://static.filmon.com/couch/channels/113/big_logo.png','')
        addDir('CBEEBIES/BBC Four','http://www.filmon.com/channel/cbeebiesbbc-four',2,'http://static.filmon.com/couch/channels/103/big_logo.png','')
        addDir('BBC News','http://www.filmon.com/channel/bbc-news',2,'http://static.filmon.com/couch/channels/27/big_logo.png','')
               
def PremiumChannels(url):
        addDir('World of Martial Arts Television','http://www.filmon.com/channel/world-of-martial-arts-television',2,'http://static.filmon.com/couch/channels/406/big_logo.png','')
        addDir('Ginx','http://www.filmon.com/channel/ginx',2,'http://static.filmon.com/couch/channels/796/big_logo.png','')
        addDir('Ebru','http://www.filmon.com/channel/ebru',2,'http://static.filmon.com/couch/channels/914/big_logo.png','')
        addDir('Halogen TV','http://www.filmon.com/channel/halogen-tv',2,'http://static.filmon.com/couch/channels/703/big_logo.png','')
        addDir('HRTV','http://www.filmon.com/channel/hrtv',2,'http://static.filmon.com/couch/channels/694/big_logo.png','')
        addDir('Clubbing TV','http://www.filmon.com/channel/clubbing-tv',2,'http://static.filmon.com/couch/channels/691/big_logo.png','')
        addDir('Sportskool','http://www.filmon.com/channel/sportskool',2,'http://static.filmon.com/couch/channels/686/big_logo.png','')
        addDir('The Ski Channel','http://www.filmon.com/channel/the-ski-channel',2,'http://static.filmon.com/couch/channels/265/big_logo.png','')
        addDir('Untamed Sports','http://www.filmon.com/channel/untamed-sports',2,'http://static.filmon.com/couch/channels/436/big_big_logo.png','')
        addDir('Parables TV','http://www.filmon.com/channel/parables-tv',2,'http://static.filmon.com/couch/channels/405/big_logo.png','')
        addDir('Wealth TV','http://www.filmon.com/channel/wealth-tv',2,'http://static.filmon.com/couch/channels/403/big_logo.png','')
        addDir('R&R Television','http://www.filmon.com/channel/rr-television',2,'http://static.filmon.com/couch/channels/402/big_logo.png','')
        addDir('WW Extreme','http://www.filmon.com/channel/ww-extreme',2,'http://static.filmon.com/couch/channels/394/big_logo.png','')
        addDir('Filmon Reels','http://www.filmon.com/channel/filmon-reels',2,'http://static.filmon.com/couch/channels/395/big_logo.png','')
        addDir('Wheels TV','http://www.filmon.com/channel/wheels-tv',2,'http://static.filmon.com/couch/channels/397/big_logo.png','')
        addDir('American Horrors','http://www.filmon.com/channel/american-horrors',2,'http://static.filmon.com/couch/channels/393/big_logo.png','')
        addDir('e Scapes HD TV','http://www.filmon.com/channel/escapes-hd-tv',2,'http://static.filmon.com/couch/channels/341/big_logo.png','')
        addDir('Havoc Television','http://www.filmon.com/channel/havoc-television',2,'http://static.filmon.com/couch/channels/335/big_logo.png','')
        addDir('My Family TV','http://www.filmon.com/channel/my-family-tv',2,'http://static.filmon.com/couch/channels/301/big_logo.png','')
        addDir('My Combat Channel','http://www.filmon.com/channel/my-combat-channel',2,'http://static.filmon.com/couch/channels/295/big_logo.png','')
        addDir('Fashion TV','http://www.filmon.com/channel/fashion-tv',2,'http://static.filmon.com/couch/channels/21/big_logo.png','')
        addDir('TVC Latino','http://www.filmon.com/channel/tvc-latino',2,'http://static.filmon.com/couch/channels/213/big_logo.png','')
        addDir('Filmon Breaking News','http://www.filmon.com/channel/filmon-breaking-news',2,'http://static.filmon.com/couch/channels/302/big_logo.png','')

def ComedyChannels(url):
        addDir('Filmon at the Improv','http://www.filmon.com/channel/filmon-at-the-improv',2,'http://static.filmon.com/couch/channels/407/big_logo.png','')
        addDir('Popcorn TV','http://www.filmon.com/channel/popcorn-tv',2,'http://static.filmon.com/couch/channels/716/big_logo.png','')
        addDir('Comedy Net','http://www.filmon.com/channel/comedy-net',2,'http://static.filmon.com/couch/channels/497/big_logo.png','')
        addDir('Kevin Spencer TV','http://www.filmon.com/channel/kevin-spencer-tv',2,'http://static.filmon.com/couch/channels/387/big_logo.png','')
        addDir('ComedyTime TV','http://www.filmon.com/channel/comedytime-tv',2,'http://static.filmon.com/couch/channels/344/big_logo.png','')
               
def AsianChannels(url):
        addDir('Arirang TV','http://www.filmon.com/channel/arirang-tv',2,'http://static.filmon.com/couch/channels/932/big_logo.png','')
               
def MovieChannels(url):
        addDir('MyFamily TV East','http://www.filmon.com/channel/myfamily-tv-east',2,'http://static.filmon.com/couch/channels/779/big_logo.png','')
        addDir('American Primetime Television','http://www.filmon.com/channel/american-primetime-television',2,'http://static.filmon.com/couch/channels/707/big_logo.png','')
        addDir('Filmon Martial Arts','http://www.filmon.com/channel/filmon-martial-arts',2,'http://static.filmon.com/couch/channels/10/big_logo.png','')
        addDir('Threshold','http://www.filmon.com/channel/threshold',2,'http://static.filmon.com/couch/channels/514/big_logo.png','')
        addDir('Filmon Stars','http://www.filmon.com/channel/filmon-stars',2,'http://static.filmon.com/couch/channels/494/big_logo.png','')
        addDir('Action Cinema','http://www.filmon.com/channel/mbc-action',2,'http://static.filmon.com/couch/channels/369/big_logo.png','')
        addDir('Inspirational Films','http://www.filmon.com/channel/inspirational-films',2,'http://static.filmon.com/couch/channels/503/big_logo.png','')
        addDir('Hollywoodland Channel','http://www.filmon.com/channel/hollywoodland-channel',2,'http://static.filmon.com/couch/channels/411/big_logo.png','')
        addDir('Sci-Fi Channel','http://www.filmon.com/channel/sci-fi-telly',2,'http://static.filmon.com/couch/channels/382/big_logo.png','')
        addDir('The Western Channel','http://www.filmon.com/channel/the-western-channel',2,'http://static.filmon.com/couch/channels/384/big_logo.png','')
        addDir('Cultra','http://www.filmon.com/channel/cultra',2,'http://static.filmon.com/couch/channels/336/big_logo.png','')
        addDir('Filmon Grab Bag TV','http://www.filmon.com/channel/filmon-grab-bag-tv',2,'http://static.filmon.com/couch/channels/310/big_logo.png','')
        addDir('Film 4','http://www.filmon.com/channel/film-4',2,'http://static.filmon.com/couch/channels/13/big_logo.png','')
        addDir('Filmon Classics','http://www.filmon.com/channel/filmon-classics',2,'http://static.filmon.com/couch/channels/206/big_logo.png','')

def LifestyleChannels(url):
        addDir('Buzz TV','http://www.filmon.com/channel/buzz-tv',2,'http://static.filmon.com/couch/channels/782/big_logo.png','')
        addDir('Steel Dreams','http://www.filmon.com/channel/steel-dreams',2,'http://static.filmon.com/couch/channels/784/big_logo.png','')
        addDir('Distant Roads','http://www.filmon.com/channel/distant-roads',2,'http://static.filmon.com/couch/channels/787/big_logo.png','')
        addDir('Travel Channel+1','http://www.filmon.com/channel/travel-channel1',2,'http://static.filmon.com/couch/channels/842/big_logo.png','')
        addDir('AMG TV','http://www.filmon.com/channel/amg-tv',2,'http://static.filmon.com/couch/channels/902/big_logo.png','')
        addDir('Eye for an Eye','http://www.filmon.com/channel/eye-for-an-eye',2,'http://static.filmon.com/couch/channels/911/big_logo.png','')
        addDir('PopStop TV','http://www.filmon.com/channel/popstop-tv',2,'http://static.filmon.com/couch/channels/770/big_logo.png','')
        addDir('The Miki Show','http://www.filmon.com/channel/the-miki-show',2,'http://static.filmon.com/couch/channels/728/big_logo.png','')
        addDir('INSP','http://www.filmon.com/channel/insp',2,'http://static.filmon.com/couch/channels/700/big_logo.png','')
        addDir('Eco-Rico','http://www.filmon.com/channel/eco-rico',2,'http://static.filmon.com/couch/channels/710/big_logo.png','')
        addDir('Men7','http://www.filmon.com/channel/men7',2,'http://static.filmon.com/couch/channels/396/big_logo.png','')
        addDir('Veg TV','http://www.filmon.com/channel/veg-tv',2,'http://static.filmon.com/couch/channels/383/big_logo.png','')
        addDir('GeoBeats Travel','http://www.filmon.com/channel/geobeats-travel',2,'http://static.filmon.com/couch/channels/386/big_logo.png','')
        addDir('Legacy TV','http://www.filmon.com/channel/legacy-tv',2,'http://static.filmon.com/couch/channels/340/big_logo.png','')
        addDir('Jewish Life TV','http://www.filmon.com/channel/jewish-life-tv',2,'http://static.filmon.com/couch/channels/332/big_logo.png','')
        addDir('Time tv','http://www.filmon.com/channel/time-tv',2,'http://static.filmon.com/couch/channels/414/big_logo.png','')
        addDir('Unreliable Sources','http://www.filmon.com/channel/unreliable-sources',2,'http://static.filmon.com/couch/channels/239/big_logo.png','')
        addDir('Motorz','http://www.filmon.com/channel/motorz',2,'http://static.filmon.com/couch/channels/262/big_logo.png','')
        addDir('http://www.filmon.com/channel/wine-channel-tv',2,'http://static.filmon.com/couch/channels/263/big_logo.png','')
        
def KidsChannels(url):
        addDir('Kartoon Klassics','http://www.filmon.com/channel/kartoon-klassics',2,'http://static.filmon.com/couch/channels/793/big_logo.png','')
        addDir('Animal Atlas','http://www.filmon.com/channel/animal-atlas',2,'http://static.filmon.com/couch/channels/799/big_logo.png','')
        addDir('Emba Kids','http://www.filmon.com/channel/emba-kids',2,'http://static.filmon.com/couch/channels/719/big_logo.png','')
        addDir('Smile of Child','http://www.filmon.com/channel/smile-of-child',2,'http://static.filmon.com/couch/channels/401/big_logo.png','')

def EducationChannels(url):
        addDir('UWTV','http://www.filmon.com/channel/uwtv',2,'http://static.filmon.com/couch/channels/808/big_logo.png','')
        addDir('The Florida Channel','http://www.filmon.com/channel/the-florida-channel',2,'http://static.filmon.com/couch/channels/305/big_logo.png','')

def ReligiousChannels(url):
        addDir('DayStar','http://www.filmon.com/channel/daystar',2,'http://static.filmon.com/couch/channels/833/big_logo.png','')
        addDir('TBN','http://www.filmon.com/channel/tbn',2,'http://static.filmon.com/couch/channels/398/big_logo.png','')
        addDir('The Church Channel','http://www.filmon.com/channel/the-church-channel',2,'http://static.filmon.com/couch/channels/399/big_logo.png','')

def HorrorChannels(url):
        addDir('Horror Channel','http://www.filmon.com/channel/horror-channel',2,'http://static.filmon.com/couch/channels/836/big_logo.png','')
        addDir('ShockORama','http://www.filmon.com/channel/shockorama',2,'http://static.filmon.com/couch/channels/509/big_logo.png','')
        addDir('Braindamage TV','http://www.filmon.com/channel/braindamage-tv',2,'http://static.filmon.com/couch/channels/339/big_logo.png','')
        addDir('Macare Theatre','http://www.filmon.com/channel/macabre-theatre',2,'http://static.filmon.com/couch/channels/315/big_logo.png','')
        addDir('RSquared','http://www.filmon.com/channel/rsquared',2,'http://static.filmon.com/couch/channels/256/big_logo.png','')
        
def NewsChannels(url):
        addDir('CNBC','http://www.filmon.com/channel/cnbc',2,'http://static.filmon.com/couch/channels/860/big_logo.png','')
        addDir('DVIDs TV','http://www.filmon.com/channel/dvids-tv',2,'http://static.filmon.com/couch/channels/725/big_logo.png','')
        addDir('Free Speech TV','http://www.filmon.com/channel/free-speech-tv',2,'http://static.filmon.com/couch/channels/697/big_logo.png','')
        addDir('Biz TV','http://www.filmon.com/channel/biztv',2,'http://static.filmon.com/couch/channels/343/big_logo.png','')
        addDir('WeatherNation','http://www.filmon.com/channel/weathernation',2,'http://static.filmon.com/couch/channels/329/big_logo.png','')
        addDir('NASA HD','http://www.filmon.com/channel/nasa-hd',2,'http://static.filmon.com/couch/channels/330/big_logo.png','')
        addDir('The Pentagon','http://www.filmon.com/channel/the-pentagon',2,'http://static.filmon.com/couch/channels/333/big_logo.png','')
        addDir('France24','http://www.filmon.com/channel/france24',2,'http://static.filmon.com/couch/channels/298/big_logo.png','')
        addDir('Russia Today','http://www.filmon.com/channel/russia-today-2',2,'http://static.filmon.com/couch/channels/93/big_logo.png','')
        addDir('AL Jazeera','http://www.filmon.com/channel/al-jazeera',2,'http://static.filmon.com/couch/channels/4/big_logo.png','')
        addDir('Bloomberg','http://www.filmon.com/channel/bloomberg',2,'http://static.filmon.com/couch/channels/81/big_logo.png','')
        
def BikiniChannels(url):
        addDir('MiamiTV','http://www.filmon.com/channel/miamitv',2,'http://static.filmon.com/couch/channels/866/big_logo.png','')
        addDir('Bikini TeeVee','http://www.filmon.com/channel/bikini-teevee',2,'http://static.filmon.com/couch/channels/380/big_logo.png','')
        addDir('Party TeeVee','http://www.filmon.com/channel/party-teevee',2,'http://static.filmon.com/couch/channels/790/big_logo.png','')
        
def ArabicChannels(url):
        addDir('iFilm','http://www.filmon.com/channel/ifilm',2,'http://static.filmon.com/couch/channels/908/big_logo.png','')
        addDir('MBC','http://www.filmon.com/channel/mbc',2,'http://static.filmon.com/couch/channels/367/big_logo.png','')
        addDir('MBC2','http://www.filmon.com/channel/mbc2',2,'http://static.filmon.com/couch/channels/368/big_logo.png','')
        addDir('MBC Action','http://www.filmon.com/channel/mbc-action',2,'http://static.filmon.com/couch/channels/369/big_logo.png','')

def GalaxieMusicChannels(url):
        addDir('GALAXIE ADULT ALTERNATIVE','http://www.filmon.com/channel/galaxie-adult-alternative',2,'http://static.filmon.com/couch/channels/536/big_logo.png','')
        addDir('GALAXIE CLASSIC MASTERS','http://www.filmon.com/channel/galaxie-classic-masters',2,'http://static.filmon.com/couch/channels/539/big_logo.png','')
        addDir('GALAXIE CLASSIC ROCK','http://www.filmon.com/channel/galaxie-classic-rock',2,'http://static.filmon.com/couch/channels/542/big_logo.png','')
        addDir('GALAXIE COUNTRY CLASSICS','http://www.filmon.com/channel/galaxie-country-classics',2,'http://static.filmon.com/couch/channels/545/big_logo.png','')
        addDir('GALAXIE EASY LISTENING','http://www.filmon.com/channel/galaxie-easy-listening',2,'http://static.filmon.com/couch/channels/548/big_logo.png','')
        addDir('GALAXIE FLASHBACK 70S','http://www.filmon.com/channel/galaxie-flashback-70s',2,'http://static.filmon.com/couch/channels/551/big_logo.png','')
        addDir('GALAXIE FOLK ROOTS','http://www.filmon.com/channel/galaxie-folk-roots',2,'http://static.filmon.com/couch/channels/554/big_logo.png','')
        addDir('GALAXIE HIT LIST','http://www.filmon.com/channel/galaxie-hit-list',2,'http://static.filmon.com/couch/channels/557/big_logo.png','')
        addDir('GALAXIE HOT COUNTRY','http://www.filmon.com/channel/galaxie-hot-country',2,'http://static.filmon.com/couch/channels/560/big_logo.png','')
        addDir('GALAXIE JAMMIN','http://www.filmon.com/channel/galaxie-jammin',2,'http://static.filmon.com/couch/channels/563/big_logo.png','')
        addDir('GALAXIE JAZZ MASTERS','http://www.filmon.com/channel/galaxie-jazz-masters',2,'http://static.filmon.com/couch/channels/566/big_logo.png','')
        addDir('GALAXIE JUKEBOX OLDIES','http://www.filmon.com/channel/galaxie-jukebox-oldies',2,'http://static.filmon.com/couch/channels/569/big_logo.png','')
        addDir('GALAXIE KIDS STUFF','http://www.filmon.com/channel/galaxie-kids-stuff',2,'http://static.filmon.com/couch/channels/572/big_logo.png','')
        addDir('GALAXIE LATINO TROPICAL','http://www.filmon.com/channel/galaxie-latino-tropical',2,'http://static.filmon.com/couch/channels/575/big_logo.png','')
        addDir('GALAXIE POP ADULT','http://www.filmon.com/channel/galaxie-pop-adult',2,'http://static.filmon.com/couch/channels/578/big_logo.png','')
        addDir('GALAXIE POP CLASSICS','http://www.filmon.com/channel/galaxie-pop-classics',2,'http://static.filmon.com/couch/channels/581/big_logo.png','')
        addDir('GALAXIE EVERTHING 80S','http://www.filmon.com/channel/galaxie-everything-80s',2,'http://static.filmon.com/couch/channels/584/big_logo.png','')
        addDir('GALAXIE ROCK','http://www.filmon.com/channel/galaxie-rock',2,'http://static.filmon.com/couch/channels/587/big_logo.png','')
        addDir('GALAXIE ROCK ALTERNAIVE','http://www.filmon.com/channel/galaxie-rock-alternative',2,'http://static.filmon.com/couch/channels/590/big_logo.png','')
        addDir('GALAXIE SMOOTH JAZZ','http://www.filmon.com/channel/galaxie-smooth-jazz',2,'http://static.filmon.com/couch/channels/593/big_logo.png','')
        addDir('GALAXIE SOUL STORM','http://www.filmon.com/channel/galaxie-soul-storm',2,'http://static.filmon.com/couch/channels/596/big_logo.png','')
        addDir('GALAXIE STANDARDS','http://www.filmon.com/channel/galaxie-standards',2,'http://static.filmon.com/couch/channels/599/big_logo.png','')
        addDir('GALAXIE THE BLUES','http://www.filmon.com/channel/galaxie-the-blues',2,'http://static.filmon.com/couch/channels/602/big_logo.png','')
        addDir('GALAXIE THE LIGHT','http://www.filmon.com/channel/galaxie-the-light',2,'http://static.filmon.com/couch/channels/605/big_logo.png','')
        addDir('GALAXIE URBAN BEATS','http://www.filmon.com/channel/galaxie-urban-beats',2,'http://static.filmon.com/couch/channels/608/big_logo.png','')
        addDir('GALAXIE NOTHIN BUT THR 90`s','http://www.filmon.com/channel/galaxie-nothin-but-90s',2,'http://static.filmon.com/couch/channels/611/big_logo.png','')
        addDir('GALAXIE MAXIMIM PARTY','http://www.filmon.com/channel/galaxie-maximum-party',2,'http://static.filmon.com/couch/channels/614/big_logo.png','')
        addDir('GALAXIE DANCE CLUBBIN','http://www.filmon.com/channel/galaxie-dance-clubbn',2,'http://static.filmon.com/couch/channels/617/big_logo.png','')
        addDir('GALXAIE BLUEGRASS','http://www.filmon.com/channel/galaxie-bluegrass',2,'http://static.filmon.com/couch/channels/620/big_logo.png','')
        addDir('GALAXIE BIG BAND','http://www.filmon.com/channel/galaxie-big-band',2,'http://static.filmon.com/couch/channels/623/big_logo.png','')
        addDir('GALAXIE JAZZ NOW','http://www.filmon.com/channel/galaxie-jazz-now',2,'http://static.filmon.com/couch/channels/626/big_logo.png','')
        addDir('GALAXIE THE CHILL LOUNGE','http://www.filmon.com/channel/galaxie-the-chill-lounge',2,'http://static.filmon.com/couch/channels/629/big_logo.png','')
        addDir('GALAXIE THE SPA','http://www.filmon.com/channel/galaxie-the-spa',2,'http://static.filmon.com/couch/channels/632/big_logo.png','')
        addDir('GALAXIE BAROQUE','http://www.filmon.com/channel/galaxie-baroque',2,'http://static.filmon.com/couch/channels/635/big_logo.png','')
        addDir('GALAXIE OPERA PLUS','http://www.filmon.com/channel/galaxie-opera-plus',2,'http://static.filmon.com/couch/channels/638/big_logo.png','')
        addDir('GALAXIE CHAMBER MUSIC','http://www.filmon.com/channel/galaxie-chamber-music',2,'http://static.filmon.com/couch/channels/641/big_logo.png','')
        addDir('GALAXIE TODAYS LATIN POP','http://www.filmon.com/channel/galaxie-todays-latin-pop',2,'http://static.filmon.com/couch/channels/644/big_logo.png','')
        addDir('GALAXIE RETRO R&B','http://www.filmon.com/channel/galaxie-retro-rb',2,'http://static.filmon.com/couch/channels/647/big_logo.png','')
        addDir('GALAXIE NO FENCES','http://www.filmon.com/channel/galaxie-no-fences',2,'http://static.filmon.com/couch/channels/650/big_logo.png','')
        addDir('GALAXIE DANCE CLASSICS','http://www.filmon.com/channel/galaxie-dance-classics',2,'http://static.filmon.com/couch/channels/653/big_logo.png','')
        addDir('GALAXIE HOLIDAY HITS','http://www.filmon.com/channel/galaxie-holiday-hits',2,'http://static.filmon.com/couch/channels/656/big_logo.png','')
        addDir('GALAXIE HARD ROCK','http://www.filmon.com/channel/galaxie-hard-rock',2,'http://static.filmon.com/couch/channels/659/big_logo.png','')
        addDir('GALAXIE ALT ROCK CLASSICS','http://www.filmon.com/channel/galaxie-alt-rock-classics',2,'http://static.filmon.com/couch/channels/662/big_logo.png','')
        addDir('GALAXIE ROCK ALT-COUNTRY AMERICANA','http://www.filmon.com/channel/galaxie-rock-alt-country-americana',2,'http://static.filmon.com/couch/channels/665/big_logo.png','')
        addDir('GALAXIE GOSPEL','http://www.filmon.com/channel/galaxie-gospel',2,'http://static.filmon.com/couch/channels/668/big_logo.png','')
        addDir('GALAXIE CELTIC','http://www.filmon.com/channel/galaxie-celtic',2,'http://static.filmon.com/couch/channels/671/big_logo.png''')
        addDir('GALAXIE RETRO LATINO','http://www.filmon.com/channel/galaxie-retro-latino',2,'http://static.filmon.com/couch/channels/674/big_logo.png','')
        addDir('GALAXIE LATINO URBANA','http://www.filmon.com/channel/galaxie-latino-urbana',2,'http://static.filmon.com/couch/channels/677/big_logo.png','')
        addDir('GALAXIE LATINO TEJANO','http://www.filmon.com/channel/galaxie-latino-tejano',2,'http://static.filmon.com/couch/channels/680/big_logo.png','')
        addDir('GALAXIE REGIONAL MEXICAN','http://www.filmon.com/channel/galaxie-regional-mexiana',2,'"http://static.filmon.com/couch/channels/683/big_logo.png','')
               
def GermanChannels(url):
        addDir('ProSieben Austria','http://www.filmon.com/channel/prosieben-austria',2,'http://static.filmon.com/couch/channels/520/big_logo.png','')
        addDir('Eins Extra','http://www.filmon.com/channel/eins-extra',2,'http://static.filmon.com/couch/channels/415/big_logo.png','')
        addDir('Eins Plus','http://www.filmon.com/channel/eins-plus',2,'http://static.filmon.com/couch/channels/418/big_logo.png','')
        addDir('Eins Festival','http://www.filmon.com/channel/eins-festival',2,'http://static.filmon.com/couch/channels/421/big_logo.png','')
        addDir('QVC Deutschland','http://www.filmon.com/channel/qvc-deutschland',2,'http://static.filmon.com/couch/channels/354/big_logo.png','')
        addDir('QVC PLUS','http://www.filmon.com/channel/qvc-plus',2,'http://static.filmon.com/couch/channels/355/big_logo.png','')
        addDir('zdf.kultur','http://www.filmon.com/channel/zdfkultur',2,'http://static.filmon.com/couch/channels/359/big_logo.png','')
        addDir('ZDFneo','http://www.filmon.com/channel/zdfneo',2,'http://static.filmon.com/couch/channels/360/big_logo.png','')
        
def LatinChannels(url):
        addDir('Andalucia TV','http://www.filmon.com/channel/andalucia-tv',2,'http://static.filmon.com/couch/channels/526/big_logo.png','')
        addDir('Telemadrid','http://www.filmon.com/channel/telemadrid',2,'http://static.filmon.com/couch/channels/529/big_logo.png','')
        addDir('RT Espanol','http://www.filmon.com/channel/rt-espaaol',2,'http://static.filmon.com/couch/channels/299/big_logo.png','')
        addDir('RTVE','http://www.filmon.com/channel/rtve',2,'http://static.filmon.com/couch/channels/23/big_logo.png','')
        addDir('RTpi America','http://www.filmon.com/channel/rtpi-america',2,'http://static.filmon.com/couch/channels/303/big_logo.png','')
        
def DocumentaryChannels(url):
        addDir('War in Color','http://www.filmon.com/channel/war-in-color',2,'http://static.filmon.com/couch/channels/491/big_logo.png','')
        addDir('War and Crime','http://www.filmon.com/channel/war-crime-network',2,'http://static.filmon.com/couch/channels/381/big_logo.png','')
               
def ItalianChannels(url):
        addDir('QVC Italia','http://www.filmon.com/channel/qvc-italia',2,'http://static.filmon.com/couch/channels/463/big_logo.png','')
        addDir('Canale Italia 84','http://www.filmon.com/channel/canale-italia-84',2,'http://static.filmon.com/couch/channels/442/big_logo.png','')
        addDir('Canale Italia','http://www.filmon.com/channel/canale-italia',2,'http://static.filmon.com/couch/channels/445/big_logo.png','')
        addDir('Studio Europa','http://www.filmon.com/channel/studio-europa',2,'http://static.filmon.com/couch/channels/451/big_logo.png','')
        addDir('Justice TV','http://www.filmon.com/channel/justice-tv',2,'http://static.filmon.com/couch/channels/454/big_logo.png','')
        addDir('RAI 1','http://www.filmon.com/channel/rai-1',2,'http://static.filmon.com/couch/channels/375/big_logo.png','')
        addDir('RAI 2','http://www.filmon.com/channel/rai-2',2,'http://static.filmon.com/couch/channels/376/big_logo.png','')
        addDir('RAI 3','http://www.filmon.com/channel/rai-3',2,'http://static.filmon.com/couch/channels/377/big_logo.png','')
        addDir('Camera dei Deputati','http://www.filmon.com/channel/camera-dei-deputati',2,'http://static.filmon.com/couch/channels/379/big_logo.png','')

def MindBodyAndSpiritChannels(url):
        addDir('Fitness Lifestyle TV','http://www.filmon.com/channel/fitness-lifestyle-tv',2,'http://static.filmon.com/couch/channels/410/big_logo.png','')
        addDir('Cornerstone TV','http://www.filmon.com/channel/cornerstone-tv',2,'http://static.filmon.com/couch/channels/212/big_logo.png','')
        addDir('Supreme Master TV','http://www.filmon.com/channel/supreme-master-tv',2,'http://static.filmon.com/couch/channels/304/big_logo.png','')

def FreeChannels(url):
        addDir('Linkct Network','http://www.filmon.com/channel/linkct-network',2,'http://static.filmon.com/couch/channels/390/big_logo.png','')

def ShoppingChannels(url):
        addDir('QVC HD','http://www.filmon.com/channel/qvc-hd',2,'http://static.filmon.com/couch/channels/413/big_logo.png','')
        addDir('9021go TV','http://www.filmon.com/channel/9021go-tv',2,'http://static.filmon.com/couch/channels/214/big_logo.png','')
        addDir('Jewelry TV','http://www.filmon.com/channel/jewelry-tv',2,'http://static.filmon.com/couch/channels/306/big_logo.png','')

def MainChannels(url):
        addDir('Phoenix','http://www.filmon.com/channel/phoenix',2,'http://static.filmon.com/couch/channels/424/big_logo.png','')

def InteractiveChannels(url):
        addDir('Battlecam People','http://www.filmon.com/channel/battlecam-people',2,'http://static.filmon.com/couch/channels/324/big_logo.png','')
        addDir('PPV Celebrity Fight','http://www.filmon.com/channel/ppv-celebrity-fight',2,'http://static.filmon.com/couch/channels/412/big_logo.png','')
        addDir('Janice TV','http://www.filmon.com/channel/janice-tv',2,'http://static.filmon.com/couch/channels/460/big_logo.png','')
        addDir('Dave Live','http://www.filmon.com/channel/davelive',2,'http://static.filmon.com/couch/channels/733/big_logo.png','')
        addDir('Kato','http://www.filmon.com/channel/kato',2,'http://static.filmon.com/couch/channels/758/big_logo.png','')
        addDir('Situation','http://www.filmon.com/channel/situation',2,'http://static.filmon.com/couch/channels/761/big_logo.png','')
        addDir('Rampage','http://www.filmon.com/channel/rampage',2,'http://static.filmon.com/couch/channels/764/big_logo.png','')
        addDir('Andy Dick','http://www.filmon.com/channel/andy-dick',2,'http://static.filmon.com/couch/channels/767/big_logo.png','')
        addDir('Zola Live','http://www.filmon.com/channel/zolar-live',2,'http://static.filmon.com/couch/channels/899/big_logo.png','')
        
     
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
        addDir(name,url,3,iconimage,description)
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
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
