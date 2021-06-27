import json
import utils


class Poll:
    def __init__(self, db="polls.json"):
        self.db = db

    def add_poll(self, args, message_id):
        polls = self.load_polls()
        answers = {}
        for i in args[1:]:
            answers[i] = 0
        polls[str(message_id)] = {"question": args[0], "answers": answers}
        self.save_polls(polls)

    def load_polls(self):
        with open(self.db, "r") as file:
            return json.load(file)

    def save_polls(self, polls):
        with open(self.db, "w") as file:
            json.dump(polls, file, indent=4)

    def get_msg_args(self, content):
        main_content = " ".join(i for i in content.split(" ")[1:])
        question = main_content.split(' "')[0]
        options = main_content.split(' "')[1:]
        options = [i[:-1] for i in options]

        return {"question": question, "options": self.perfect_options(options)}

    def perfect_options(self, options):
        string = ""
        for i in range(len(options)):
            if options[i] == options[-1]:
                string += ":" + utils.num_tt(i) + ": " + options[i]
            else:
                string += ":" + utils.num_tt(i) + ": " + options[i] + "\n"
        return string

    def check_format(self, content):
        #to do
        pass

    async def add_reactions(self, message, options):
        for i in range(len(options.split("\n"))):
            await message.add_reaction("\N{SLIGHTLY SMILING FACE}")
