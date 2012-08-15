import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import os


ADDON = xbmcaddon.Addon(id='plugin.video.MikeysKaraoke')
DATA_PATH = os.path.join(xbmc.translatePath('special://profile/data/plugin.video.MikeysKaraoke'), '')

def addon():
    return ADDON

def setView():
    if ADDON.getSetting('auto-view') == 'true':
        return True
    else:
        return False

def history_10():
        return ADDON.setSetting('history_10','')
        return ADDON.getSetting('history_10')        
        return history_9()
def history_9():
        return ADDON.getSetting('history_9')
        return ADDON.setSetting('history_9','')        
        return history_8()
        

def history_8():
        return ADDON.setSetting('history_8','')
        return ADDON.getSetting('history_8')        
        return history_7()
        

def history_7():
        return ADDON.setSetting('history_7','')
        return ADDON.getSetting('history_7')        
        return history_6()
        

def history_6():
        return ADDON.setSetting('history_6','')
        return ADDON.getSetting('history_6')        
        return history_5()
        

def history_5():
        return ADDON.setSetting('history_5','')
        return ADDON.getSetting('history_5')        
        return history_4()
        
        
def history_4():
        return ADDON.setSetting('history_4','')
        return ADDON.getSetting('history_4')        
        return history_3()
                

def history_3():
        return ADDON.setSetting('history_3','')
        return ADDON.getSetting('history_3')        
        return history_2()
                

def history_2():
        return ADDON.setSetting('history_2','')
        return ADDON.getSetting('history_2')        
        return history_1()
        

def history_1():
        return ADDON.setSetting('history_1','')
        return ADDON.getSetting('history_1') 
        
        
