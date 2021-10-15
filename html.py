import requests, sys, os
from huepy import *

os.system('cls')

print(green(r"""
 _     _ _______ _______        _______ _______ _______ _______ _     _
 |_____|    |    |  |  | |      |______ |______    |    |       |_____|
 |     |    |    |  |  | |_____ |       |______    |    |_____  |     |
                                                                       
"""))

url = input(info('Enter your URL\n> '))

if url.startswith('https://' or "http://"):
    print(good('Valid URL!'))
else:
    print(bad('Invalid URL provided, exiting...'))
    sys.exit()

def html_fetch():
    r = requests.get(url)
    with open('index.html','w') as f:
        f.write(r.text)
        print(good('Successfully wrote the result to index.html'))

html_fetch()