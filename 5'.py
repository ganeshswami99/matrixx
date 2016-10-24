#!/usr/bin/python

import os

os.system("reset")
s="samba"
print"""\n\t\t\t\t\t\t\t Server(Nc)\n				
	Press 1.Install samba Server.
	Press 2.Start the Server.
	Press 3.Stop  the Server
	Press 4.Connect to server
	Press 5.Connect to Client
	Press 6.Exit to Main Menu"""
ch=raw_input("\nEnter your choice:")
if(ch=='1'):
	print"Installing........",os.system("yum install "+s+"  -y")
elif(ch=='2'):
	os.system("service "+s+" start")
elif(ch=='3'):
	os.system("service "s+" stop ")
elif(ch=='4'):
	os.system("service "+s+" restart")
elif(ch=='5'):
	os.sytsem("yum install "+s)
elif(ch=='6'):
	os.system("python  /root/Desktop/main.py")
else:
	print"Enterd wrong choice"
	os.system("pyhton /root/Desktop/2-1.py")
