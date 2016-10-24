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
	os.system(""+d+"  --menu  '------[MAIL-Server]-----' 18  50  6  	1 'Install Software'  											2 'Restart the Server' 											3 'Send mail to client' 										4 'Open mail to check '  											5 'Reply to mail'  											6 'Exit to Main Menu'  2>/tmp/ch.txt")
	f=open('/tmp/ch.txt','r')
	ch=f.read()
	f.close()
	if(ch=='1'):
		os.system("yum install postfix -y")
	elif(ch=='2'):
		h=os.system("hostname")
		os.system("service postfix restart")
	elif(ch=='3'):
		os.system(""+d+"  --inputbox 'Enter hostname:' 10 30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+d+"  --msgbox 'Press 'CTRL+D' to send MAIL:' 10 30  2>/tmp/ch1.txt")
		os.system("mail "+ch1)
	elif(ch=='4'):
		os.system("mail ")
		time.sleep(4)
		os.system("q")
	elif(ch=='5'):
		os.system(""+d+"  --inputbox 'Enter hostname:' 10 30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system("mail  "+ch1)
		os.system("reply")
	elif(ch=='6'):
		os.system(""+loc+"main.py")
	else:
		os.system(""+d+"  --infobox  'Choose OPTION 6 to EXIT' 5 30")
		time.sleep(2)
		os.system(""+loc+"7-4.py")
ssh()

