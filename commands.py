import utils


class Commands:
    def __init__(self, client, Poll, UI):
        self.client = client
        self.commands = [self.help, self.poll]
        self.Poll = Poll
        self.UI = UI

    async def help(self, message):
        await message.channel.send("No")

    async def not_found(self, message):
        await message.channel.send("Command not found")

    async def poll(self, message):
        args = self.Poll.get_msg_args(message.content)
        embed = self.UI.construct_poll(args, self.Poll)
        posted_poll = await message.channel.send(content=None, embed=embed)
        self.Poll.add_poll_db(posted_poll.id, args)
        await self.Poll.add_reactions(posted_poll, args["options"])

    def get_commands(self):
        return self.commands

    def get_commands_as_strings(self):
        new_arr = []
        for i in self.commands:
            new_arr.append(i.__name__)
        return new_arr

    def is_command(self, message, prefix):
        prefix_len = len(prefix)
        if message[0:prefix_len].lower() == prefix:
            return True

        return False

    def get_command(self, message, prefix):
        if self.is_command(message, prefix):
            len_prefix = len(prefix)
            command = message.split(" ")[0][len_prefix:]

            return command

        else:
            return False

    async def execute_command(self, command, message):
        command_list = self.get_commands_as_strings()
        if command in command_list:
            await self.get_commands()[utils.index_of(command, command_list)](message)
        else:
            await self.not_found(message)
