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
	os.system(""+d+"  --menu  '------[NFS-Server]-----' 18  50  6  	1 'Install Software' 											2 'Enter file Location to Share'  											3 'Enter IP of Client' 											4 'Restart service' 											5 'At Client Site '  						  											6 'Exit to Main Menu'  2>/tmp/ch.txt")
	f=open('/tmp/ch.txt','r')
	ch=f.read()
	f.close()
	if(ch=='1'):
		os.system("yum install  nfs-utils -y")
	elif(ch=='2'):
		os.system(""+d+"  --inputbox 'Enter File Location:' 10 30  2>/tmp/ch1.txt")
		location=fun1()
	elif(ch=='3'):
		os.system(""+d+"  --inputbox 'Enter client IP' 10 30  2>/tmp/ch1.txt")
		cl=fun1()
		os.system("cat "+cl+" b.txt >>/etc/exports")
	elif(ch=='4'):
		os.system("service  nfs restart")
	elif(ch=='5'):
		os.system("yum install nfs-utils  -y ")
		os.system(""+d+"  --inputbox 'Enter server IP' 10 30  2>/tmp/ch1.txt")
		ser=fun1()
		fileloc=os.system("showmount  -e  "+ser)
		os.system("mkdir  /media/mydata/")
		os.system("mount "+cl+":"+location+"/media/mydata")
		time.sleep(4)
	elif(ch=='6'):
		os.system(""+loc+"main.py")
	else:
		os.system(""+d+"  --infobox  'Choose OPTION 6 to EXIT' 5 30")
		time.sleep(2)
		os.system(""+loc+"7-5.py")
ssh()

