#!/usr/bin/python

import os

def speedy(ch):
	if(True):
		print("scanning...",os.system("nmap  -T4 " +ch))		
	elif(False):
		print("\nEntered wrong input\n Try again..\n")
while(True):
	os.system("reset")
	print"\n\t\t\t\t----Network Mapper----- (NMAP)\n"
	print"\tPrequisites NMAP for scanning\n"
	i=raw_input("\nPress 'y'--->'yes' otherwise 'n'--->'no'")
	if(i=='y'or i=='Y' ):
		temp=os.system("yum install nmap -y")
		print"NMAP installing....",temp
	else:
		print"\nEntered wrong input\n Try again..\n"		
	print"""\tPress 1.IP for single system scanning"	
		\tPress 2.IP(Internet Protocol) for whole scanning"
		\tPress 3.IP to check O.S Version Verbosily
		\tPress 4.IP for scan through Port no.
		\tPress 5.IP for scan mutiple Port no.
		\tPress 6.Scanning through Website 
  		\tPress 7.IP for all information
		\tPress 8.Exit to Main Menu """
	ch1=raw_input("\n\tEnter your choice:")
	if(ch1=='1'):
		a1=raw_input("\nEnter IP for scanning:")
		c1=raw_input("\nPress 's' for speed scanning:")
		if(c1=='s' or c1=='S'):
			speedy(a1)
		else:
			print"Scanning.....",os.system("nmap " +a1)
	if(ch1=='2'):
		a2=raw_input("\nEnter IP for whole scanning along with net mask:")
		c2=raw_input("\nPress 's' for speed scanning:")
		if(c2=='s' or c2=='S'):
			speedy(a2)
		else:
			print"Scanning.....",os.system("nmap " +a2)
	if(ch1=='3'):
		a31=raw_input("\nEnter IP :")
		print"Scanning.....",os.system("nmap  -p  -o  -A  -V "+a41)
	
	if(ch1=='4'):
		a41=raw_input("\nEnter IP for port scanning:")
		a42=raw_input("\nEnter the Port the number:")
		print"Scanning.....",os.system("nmap  -p  " +a41+""+a42)
	if(ch1=='5'):
		a51=raw_input("\nEnter IP:")
		a52=raw_input("\nEnter the starting port no.:")
		a53=raw_input("\nEnter the last upto which port no.:")
		print"Scanning.....",os.system("nmap  -p  " +a52+"-"+a53+""+a51)
	if(ch1=='6'):
		a6=raw_input("\nEnter address or an IP")
		c6=raw_input("\nPress 's' for speed scanning\n")
	if(ch1=='7'):
		a7=raw_input("Enter the IP")
		print"Scanning...",os.system("nmap -A " +a7)
		if(c6=='s' or c6=='S'):
			speedy(ch)
  		else:
			print"Scanning.....",os.system("nmap    " +a7)						
	if(ch1=='8'):
		os.system("python  /root/Desktop/1.py")
	
	else:
		print"Entered wrong choice"
		os.system("python  /root/Desktop/1-1.pyc")
	a=os.system("python /root/Desktop/1-1.py")
	return a
	
