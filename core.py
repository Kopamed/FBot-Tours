import json
import requests
import discord
import asyncio
from beeprint import pp

def load_polls():
    with open("polls.json", "r") as file:
        return json.load(file)

def save_polls(polls):
    with open("polls.json", "w") as file:
        json.dump(polls, file, indent = 4)


def add_poll(args, message_id):
    polls = load_polls()
    answers = []
    for i in args[1:]:
        answers.append(i)
    polls[str(message_id)] = {"question": args[0], "answers":answers}
    save_polls(polls)



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
        num = "7️⃣"
    
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


    if q_and_o[0][0:4] == "show":
        q_and_o = q_and_o[0].split()
        print(q_and_o)
        if len(q_and_o) == 2:
            polls = load_polls()
            if str(q_and_o[1]) in polls:
                polls = polls[str(q_and_o[1])]
                q_msg = "{}\n\n"
                opt_msg = "{}\n{}{}{}\n\n"

                

                try:
                    reactions = await message.channel.fetch_message(int(q_and_o[1]))
                    print(reactions.reactions)


                    total_reactions= 0
                    count = 0
                    vote_count = {}
                    for reaction in reactions.reactions:
                        total_reactions += reaction.count -1
                        vote_count[polls["answers"][count]] = reaction.count - 1
                        count += 1
                        final_message = ""
                        final_message += q_msg.format(polls["question"])
                        reactors_h = await reaction.get_reaction_users()

        #from here you can do whatever you need with the member objects
                    for member in reactors_h:
                        print(member.name)

                    for ques in vote_count:
                        final_message+=opt_msg.format(ques, "test", round(vote_count[ques]/total_reactions), )



                    print(vote_count)
                    print(total_reactions)

                except discord.errors.NotFound:
                    await message.channel.send("Error: Wrong channel - The message has been found in the poll database, but has not been found in this channel. Send the show command in the channel where the message is")



        else:
            await message.channel.send(f'Error: You only need 1 argument; the id - Example: ```{prefix}poll show message_id_of_the_bots_poll_message```')
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

        add_poll(q_and_o, message_id.id)


async def code_ref(message):
    await message.channel.send("Latest Release: https://github.com/Kopamed/FBot-Tours\nReal-Time Code on: https://repl.it/@ServerrHost/FireBot-Tours\nHosted using the help of: https://uptimerobot.com")


    
async def help_commands(message, PREFIX):
    await message.channel.send(f"{PREFIX}help\n{PREFIX}poll\n{PREFIX}country-stats\n{PREFIX}code\n")
    return
    

