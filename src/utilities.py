import requests
from string import ascii_uppercase as uppercase
import json
from progress.bar import Bar
from all_words import all_words
import random


def fetch_category_items(category, pages, subcategories=None):
    category_items = []

    with Bar('Processing', max=pages) as bar:

        for page in range(1, pages+1):
            base_url = "http://stapi.co/api/v1/rest"
            data = json.loads(
                requests.get(
                    f"{base_url}/{category}/search/?pageNumber={page}").text
            )

        # if category ends in y, change ending to 'ies'
        if category.endswith('y'):
            category = category[:-1] + 'ies'
        else:
            category += 's'

        # print(category)
        # print(data)
        exit()

        items = []

        if subcategories:
            for spec in data[category]:
                for sub in subcategories:
                    items.append(data[sub])
        else:
            items.append(data)
        bar.next()

    bar.finish()

    return sorted(items)

    # for loc in response['astronomical_objects']:
    #     if loc.get('planet'):
    #         print(loc)
    # print(response['page']['totalPages'])
    # exit()

    # for item in response[category + 's']:

    # if "'" in item['name']:
    #     print(item['name'])
    #     continue

    # words = item['name'].split(' ')

    # if len(words) > 2:
    #     words = words[1:]

    # if len(''.join(words)) >= 12:
    #     words = words[1:]

    # .title().replace('-', '').replace(' ', '')) # remove hyphens, TitleCase
    # category_items.append(' '.join(words))


def write_category_to_file(category_name, category_items):
    with open(f"{category_name}_1.json", "w") as category_file:

        category_file.write(json.dumps(category_items, indent=4))

# print(fetch_category_items('astronomicalObject' ,1))

# sorted_names = {
#     'first': sorted(set(names['first'])),
#     'last': sorted(set(names['last']))
# }
# content = 'names = '

# with open('text.py', 'w') as file:
#     json.dump(sorted_names, file, indent=4)


"""
with open('species.py', 'w') as names_file:
    content = 'species="'
    content += json.dumps(species) + "\""

    names_file.write(content)
"""


def generate_alphabet_lists(items: list, skip=[]):
    output = {letter: [] for letter in uppercase}

    print(output)

    for item in items:
        skip_it = False
        for word in skip:

            if word in item:
                print(item)
                skip_it = True
                break

        if skip_it:
            continue

        if '1' in item or \
            '2' in item or \
            '3' in item or \
            '4' in item or \
            '5' in item or \
            '6' in item or \
            '7' in item or \
            '8' in item or \
            '9' in item or \
                '0' in item:
            # print(item)
            continue

        key = item[0].upper()

        output[key].append(item)

    for key in output:
        output[key] = sorted(set(output[key]))

    return output


with open('words.json', 'r') as file:
    content = json.loads(file.read())

output = generate_alphabet_lists(
    content['nouns']
)

print(output)

astro_objs_skips= [
        'System',
        'Sector',
        'Belt',
        'Window',
        'Tropics',
        'Homeworld',
        'Star',
        'Plane',
        'Time'
        'Runners',
        'Void',
        'Barrens'
        'Fold',
        'Asteroid',
        'Cloud',
        'Stevens',
        'Planet',
        'Zone',
        'Area',
        'Field',
        'Gaul',
        'Sydney'
        'Rim',
        'Region',
        'Frontier',
        'Distortion',
        'Passage',
        'Border',
        'Midwest',
        'Memory',
        'Mariposa',
        'Halana',
        'Brooklyn',
        'Mecca',
        'Paris',
        'L-S',
        'Junkyard',
        'Theater',
        'Layer',
        'Hole In Space',
        'Great',
        'Finley',
        'Eastern',
        ' Arm',
        'Point',
        'Space',
        'Cluster',
        'Badlands',
        'Diaspora'
    ]


# print(output)
write_category_to_file('nouns', output)

# names = {
#     'first': generate_alphabet_lists(names['first']),
#     'last': generate_alphabet_lists(names['last'])
# }


# write_category_to_file('names', names)


# print(names)
if __name__ == "__main__":
    output = f"Words Dict Keys\n-----\n"
    output += "\n".join([key for key in all_words.keys()])
    # print(output)
