from url_validator import is_valid_url

import requests
import json
from discord_webhook import DiscordEmbed, DiscordWebhook

from colorama import Fore, Back, Style


def Webhook_check():
    while True:
        try:
            print(Fore.BLUE + "Please provide a Webhook URL to get Started: ", end='')
            print(Style.RESET_ALL, end='')
            
            webhook_url = input()
            
            if not is_valid_url(webhook_url):
                raise ValueError(Fore.RED + 'Please provide a valid url, in the form of protocol (https), hostname (site.com), and arguments (.../example)\n')
            return True
        
        except ValueError as e:
            print(e)
            return False
            
    webhook = DiscordWebhook(url=webhook_url, \
    username="Lyric Bot", avatar_url="https://i.pinimg.com/originals/69/96/5c/69965c2849ec9b7148a5547ce6714735.jpg")


def Artist_check():
    while True:
        try: 
            print(Fore.CYAN + "\nEnter an artist of the song: ", end='')
            print(Style.RESET_ALL, end='')
            
            artist_input = input().title()

            if not artist_input:
                raise ValueError('Empty string, try again!\n')
            return True
        
        except ValueError as e:
            print(e)
            return False
            
def Song_check():
    while True:
        try:
            print(Fore.CYAN + "\nEnter a song name to look up: ", end='')
            print(Style.RESET_ALL, end='')
            
            song_input = input().title()
            
            if not song_input:
                raise ValueError('Empty string, try again!')
            return True
        
        except ValueError as e:
            print(e)
            return False

def Timeout_check():
    try:
        r = requests.get("https://api.lyrics.ovh/v1/%s/%s" % (artist_input, song_input), timeout=1)
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
        while True:
            timeout = str(raw_input('Server taking too long. Would you like to try again with a different artist and song? (y/n) :')).lower().strip()
            if reply[:1] == 'y':
                return "Again"
            if reply[:1] == 'n':
                return False
        return False
    return True

def Request_check():
    try:
        r = requests.get("https://api.lyrics.ovh/v1/%s/%s" % (artist_input, song_input), timeout=10)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print('Invalid Request, do you ')
        return False
    return True

def Response_check():

    with open("lyrics.txt", "w") as file:
        file.write(r.json()["lyrics"])
    
    embed = DiscordEmbed(title='{artist} - {song}'.format(artist=artist_input, song=song_input), description='Have fun and sing along!', color='ff9b00')

    with open("lyrics.txt", "rb") as f:
        webhook.add_embed(embed)
        webhook.add_file(file=f.read(), filename='lyrics.txt')

    response = webhook.execute()




print(Fore.GREEN + "Welcome to the Lyric Bot!\n")
