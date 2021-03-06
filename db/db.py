

"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

import json
ROOMS_DB = "/Users/annakelley/demo2/db/rooms.json"


def get_rooms():
    try:
        with open(ROOMS_DB) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return None


def fetch_pets():
    """
    A function to return all pets in the data store.
    """
    return {"tigers": 2, "lions": 3, "zebras": 1}
