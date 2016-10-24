#!/usr/bin/python

import os

os.system("reset")
loc="python /root/Desktop/"
print"""\n\t\t\t\t\t\t\t Server(Nc)\n				
	Press 1.Install SSH Server.
	Press 2.Connect to the Server.
	Press 3.Restart the Server
	Press 4.Stop the server
	Press 5.Exit to Main Menu"""
ch=raw_input("\nEnter your choice:")
if(ch=='1'):
	print"Installing........",os.system("yum install ssh  -y")
elif(ch=='2'):
	print"IP of an system to connect:",x
	os.system("ssh -X root@"+x)
elif(ch=='3'):
	os.system("service sshd restart ")
elif(ch=='4'):
	os.system("service sshd stop")
elif(ch=='5'):
	os.system(""+loc+"main.py")
else:
	print"Enterd wrong choice"
	os.system(""+loc+"2-1.py")
