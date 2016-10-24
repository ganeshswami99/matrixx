#!/usr/bin/python

import os, time

os.system("reset")
loc="python "
d = "dialog"
def fun1():
	f1=open('/tmp/ch1.txt','r')
	ch1=f1.read()
	f1.close()
	return ch1
def exit():
	time.sleep(4)
	os.system(""+loc+" main.py")
def ssh():
	os.system(""+d+"  --menu  '------[SSH-Server]-----' 18  50  6  	1 'Install SSH Server'  										2 'Restart the Server' 											3 'Connect to client' 											4 'Stop  the Server'  											5 'Generate KEY again'  										6 'Exit to Main Menu'  2>/tmp/ch.txt")
	f=open('/tmp/ch.txt','r')
	ch=f.read()
	f.close()
	if(ch=='1'):
		os.system("yum install ssh  -y")
	elif(ch=='2'):
		os.system("service sshd restart")
	elif(ch=='3'):
		os.system(""+d+"  --inputbox 'Enter IP:' 10 30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system("ssh -X root@"+ch1)
	elif(ch=='4'):
		os.system("service sshd stop")
	elif(ch=='5'):
		os.system("cd /root/ssh/")
		os.system("rm -f *")
		os.system(""+loc+"main.py")
	elif(ch=='6'):
		os.system(""+loc+"main.py")
	else:
		os.system(""+d+"  --infobox  'Choose OPTION 6 to EXIT' 5 30")
		time.sleep(2)
		os.system(""+loc+"7-3.py")
ssh()

