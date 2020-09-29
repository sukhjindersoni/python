#! /usr/bin/python3

print("content-type: text/html")
print()

import cgi 
import subprocess as sp

form= cgi.FieldStorage()

tempimg=form.getvalue("ti")
tempcom=form.getvalue("tc")

#tempcmd="sudo docker run -dit --rm {0} {1}".format(tempimg,tempcom)
tempcmd="sudo docker run --name random --rm centos date"
tempoutput = sp.getstatusoutput(tempcmd)

tempstatus= tempoutput[0]
tempout= tempoutput[1]

if tempstatus==0:
	print(tempout)
	
else:
	print("Some Error")
	print(tempstatus)
	print(tempout)








