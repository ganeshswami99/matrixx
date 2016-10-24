#!/usr/bin/python

import os, time
os.system("reset")
t="telnet"
loc="python "
d = "dialog"
def exit():
	time.sleep(4)
	os.system(""+loc+" main.py")
def fun1():
	f1=open('/tmp/ch1.txt','r')
	ch1=f1.read()
	f1.close()
	return ch1
def telnet():
	os.system(""+d+"  --menu  '------[Telnet-Server]-----' 18  50  5  	1 'Install Telnet Server'  											2 'Restart the Server' 											3 'Connect to Server'  											4 'Stop server'  							 				5 'Exit to Main Menu'  2>/tmp/ch.txt")
	f=open('/tmp/ch.txt','r')
	ch=f.read()
	f.close()
	if(ch=='1'):
		os.system("yum install "+t+"-server  -y")
	elif(ch=='2'):
		os.system("service xinetd.d restart")		
	elif(ch=='3'):
		os.system(""+d+"  --inputbox 'Enter the IP' 10  60   2>/tmp/ch1.txt")
		f=open('/tmp/ch1.txt','r')
		ch=f.read()
		f.close()
		os.system(""+t+" " +ch)
	elif(ch=='4'):
		os.system("service "+t+" stop ")
	elif(ch=='5'):
		os.system(""+loc+" main.py")
	else:
		os.system(""+d+"  --infobox  'Choose OPTION 5 to EXIT' 5 30")
		time.sleep(2)
		os.system(""+loc+" 7-1.py")
telnet()
