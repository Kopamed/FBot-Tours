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
        print(f'[+] Received message: {message.content}')
