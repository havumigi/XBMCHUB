'''
Created on 24 feb 2012

@author: Batch
'''
import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import os
import re
ADDON = xbmcaddon.Addon(id='plugin.video.EasyNews')


def addon():
    return ADDON

def MOVIE_FILESIZE():
    quality = ADDON.getSetting('moviefilesize')
    if quality == '0':
        return ''
    elif quality == '1':
        return '18'
    elif quality == '2':
        return '19'
    elif quality == '3':
        return '20'
    elif quality == '4':
        return '21'
    elif quality == '5':
        return '22'
    elif quality == '6':
        return '23'
    elif quality == '7':
        return '24'
    elif quality == '8':
        return '26'
    elif quality == '9':
        return '28'
    elif quality == '10':
        return '39'
    elif quality == '11':
        return '30'
        
        
def TV_FILESIZE():
    quality = ADDON.getSetting('tvfilesize')
    if quality == '0':
        return ''
    elif quality == '1':
        return '18'
    elif quality == '2':
        return '19'
    elif quality == '3':
        return '20'
    elif quality == '4':
        return '21'
    elif quality == '5':
        return '22'
    elif quality == '6':
        return '23'
    elif quality == '7':
        return '24'
    elif quality == '8':
        return '26'
    elif quality == '9':
        return '28'
    elif quality == '10':
        return '39'
    elif quality == '11':
        return '30'

def MOVIE_FILENAME():
    quality = ADDON.getSetting('moviefilename')
    if quality == '0':
        return ''
    elif quality == '1':   
        return 'avi'
    elif quality == '2':
        return 'mkv'
    elif quality == '3':
        return 'mp4'
    elif quality == '4':
        return 'iso'
    elif quality == '5':
        return 'divx'
    elif quality == '6':
        return 'mpg'
    elif quality == '7':
        return 'flv'
    elif quality == '8':
        return 'wmv'
    elif quality == '9':
        return 'mov'
    elif quality == '10':
        return 'asf'
    elif quality == '11':
        return 'rm'

def TV_FILENAME():
    quality = ADDON.getSetting('tvfilename')
    if quality == '0':
        return ''
    elif quality == '1':   
        return 'avi'
    elif quality == '2':
        return 'mkv'
    elif quality == '3':
        return 'mp4'
    elif quality == '4':
        return 'iso'
    elif quality == '5':
        return 'divx'
    elif quality == '6':
        return 'mpg'
    elif quality == '7':
        return 'flv'
    elif quality == '8':
        return 'wmv'
    elif quality == '9':
        return 'mov'
    elif quality == '10':
        return 'asf'
    elif quality == '11':
        return 'rm'
        
        
