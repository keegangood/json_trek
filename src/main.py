import json
from random import choice as random_choice, random
from utilities import words
from species import species
from klingon import klingon


class DummyTrek:
    VALID_FIELDS = [
        "username",
        "email",
        "first_name",
        "last_name",
        "occupation",
        "address",
    ]

    def user_profile(self, fields: list) -> dict:
        """Generates random values for each of the given fields in the fields list
        Returns a dictionary of fields and their values"""
        profile = {}
        for field in fields:
            if field == "username":
                profile["username"] = self.get_username()

        return profile

    def get_username(self) -> str:
        """Return an adjective and a noun in camelCase, representing a username"""
        return random_choice(species) + random_choice(words["nouns"]).capitalize()

    def ipsum(self, n: int = 30, lang: str = "klingon") -> str:
        """Return a string of n words from specified language (lang)"""
        if lang == "human":
            pass
            # words = human_words
        else:
            words = klingon_words
        text = ""
        for i in range(n):
            text += random_choice(klingon_words)

            # the first word should be titleized
            if len(text.split(" ")) == 1:
                text = text.title() + " "
            else:
                # random number between 0 and 1
                chance = random()

                # add punctuation based on a random chance
                if chance < 0.1:
                    text += "? "
                elif chance < 0.2:
                    text += ". "
                elif chance < 0.4:
                    text += "! "
                else:
                    text += " "

                # if punctuation was added,
                # titleize the next word
                if chance < 0.4:
                    text += random_choice(words["klingon"]).title()
                else:
                    text += random_choice(words["klingon"])

                # The final character should be !
                if i == n - 1:
                    text += "!"

        return text


trek = DummyTrek()

print(trek.user_profile(["username"]))
print(DummyTrek().ipsum(10))
