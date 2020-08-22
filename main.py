import os
import random
import requests
from colorama import Fore

token = 'NzQ2NTkwNDg2MTQzMzAzNzIw.X0Cipw.2NnHhKm1otYrzmi9hUVnIbgS2TM'

intro = f''' 
Options:
  {Fore.GREEN}1{Fore.RESET}) Russian
  {Fore.GREEN}2{Fore.RESET}) English
  {Fore.GREEN}3{Fore.RESET}) Japan
  {Fore.GREEN}4{Fore.RESET}) Dutch

'''

print(intro)
lang = input('Option: \n > ')
os.system('cls')

if lang == '1':
  langu = 'ru'
if lang == '2':
  langu = 'en'
if lang == '3':
  langu = 'ja' 
if lang == '4':
  langu = 'nl'
else:
  while True:
    print(f'{Fore.RED}> Error \n Please restart.')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': token,
  }
request = requests.Session()
payload = {
    'locale': f"{langu}",
  }
while True:
    try:
        request.patch("https://discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
    except:
      print(f'{Fore.RED}> Error{Fore.RESET}')
    else:
      print(f'{Fore.GREEN}Success, Please close the program.{Fore.RESET}')
# Enjoy
# For issues contact XRXK#1337
