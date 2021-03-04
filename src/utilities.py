import requests
import json
from progress.bar import Bar
import names
from all_words import all_words

# klingon = words["klingon"]
first_names = names.names["first"]
last_names = names.names["last"]

# print(klingon)


def fetch_category_items(category, pages):
    category_items = []
    for page in range(pages):
        base_url = "http://stapi.co/api/v1/rest"
        # response = json.loads()

        response = requests.get(f"{base_url}/{category}/search/?pageNumber={page}").text
        # for  in response["occupations"]:
        #     occupations.append(occupation["name"])

    return response


print(fetch_category_items("astronomicalObject", 1))


def write_category_to_file(category_name, category_list):
    with open("occupations.py", "w") as category_file:
        content = 'occupations="'
        content += json.dumps(occupations) + '"'

        category_file.write(content)


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