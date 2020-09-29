#! /usr/bin/python3

print("content-type: text/html")
print()pul

import cgi 
import subprocess as sp

form= cgi.FieldStorage()
pulli=form.getvalue("pi")

pullcmd="docker pull {0}".format(pulli)

pulloutput = sp.getstatusoutput(pullcmd)

pullstatus= pulloutput[0]
pullout= pulloutput[1]

if pullstatus==0:
	
	print("Pull Seccess")
	print(pullstatus)
else:
	print("Some Error")
	print(pullout)

