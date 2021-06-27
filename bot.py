import customToken
import commands
import poll


class Bot:
    def __init__(self, prefix, client):
        self.prefix = prefix
        if " " in self.prefix:
            self.self_destruct()
        self.p_len = len(prefix)
        self.Token = customToken.Token("token.txt")
        self.client = client
        self.Poll = poll.Poll()
        self.Commands = commands.Commands(self.client, self.Poll)

    async def on_ready(self):
        print(f'[+] {self.client.user} has connected to Discord!')
        print(f'[+] Token: {self.Token.get_token()}')
        print(f'[+] Prefix: {self.prefix}')

    async def on_message(self, message):
        if message.author == self.client.user:
            return

        command = self.Commands.get_command(message.content, self.prefix)
        if command != False:
            await self.Commands.execute_command(command, message)

    async def on_reaction_add(self, payload):
        if payload.member == self.client.user:
            return
        self.Poll.log_reaction(payload)

    async def on_reaction_remove(self, payload):
        pass

    def self_destruct(self):
        print("[-] PREFIX CAN NOT HAVE SPACES IN IT")
        return 69/0
