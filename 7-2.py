#!/usr/bin/python

import os, time

os.system("reset")
loc="python "
s="samba"
d = "dialog"
def fun1():
	f1=open('/tmp/ch1.txt','r')
	ch1=f1.read()
	f1.close()
	return ch1
def exit():
	time.sleep(4)
	os.system(""+loc+" main.py")
def samba():
	os.system(""+d+"  --menu  '------[SMB-Server Message Block]-----' 18  50  6  	1 'Install samba Server'  											2 'Enter the file Location to share' 											3 'Restart  the Server'  											4 'ADD Samba user'  							 				5 'At client Site' 											6 'EXIT to MAIN-MENU' 2>/tmp/ch.txt")

	f=open('/tmp/ch.txt','r')
	ch=f.read()
	f.close()	
	if(ch=='1'):
		os.system("yum install "+s+"  -y")
	elif(ch=='2'):
		os.system(""+d+"  --inputbox 'Enter File location :' 10 30  2>/tmp/ch1.txt")
		ch8=fun1()
		os.system("cat >>"+ch8+ "a.txt")
		os.system("cat  <a.txt >>/etc/samba/smb.conf")
	elif(ch=='3'):
		os.system("service "+s+"restart")
	elif(ch=='4'):
		os.system(""+d+"  --inputbox 'Enter User name :' 10 30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system("useradd  -s  /sbin/nologin "+ch9)
		os.system("sampasswd  -a "+ch9)
		os.system("service "+s+" restart")
		os.system("setenforce 0")
		os.system("iptables -F")
		os.system("chmod o+w "+ch8)
	elif(ch=='5'):
		os.system(""+d+"  --inputbox 'Enter IP :' 10 30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system("ssh -x root@"+ch1+" -y ")
		os.system("mkdir  /media/new/")
		os.system("mount  //"+ch1+"/"+ch8+"  /media/new/")
		os.system("mount  -o  username="+ch9+"//"+ch1+"  /media/new/")
		os.system("chmod  o+w  "+ch8)
	elif(ch=='6'):
		os.system(""+loc+"main.py")
	else:
		os.system(""+d+"  --infobox  'Choose OPTION 8 to EXIT' 5 30")
		time.sleep(2)
		os.system(""+loc+"7-2.py")
samba()

