# python script to implement DNS cache 

# python
from datetime import datetime
import socket 
import sys
import time
import os
if os.path.isfile('out.txt'):
   File = file('out.txt')
   line = File.readlines()
   TTL = long(line[1]) + 5
   print "TTL = %d" % TTL
   system_Time = int(round(time.time()))
   print "system time = %d" % system_Time
   #print "%d >  %d" % (system , TTL)
   if system_Time > TTL:
      system_Time = int(round(time.time()))
      domain_name = socket.gethostbyname('www.google.com')
      print "File reloded"   
      File = open('out.txt', 'w')
      sys.stdout = File
      print domain_name
      print system_Time 
      
       
   else:
      
      File = open('out.txt')
      line = File.readlines()
      ip = line[0]
      print "using ip %s" % ip 
# ping test on ip
      #response = os.system("ping -c 1 " + ip)
      #if response == 0:
       #   print ip, 'is up!'
      #else:
       #   print hip, 'is down!'
else :
     system_Time = int(round(time.time()))
     domain_name = socket.gethostbyname('www.google.com')   
     File = file('out.txt', 'w')
     sys.stdout = File
     print domain_name
     print system_Time
     print "File created"

File.close()
