import discord
import os
from dotenv import load_dotenv
from core import *
import keep_alive
import random




PREFIX = "f."
PREFIX_LEN = len(PREFIX)


load_dotenv()
TOKEN = os.getenv('token')


client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')



@client.event
async def on_message(message):
    if len(message.content) >= 2 and message.content[0:2] == "f.":
        if len(message.content.split()) == 2:
            message_id = message.content.split()[1]
            dynos_message = await message.channel.fetch_message(message_id)
            print(dynos_message.reactions)
            users = await dynos_message.reactions[0].users().flatten()
            # users is now a list of User...
            winner = random.choice(users)
            await message.channel.send('{} has won the raffle.'.format(winner))
        


client.run(TOKEN)
