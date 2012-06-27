#Author: wangkendy
#2012/6/6

import sys
import urllib
import getopt
import hashlib

def usage():
	print sys.argv[0], "-a [login|logout] -u <username> -p <password>"
	sys.exit(2)

def login(username, password):
	password = hashlib.md5(password).hexdigest()[8:24]
	params = urllib.urlencode({'username':username, 
							'password':password, 'drop':0, 
							'type':1, 'n':100})
	posturl = 'http://gw.bupt.edu.cn/cgi-bin/do_login'
	f = urllib.urlopen(posturl, params)
	print f.read()

def logout(username, password):
	params = "username="+username+"&password="+password+"&drop=0&type=1&n=1"
	posturl = 'http://gw.bupt.edu.cn/cgi-bin/force_logout'
	f = urllib.urlopen(posturl, params)
	print f.read()

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
			logout(username, passwd)
		else:
			usage()
	else:
		usage()
if __name__ == "__main__":
	main()
