#python-flask-docker-redhat-aws
#task2 #linuxworld 

 Docker Manager 

A basic webpage able to :
- Launch a Docker Container
- Remove a Docker Container
- Find the IPAddress of a Docker Container
- Run any command on any Temporary Docker Container - By Creating the container running the command and then removing the container.
- Few Other Docker Commands like the Current OS or Containers running , 
 currently present images , docker information and docker help
 
The Whole system is on httpd Apache webserver running on top of Redhat , using python , docker , CGI and API .
Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels.
The Common Gateway Interface (CGI) provides the middleware between WWW servers and external databases and information sources.
An application programming interface (API) is a computing interface which defines interactions between multiple software intermediaries. It defines the kinds of calls or requests that can be made, how to make them, the data formats that should be used, the conventions to follow, etc.


Working :-
#! /usr/bin/python3   - Is the part of the header of the file which gives the cgi the path to the python compiler to execute and run the code before reaching back to the client browser

print("content-type: text/html")   - Is used to tell that the final result is to be given in text and in HTML format.

print()  - This empty print statement prints a empty line due to the end="\n" and is used to differentiate between the header and the body of the file.

sudo is required in every command of docker because only the root user or the user with all the privilages can run the docker commands using API so the "sudoers" file is configured for the "apache" user 

-- Launching Container
After fetching the value inputed by the user the values are stored in 2 different variables "ln , li" from which the values are captured  in "launchname and launchimg"(no particular names) variables using the "FieldStorage()" and "getvalue()" of the "cgi" module of python and the values are then given to the format() which replaces them in 

launchcmd="sudo docker run -d --name {0} {1}"
As
launchcmd="sudo docker run -d --name {0} {1}".format(launchname,launchimg)
{0} is for the 0 index value of the "format()" and takes the value of "launchname" likewise {1} is for 1 index

Then using the "getstatusoutput()" of "subprocess" module 
The "getstatusoutput()" is different form the "getoutput()" of "subprocess" module as it also gives the 'Status Code' of the command which is 0 if the command was successful and and other number means some error
Using "if else statement" on the status code of the error -
If it is Zero then the output is printed on a new brower tab 
if launchstatus==0:
	print("OS Launched")
else:
	print("Some Error")

-- Removing Container

The value is the name of the os or the container the user wants to remove and it is fetched in a variable "rn" which is then fetched with "getvalue()" to the variable "rmname" and placed in the string 

removecmd="sudo docker container rm {0} -f".format(rmname)
Then using the subprocess the command is executed and output is Given "Os Removed"

-- IPAddress of a Container

The value is the name of the container in "ipn" fetched by "ipcheck" variable using "getvalue()" 

ipcmd="sudo docker container inspect --format '{{.NetworkSettings.IPAddress}}' {0}".format(ipcheck)

docker inspect name -- the file is in .json , is used to inspect the container and displays the information about the container like the macaddress and the ipaddress but the ipaddress. Using --format we can fetch the ipaddress inside the var NetworkSettings and that itself is in one var thats why itsw written as 
'{{.NetworkSettings.IPAddress}}'
in the command

The issue in ip command is the use of {{}} , as the "format()"'s default syntax is {} it considers 
'{{.NetworkSettings.IPAddress}}'
the same and prints 
{.NetworkSettings.IPAddress}
rather than the IPAddess of the Docker Container
So we can use "String Cancatination" in it 

ipcmd1="sudo docker container inspect --format '{{.NetworkSettings.IPAddress}}' "
ipcmd2= "{0}".format(ipcheck)
ipcmd=ipcmd1+ipcmd2

And then using "subprocess" the command is executed .

-- Running a command on Temporary Container

Two values "Container image and the Command" are inputed in "ti and tc" and placed in 
tempcmd="sudo docker run --rm {0} {1}".format(tempimg,tempcom)

run creates the container and --rm removes it as soon as the command is executed 
and the subprocess executes it.

-- Docker Commands

The value inputed is Docker Coammnd it is inputed using a list of already given choices and the value is stored in "dc" fetched by "dcom"
then "elif statement" is used for the different cases .





























