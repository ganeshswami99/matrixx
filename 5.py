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
def iptables():
	os.system(""+d+"  --menu  '-----****[Firewall OPTIONS ]****-----' 20  54  9 	1 'Iptables FLUSH' 											2 'To Check tables' 											3 'To Scan' 											4 'To Reject PING from Specific IP' 											5 'Receive LIMIT-Packets' 											6 'DONT REPLY' 											7 'Closed specific PORT' 											8 'TO ACCEPT ping' 											9 'EXIT to MAIN-MENU' 2>/tmp/ch7.txt")
	f=open('/tmp/ch7.txt','r')
	ch=f.read()
	f.close()
	if   ch =='1':
		os.system("iptables -F")
		exit()
	elif ch=='2' :
		os.system(""+d+"  --inputbox 'Enter table name:' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system("iptables -t "+ch1+" -L")
		exit()		
	elif ch =='3' :
		os.system(""+d+"  --inputbox 'Enter IP address of Client:' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+d+"  --inputbox 'Enter Protocol:' 10  30  2>/tmp/ch2.txt")
		ch2=fun2()
		os.system("iptables -I INPUT -p "+ch2+" -s "+ch1)
		exit()
	elif ch =='4' :
		os.system(""+d+"  --inputbox 'Enter IP address of Client:' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+d+"  --inputbox 'Enter Protocol:' 10  30  2>/tmp/ch2.txt")
		ch2=fun2()
		os.system("iptables -I INPUT -p "+ch2+"  -d "+ch1+" -j REJECT")
		exit()
	elif ch =='5':
		os.system(""+d+"  --inputbox 'Enter Protocol:' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+d+"  --inputbox 'Enter Limit:' 10  30  2>/tmp/ch2.txt")
		ch2=fun2()
		os.system("iptables -I INPUT -p "+ch1+" -m  connlimit --connlimit-above "+ch2+" -j REJECT")
		exit()
	elif ch=='6' :
		os.system(""+d+"  --inputbox 'Enter Protocol:' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system("iptables -I INPUT -p "+ch1+"  -j DROP")
		exit()
	elif ch=='7' :
		os.system(""+d+"  --inputbox 'Enter Protocol:' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+d+"  --inputbox 'Enter Port No.:' 10  30  2>/tmp/ch2.txt")
		ch2=fun2()
		os.system("iptables -A INPUT -p "+ch1+" --dport "+ch2+" -j DROP")
		exit()
	elif ch =='8' :
		os.system(""+d+"  --inputbox 'Enter IP address of Client:' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+d+"  --inputbox 'Enter Protocol:' 10  30  2>/tmp/ch2.txt")
		ch2=fun2()
		os.system("iptables -I INPUT -p "+ch2+"  -d "+ch1+" -j ACCEPT")
		os.system("service network restart")
		exit()
	elif ch=='9':
		os.system(""+loc+"main.py")
	else:
		os.system(""+d+"  --infobox  'Choose option 9 for EXIT' 5 30")
		time.sleep(2)
		os.system(""+loc+"5.py")
	
iptables()

