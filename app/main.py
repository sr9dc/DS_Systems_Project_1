from url_validator import is_valid_url

import requests
import json
from discord_webhook import DiscordEmbed, DiscordWebhook
import random
import time

from rich import print
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table


# Specialized Console
console = Console()

# Log
table = Table(show_header=True, header_style="bold green")
table.add_column("Time", style="dim")
table.add_column("Artist")
table.add_column("Song")

console.status("Test", spinner='dots')


# Welcome Screen
print("[bold magenta]Hello, Welcome to the Lyric Bot![/bold magenta] :smiley:\n")
time.sleep(1)

print("[cyan]To get started, type a number in for what you want to do:\n[/cyan]")
time.sleep(1)

print("[yellow](1) View the README. :books:[/]")
print("[blue](2) Submit a Lyric Request. :airplane:[/]")
print("[green](3) View your Lyric Requests. :eyes:[/]")
print("[#F1948A](help) See this screen again. :open_hands:")
print("[#FF8C00](exit) Exit the app. :pile_of_poo:[/]\n")
    

while(True):
    
    choice = ""
    choices = ["1", "2", "3", "help", "exit"]
    while choice not in choices:
        choice = input(">> ").lower().strip()
        if choice not in choices:
            print("[red]Sorry, I didn't catch that. Enter again.[/]")

    if(choice =="1"):
        print("[yellow]\nViewing the README...[/]\n")
        time.sleep(1)
        
        with open("README.md") as readme:
            markdown = Markdown(readme.read())
        console.print(markdown)
        print("\n\n\n")
        time.sleep(1)
        continue


    if(choice =="2"):
        print("[blue]\nGetting Submission Prompt Ready...[/]")
        time.sleep(1)
        
        while(True):
            try:
                webhook_url = console.input("\n[#5499C7]Input a Webhook URL to get Started: [/]")
                if not is_valid_url(webhook_url):
                    raise ValueError("Please provide a valid url, in the form of a protocol (https), hostname (site.com), and arguments (.../example)\n")  
            except ValueError as e:
                print("[red]"+str(e)+"[/]")
                continue
            
            if requests.get(webhook_url).status_code != 200:
                print("[red]"+"The URL isn't returning a status of 200, which is incorrect. Please provide the correct Webhook URL"+"[/]")
                continue
                
            
        
            
            webhook = DiscordWebhook(url=webhook_url, content="Here are the lyrics to your song!", \
                username="Lyric Bot", avatar_url="https://i.pinimg.com/originals/69/96/5c/69965c2849ec9b7148a5547ce6714735.jpg")
            
            while(True):
            
                # Artist Input Part
                while(True):
                    try: 
                        artist_input = console.input("\n[#73C6B6]Enter an artist of a song: [/]").title()
                        
                        if not artist_input:
                            raise ValueError('Empty string, try again.\n')    
                    except ValueError as e:
                        print("[red]"+str(e)+"[/]")
                        continue
                    
                    break
                
                # Song Input Part
                while(True):
                    try:
                        song_input = console.input("\n[#5499C7]Enter a song name to look up: [/]").title()

                        if not song_input:
                            raise ValueError('Empty string, try again.\n')
                    except ValueError as e:
                        print("[red]"+str(e)+"[/]")
                        continue
                    
                    break
            
                # Request Part

                try:
                    r = requests.get("https://api.lyrics.ovh/v1/%s/%s" % (artist_input, song_input), timeout=10)
                except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                    print("[red]Server taking too long. This likely means the song is not in the database.[/]")
                    continue
                
                try:
                    r.raise_for_status()
                except requests.exceptions.HTTPError as e: 
                    print('[red]Invalid Request. This likely means that the song name is mistyped. Try again.[/]')
                    continue
                    
                # Response Part
                with open("app/lyrics.txt", "w") as file:
                    file.write(r.json()["lyrics"])
                
                embed = DiscordEmbed(title="{artist} - {song}".format(artist=artist_input, song=song_input), \
                    description="Sing along!", color = f'{"%06x" % random.randint(0, 0xFFFFFF)}')
                
                with open("app/lyrics.txt", "rb") as file:
                    webhook.add_embed(embed)
                    webhook.add_file(file=file.read(), filename='lyrics.txt')
                    
                response = webhook.execute()
                
                table.add_row(
                    time.strftime("%H:%M:%S", time.localtime()), artist_input, song_input
                )
                
                
                time.sleep(1)
                print("[bold #7DCEA0]\nSuccess! It should now be in your discord channel![/]\n")
                time.sleep(1)
                
        
                break
            break
        time.sleep(1)
        continue

    if(choice =="3"):
        console.print(table)
        
        time.sleep(1)
        continue
    
    if(choice =="help"):
        time.sleep(1)
        print("[cyan]\nHere we go again, type a number in for what you want to do:\n[/cyan]")
        time.sleep(1)
        print("[yellow](1) View the README. [/]")
        print("[blue](2) Submit a Lyric Request. [/]")
        print("[green](3) View your Lyric Requests. [/]")
        print("[#F1948A](help) See this screen again")
        print("[#FF8C00](exit) Exit the app. [/]\n")
        continue
    
    if(choice =="exit"):
        print("[#FF8C00]\nThank you for using the App... \n\n[bold magenta]Goodbye![/][/]\n")
        exit()
            


            

