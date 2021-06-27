import json


class UI:
    def __init__(self, embed, path):
        self.embed = embed
        self.cfg = json.loads(open(path, "r").read())

    def reload_cfg(self):
        self.cfg = self.cfg = json.loads(open(self.path, "r").read())

    def construct_poll(self, args):

        poll = self.embed(
            title=args["question"],
            description=args["options"] #how to improve: make a poll object when poll is called in commands, making the poll obj have an attribute of get_question() and get_option()
        )
        return poll
