#!/usr/bin/python

import  os,time


loc="python  "
os.system("reset")
d='dialog'
def exit():
	time.sleep(4)
	os.system(""+loc+" main.py")
def sniff():
	os.system(""+d+"  --menu  '---------==*****| Welcome to Networking Scanning Tool|*****====------ ' 15  80   5 								 		1 'Using  Ettercap' 										2 'Using TCPDUMP' 										3 'Using Wireshark' 										4 'Using Xplico' 										5 'Exit To Menu'  2>/tmp/ch.txt") 
	f=open('/tmp/ch.txt','r')
	ch=f.read()
	f.close()
	if   ch=='1' :
		os.system(""+d+"  --infobox  'Requires Ettercap to install' 5 30")
		time.sleep(2)
		os.system("yum install ettercap -y")
		os.system("ettercap -G")
		exit()
	elif ch=='2' :
		os.system(""+loc+"3-2.py")
	elif ch=='3' :
		os.system(""+d+"  --infobox  'Requires Wireshark to install' 5 30")
		time.sleep(2)
		os.system("yum install  wireshark  -y")
		os.system("wireshark  -G")
		exit()
	elif ch=='4' :
		os.system(""+d+"  --infobox  'Requires xplico to install' 5 30")
		time.sleep(2)
		os.system("yum install xplico -y")
		os.system("xplico  -G")
		exit()
	elif ch=='5' :
		os.system(""+loc+"main.py")
	else :
		os.system(""+d+"  --infobox  'Choose option 5 to EXIT' 5 30")
		time.sleep(2)
		os.system(""+loc+"3.py")
sniff()

