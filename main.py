#!/usr/bin/python

import os,time

loc="python "
os.system("reset")
d="dialog"
def main():
	os.system(""+d+"  --menu  'Enter Your Choice :-' 20  40  8  		1 'Cryptography Analysis' 										2 'Use Network Scanning Tool' 										3 'Use Network Sniffing Tool' 										4 'ARP Poisning' 										5 'Firewall'   										6 'DOS-Attack' 										7 'Server' 										8 'EXIT'  2>/tmp/ch.txt") 
	f=open('/tmp/ch.txt','r')
	ch=f.read()
	f.close()
	if ch=='1' :
		os.system(" "+loc+"2.py") 
	elif ch=='2':
		os.system(" "+loc+"1.py")
	elif ch=='3' :
		os.system(" "+loc+"3.py")
	elif ch=='4' :
		os.system(" "+loc+"4.py")
	elif ch=='5' :
		os.system(" "+loc+"5.py")
	elif ch=='6' :
		os.system(" "+loc+"6.py")
	elif ch=='7' :
		os.system(" "+loc+"7.py")	
	elif ch=='8' :
		os.system(""+d+"  --infobox 'Thank you...'  5  20")
		os.system("exit")
	else:		
		os.system(""+d+"  --infobox  'Choose option 7 to EXIT' 5 30")
		time.sleep(2)
		main()
main()
