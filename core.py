import requests
import discord
import asyncio
from beeprint import pp

def num_te(num):
    if num == 0:
        num = "0️⃣"

    elif num == 1:
        num = "1️⃣"

    elif num == 2:
        num = "2️⃣"

    elif num == 3:
        num = "3️⃣"

    elif num == 4:
        num = "4️⃣"

    elif num == 5:
        num = "5️⃣"

    elif num == 6:
        num = "6️⃣"
    
    elif num == 7:
        num = "seven"
    
    elif num == 8:
        num = "8️⃣"
    
    elif num == 9:
        num = "9️⃣"

    else:
        num = "🧩" 

    return num


def num_tt(num):
    if num == 0:
        num = "zero"

    elif num == 1:
        num = "one"

    elif num == 2:
        num = "two"

    elif num == 3:
        num = "three"

    elif num == 4:
        num = "four"

    elif num == 5:
        num = "five"

    elif num == 6:
        num = "six"
    
    elif num == 7:
        num = "seven"
    
    elif num == 8:
        num = "eight"
    
    elif num == 9:
        num = "nine"

    else:
        num = "jigsaw" 

    return num


async def fetch_country_stats(message, args, prefix):
    
    await message.channel.send("Coming soon!")
    return

    if args == []:
        await message.channel.send(f"Invalid usage - Example: ```{prefix}country-stats country_name_goes_here```")
        return
    

    name = args[0]
    country_res = requests.get(f"https://restcountries.eu/rest/v2/name/{name}")
    
    pp(country_res.json())



    
async def start_poll(message, args, prefix, client):
    
    if args == []:
        await message.channel.send(f'Invalid usage - Example: ```{prefix}poll Question goes here "options must be" "in quotation marks" "and seperated" "by spaces"```To see poll results do ```{prefix}poll show message_id_goes_here```')
        return
    
    q_and_o = [a[:-1] if a[-1] == '"' else a for a in " ".join(i for i in args).split(' "')]

    if q_and_o[0] == "show":
        await message.channel.send(f'Coming Soon!')
        return



    if len(q_and_o) == 1:
        await message.channel.send(f'Error: You forgot to add options - Example: ```{prefix}poll Question goes here "options must be" "in quotation marks" "and seperated" "by spaces"```')
        return
    
    elif len(q_and_o) == 2:
        await message.channel.send(f'Error: You need more than 1 option - Example: ```{prefix}poll Question goes here "options must be" "in quotation marks" "and seperated" "by spaces"```')
        return

    elif len(q_and_o) >= 12:
        await message.channel.send(f'Error: You can only have a maximum of 10 options  - Example: ```{prefix}poll Question goes here "options must be" "in quotation marks" "and seperated" "by spaces"```')
        return

    else:
        final_message = f"**{q_and_o[0]}**\n\n"
        for i in range(len(q_and_o)-1):
            final_message += f":{num_tt(i)}: {q_and_o[i]}\n"

        message_id = await message.channel.send(final_message)
        
        for i in range(len(q_and_o)-1):
            await message_id.add_reaction(num_te(i))


async def code_ref(message):
    await message.channel.send("")


    
async def help_commands(message, PREFIX):
    await message.channel.send(f"{PREFIX}help\n{PREFIX}poll\n{PREFIX}country-stats\n{PREFIX}code\n")
    return
    

