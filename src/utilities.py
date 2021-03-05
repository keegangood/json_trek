import requests
import json
from progress.bar import Bar
from names import names
from all_words import all_words

# klingon = words["klingon"]

# print(klingon)


def fetch_category_items(category, pages):
    category_items = []
    for page in range(pages):
        base_url = "http://stapi.co/api/v1/rest"
        response = json.loads(
            requests.get(
                f"{base_url}/{category}/search/?pageNumber={page}").text
        )

        print(response)
        print(response['page']['totalPages'])
        exit()

        for item in response[category + 's']:

            # if "'" in item['name']:
            #     print(item['name'])
            #     continue

            words = item['name'].split(' ')

            if len(words) > 2:
                words = words[1:]

            # if len(''.join(words)) >= 12:
            #     words = words[1:]

            # .title().replace('-', '').replace(' ', ''))
            category_items.append(' '.join(words))

    return sorted(set(category_items))


def write_category_to_file(category_name, category_items):
    with open(f"{category_name}.py", "a") as category_file:
        content = f'{category_name}='
        content += json.dumps(category_items)

        category_file.write(content)


# results = fetch_category_items("character", 1)
# print(results)
# write_category_to_file('animals', results)

sorted_names = {
    'first': sorted(set(names['first'])),
    'last': sorted(set(names['last']))
}
content = 'names = '
content += json.dumps(sorted_names)

with open('text.py', 'w') as file:
    file.write(content)

"""
with Bar('Processing', max=12) as bar:

    for page in range(1,13):
        response = requests.get(f'{base_url}/species/search?pageNumber={page}')

        data = json.loads(response.text)

        for spec in data['species']:
            species.append(spec['name'])

        bar.next()

bar.finish()
"""
"""
with open('species.py', 'w') as names_file:
    content = 'species="'
    content += json.dumps(species) + "\""

    names_file.write(content)
"""

if __name__ == "__main__":
    output = f"Words Dict Keys\n-----\n"
    output += "\n".join([key for key in all_words.keys()])
    # print(output)
