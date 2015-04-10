'''
Created on Dec 31, 2013

@author: Rod
'''

import os
import sys
import datetime
from FileAttrClass import FileAttr
if __name__ == '__main__':
    print ("Hello World DirWalk main")
    picexts = [".jpg", ".bmp", ".png", ".gif", ".jpeg", '.tif']
    ignoreexts = [".xml", ".db", ".ds_store", 'avi', '.attr', '.thm', '.mov', '.avi', '.mp4', '.c6e', '.ini', '.info', '.lnk', '.alb', '', '.mpg', '.12', '.wmf', '.zip', '.psd', '.docx', '.3gp', '.jpg_disabled', '.avin' ]
    #C:\Users\Rod\Pictures\VegasPhoenix\thumbnails
    #"C:/Temp/realtemp/ee-datasets-master"
    #C:\Users\Rod\Pictures
    #c:\Users\Rod\Pictures\iphoto dec2006thrujan2007
    rootdir = "C:\Users\Rod\Pictures" 
    dirs = []
    totaldirs = 0
    for root, subFolders, files in os.walk(rootdir):
        for folder in subFolders:
            dirPathName = os.path.join(root,folder)
            print (dirPathName)
            dirs.append(dirPathName)
            totaldirs = totaldirs + 1
    print ("total dirs is " + str(totaldirs) ) 
    
            