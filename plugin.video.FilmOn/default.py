import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,base64,datetime
import settings


#Global Constants
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
ADDON = xbmcaddon.Addon(id='plugin.video.FilmOn')
channel= 'http://www.filmon.com/channel/'
logo = 'http://static.filmon.com/couch/channels/'
res= settings.res()


        
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
        addDir('Filmon Live',channel+'live',2,logo+'689/big_logo.png',"Here at the FilmOn studios you never know who you'll catch recording live. From Andy Dick to Rampage Jackson, a different show is filmed live every day.")
        addDir('CBS Palo Alto',channel+'cbs-palo-alto',2,logo+'967/big_logo.png','')
        addDir('ABC Palo Alto',channel+'abc-palo-alto',2,logo+'970/big_logo.png','')
        addDir('NBC Palo Alto',channel+'nbc-palo-alto',2,logo+'973/big_logo.png','')
        addDir('Fox Palo Alto',channel+'fox-palo-alto',2,logo+'976/big_logo.png','')
        addDir('TV5Monde Europe',channel+'tv5monde-europe',2,logo+'517/big_logo.png',"Various entertainment and news programming.")
        addDir('BLU',channel+'blu',2,logo+'448/big_logo.png',"Culture, Cinema & Community Television.")
        addDir('Canal+ TV',channel+'canal',2,logo+'363/big_logo.png',"See classic motorsport, car clips & much more on Renault TV.")
        addDir('M6 Boutique La Chaine',channel+'m6-bo',2,logo+'364/big_logo.png',"French Variety and News Broadcaster.")
        setView('movies', 'default') 
        
def SportsChannels(url):
        addDir('Filmon Football',channel+'filmon-football',2,logo+'374/big_logo.png',"Watch UK football games, Russian Football Premier Liga, England International and premiership, FIFA and UEFA. Streaming football England FA Cup, coverage, scores, results, news videos and highlights.")
        addDir('Filmon Collage Basekitball',channel+'filmon-college-basketball',2,logo+'485/big_logo.png',"Non stop College Basketball action brought to you from FilmOn.")
        addDir('Filmon Collage Football',channel+'filmon-college-football',2,logo+'488/big_logo.png',"Get the latest NCAA college football streaming video, news, scores, stats, standings, and more. Watch Air Force, Navy, Army, as well as all state the programs.")
        addDir('X-Treme Sports',channel+'x-treme-sports',2,logo+'326/big_logo.png',"The X-treme Sports channel brings you award winning extreme sports films from around the globe.")
        addDir('Masked Republic AAA Lucha Libre',channel+'masked-republic-aaa-lucha-libre',2,logo+'802/big_logo.png',"Masked Republic AAA is the best Mexican wrestling in the world, wonderfully colorful and amazingly entertaining, well known for its masks, acrobatics, and often circus like antics, is the most popular sport in Mexico next to soccer.")
        addDir('UFC Next',channel+'ufc-next',2,logo+'713/big_logo.png','')
        addDir('Skiers World TV',channel+'skiers-world-tv',2,logo+'408/big_logo.png',"Skiers World has a 28 year history and is seen every season by millions of people across Canada, running from November to March. Each week hosts Mike Douglas, Edith Rozsa, Joe Lammers and Chris Robinson explore great skiing, resort life, and a wide variety of activities that make skiing the unique lifestyle sport that it is. Special segments include The Freestyle File, The Race Report and Personal Performance Tips with Steve Young and Josh Foster. Skiers World is also distributed internationally. The show is enjoyed in many countries around the world including the United States, Great Britain, Australia, New Zealand, Romania, Greece and Israel.")
        addDir('NWA Wrestling',channel+'nwa-wrestling',2,logo+'373/big_logo.png',"The National Wrestling Alliance was founded in 1948 and is the worlds oldest and largest pro wrestling sanctioning body. watch the best of NWA wrestling 24/7.")
        addDir('Thats Boating TV',channel+'thats-boating-tv',2,logo+'388/big_logo.png',"The best of Boating, Yachting and Life on the Water.")
        addDir('Eighteen Holes TV',channel+'eighteen-holes-tv',2,logo+'389/big_logo.png',"Around the world of golf.")
        addDir('Badass Sports TV',channel+'badass-sports-tv',2,logo+'391/big_logo.png',"Badass Sports brings you extreme sports from around the globe.")
        addDir('Pursuit Channel',channel+'pursuit-channel',2,logo+'349/big_logo.png',"Pursuit Channel - The Best Place for Hunting, Fishing, and the Outdoors.")
        addDir('Dubai Sports',channel+'dubai-sports',2,logo+'79/big_logo.png',"The 24/7 sports channel based in Dubai, United Arab Emirates is the home for sports news around the country.")
        setView('movies', 'default') 
        
def MusicChannels(url):
        addDir('Filmon Jazz and Blues',channel+'filmon-jazz-and-blues',2,logo+'530/big_logo.png',"Jazz and Blues Legends in concert and Documentary.")
        addDir('JCTV Music',channel+'jctv',2,logo+'400/big_logo.png',"Youth Oriented Programming.")
        addDir('The Noise Network',channel+'the-noise-network',2,logo+'385/big_logo.png',"The Noise Network beings you the greatest bands and interviews 24/7.")
        addDir('Urban Music Network',channel+'urban-music-network',2,logo+'347/big_logo.png',"RnB, Hip Hop, Soul and Reggae concerts, documentaries and films.")
        addDir('The Soundtrack Channel',channel+'the-soundtrack-channel',2,logo+'350/big_logo.png',"Music Videos and Movie trailers all day, every day.")
        addDir('THe Country Network',channel+'the-country-network',2,logo+'342/big_logo.png',"The Country Network showcases the best in country music videos and related content, 24 hours a day, 365 days a year.")
        addDir('Classic Arts Showcase',channel+'classic-arts-showcase',2,logo+'309/big_logo.png',"Includes video samplings of art, music, ballet, theatrical performances and classic films")
        addDir('Filmon Rock TV',channel+'filmon-rock-tv',2,logo+'311/big_logo.png',"Music programming from concerts to documentary.")
        addDir('4 Music',channel+'4-music',2,logo+'95/big_logo.png',"4Music brings you closer to the music you love - be it through the latest video exclusives, live performances, interviews, documentaries or festival coverage.")
        addDir('Viva',channel+'viva',2,logo+'8/big_logo.png',"A unique mix of award-winning comedy, the best in rock and pop and fabulous new programming, VIVA is the exciting new channel from MTV. VIVA is a playful home for great shows.")
        addDir('Film On Music Legends TV',channel+'filmon-music-legends-tv',2,logo+'257/big_logo.png',"FilmOn brings you the legends of music.")
        setView('movies', 'default') 
        
def UkTvChannels(url):
        addDir('BBC One',channel+'bbc-one',2,logo+'14/big_logo.png',"BBC One offers something of value for everyone with a range of high-quality, popular programming for a modern UK audience. The channel was named Channel of the Year at the 2007 Broadcast Awards.")
        addDir('BBC Two',channel+'bbc-two',2,logo+'25/big_logo.png',"BBC Two prides itself on a rich mix of innovative, entertaining and challenging programmes, including documentaries, the arts, current affairs, comedy, drama and history, bringing subjects to life in highly imaginative ways.")
        addDir('ITV1',channel+'itv1',2,logo+'11/big_logo.png',"ITV1 is the UK's biggest commercial television network watched on average by 45m people in a typical week. ITV1 provides programming across all genres including drama, entertainment, current affairs, news, film and sport.")
        addDir('Channel 4',channel+'channel-4',2,logo+'2/big_logo.png',"Channel 4 offers an alternative to mainstream broadcasters with distinctive, entertaining and informative programming, appealing to the tastes of a culturally diverse society.")
        addDir('Channel 5',channel+'channel-5',2,logo+'22/big_logo.png',"Five was launched as Britain's fifth and final terrestrial broadcaster on the 31st March 1997. Currently well over 30 million UK viewers watch Five any given week tuning in for programming as diverse as the CSI franchise, Extraordinary People, live UEFA CUP Football, House, Home & Away and Paul Merton in China, as well as the channel's award winning children's strand, Milkshake! 2008 saw the arrival of the hit Australian soap Neighbours, and a revamped and relaunched Five News fronted by Natasha Kaplinsky.")
        addDir('ITV2',channel+'itv2',2,logo+'67/big_logo.png',"Welcome to the UK's number one digital channel! ITV2 is home to a lively mix of fun, exciting programming, including entertainment, drama, comedy and movies. Youll find original dramas, the hottest shows from the US such as (BAFTA-winning) Entourage, and exciting entertainment.")
        addDir('ITV3',channel+'itv3',2,logo+'26/big_logo.png',"Where great stories are beautifully told ITV3 offers viewers a unique collection of classic and contemporary dramas, movies and original commissions. It also gives you the chance to go behind the scenes and witness the making of some of ITV's best-loved dramas. There's another chance to see some of ITV's popular detective dramas from over the years, including Inspector Morse, Poirot, Midsomer Murders, A Touch of Frost, Prime Suspect and Foyle's War. Other classics you wont want to miss include Quantum Leap and Due South.")
        addDir('ITV4',channel+'itv4',2,logo+'101/big_logo.png',"ITV4 broadcasts a compelling line up of challenging drama; comedy that pushes boundaries; and movies that won't stick to the mainstream. All alongside live and exclusive UEFA Champions League and world class boxing.")
        addDir('E4',channel+'e4',2,logo+'65/big_logo.png',"With E4 the E stands for entertainment. Programming includes Friends, ER, The O.C., Smallville, The Sopranos, What About Brian?, Desperate Housewives, 90210, Gilmore Girls, One Tree Hill, Scrubs, and British dramas such as Shameless, Hollyoaks, Skins and Nearly Famous. Some of the imports, e.g. The O.C., Ugly Betty and Desperate Housewives, are screened on E4 up to one week ahead of their Channel 4 broadcasts.")
        addDir('Film 4',channel+'film-4',2,logo+'13/big_logo.png',"Free, every day. Film4's unbeatable line-up of great movies guarantees something for every type of film fan. Film4 showcases the widest range of titles including classics, the latest Hollywood epics, the best of US and UK independent cinema, foreign flicks and cult cinema.")
        addDir('More4',channel+'more4',2,logo+'97/big_logo.png',"Channel 4's TV channel for grown ups that want both mind and sense of humour stimulated. In short, intelligent and thought-provoking television. More4 certainly doesn't shy away from controversy, and definitely courts debate. It tackles the hard hitting issue through it's commentary and news shows, and brings in cutting edge dramas and comedies totally unafraid of expressing a point of view.")
        addDir('5USA',channel+'5usa',2,logo+'845/big_logo.png',"5 USA reflects the energy, pulse and guts of the USAs great cities. 5 USA will be showcasing the best of American TV including The Beast, starring Patrick Swayze as unorthodox, undercover FBI agent; acclaimed comedy 30 Rock and hit series, The Shield with the further exploits of Detective Vic Mackey.")
        addDir('5USA+1',channel+'5usa1',2,logo+'848/big_logo.png','')
        addDir('5*',channel+'5',2,logo+'851/big_logo.png',"5 star is an entertainment channel for people who like their drama sexier, their documentaries harder, their movies bigger and their soaps soapier. 5 Star is unpredictable, mischievous and relevant with exclusive new shows, blockbuster movies and US series. 5 Star is for people who like to be entertained....")
        addDir('5*+1',channel+'51',2,logo+'854/big_logo.png',"5 star is an entertainment channel for people who like their drama sexier, their documentaries harder, their movies bigger and their soaps soapier. 5 Star is unpredictable, mischievous and relevant with exclusive new shows, blockbuster movies and US series. 5 Star is for people who like to be entertained....")
        addDir('Channel5+1',channel+'channel51',2,logo+'857/big_logo.png',"Channel 5+1 means you never need miss such great shows as Celebrity Big Brother, Neighbours the CSI franchise, The Gadget Show and some great sport!")
        addDir('Dave',channel+'dave',2,logo+'370/big_logo.png',"Dave, the new UKTV entertainment channel, is the home of witty banter'. Dave features top quiz shows and cult comedies, including QI, Top Gear, Never Mind The Buzzcocks, The Catherine Tate Show, and new series such as Argumental.")
        addDir('Pick TV',channel+'pick-tv',2,logo+'371/big_logo.png',"Pick TV offers a compelling mix of general entertainment from quality drama and documentaries to lifestyle and factual entertainment programming. Pick TV showcases favourites from Sky1 and Sky Arts and brings you the latest news and reviews from the worlds of Sky Movies and Sky Sports. Recent highlights from Pick TV include Are You Smarter Than A Ten Year Old?, Coach Trip and Road Wars.")
        addDir('Really',channel+'really',2,logo+'372/big_logo.png',"All the best reality TV programmes including Masterchef & Snog, Marry, Avoid? You 'Really' couldn't make it up!")
        addDir('BBC1 North Island',channel+'bbc-1-north-ireland',2,logo+'361/big_logo.png',"BBC Northern Ireland broadcasts news, sport, entertainment, music, and educational programmes.")
        addDir('CBBC/BBC Three',channel+'cbbcbbc-three',2,logo+'113/big_logo.png',"Offering a broad mix of drama, entertainment, news and factual shows, CBBC is the exciting digital channel for 6 -12 year olds. Broadcast twelve hours a day, every day, this interactive channel hosts a brand new world of compelling programmes that children can really get into. The shows help children make sense of and embrace the world around them while encouraging independent thinking. Some favourites include Roar, Jackanory, Raven and the infamous Tracy Beaker. Programmes introduce children to wildlife, art, sport, music and lots of activities to help them develop more interests and build relationships. BBC4 brings viewers an alternative and wonderful mix of culture, arts, world cinema, science, history, business and current affairs. It unapologetically aims to be British television's most culturally enriching channel. Expect to see some great documentaries, performances, music, films and topical features as well as some cracking drama and comedy.")
        addDir('CBEEBIES/BBC Four',channel+'cbeebiesbbc-four',2,logo+'103/big_logo.png',"CBeebies is dedicated to preschoolers. Packed full of their favourite characters, CBeebies offers 13 hours of programmes every day which encourage your child to play along and learn. Its also completely advert free and with a dedicated website and interactive service, at CBeebies it's Playtime All the Time! BBC4 brings viewers an alternative and wonderful mix of culture, arts, world cinema, science, history, business and current affairs. It unapologetically aims to be British television's most culturally enriching channel. Expect to see some great documentaries, performances, music, films and topical features as well as some cracking drama and comedy.")
        addDir('BBC News',channel+'bbc-news',2,logo+'27/big_logo.png',"The BBC's 24-hour news and information channel that features the most up-to-date news, interviews, business reports, sports results, and weather. Plus, catch the best of the BBC's award-winning current affairs, documentary, and lifestyle programming.")
        setView('movies', 'default') 
        
def PremiumChannels(url):
        addDir('World of Martial Arts Television',channel+'world-of-martial-arts-television',2,logo+'406/big_logo.png',"World Of Martial Arts Instruction & Education.")
        addDir('Ginx',channel+'ginx',2,logo+'796/big_logo.png',"Ginx is your portal into the world's first international video game TV channel. Be a part of the Ginx revolution and get involved!")
        addDir('Ebru',channel+'ebru',2,logo+'914/big_logo.png',"Ebru TV takes pride in being the newest cable network that offers a complete television experience that is both wholesome and exhilarating for family viewers of all ages. Ebru TVs wide range of high quality programs serve to viewers eager for more inclusive and representative portrayals of their lifestyles. It offers members of diverse communities a place to share their unique stories and contributions.")
        addDir('Erbu TV US',channel+'ebru-tv-us',2,logo+'979/big_logo.png','')
        addDir('Halogen TV',channel+'halogen-tv',2,logo+'703/big_logo.png',"Halogen TV is an empowering television network that entertains and motivates individuals looking to be the change they want to see in the world.")
        addDir('HRTV',channel+'hrtv',2,logo+'694/big_logo.png',"HRTV is a 24-hour television based multimedia network dedicated to horseracing which features racing action from many of the sport's greatest racetracks around the world. HRTV also features other forms of equestrian competition, as well as original programming and award-winning documentaries covering a variety of racing and general equestrian topics.")
        addDir('Clubbing TV',channel+'clubbing-tv',2,logo+'691/big_logo.png',"Music Videos dedicated to the clubbing scene.")
        addDir('Sportskool',channel+'sportskool',2,logo+'686/big_logo.png',"Sports programming aimed at teaching enthusiasts to further their skills.")
        addDir('The Ski Channel',channel+'the-ski-channel',2,logo+'265/big_logo.png',"News and videos covering skiing and mountain sports. Ski like the pros with ski resort insider tips on ski conditions, ski runs and ski equipment.")
        addDir('Untamed Sports',channel+'untamed-sports',2,logo+'436/big_big_logo.png',"A gateway for those of us who are devoted, and aspire to participate in outdoor sports and activities.")
        addDir('Parables TV',channel+'parables-tv',2,logo+'405/big_logo.png',"ntroducing the Parables TV Network, a Christian movie channel that will connect viewers with the best in inspirational entertainment anytime, anywhere. Parables TV is poised to be the destination for Christian movies that will also feature original series, documentaries, as well as specials that are profound and uplifting stories of faith. Parables TV aims to deliver on its mission to connect viewers with stories that uplift, inspire, connect and fulfill messages of hope, while entertaining and captivating our viewers.")
        addDir('Wealth TV',channel+'wealth-tv',2,logo+'403/big_logo.png',"WealthTV...it's your life, spend well. WealthTV is a 24/7 high definition lifestyle and entertainment network.")
        addDir('R&R Television',channel+'rr-television',2,logo+'402/big_logo.png',"RRTV allows each viewer the unique and rare opportunity to experience the world through a rich retelling of shared journeys and exciting, eye-opening adventures. Tune in to Resorts and Recreation Television and get hip to the world around you.")
        addDir('WW Extreme',channel+'ww-extreme',2,logo+'394/big_logo.png',"All sorts of Extreme Sports.")
        addDir('Filmon Reels',channel+'filmon-reels',2,logo+'395/big_logo.png',"Classic films from the golden era.")
        addDir('Wheels TV',channel+'wheels-tv',2,logo+'397/big_logo.png',"WheelsTV is a multifaceted media brand owned by Automotive Networks Corporation that produces and distributes original automotive content.")
        addDir('American Horrors',channel+'american-horrors',2,logo+'393/big_logo.png',"Hart Fisher's Classic & Modern Horror Channel.")
        addDir('e Scapes HD TV',channel+'escapes-hd-tv',2,logo+'341/big_logo.png',"eScapes Television broadcasts high-definition scenic video of beaches, nature scenes, lighthouses, and more, set to adult contemporary radio.")
        addDir('Havoc Television',channel+'havoc-television',2,logo+'335/big_logo.png',"Havoc Television specializes in independent music and action sports videos.")
        addDir('My Family TV',channel+'my-family-tv',2,logo+'301/big_logo.png',"Family friendly programming including Extreme sports and the great outdoors, Reality shows, Fitness, Home Improvement, Kids entertainment, Classic TV Programs, Hollywood Movies and more.")
        addDir('My Combat Channel',channel+'my-combat-channel',2,logo+'295/big_logo.png',"My Combat Channel is a 24/7 combat sports TV network.")
        addDir('Fashion TV',channel+'fashion-tv',2,logo+'21/big_logo.png',"International Fashion TV channel dedicated to fashion shows, fashion models & designers that broadcasts 24 hours a day.")
        addDir('TVC Latino',channel+'tvc-latino',2,logo+'213/big_logo.png',"TVC+Latino is the US feed for the number 1 cable system in Mexico. TVC+Latino has exclusive, high quality programming superior to most other Spanish speaking networks available today")
        addDir('Filmon Breaking News',channel+'filmon-breaking-news',2,logo+'302/big_logo.png',"24/7 Breaking News.")
        setView('movies', 'default')
         
def ComedyChannels(url):
        addDir('Filmon at the Improv',channel+'filmon-at-the-improv',2,logo+'407/big_logo.png',"classic episodes of AN EVENING AT THE IMPROV featuring the world;s best comics around the clock.")
        addDir('Popcorn TV',channel+'popcorn-tv',2,logo+'716/big_logo.png',"Laugh out loud comedy, goofs and gaffs TV.")
        addDir('Comedy Net',channel+'comedy-net',2,logo+'497/big_logo.png',"Stand-up comedy channel.")
        addDir('Kevin Spencer TV',channel+'kevin-spencer-tv',2,logo+'387/big_logo.png',"Canada's most popular animated series for adults.")
        addDir('ComedyTime TV',channel+'comedytime-tv',2,logo+'344/big_logo.png',"Comedy Time TV brings you the best amateur Stand Up comedy on the circuit.")
        setView('movies', 'default') 
        
def AsianChannels(url):
        addDir('Arirang TV',channel+'arirang-tv',2,logo+'932/big_logo.png',"Arirang TV, operated by the Korea International Broadcasting Foundation, is an international English-language network based in Seoul, South Korea. Launched in 1997, Arirang TV is currently viewed by more than 97.3 million households in the Asia-Pacific region, Europe, Middle East, North Africa and the Americas 24 hours a day. Broadcasts a wide range of programmes such as Korean News, cultural, educational and entertainment shows, dramas, documentaries and more.")
        setView('movies', 'default') 
        
def MovieChannels(url):
        addDir('MyFamily TV East',channel+'myfamily-tv-east',2,logo+'779/big_logo.png','')
        addDir('American Primetime Television',channel+'american-primetime-television',2,logo+'707/big_logo.png',"Various entertainment programming including Movies and TV series.")
        addDir('Filmon Martial Arts',channel+'filmon-martial-arts',2,logo+'10/big_logo.png',"Cult and Classic Martial Arts movies.")
        addDir('Threshold',channel+'threshold',2,logo+'514/big_logo.png','')
        addDir('Filmon Stars',channel+'filmon-stars',2,logo+'494/big_logo.png',"Filmon's very own channel for the Stars and their movies.")
        addDir('Action Cinema',channel+'mbc-action',2,logo+'369/big_logo.png',"The best in Action Cinema.")
        addDir('Inspirational Films',channel+'inspirational-films',2,logo+'503/big_logo.png',"A channel of American movies.")
        addDir('Hollywoodland Channel',channel+'hollywoodland-channel',2,logo+'411/big_logo.png',"Classic Hollywood Movies.")
        addDir('Sci-Fi Channel',channel+'sci-fi-telly',2,logo+'382/big_logo.png',"Classic Sci-Fi films.")
        addDir('The Western Channel',channel+'the-western-channel',2,logo+'384/big_logo.png',"The best in Classic Westerns.")
        addDir('Cultra',channel+'cultra',2,logo+'336/big_logo.png',"Cultra brings you the best in cult movies covering all genres.")
        addDir('Filmon Grab Bag TV',channel+'filmon-grab-bag-tv',2,logo+'310/big_logo.png',"A variety of films and documentary brought to you by FilmOn.")
        addDir('Filmon Classics',channel+'filmon-classics',2,logo+'206/big_logo.png',"Classic movies.")
        setView('movies', 'default') 
        
def LifestyleChannels(url):
        addDir('Buzz TV',channel+'buzz-tv',2,logo+'782/big_logo.png','')
        addDir('Steel Dreams',channel+'steel-dreams',2,logo+'784/big_logo.png','REAL. LIFE.. ACTION... Steel Dreams is the weekly half-hour television show that launched todays popular motor sports programming with unprecedented border-to-border and coast-to-coast on site coverage of exciting races, speed events and big shows filled with industry superstars, high-profile celebrities and famed designer/builders.')
        addDir('Distant Roads',channel+'distant-roads',2,logo+'787/big_logo.png',"The longest running, most widely watched family road travel and RV television series in the world. Includes parasailing, ballooning, hiking, and golfing.")
        addDir('Travel Channel+1',channel+'travel-channel1',2,logo+'842/big_logo.png',"Inspirational, informative and entertaining, Travel Channel presents a uniquely panoramic and objective perspective on the travel experience.")
        addDir('AMG TV',channel+'amg-tv',2,logo+'902/big_logo.png',"AMGTV is one of the newest entertainment program networks providing a 24/7 lineup of general entertainment family programming. AMGTV programming is useful and informative, entertaining and distinctive. A slice of life with shows that highlight the entertainment wishes of viewers Movies Classic to First Run, Home Life, Adventure, Sports, Drama, News, Comedy, Health, Finance, Instruction, Travel, Educational Programs and Entertainment Childrens programs. New shows and movies every season!")
        addDir('Eye for an Eye',channel+'eye-for-an-eye',2,logo+'911/big_logo.png',"Judge Akim Extreme Akim Anastopoulo hosts this popular courtroom drama series with a modern take on the criminal justice system. The Eye for an Eye series aims to make the judgments fit the crimes in often hilarious ways, featuring hosts Kato Kaelin and Tommy Habeeb, and bailiff Big Sugar Ray Phillips.")
        addDir('PopStop TV',channel+'popstop-tv',2,logo+'770/big_logo.png',"Pop culture E! Entertainment-style celebrity coverage with XiXi Yang.")
        addDir('The Miki Show',channel+'the-miki-show',2,logo+'728/big_logo.png',"All the latest video game reviews.")
        addDir('INSP',channel+'insp',2,logo+'700/big_logo.png',"American TV series, movies and entertainment programming.")
        addDir('Eco-Rico',channel+'eco-rico',2,logo+'710/big_logo.png',"An Eco-lifestyle Food Network con SABOR! A salsa-rific cooking show, organic Latin food, recipes & tips. Eat good, feel good & look good while ya do good! Because happy people don't want to blow up the planet. They want to save it!")
        addDir('Men7',channel+'men7',2,logo+'396/big_logo.png',"All Things Men.")
        addDir('Veg TV',channel+'veg-tv',2,logo+'383/big_logo.png',"Veg TV is your view to a healthier you, 24/7.")
        addDir('GeoBeats Travel',channel+'geobeats-travel',2,logo+'386/big_logo.png',"Guided tours of your next International destination.")
        addDir('Legacy TV',channel+'legacy-tv',2,logo+'340/big_logo.png',"Christian Oriented Programming.")
        addDir('Jewish Life TV',channel+'jewish-life-tv',2,logo+'332/big_logo.png','Jewish Culture.')
        addDir('Time tv',channel+'time-tv',2,logo+'414/big_logo.png','News & Entertainment from India.')
        addDir('Unreliable Sources',channel+'unreliable-sources',2,logo+'239/big_logo.png','24/7 topics and News with the Unreliable Sources team.')
        addDir('Motorz',channel+'motorz',2,logo+'262/big_logo.png','We deliver everything Motorz 24/7.')
        addDir('Wine',channel+'wine-channel-tv',2,logo+'263/big_logo.png','Discovering Wine around the world.')
        setView('movies', 'default') 
        
def KidsChannels(url):
        addDir('Kartoon Klassics',channel+'kartoon-klassics',2,logo+'793/big_logo.png','')
        addDir('Animal Atlas',channel+'animal-atlas',2,logo+'799/big_logo.png',"Animal Atlas takes children on a tour of discovery to uncover the secrets of how animals live and thrive. Children will meet animals from the familiar to the astounding, from the domesticated to the wild, including the diverse creatures of the African savanna, the finned and flippered of the big deep, the colorful cast of the equatorial rainforest, and every other animal on the planet. Learning about animals has never been so heartwarming and wildly entertaining!")
        addDir('Emba Kids',channel+'emba-kids',2,logo+'719/big_logo.png',"Kids cartoons from Sonic The Hedgehog to Highlander and lots lots more.")
        addDir('Smile of Child',channel+'smile-of-child',2,logo+'401/big_logo.png',"The children's television network, wholesome quality programming for kids, 24 hours a day, helping children build positive social and spiritual skills at a young age.")

def EducationChannels(url):
        addDir('UWTV',channel+'uwtv',2,logo+'808/big_logo.png',"UWTV is a service of the University of Washington, and provides our worldwide audience with unique, high-quality educational programming. UWTV programs show how UW responds to critical issues facing our region and the world: by being responsible and engaged global citizens, shaping a more sustainable future, driving innovations that serve society and creating healthier lives.")
        addDir('The Florida Channel',channel+'the-florida-channel',2,logo+'305/big_logo.png',"The Florida Channel is committed to serving the people of Florida with quality Legislative coverage - bringing the people closer to their government.")

def ReligiousChannels(url):
        addDir('DayStar',channel+'daystar',2,logo+'833/big_logo.png','')
        addDir('TBN',channel+'tbn',2,logo+'398/big_logo.png',"Trinity Broadcasting Network. Delivering the Christian message of hope around the globe.")
        addDir('The Church Channel',channel+'the-church-channel',2,logo+'399/big_logo.png',"The Church Channel is the only network broadcasting the very best in church services and ministry programs from across the nation, 24 hours a day, seven days a week.")
        setView('movies', 'default') 
        
def HorrorChannels(url):
        addDir('Horror Channel',channel+'horror-channel',2,logo+'836/big_logo.png',"Horror Channel is the UK's first channel dedicated to the dark side of cinema and television. With an eclectic mix of ground-breaking and genre-defining content including horror films, documentaries, Director's Nights and supernatural series, you'll be entertained, informed and terrified.")
        addDir('ShockORama',channel+'shockorama',2,logo+'509/big_logo.png',"The shock horror channel.")
        addDir('Braindamage TV',channel+'braindamage-tv',2,logo+'339/big_logo.png',"Dedicated to horror movies.")
        addDir('Macare Theatre',channel+'macabre-theatre',2,logo+'315/big_logo.png',"Classic horror movies.")
        addDir('RSquared',channel+'rsquared',2,logo+'256/big_logo.png',"Independent horror movies all day every day.")
        setView('movies', 'default')
         
def NewsChannels(url):
        addDir('CNBC',channel+'cnbc',2,logo+'860/big_logo.png',"This international television leader reports financial news, stock-market action and emerging business trends. CNBC features breaking news, interviews with corporate, government and Wall Street experts.")
        addDir('DVIDs TV',channel+'dvids-tv',2,logo+'725/big_logo.png',"Exciting military footage captured by journalists with the full cooperation of the US Defense department.")
        addDir('Free Speech TV',channel+'free-speech-tv',2,logo+'697/big_logo.png',"The News channel powered by the people.")
        addDir('Biz TV',channel+'biztv',2,logo+'343/big_logo.png',"BIZ TV is the only network committed to original, educational and inspiring programming about real people succeeding in business.")
        addDir('WeatherNation',channel+'weathernation',2,logo+'329/big_logo.png',"Real weather, pure and simple. Get seven day and extended weather forecasts with maps, radar reports and trend charts. Read articles and share your tips.")
        addDir('NASA HD',channel+'nasa-hd',2,logo+'330/big_logo.png',"NASA's vision: To reach for new heights and reveal the unknown so that what we do and learn will benefit all humankind.")
        addDir('The Pentagon',channel+'the-pentagon',2,logo+'333/big_logo.png',"Broadcasts military news and information for the members of the U.S. Armed Forces.")
        addDir('France24',channel+'france24',2,logo+'298/big_logo.png',"Offering a French perspective on world events. Multilingual broadcast in French, English, and Arabic.")
        addDir('Russia Today',channel+'russia-today-2',2,logo+'93/big_logo.png',"RT, previously known as Russia Today, is a globally broadcast English-language news channel from Russia, and the first all-digital Russian TV network, sponsored by the state owned Russian news agency RIA-Novosti.")
        addDir('AL Jazeera',channel+'al-jazeera',2,logo+'4/big_logo.png',"Al Jazeera English is international news that takes you to the heart of the story. Join us every evening for in depth news and analysis from around the globe uniquely brought to you from inside the Middle East, London and Washington DC. A wealth of diverse programming will take you closer to global issues which give a voice to untold stories, promote debate and challenge your perceptions.")
        addDir('Bloomberg',channel+'bloomberg',2,logo+'81/big_logo.png',"A sophisticated 24-hour business and financial news channel, BLOOMBERG TELEVISION delivers power tools for power players and serious investors via 10 networks in seven languages, reaching over 200 million homes around the world. We build on our world-class resources to present up-to-the-minute coverage of financial news and markets, bringing our journalistic expertise to our programming with the best reporters to deliver the news and the best journalists to add perspective and analysis.")
        setView('movies', 'default')
         
def BikiniChannels(url):
        addDir('MiamiTV',channel+'miamitv',2,logo+'866/big_logo.png',"Miami TV - Girls Models is an online channel that delivers programming related to exotic women in the fashion & art world, style & beauty in great productions.")
        addDir('Bikini TeeVee',channel+'bikini-teevee',2,logo+'380/big_logo.png',"Babes in bikini's, all day everyday.")
        addDir('Party TeeVee',channel+'party-teevee',2,logo+'790/big_logo.png',"Join the party and celebrate girls, parties & nightclubs from around the globe.")
        setView('movies', 'default') 
        
def ArabicChannels(url):
        addDir('iFilm',channel+'ifilm',2,logo+'908/big_logo.png','')
        addDir('MBC',channel+'mbc',2,logo+'367/big_logo.png','News and entertainment programmes.')
        addDir('MBC2',channel+'mbc2',2,logo+'368/big_logo.png',"American Hollywood movies as well as British, Canadian, French, Indian, Chinese and other foreign films.")
        addDir('MBC Action',channel+'mbc-action',2,logo+'369/big_logo.png',"American Series, Movies and fight events.")
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
        addDir('ProSieben Austria',channel+'prosieben-austria',2,logo+'520/big_logo.png',"ProSieben program brands, blockbusters, American television series, Stefan Raab events, Germanys next top model - with Heidi Klum, and Galileo.")
        addDir('Eins Extra',channel+'eins-extra',2,logo+'415/big_logo.png',"German Variety and Movies.")
        addDir('Eins Plus',channel+'eins-plus',2,logo+'418/big_logo.png',"German Variety and Movies.")
        addDir('Eins Festival',channel+'eins-festival',2,logo+'421/big_logo.png',"German Variety and Movies.")
        addDir('QVC Deutschland',channel+'qvc-deutschland',2,logo+'354/big_logo.png',"Home Shopping from Germany.")
        addDir('QVC PLUS',channel+'qvc-plus',2,logo+'355/big_logo.png',"Home Shopping from Germany.")
        addDir('zdf.kultur',channel+'zdfkultur',2,logo+'359/big_logo.png','The pop-culture channel.')
        addDir('ZDFneo',channel+'zdfneo',2,logo+'360/big_logo.png',"ZDFneo broadcasts comedy and drama series produced in-house. Shows imported from America and the United Kingdom plus a few documentaries, music shows, and movies round out the schedule.")
        setView('movies', 'default') 
        
def LatinChannels(url):
        addDir('Andalucia TV',channel+'andalucia-tv',2,logo+'526/big_logo.png',"Various news and entertainment programming.")
        addDir('Telemadrid',channel+'telemadrid',2,logo+'529/big_logo.png','Educational programming.')
        addDir('RT Espanol',channel+'rt-espaaol',2,logo+'299/big_logo.png','RT is the first TV channel broadcasting in Spanish from Russia to the world.')
        addDir('RTVE',channel+'rtve',2,logo+'23/big_logo.png',"TVE Internacional is an internationally broadcast Spanish-language channel run by Spains national broadcaster, TVE. Programming includes a mix of news, discussion-based programmes and drama and documentaries from TVEs La 1 and La 2 Spanish networks.")
        addDir('RTpi America',channel+'rtpi-america',2,logo+'303/big_logo.png','Portuguese Public Broadcaster.')
        setView('movies', 'default') 
        
def DocumentaryChannels(url):
        addDir('War in Color',channel+'war-in-color',2,logo+'491/big_logo.png','')
        addDir('War and Crime',channel+'war-crime-network',2,logo+'381/big_logo.png','Crime Documentaries & War Shows.')
        setView('movies', 'default') 
        
def ItalianChannels(url):
        addDir('QVC Italia',channel+'qvc-italia',2,logo+'463/big_logo.png','The home shopping channel.')
        addDir('Canale Italia 84',channel+'canale-italia-84',2,logo+'442/big_logo.png','Italian shopping channel.')
        addDir('Canale Italia',channel+'canale-italia',2,logo+'445/big_logo.png','Italian shopping channel.')
        addDir('Studio Europa',channel+'studio-europa',2,logo+'451/big_logo.png','Variety Programming from Italy.')
        addDir('Justice TV',channel+'justice-tv',2,logo+'454/big_logo.png','Legal News from Italy.')
        addDir('RAI 1',channel+'rai-1',2,logo+'375/big_logo.png','Italian Variety and News Broadcaster.')
        addDir('RAI 2',channel+'rai-2',2,logo+'376/big_logo.png','Italian Variety and News Broadcaster.')
        addDir('RAI 3',channel+'rai-3',2,logo+'377/big_logo.png','Italian Variety and News Broadcaster.')
        addDir('Camera dei Deputati',channel+'camera-dei-deputati',2,logo+'379/big_logo.png','Italian Government Coverage.')
        setView('movies', 'default') 
        
def MindBodyAndSpiritChannels(url):
        addDir('Fitness Lifestyle TV',channel+'fitness-lifestyle-tv',2,logo+'410/big_logo.png','The Right Fit Lifestyle.')
        addDir('Cornerstone TV',channel+'cornerstone-tv',2,logo+'212/big_logo.png','')
        addDir('Supreme Master TV',channel+'supreme-master-tv',2,logo+'304/big_logo.png','Supreme Master Television is an international, non-profit channel airing constructive news and programs that foster peace and promote healthy, green living. Broadcasting on 14 satellite platforms and on over 95 cable and IPTV networks, in more than 60 languages and over 40 language subtitles to date.')
        setView('movies', 'default') 
        
def FreeChannels(url):
        addDir('Linkct Network',channel+'linkct-network',2,logo+'390/big_logo.png','')
        setView('movies', 'default') 
        
def ShoppingChannels(url):
        addDir('QVC HD',channel+'qvc-hd',2,logo+'413/big_logo.png','The home shopping channel brought to you in HD.')
        addDir('9021go TV',channel+'9021go-tv',2,logo+'214/big_logo.png','')
        addDir('Jewelry TV',channel+'jewelry-tv',2,logo+'306/big_logo.png',"JTV.com offers the largest selection of fine jewelry and loose gemstones in the world at up to 80% off retail prices.")
        setView('movies', 'default') 
        
def MainChannels(url):
        addDir('Phoenix',channel+'phoenix',2,logo+'424/big_logo.png','German Variety and Movies.')
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
        req = urllib2.Request(url)
        req.add_header('User-Agent', USER_AGENT)
        response = urllib2.urlopen(req)
        link1=response.read()
        response.close()  
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
                addLink(name,url,playPath,app,pageUrl,swfUrl,tcUrl)
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
                    addLink(name,url,playPath,app,pageUrl,swfUrl,tcUrl)
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
        xbmcgui.Dialog().ok('FilmOn','            To Use This Plugin Please Sign Up To ','                    [COLOR yellow][B]WWW.XBMCHUB.COM[/B][/COLOR]','Please put XBMCHUB User and Pass in Addon Settings')
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
