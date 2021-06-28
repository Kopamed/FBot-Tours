class Token:
    def __init__(self, path):
        self.path = path
        self.token = open(path, "r").read().strip("\n")


    def reload_token(self):
        with open(self.path) as fi:
            self.token = fi.read().strip("\n")


    def get_token(self):
        return self.token


    def __str__(self):
        return self.get_token()
