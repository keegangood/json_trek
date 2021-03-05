import json
from random import choice as random_choice, random
from klingon_words import klingon_words
from names import names
from human_words import human_words

class DummyTrek:
    """
    Star-Trek-themed dummy data generator.

    from DummyTrek import DummyTrek

    trek = DummyTrek()
    """

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
            elif field == "email":
                profile['email'] = self.get_email()
            elif field == 'first_name':
                profile['first_name'] = self.get_name('first')
            elif field == 'last_name':
                profile['last_name'] = self.get_name('last')
        return profile

    def get_username(self) -> str:
        """Return an adjective and a noun in camelCase, representing a username"""
        species = human_words['species']
        animals = human_words['animals']
        return random_choice(species) + random_choice(animals)

    def get_email(self):
        """Return a fake email address
        
        e.g. """
        suffixes = ['com', 'trek', 'edu', 'fed', 'net']
        return f'{self.get_username()}@sector{int(random() * 100)}.{random_choice(suffixes)}'

    def get_name(self, first_or_last='first'):
        return random_choice(names[first_or_last])

    def ipsum(self, n: int = 30, lang: str = "klingon") -> str:
        """Return a string of n words from specified language (lang)"""
        if lang == "human":
            words = []

            for key, word_list in human_words.items():
                if key in ['animals']:
                    continue
                for word in word_list:
                    words.append(word)

        else:
            words = klingon_words
        text = ""
        for i in range(n):
            text += random_choice(words)

            # the first word should be titleized
            if i == 0:
                text = text.capitalize() + " "
            else:
                # random number between 0 and 1
                chance = random()

                # add punctuation based on a random chance
                if chance < 0.1:
                    text += "? "
                elif chance < 0.2:
                    text += ". "
                elif chance < 0.3:
                    text += "! "
                else:
                    text += " "

                word = ''
                while not word.isalpha():
                    word = random_choice(words)

                # if punctuation was added,
                # capitalize the next word
                if chance < 0.6:
                    text += word.capitalize()
                else:
                    text += word.lower()

                # The final character should be !
                if i == n - 1:
                    text += "!"
                else:
                    text += ' '

        return text


trek = DummyTrek()

# print(trek.user_profile(["username", "email", "first_name", "last_name"]))
print(DummyTrek().ipsum(10, 'human'))
