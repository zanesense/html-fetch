import os,sys,json

try:
    import requests
    from huepy import *
except:
    print('''\033[91m
    Required modules are missing, try pip install -r requirements.txt
    ''')
    sys.exit()

os.system('clear')

print(green(r"""
 _     _ _______ _______        _______ _______ _______ _______ _     _
 |_____|    |    |  |  | |      |______ |______    |    |       |_____|
 |     |    |    |  |  | |_____ |       |______    |    |_____  |     |
                                                                       
"""))

url = input(info("Enter your url\n>> "))
if url.startswith('https://' or "http://"):
    print(bad('Don\'t include http or https in the url!!'))
    sys.exit()
url_ssl = input(info("Use [1] http or [2] https?\n>> "))
if url_ssl == "1":
    finalurl = "http://"+url 
elif url_ssl == "2":
    finalurl = "https://"+url
else:
    print(bad("Provide a valid option!!"))
    sys.exit()

f = open("proxies.json","r")
proxies = json.load(f)
use_proxy = input(info("Use proxy? (y/n)\n>> "))

def get_html():
    if use_proxy == "y":
        r=requests.get(finalurl, proxies=proxies)
    else:
        r=requests.get(finalurl)
    with open("index.html","w") as f:
        f.write(r.text)
        print(good("Results exported as index.html in current dir."))

try:
    get_html()
except:
    print(bad("Something happened, check your internet!!"))
    sys.exit()
