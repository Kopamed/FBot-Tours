import discord
import os

from core import *
import keep_alive




PREFIX = "f."
PREFIX_LEN = len(PREFIX)


TOKEN = os.environ['token']


client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')



@client.event
async def on_message(message):
    print(message.content)
    if message.content == "" or message.author == client.user:
        return

    command = None

    if message.content[0:PREFIX_LEN] == PREFIX:
        try:
            command = message.content.split()[0][PREFIX_LEN:]
        except:
            command = None

        args = message.content.split()[1:]
        


    if command == "country-stats":
        await fetch_country_stats(message, args, PREFIX)


    elif command == "poll":
        await start_poll(message, args, PREFIX, client)

    elif command == "help":
        await help_commands(message, PREFIX)

    elif command == "code":
        await code_ref(message)
        
    
    
         

keep_alive.keep_alive()
client.run(TOKEN)
