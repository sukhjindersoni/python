#! /usr/bin/python3

print("content-type: text/html")
print()

import cgi 
import subprocess as sp

form= cgi.FieldStorage()
dcom=form.getvalue("dc")

if (dcom=="Current Running Containers"):
	dcmd="sudo docker ps"
elif (dcom=="Images Present"):
	dcmd="sudo docker images"
elif (dcom=="Information"):
	dcmd="sudo docker info"
elif ( dcom=="Help"):
	dcmd="sudo docker --help"
else:
	print("Give an Input")

doutput = sp.getstatusoutput(dcmd)

dstatus= doutput[0]
dout= doutput[1]

if dstatus==0:
	print("<pre>{0}</pre>".format(dout))
else:
	print("Some Error")
	print(doutput[1])

