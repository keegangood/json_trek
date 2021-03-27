from string import ascii_uppercase as ABCs
from random import choice as random_choice, random, randint
from all_words import all_words

class JSONTrek:
    """
    Star-Trek-themed dummy data generator.

    from JSONTrek import JSONTrek

    trek = JSONTrek()
    """
    def __init__(self):
        self.names         = all_words.get('names')
        self.animals       = all_words.get('animals')
        self.astro_objs    = all_words.get('astronomical_objects')
        self.klingon_words = all_words.get('klingon_words')
        self.names         = all_words.get('names')
        self.nouns         = all_words.get('nouns')
        self.occupations   = all_words.get('occupations')
        self.species       = all_words.get('species')
        self.trek_nouns    = all_words.get('trek_nouns')

    VALID_FIELDS = [
        "username",
        "email",
        "first_name",
        "last_name",
        "occupation",
        "address",
    ]


    def user_profile(self, fields: list=VALID_FIELDS) -> dict:
        """Generates random values for each of the given fields in the fields list
        Returns a dictionary of fields and their values"""
        profile = {}
        for field in fields:
            if field == "username":
                profile["username"] = self.username()
            elif field == "email":
                profile['email'] = self.email()
            elif field == 'first_name':
                profile['first_name'] = self.findName('first')
            elif field == 'last_name':
                profile['last_name'] = self.findName('last')
            elif field == 'occupation':
                profile['occupation'] = self.occupation()
        return profile

    def username(self) -> str:
        """Return an adjective and a noun in camelCase, representing a username"""


        species = self.species.get(random_choice(ABCs))
        nouns = self.nouns.get(random_choice(ABCs))




        # username starts with a random species name
        username = random_choice(species)

        # 70% chance of noun, 30% chance of animal
        if random() > .7:
            username += random_choice(self.animals)
        else:
            username += random_choice(nouns).capitalize()

        return username + str(int(random() * 100))

    def email(self):
        """Return a fake email address

        e.g. """
        suffixes = ['com', 'trek', 'edu', 'fed', 'net']
        return f'{self.username()}@sector{int(random() * 100)}.{random_choice(suffixes)}'

    def findName(self, first_or_last:str='first') -> str:
        '''Choose a random letter and then choose a random first or last name
        from the list of names using the random letter as a key'''
        letter = random_choice(ABCs)
        return random_choice(self.names[first_or_last][letter])

    def occupation(self) -> str:
        return random_choice(self.occupations[random_choice(ABCs)])

    def address(self) -> str:
        cardinals = ['N.', 'N.E.', 'E.', 'S.E.', 'S.', 'S.W.', 'W.', 'N.W.']
        street_types = ['Ave.', 'St.', 'Ln.', 'Ct.', 'Blvd.', 'Way', 'Hwy.']

        address = {
            'street': '',
            'city': random_choice(self.astro_objs[random_choice(ABCs)]),
            'state': random_choice(ABCs) + random_choice(ABCs),
            'country': random_choice(self.astro_objs[random_choice(ABCs)]),
            'zipcode': f'{randint(12345, 99999)}-{randint(1000, 9999)}'
        }

        address['street'] += str(randint(1, 999)) + ' '

        if random() > .7:
            address['street'] += random_choice(cardinals) + ' '

        address['street'] += random_choice(all_words['species'][random_choice(ABCs)]) + ' '
        address['street'] += random_choice(street_types) + ' '



        return address

    def ipsum(self, n: int = 30, lang: str = "human") -> str:
        """Return a string of n words from specified language (lang)"""
        if lang == 'klingon':
            words = all_words['klingon_words']

        elif lang == "human":
            to_include = ['astronomical_objects', 'species', 'trek_nouns','trek_nouns', 'trek_nouns','trek_nouns']

            words = []

            for key in to_include:

                # if the value is a list, add all its items to the words list
                if isinstance(all_words.get(key), list):
                    words.extend(all_words.get(key))

                # if the value is a dict, add the lists at each letter
                else:
                    # loop through alphabet and use each 
                    # as a key to add the list at that key
                    for letter in ABCs:
                        words.extend(all_words[key][letter])
                        
            print(sorted(words))
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


trek = JSONTrek()

print(trek.user_profile(["username", "email", "first_name", "last_name", "occupation"]))
print(trek.ipsum())

# print(trek.address())
