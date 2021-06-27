import poll
import ui
import discord

class Commands:
    def __init__(self, client):
        self.client = client
        self.commands = [self.help, self.poll]
        self.Poll = poll.Poll()
        self.UI = ui.UI(discord.Embed, "ui.cfg")

    async def help(self, message):
        await message.channel.send("No")

    async def not_found(self, message):
        await message.channel.send("Command not found")

    async def poll(self, message):
        args = self.Poll.get_msg_args(message.content)
        embed = self.UI.construct_poll(args)
        posted_poll = await message.channel.send(content=None, embed=embed)
        await self.Poll.add_reactions(posted_poll, args["options"])

    def get_commands(self):
        return self.commands

    def get_commands_as_strings(self):
        new_arr = []
        for i in self.commands:
            new_arr.append(i.__name__)
        return new_arr
