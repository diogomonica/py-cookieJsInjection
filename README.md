# Cookie Javascript Injection Sidejacking

This software sniffs any interface for cookies, and generates javascript code that can be injected into any browser, by pasting it into the URL bar.

# Usage

To run the cookieJsInjection open a shell (e.g., bash) and execute the following command (cookieJsInjection requires scapy to run - http://www.secdev.org/projects/scapy/):

`./cookieJsInjection.py IFACE`

Where `IFACE` represents the network interface you wish to sniff on (e.g. eth0, wlan0, etc). 

If you supply the flag `-f`, it will only output facebook cookies, keeping track of the profiles captured in the session, and eliminating duplicate entries:

`./cookieJsInjection.py IFACE -f`
                                       

# Background
More information on sidejacking - http://en.wikipedia.org/wiki/Session_hijacking