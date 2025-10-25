import json
import pickle
import os
import requests as req

base_url = 'https://pokeapi.co/api/v2/'
cache_dir = 'cache'

# ensure cache directory exists
os.makedirs(cache_dir, exist_ok=True)

def _cache_filename(resource_type: str, name: str) -> str:
    safe_name = name.replace('/', '_')
    return os.path.join(cache_dir, f"{resource_type}_{safe_name}.pkl")


class Trainer:
    def __init__(self, poke_list, name):
        self.pokemon = []
        for p in poke_list:
            self.pokemon.append(p)
        self.name = name
        self.bag = {}  # placeholder for items (e.g., potions)

    def __str__(self):
        temp = ''
        for i, p in enumerate(self.pokemon, start=1):
            temp += f"{i}. {p.name.title()} "
        return temp


class Pokemon:
    def __init__(self, nam, level):
        poke = holsim('pokemon/', nam)
        self.name = poke.get('name', nam)
        self.moveset = poke.get('moves', [])
        self.level = level
        # stats: find HP, attack, defense by name
        stats = {s.get('stat', {}).get('name'): s.get('base_stat') for s in poke.get('stats', [])}
        self.hp = stats.get('hp', 1)
        self.attack = stats.get('attack', max(1, level * 5))
        self.defense = stats.get('defense', max(1, level * 5))
        types = poke.get('types', [])
        if len(types) > 0:
            self.typ1 = types[0]['type']['name']
        else:
            self.typ1 = None
        if len(types) > 1:
            self.typ2 = types[1]['type']['name']
        else:
            self.typ2 = None


def holmove(url, name):
    """
    Fetch move details using cache (cache/move_{name}.pkl) or from given URL.
    """
    filename = _cache_filename('move', name)
    if os.path.exists(filename):
        with open(filename, 'rb') as datei:
            x = pickle.load(datei)
    else:
        r = req.get(url)
        r.raise_for_status()
        x = r.json()
        with open(filename, 'wb') as datei:
            pickle.dump(x, datei)
    return x


def holdirec(z):
    # take last part of URL as a name
    name = z.rsplit('/', 1)[-1] or 'resource'
    filename = _cache_filename('resource', name)
    if os.path.exists(filename):
        with open(filename, 'rb') as datei:
            x = pickle.load(datei)
    else:
        r = req.get(z)
        r.raise_for_status()
        x = r.json()
        with open(filename, 'wb') as datei:
            pickle.dump(x, datei)
    return x


def holsim(z, n):
    """
    Fetch a resource from the API path base_url + z + n, or load from cache file in cache/.
    """
    resource_type = z.rstrip('/').replace('/', '_')
    filename = _cache_filename(resource_type, n)
    if os.path.exists(filename):
        with open(filename, 'rb') as datei:
            x = pickle.load(datei)
    else:
        r = req.get(base_url + z + n)
        r.raise_for_status()
        x = r.json()
        with open(filename, 'wb') as datei:
            pickle.dump(x, datei)
    return x
