import urllib.request
import json
import os
import bs4
import requests
from bs4 import BeautifulSoup as BS

RED, WHITE, CYAN, GREEN, DEFAULT, CYANCLARO, BOLD = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m', '\033[1;36m', '\033[1m'

os.system("clear")
print(f"""{GREEN}{BOLD}
██╗██████╗░░░░░░░██╗███╗░░██╗███████╗░█████╗░
██║██╔══██╗░░░░░░██║████╗░██║██╔════╝██╔══██╗
██║██████╔╝█████╗██║██╔██╗██║█████╗░░██║░░██║
██║██╔═══╝░╚════╝██║██║╚████║██╔══╝░░██║░░██║
██║██║░░░░░░░░░░░██║██║░╚███║██║░░░░░╚█████╔╝
╚═╝╚═╝░░░░░░░░░░░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░
""")
print("   ")
print(f"{RED}АВТОР: t.me/DarkUserWitch - ВЕДЬМА\nКАНАЛ: t.me/Scm_security")

getIP = input(f"{GREEN}[•_•] Введите айпи > ")
url = "https://ipinfo.io/" + getIP + "/json"

try:
    getInfo = urllib.request.urlopen( url )

except:
    print( "  " )
    print( "\n               {RED}      НЕВЕРНЫЙ АЙПИ! \n" )
    print( " " )
    print( " " )
    os.system("python ip-info.py")

infoList = json.load(getInfo)

def whoisIPinfo(ip):

    try:

        myComand = "whois " + getIP
        whoisInfo = os.popen( myComand ).read()
        return whoisInfo

    except:

        return "\n [×_ ×] — Ошибка — [× _×] \n"

     
print( "-" * 60 )
try:
	print( "Айпи: ", infoList["ip"] )
	print( "Город: ", infoList["city"] )
	print( "Регион: ", infoList["region"] )
	print( "Страна: ", infoList["country"] )
	print( "ИмяХоста: ", infoList["hostname"] )
	print( "-" * 60 )
	print( "-" * 60)
	print( whoisIPinfo ( getIP ) )
	print( f"{CYAN}ДЛЯ ПОВТОРНОГО ПРОБИВА ВВЕДИТЕ КОМАНДУ [°∆°] /ip ЧТОБЫ ВЫЙТИ CTRL + C")
	command = input(">")
	if command == "/ip":
		os.system("python3 ip-info.py")
except:
	print( f"{BOLD} многое не удалось найти... " )
	print(f"{CYAN}ДЛЯ ПОВТОРНОГО ПРОБИВА ВВЕДИТЕ КОМАНДУ [°∆°] /ip ЧТОБЫ ВЫЙТИ CTRL + C")
	command = input(">")
	if command == "/ip":
		os.system("python3 ip-info.py")