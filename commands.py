class Commands:
    def __init__(self, client):
        self.client = client
        self.commands = [self.help]

    async def help(self, message):
        await message.channel.send("No")

    async def not_found(self, message):
        await message.channel.send("Command not found")

    def get_commands(self):
        return self.commands

    def get_commands_as_strings(self):
        new_arr = []
        for i in self.commands:
            new_arr.append(i.__name__)
        return new_arr
