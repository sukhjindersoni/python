#! /usr/bin/python3

print("content-type: text/html")
print()

import cgi 
import subprocess as sp

form= cgi.FieldStorage()
ipcheck=form.getvalue("ipn")

ipcmd1="sudo docker container inspect --format '{{.NetworkSettings.IPAddress}}' "
ipcmd2= "{0}".format(ipcheck)
ipcmd=ipcmd1+ipcmd2

ipoutput = sp.getstatusoutput(ipcmd)

ipstatus= ipoutput[0]
ipout= ipoutput[1]

if ipstatus==0:
	
	print(ipout)
else:
	print("Some Error")
	print(ipstatus)

