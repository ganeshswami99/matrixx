#!/usr/bin/python

import os,time

loc="python "
os.system("reset")
d='dialog'
def exit():
	time.sleep(4)
	os.system(""+loc+" main.py")
def scan():
	os.system(""+d+"  --menu  '---------==*****| Welcome to Networking Scanning Tool|*****====------ ' 15  80  6  										1 'Network Mapper (NMAP)'   										2 'Net Cat (NC)'  										3 'HPING3'  										4 'To use Wireshark' 										5 'Meta-Exploit(Msfconsole)'  										6 'Exit to Main Menu'  2>/tmp/ch1.txt"  )  	 	  

	f=open('/tmp/ch1.txt','r')
	ch=f.read()
	f.close()
	if ch == '1' :
		os.system(" "+loc+"1-1.py")
		exit()
	elif ch=='2' :
		os.system(" "+loc+"1-2.py")
		exit()
	elif ch=='3' :
		os.system(" "+loc+"1-3.py")
		exit()
	elif ch=='4' : 
		os.system(""+d+"  --inputbox 'Prequisites Wireshark for scanning---- \n Press y--->YES otherwise n--->NO' 10  60   2>/tmp/ch.txt")
		f=open('/tmp/ch.txt','r')
		ch=f.read()
		f.close()
		if(ch=='y'or ch=='Y' ):
			os.system("yum install wireshark -y")
			os.system(""+loc+"main.py")
		else:
			os.system("wireshark -G")  							
			os.system(""+loc+"main.py")
		exit()
	elif ch=='5' :
		os.system(""+d+"  --inputbox '------[ METAEXPLOIT for scanning ]------' 10 46 2>/tmp/ch.txt")
		os.system("msfconsole")
		exit()
	elif ch=='6' :
		os.system(""+loc+"main.py")
	else:
		os.system(""+d+"  --infobox  'Choose option 6 for EXIT' 5 30")
		time.sleep(2)
		os.system(""+loc+"1.py")
	
scan()

