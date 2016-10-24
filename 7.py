#!/usr/bin/python

import os,time

loc="python "
os.system("reset")
d='dialog'
def exit():
	time.sleep(4)
	os.system(""+loc+" main.py")
def scan():
	os.system(""+d+"  --menu  '---------==*****| Welcome to  Server Setup|*****====------ ' 20  70  6  										1 'Telnet Server'   										2 'SAMBA-Server'  										3 'SSH-Server'  									4 'MAIL Server'  										5 'NFS Server' 										6 'EXIT to MAIN-MENU' 2>/tmp/ch1.txt"  )  	 	  

	f=open('/tmp/ch1.txt','r')
	ch=f.read()
	f.close()
	if ch == '1' :
		os.system(" "+loc+"7-1.py")
		exit()
	elif ch=='2' :
		os.system(" "+loc+"7-2.py")
		exit()
	elif ch=='3' :
		os.system(" "+loc+"7-3.py")
		exit()
	elif ch=='4' :
		os.system(" "+loc+"7-4.py")
		exit()
	elif ch=='5' :
		os.system(" "+loc+"7-5.py")
		exit()
	elif ch=='6' :
		os.system(""+loc+"main.py")
	else:
		os.system(""+d+"  --infobox  'Choose option 6 for EXIT' 5 30")
		time.sleep(2)
		os.system(""+loc+"7.py")
	
scan()

