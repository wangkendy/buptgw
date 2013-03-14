#!/usr/bin/env python
#Author: wangkendy (wkendy@gmail.com)
#2012/9/7

import sys
import urllib
import getopt
import hashlib
import re

def usage():
	print sys.argv[0], "-a [login|logout|check] -u <username> -p <password>"
	sys.exit(2)

def login(username, password):
	pid = "1"
	calg = "12345678"
	password = pid + password + calg
	password = hashlib.md5(password).hexdigest()+calg+pid
	params = urllib.urlencode({'DDDDD':username, 
							'upass':password, 'R1':0, 
							'R2':1, 'para':'00', 'n':100, '0MKKey':'123456'})
	posturl = 'http://gw.bupt.edu.cn'
	f = urllib.urlopen(posturl, params)
	response = f.read()
#print response
	match = re.search('You have successfully logged into our system.', response);
	if (match):
		print match.group(0)
	else:
		print "Login failed.\n"

def check():
	geturl = 'http://gw.bupt.edu.cn/'
	f = urllib.urlopen(geturl)
	response = f.read()
#time='4435      ';flow='635853    ';fsele=1;fee='0         '
	match = re.search(r'time=\'(\d+)\s*\';flow=\'(\d+)\s*\';fsele=(\d+);fee=\'(\d+)\s+\'', response)	
	if match:
		time = int(match.group(1))
		flow = int(match.group(2))
		fsele = int(match.group(3))
		fee = int(match.group(4))
		print 'Used time : %d Min' % time
		print 'Used internet traffic : %f MByte' % (flow*1.0/1024)
		if fsele==1:
			print 'Balance : RMB ', (fee*1.0/10000)
	else:
		print "You are not logged in.\n"

#get http://gw.bupt.edu.cn/F.htm logout
def logout():
	geturl = 'http://gw.bupt.edu.cn/F.htm'
	f = urllib.urlopen(geturl)
	response = f.read()
#print response
#match = re.search('Logout successfully', response)
#	if match:
#		print match.group(0)
	match = re.search(r'Msg=(\d+);time=\'(\d+)\s*\';flow=\'(\d+)\s*\';fsele=(\d+);fee=\'(\d+)\s+\'', response)	
	if match:
		Msg = int(match.group(1))
		time = int(match.group(2))
		flow = int(match.group(3))
		fsele = int(match.group(4))
		fee = int(match.group(5))
		if Msg == 14:
			print 'Logout successfully.'
		else:
			print "Error Code:%d" % Msg
		print 'Used time : %d Min' % time
		print 'Used internet traffic : %f MByte' % (flow*1.0/1024)
		if fsele==1:
			print 'Balance : RMB ', (fee*1.0/10000)
	else:
		print "You are not logged in.\n"

def main():
	try:
		(opts, args) = getopt.getopt(sys.argv[1:], "a:u:p:h")
	except getopt.GetoptError, err:
		print str(err)
		usage()
		sys.exit(2)

	action = None
	username = None
	passwd = None
	for (o, a) in opts:
		if o == "-a":
			action = a
		elif o == "-u":
			username = a;
		elif o == "-p":
			passwd = a
		elif o == "-h":
			usage()
	
	if (action and username and passwd):
		if action == "login":
			login(username, passwd)
		elif action == "logout":
			logout()
		else:
			usage()
	elif action == "logout":
		logout()
	elif action == "check":
		check()
	else:
		usage()
if __name__ == "__main__":
	main()
