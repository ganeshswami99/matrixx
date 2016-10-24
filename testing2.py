#!/usr/bin/python

import os
x=raw_input("\t\t\t\t\t\t\t-----==**Welcome to the Network sniffing Tool**==------")
print "Press 1.Using Ettercap "
print "Press 2.Using TCPdump " 
print "Press 3.Using Wireshark"
print "Press
y1=raw_input("Enter the startting port no ")
y2=raw_input("Enter the  port no. upto")
os.system("nmap -p  " +y1+"-"+y2+" "+x)
