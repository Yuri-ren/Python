import os

data=os.popen('df -h').read()
print type(data)
print data
