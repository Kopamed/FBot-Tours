import json


class UI:
    def __init__(self, embed, path):
        self.embed = embed
        self.cfg = json.loads(open(path, "r").read())

    def reload_cfg(self):
        self.cfg = self.cfg = json.loads(open(self.path, "r").read())

    def construct_poll(self, args, pollObject):

        poll = self.embed(
            title=args["question"],
            description=pollObject.perfect_options(args["options"]) #how to improve: make a poll object when poll is called in commands, making the poll obj have an attribute of get_question() and get_option()
        )
        return poll
        #also tidy up the pollObject bs like wtf

    def edit_poll(self, poll_info):
        pass
