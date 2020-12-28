#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# ur a loser LOL.
subprocess.call('clear',shell=True)

#i told ya.
remoteServer   =input("Enter a remote host to scan:")
remoteServerIP = socket.gethostbyname(remoteServer)

# hahahahahahaha LOSER!
print("-" * 60)
print("please wait, scanning remote host", remoteServerIP)
print("-" * 60)

#check what time the scan started 
t1=datetime.now()

#it scanns all pots from 1 to 1024

#i like blueberries.

try:
  for port in range(1,100):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result=sock.connect_ex((remoteServerIP,port))
    # print("currently testing")
    if result==0:
       print("Port{}:	Open".format(port))
    sock.close()
except KeyboardInterrupt:
  print("You pressed Ctrl+C")
  sys.exit()

except socket.gaierror:
  print('Hostname could not be resolved. Exiting')
  sys.exit()

except socket.error:
  print("Couldn't connect to server")
  sys.exit() 
# Checking the time again
t2=datetime.now()

# Calculates the differences or time, to see how long it took to run the script
total=t2-t1
# Printing the information to screen
print('scanning Completed in:',total)
