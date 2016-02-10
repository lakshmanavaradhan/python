# python
scripts 
import socket 
from joblib import Memory
mem =Memory(cachedir='/tmp/joblib')
a = socket.gethostbyname('www.google.com')   
b = mem.cache(a)
print b
