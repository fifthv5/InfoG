import socket
import phonenumbers
import requests
from phonenumbers import geocoder
import os 
import platform

Bl = '\033[30m'  
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'

def toolname():
    print(f'''{Wh}
     ___                                               ____________
    |%%%|                                             |@@@@@@@@@@@@|
    |%%%|  ____       ___   _________   ____________  |@@@@________|       
    |%%%| |%%%%\     |%%%| |%%% _____| |%%%______%%%| |@@@|
    |%%%| |%%%%%\    |%%%| |%%%|_____  |%%|      |%%| |@@@|       ___
    |%%%| |%%%%%%\   |%%%| |%%%_____|  |%%|      |%%| |@@@|      |@@@|
    |%%%| |%%%|\%%\  |%%%| |%%%|       |%%|      |%%| |@@@|______|@@@|
    |%%%| |%%%| \%%\ |%%%| |%%%|       |%%|______|%%| |@@@@@@@@@@@@@@|
    |___| |___|  \_______| |___|       |____________| |______________|By: Fifthv5
    For more visit: https://github/fifthv5
{Gr}'''

def domain_name():
    print(socket.gethostbyname(input('Domain name: ')))


def your_ip():
    your_ip=requests.get('https://geolocation-db.com/json/').json() 
    print('Your public IP address: ',your_ip.get('IPv4'))
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print('Your device name: ',hostname)
    print('Your private IP address ',ip_address)


def ip_lookup():
    enter_ip = input('IP Address: ')
    response = requests.get(f"https://geolocation-db.com/json/{enter_ip}&position=true").json()
    for key, value in response.items():
        print(key, ' : ', value)


def ph_num_lookup():
    your_ph_num = input('Your Number: ')
    phone_number = phonenumbers.parse(your_ph_num)
    # put your phonenumber with the country code eg:+1xxxxxxxx
    print(geocoder.description_for_number(phone_number,
                                          'en'))


    from phonenumbers import carrier
    service_provider = phonenumbers.parse(your_ph_num)
    # put your phonenumber with the country code eg:+1xxxxxxxx
    print(carrier.name_for_number(service_provider,
                                  'en'))
    
    
def ip_grabber():
    if platform.system() == 'Windows':
        print('IP-Grabber is not supported on Windows')
    else:
        os.system('cd IP-Grabber && sudo chmod 777 * && bash ip-grabber.sh')
def clear():
     os.system("clear")
