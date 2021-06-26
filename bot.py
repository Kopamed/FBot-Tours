import customToken


class Bot:
    def __init__(self, prefix, client):
        self.prefix = prefix
        self.p_len = len(prefix)
        self.Token = customToken.Token("token.txt")
        self.client = client

    async def on_ready(self):
        print(f'[+] {self.client.user} has connected to Discord!')
        print(f'[+] Token: {self.Token.get_token()}')
        print(f'[+] Prefix: {self.prefix}')

    async def on_message(self, message):
        if message.author == self.client.user:
            return

        command = self.get_command(message.content)
        if command != False:
            print(command)

    def is_command(self, message):
        prefix_len = len(self.prefix)
        if message[0:prefix_len].lower() == self.prefix:
            return True

        return False

    def get_command(self, message):
        if self.is_command(message):
            len_prefix = len(self.prefix)
            command = message.split(" ")[0][len_prefix:]

            return command

        else:
            return False