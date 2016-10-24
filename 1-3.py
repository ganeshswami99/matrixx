#!/usr/bin/python

import os,time

os.system("reset")
h="hping3"
d='dialog'
loc="python "
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


def hping():
	os.system(""+d+"  --menu  '------[HPING3]-----' 18  50  4  	1 '1.IP for single system scanning and Port no.'  										2 'IP for scan mutiple Port no.' 										3 'Website Address or IP'  										4 'Exit to Main-Menu'  2>/tmp/ch1.txt")
	f=open('/tmp/ch1.txt','r')
	ch=f.read()
	f.close()
	if ch=='1' :
		os.system(""+d+"  --inputbox 'Enter the IP address of the server' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+d+"  --inputbox 'Enter the Port no.' 10  30  2>/tmp/ch2.txt")
		ch2=fun2()
		os.system(""+h+" -S  --scan" +ch1+""+ch2)
	elif ch=='2' :
		os.system(""+d+"  --inputbox 'Enter the IP address of  system  or Website address' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+d+"  --inputbox 'Enter Starting Port no.' 10  30  2>/tmp/ch2.txt")
		ch2=fun2()
		os.system(""+d+"  --inputbox 'Enter Last port no' 10  30  2>/tmp/ch3.txt")
		f2=open('/tmp/ch1.txt','r')
		ch3=f2.read()
		f2.close()
		os.system(""+h+" -S --scan " +ch2+ "-" +ch3+ " "+ch1)
	elif ch=='3' :
		os.system(""+d+"  --inputbox 'Enter address of website or IP' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+d+"  --inputbox 'Enter Port no.' 10  30  2>/tmp/ch2.txt")
		ch2=fun2()
		os.system(""+h+" -S  --scan " +ch1+" -z "+ch2)
	elif ch=='4' :
		os.system(""+loc+"main.py")
		
	else:
		os.system(""+d+"  --infobox  'Choose option 4 to EXIT' 5 30")
		time.sleep(2)
		os.system(""+loc+"1-3.py")

hping()


