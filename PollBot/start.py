import discord
import bot


def run():
    client = discord.Client()
    Bot = bot.Bot("}", client)
    print("[+] Bot init!")

    @client.event
    async def on_ready():
        await Bot.on_ready()

    @client.event
    async def on_message(message):
        await Bot.on_message(message)

    @client.event
    async def on_raw_reaction_add(payload):
        await Bot.on_reaction_add(payload)

    @client.event
    async def on_raw_reaction_remove(payload):
        await Bot.on_reaction_remove(payload)

    client.run(Bot.Token.get_token())
