import json


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
