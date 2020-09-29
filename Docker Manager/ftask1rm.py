#! /usr/bin/python3

print("content-type: text/html")
print()

import cgi 
import subprocess as sp

form= cgi.FieldStorage()
rmname=form.getvalue("rn")

removecmd="sudo docker container rm {0} -f".format(rmname)

removeoutput = sp.getstatusoutput(removecmd)

removestatus= removeoutput[0]
removeout= removeoutput[1]

if removestatus==0:
	print("OS Removed")
	print(removeoutput[0])
else:
	print("Some Error")
	print(removeoutput[1])

