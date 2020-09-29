#! /usr/bin/python3

print("content-type: text/html")
print()

import cgi 
import subprocess as sp

form= cgi.FieldStorage()

launchname= form.getvalue("ln")
launchimg=form.getvalue("li")

launchcmd="sudo docker run -d --name {0} {1}".format(launchname,launchimg)

launchoutput = sp.getstatusoutput(launchcmd)

launchstatus= launchoutput[0]
launchout= launchoutput[1]

if launchstatus==0:
	print("OS Launched")
else:
	print("Some Error")






