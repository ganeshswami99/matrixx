#!/usr/bin/python

import os,time


def speedy(ch):
	if(True):
		os.system(""+a+"  -T4  "+ch)		
	elif(False):
		os,system(""+d+" --textbox 'Entered wrong input\n Try again..\n' 10 30")
def fun1():
	f1=open('/tmp/ch1.txt','r')
	ch1=f1.read()
	f1.close()
	return ch1
def fun2():
	f2=open('/tmp/ch2.txt','r')
	ch2=f2.read()
	f2.close()
	return ch2

os.system("reset")
a="nmap"
d='dialog'
loc="python "
def nmap():
	os.system(""+d+"  --inputbox 'Prequisites NMAP for scanning---- \n Press y--->YES otherwise n--->NO' 10  60   2>/tmp/ch.txt")
	f=open('/tmp/ch.txt','r')
	ch=f.read()
	f.close()
	if ch=='y'or ch=='Y' :
		os.system("yum install nmap -y")
	else:
		os.system(""+d+"  --menu  '------[Network Mapper-(NMAP)]-----' 18  50  8  	1 'IP for single system scanning'  											2 'IP(Internet Protocol) for whole scanning' 											3 'IP to check O.S Version Verbosily'  											4 'IP for scan through Port no.'  											5 'IP for scan mutiple Port no.'  											6 'Scanning through Website '  											7 'IP for all information'  											8 'Exit to Main Menu'  2>/tmp/ch.txt")
	f=open('/tmp/ch.txt','r')
	ch=f.read()
	f.close()
	if ch=='1' :
		os.system(""+d+"  --inputbox 'Enter IP for scanning:' 10 30  2>/tmp/ch1.txt")
		ch1=fun1()	
		os.system(""+d+"  --inputbox 'Press 's' for speed scanning' 10 30 2>/tmp/ch2.txt")
		ch2=fun2()		
		if ch2=='s' or ch2=='S' :
			speedy(ch1)
		else:
			os.system(""+a+" "+ch1)
	elif ch=='2' :
		os.system(""+d+"  --inputbox 'Enter IP for whole scanning along with net mask:' 10 30 2>/tmp/ch1.txt")
		ch1=fun1()	
		os.system(""+d+"  --inputbox 'Press 's' for speed scanning' 10 30 2>/tmp/ch2.txt")
		ch2=fun2()	
		if(ch2=='s' or ch2=='S'):
			speedy(ch1)
		else:
			os.system(""+a+" "+ch1)
	elif ch=='3' :
		os.system(""+d+"  --inputbox 'Enter IP :' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+a+"  -O  "+ch1)

	elif ch=='4' :
		os.system(""+d+"  --inputbox 'Enter IP :' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()	
		os.system(""+d+"  --inputbox 'Enter the Port the number:' 10  30 2>/tmp/ch2.txt")
		ch2=fun2()	
		os.system(""+a+" " +ch1+" -p "+ch2)
	elif ch=='5' :
		os.system(""+d+"  --inputbox 'Enter IP :' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()	
		os.system(""+d+"  --inputbox 'Enter start port no. :' 10 30  2>/tmp/ch2.txt")
		ch2=fun2()
		os.system(""+d+"  --inputbox 'Enter last port no. :' 10  30 2>/tmp/ch3.txt")
		f3=open('/tmp/ch3.txt','r')
		ch3=f3.read()
		f3.close()
		os.system(""+a+" " +ch1+" -p "+ch2+"-"+ch3)
	elif ch=='6' :
		os.system(""+d+"  --inputbox 'Enter address or an IP :' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+d+"  --inputbox 'Press 's' for speed scanning:' 10  30  2>/tmp/ch2.txt")
		ch2=fun2()
		if(ch2=='s' or ch2=='S'):
			speedy(ch1)
		else:
			os.system(""+a+" "+ch1)
	elif ch=='7' :
		os.system(""+d+"  --inputbox 'Enter IP :' 10  30   2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+a+" -A " +ch1)
	elif ch=='8' :
		os.system("python main.py")	
	else:
		os.system(""+d+"  --infobox  'Choose OPTION 8 to EXIT' 5 30")
		time.sleep(2)
		os.system(""+loc+"1-1.py")
	
nmap()

