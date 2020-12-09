from sys import *
from os import *

show = """
    dorks:
        [0] - manual
        [f] - file
        [1] - sql injection
        [2] - wordpress
        [3] - xss
        [4] - camera
        [5] - password
    Countries:
        [en] - English
        [tr] - Turkish
        [zh] - Chinese
        [ru] - Russian
    exit [q]
"""
the_dork = [
    "view_items.php?id=",
    '("Comment on Hello world!")',
    'intitle:”Android Webcam Server” inurl:”8080″',
    'intitle:”Android Webcam Server” inurl:”8080″',
    'inurl:admin/password.txt',
]
sql = [
    "productlist.php?tid=",
    "showsub.php?id=",
    "view_items.php?id=",
    "_news/news.php?id=",
]
xss = [
    'inurl:".php?years="',
    'inurl:".php?txt="',
    'inurl:com_feedpostold/feedpost.php?url=',
    '(inurl:headersearch.php?sid=',
]
wp = [
    '("uncategorized/hello-world")',
    '("author/admin")',
    '("Proudly powered by WordPress")',
    '("Welcome to WordPress. This is your first post.")',
]
passs = [
    '"whoops! there was an error." "db_password"',
    '("phpMyAdmin MySQL-Dump" filetype:txt")',
    '("your password is" filetype:log")',
    '(allintitle: restricted filetype: mail")',
]
cam = [
    '“Powered by WebcamXP” “Pro|Broadcast”',
    'intitle:”My WebcamXP Server!” inurl:”8080″',
    'inurl:”webcam7″ intitle:”8080″',
    'intitle:”Live View / – AXIS” | inurl:view/views.html',
]

#sa = 0
#so max 100
#t = 'com'
sssss = "how many doing search"
def run_dork(k,t,sa,so,l):
    url = ""
    for a in search(k, tld=t, start=sa, lang=l, stop=so, pause=15.0):
        print(a)
        url = url + a
        url = url + "\n"
    #kodlar hatalı veya benim derleyicim düzgün çalışmıyor
    """
    fs = input("do you want save dorks [y/n]:")
    if fs == "y":
        print("please not forget to file extensions")
        with open("links.txt", 'w+') as file:
            file.write(url)
            file.close()
        print("save as links.txt")
    else:
        return
    """
def dorks(d):
    l = input("please enter country:")
    if d == "1":
        sayi= int(input("how many doing search [Max:100]:"))
        for run in range(0, len(sql)):
            print("step"+str(run+1))
            cont = input("do you want continue [y/n]:")
            if cont == "y":
                run_dork(sql[run], 'com', 0, sayi, l)
            else:
                return
    if d == "2":
        sayi= int(input("how many doing search [Max:100]:"))
        for run in range(0, len(wp)):
            print("step"+str(run+1))
            cont = input("do you want continue [y/n]:")
            if cont == "y":
                run_dork(wp[run], 'com', 0, sayi, l)
            else:
                return
    if d == "3":
        sayi= int(input("how many doing search [Max:100]:"))
        for run in range(0, len(xss)):
            print("step"+str(run+1))
            cont = input("do you want continue [y/n]:")
            if cont == "y":
                run_dork(xss[run], 'com', 0, sayi, l)
            else:
                return
    if d == "4":
        sayi= int(input("how many doing search [Max:100]:"))
        for run in range(0, len(cam)):
            print("step"+str(run+1))
            cont = input("do you want continue [y/n]:")
            if cont == "y":
                run_dork(cam[run], 'com', 0, sayi, l)
            else:
                return
    if d == "5":
        sayi= int(input("how many doing search [Max:100]:"))
        for run in range(0, len(passs)):
            print("step"+str(run+1))
            cont = input("do you want continue [y/n]:")
            if cont == "y":
                run_dork(passs[run], 'com', 0, sayi, l)
            else:
                return
    if d == "0":
        dorkk = input("dork:")
        sayi= int(input("how many doing search [Max:100]:"))
        run_dork(dorkk, 'com', 0, sayi, l)
    if d == "f":
        #kodlar hatalı veya benim derleyicim düzgün çalışmıyor
        """
        dfi = input("file name:")
        fi = open(dfi, "r")
        dr = fi.readlines()
        for j in range(0, len(dr)):
            run_dork(dr[j], 'com', 0, sayi, l)
        """
        print("sorry but this is wrong")
def setup():
    try :
        import pip
    except ImportError:
        print("pip module not found")
        print("please install pip module")
    system("python3 -m pip install --upgrade pip")
    #system("python3 -m pip install beautifulsoup4")
    system("python3 -m pip install google")
def sea(x):
    if x == "setup":
        setup()
    if x == "show modules":
        print(show)
    if x == "0":
        dorks("0")
    if x == "1":
        dorks("1")
    if x == "2":
        dorks("2")
    if x == "3":
        dorks("3")
    if x == "4":
        dorks("4")
    if x == "5":
        dorks("5")
    if x == "f":
        dorks("f")
    if x == "q":
        exit()
def console():
    print(show)
    while True:
        x = input("/dose/__&")
        sea(x)
            
if __name__ == '__main__':
    try :
        from googlesearch import search
    except:
        kur = input("do you want setuptools [y/n]:")
        if kur == "y":
            setup()
        else:
            print("setuptools not found")
            exit()
    console()
