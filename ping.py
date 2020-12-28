#!/usr/bin/python
import subprocess

DB=[]
thefile=open("IPs_Found.txt","a")
for brier_creek in range(75,85):
  address="192.168.1."+str(brier_creek)
  res=subprocess.call(['ping','-c','3',address])
  if res==0:
    print("ping to",address,"ok")
    DB.append(address)
    thefile.write(address)
  elif res==2:
    print("no response from",address)
  else:
    print("ping to",address,"failed")
print("loser")
print("IP Address currently in use include:")
print("********************************************")
for result in range(0,len(DB)):
   print(DB[result])
thefile.close()
