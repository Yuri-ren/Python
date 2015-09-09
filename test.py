import re
import urllib

filename='test'
s='http://imgsrc.baidu.com/forum/w%3D580/sign=cfad46188401a18bf0eb1247ae2f0761/fd0ee924b899a90108719b021e950a7b0208f579.jpg'
print s 
urllib.urlretrieve(s,"test.gif")
