import json
import utils
import discord


class UI:
    def __init__(self, embed, path):
        self.embed = embed
        self.cfg = json.loads(open(path, "r").read())

    def reload_cfg(self):
        self.cfg = json.loads(open(self.path, "r").read())

    def construct_poll(self, args, pollObject):

        poll = self.embed(
            title=args["question"],
            description=utils.to_str(pollObject.perfect_options(args["options"])), #how to improve: make a poll object when poll is called in commands, making the poll obj have an attribute of get_question() and get_option()
            colour=0x0892d0
        )
        poll.set_footer(text=self.cfg["footer"])
        return poll
        #also tidy up the pollObject bs like wtf

    async def edit_poll(self, poll_info, message, pollObject):
        poll = self.embed(
            title=poll_info["question"],
            description=utils.to_str(pollObject.perfect_options(utils.get_keys(poll_info["options"]), poll_info)),
            colour=0x0892d0
            # how to improve: make a poll object when poll is called in commands, making the poll obj have an attribute of get_question() and get_option()
        )
        poll.set_footer(text=self.cfg["footer"])


        await message.edit(content=None, embed=poll)

