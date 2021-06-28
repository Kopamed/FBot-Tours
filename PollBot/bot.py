import customToken
import commands
import poll
import ui
import discord


class Bot:
    def __init__(self, prefix, client, status='{}help'):
        self.prefix = prefix
        self.status = status.format(self.prefix)
        self.client = client
        if " " in self.prefix:
            self.self_destruct()
        self.Token = customToken.Token("db/token.txt")
        self.UI = ui.UI(discord.Embed, "db/ui.cfg")
        self.Poll = poll.Poll(self.UI, "db/polls.json")
        self.Commands = commands.Commands(self.client, self.Poll, self.UI)


    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game(self.status))
        print(f'[+] {self.client.user} has connected to Discord!')
        print(f'[+] Status: {self.status}')
        print(f'[+] Token: {self.Token.get_token()}')
        print(f'[+] Prefix: {self.prefix}')

    async def on_message(self, message):
        if message.author == self.client.user:
            return

        command = self.Commands.get_command(message.content, self.prefix)
        if command != False:
            await self.Commands.execute_command(command, message, self.prefix)

    async def on_reaction_add(self, payload):
        if payload.member == self.client.user:
            return
        message = await self.get_message(payload.channel_id, payload.message_id)
        await self.Poll.log_reaction(payload, message)

    async def on_reaction_remove(self, payload):
        if payload.member == self.client.user:
            return
        member = await self.get_member(payload.guild_id, payload.user_id)
        message = await self.get_message(payload.channel_id, payload.message_id)
        await self.Poll.log_unreaction(payload, member, message)

    async def get_member(self, guild_id, id):
        guild =  self.client.get_guild(guild_id)
        return await guild.fetch_member(id)

    async def get_message(self, channel_id, id):
        channel = self.client.get_channel(channel_id)
        return await channel.fetch_message(id)

    def self_destruct(self):
        print("[-] PREFIX CAN NOT HAVE SPACES IN IT")
        return 69/0
