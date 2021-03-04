import json
from random import choice, random
from utilities import words

class DummyTrek:
    VALID_FIELDS = [
        'username',
        'email',
        'first_name',
        'last_name',
        'occupation',
        'address'
    ]

    def user_profile(self, fields:list):
        profile = {}
        for field in fields:
            if field == 'username':
                profile['username'] = self.get_username()

        return profile

    def get_username(self):
        return choice(words['adjectives']) + choice(words['nouns']).capitalize()

    def ipsum(self, n:int=30, lang:str='klingon'):
        '''Return a stringn words from specified language (lang)'''
        
        text = ''
        for i in range(n):
            text += choice(words['klingon'])

            # the first word should be titleized
            if len(text.split(' ')) == 1:
                text = text.title() + ' '
            else:
                # random number between 0 and 1
                chance = random()
                
                # add punctuation based on a random chance
                if chance < .1:
                    text += '? '
                elif chance < .2:
                    text += '. '
                elif chance < .4:
                    text += '! '
                else:
                    text += ' '
                
                # if punctuation was added,
                # titleize the next word
                if chance < .4:
                    text += choice(words['klingon']).title()
                else:
                    text += choice(words['klingon'])
                
                # The final character should be !
                if i == n - 1:
                    text += '!'

        return text

trek = DummyTrek()

print(trek.user_profile(['username']))
# print(DummyTrek().ipsum(10))
