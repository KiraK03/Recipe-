import requests


def recipe_search(ingredient):
    app_id = '918709a2'
    app_key = '364da60af4b9debb35a4fb39fa468d91'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']


def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)

    for result in results:
        recipe = result['recipe']

        print(recipe['label'])
        print(recipe['url'])
        print()

run()
