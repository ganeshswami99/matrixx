#!/usr/bin/python
import os,time

os.system("reset")
t="tcpdump"
loc="python  "
d='dialog'
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
def tcpdump():
	os.system(""+d+"  --menu  '------[TCPDUMP]-----' 18  50  7  	1 'Check the Traffic On Network'  											2 'Save the Traffic to file verbosely' 											3 'Read the file'  											4 'To check packet from specific IP '  											5 'To check the packet for two IP & Port'  											6 'For Broadcast '  						 											7 'Exit to Main Menu'  2>/tmp/ch2.txt")
	f=open('/tmp/ch2.txt','r')
	ch=f.read()
	f.close()
	if  ch=='1' :
		os.system(""+t)
	elif  ch =='2' :
		os.system(""+d+"  --inputbox 'Enter your LAN card name:' 10 30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+d+"  --infobox  'Press Ctrl+c to stop receiving' 10 30 ")
		time.sleep(2)	
		os.system(""+d+"  --inputbox 'Enter file name:' 10 30 2>/tmp/ch2.txt")
		ch2=fun2()		
		os.system(""+t+" -i " +ch1+" -v  -w  " +ch2)
		exit()
	elif ch =='3' :
		os.system(""+d+"  --inputbox 'Enter the file name:' 10 30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+t+" -r "+ch1)
		exit()
	elif ch =='4' :
		os.system(""+d+"  --inputbox 'Enter IP of Server:' 10 30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+d+" ---inputbox 'Enter LAN CARD name:' 10 30 2>/tmp/ch2.txt")
		ch2=fun2()		
		os.system(""+t+" -i "+ch2+" icmp  -n and host "+ch1)
		exit()
	elif ch =='5' :
		os.system(""+d+"  --inputbox 'Enter First IP:' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()	
		os.system(""+d+"  --inputbox 'Enter the Port:' 10  2>/tmp/ch2.txt")
		ch2=fun2()
		os.system(""+d+"  --inputbox 'Enter Second IP:'10  2>/tmp/ch3.txt")
		f3=open('/tmp/ch3.txt','r')
		ch3=f3.read()
		f3.close()
		os.system(""+d+"  --inputbox 'Enter the Port'10  2>/tmp/ch4.txt")
		f4=open('/tmp/ch4.txt','r')
		ch4=f4.read()
		f4.close()
		os.system(""+t+" -i "+ch1+" host "+ch2+"or  host "+ch3+"and "+ch2+"or "+ch4)
		exit()	
	elif ch =='6' :
		os.system(""+d+"  --inputbox 'Enter the file name' 10  30  2>/tmp/ch1.txt")
		ch1=fun1()
		os.system(""+t+"  -i  "+ch1+" broadcast  -n")
		exit()
	elif ch  =='7' :
		os.system(""+loc+"main.py")
	else:
		os.system(""+d+"  --infobox  'Choose option 7 to EXIT' 5 30")
		time.sleep(2)
		os.system(""+loc+"3-2.py")

tcpdump()


