import json
import utils


class Poll:
    def __init__(self, db="polls.json"):
        self.db = db

    def add_poll_db(self, message_id, args):
        polls = self.load_polls()
        options = {}
        for i in args["options"]:
            options[i] = {"votes": 0, "names": []}
        polls[str(message_id)] = {"question": args["question"], "options": options}
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

        return {"question": question, "options": options}

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
        options = self.perfect_options(options) #gotta tidy this bs up
        for i in range(len(options.split("\n"))):
            if i >= 12:
                await message.add_reaction(utils.num_te(i))
                return
            await message.add_reaction(utils.num_te(i))

    def log_reaction(self, payload):
        polls = self.load_polls()
        if str(payload.message_id) in polls:
            vote_id = self.get_vote_option(payload, polls[str(payload.message_id)])
            self.add_vote(str(payload.message_id), str(payload.member), vote_id)

    def get_vote_option(self, payload, poll_info):
        return utils.index_of(str(payload.emoji), utils.emojis)

    def add_vote(self, msg_id, member_name, vote_id):
        #oh shit i gotta tidy this dumpsterfire up
        #sorry about the microsoft code below, to whoever is reading this
        poll = self.load_polls()[msg_id]
        option_keys = utils.get_keys(poll["options"])
        if vote_id == -1 and len(poll["options"]) >11: #number is the amount of available emojis that connect to one option
            for i in option_keys[10:]:#the number -1
                if member_name not in poll["options"][i]["names"]:
                    poll["options"][i]["votes"] += 1
                    poll["options"][i]["names"].append(member_name)
        else:#i am cringing at how messy this is.. oof
            if member_name not in poll["options"][option_keys[vote_id]]["names"]:
                poll["options"][option_keys[vote_id]]["votes"] += 1
                poll["options"][option_keys[vote_id]]["names"].append(member_name)

        whole_poll = self.load_polls()
        whole_poll[msg_id] = poll
        self.save_polls(whole_poll)
