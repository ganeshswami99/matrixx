#!/usr/bin/python

import os

os.system("reset")
t="telnet"
loc="python /root/Desktop/"
print"""\n\t\t\t\t\t\t\tTelnet Server(Nc)\n				
	Press 1.Install Telnet Server.
	Press 2.Start the Server.
	Press 3.Stop  the Server
	Press 4.Connect to server
	Press 5.Connect to Client
	Press 6.Exit to Main Menu"""
ch=raw_input("\nEnter your choice:")
if(ch=='1'):
	print"Installing........\n",os.system("yum install "+t+"-server  -y")
elif(ch=='2'):
	os.system("service "+t+"  start")
elif(ch=='3'):
	os.system("service "+t+" stop ")
elif(ch=='4'):
	os.system("service "+t+" restart")
elif(ch=='5'):
	os.sytsem("yum install "+t)
elif(ch=='6'):
	os.system(""+loc+"1.py")
else:
	print"Enterd wrong choice"
	os.system(""+loc+"2-1.py")
