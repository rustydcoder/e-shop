import json
from random import shuffle

PRODUCT_NAME = ['plantain', 'banana', 'beans', 'bread', 'apple', 'pineapple', 'maize', 'corn', 'rice', 'jelly', 'grape']
shuffle(PRODUCT_NAME)


def save_db(_data: dict, filepath='e-shop.json'):
    """save json file"""
    try:
        for k, v in _data.items():
            if not type(v) is dict:
                _data[k] = v.__dict__
        with open(filepath, 'w') as f:
            json.dump(_data, f)
            print('saved to store')
    except:
        print('file not successfully saved')


def load_db(filepath='e-shop.json'):
    """loads the database"""
    try:
        with open(filepath, 'r') as f:
            print('Store loaded')
            return json.load(f)
    except FileNotFoundError:
        print('Creating a storage')
        return {}
