import json

all_words = {}

filenames = ['animals', 'astronomical_objects', 'klingon_words',
             'names', 'nouns', 'occupations', 'species']


for filename in filenames:
    with open(f'json/{filename}.json', 'r') as json_file:
        all_words[filename] = json.load(json_file)
