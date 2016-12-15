#Save all Images from a web site using urllib, re and BeautifulSoup. 
#Works fine in python 2.7

import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter -')
fhand = urllib.urlopen(url)
html= fhand.read()

soup=BeautifulSoup(html)

for link in soup.findAll('img'):
    imgPath = link.get('src')
    imgPathList = re.findall('[^/\\&\?]+\.\w{3,4}',imgPath)
    if imgPath.startswith('/'):continue
    
    #print imgPath
    imgName = imgPathList[len(imgPathList) -1]
    urllib.urlretrieve(imgPath,imgName)

print 'Done!'   
