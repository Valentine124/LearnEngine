import yaml
import json


API_KEYS = 'models/apikeys.yaml'

with open(API_KEYS, 'r') as key_file:
    keys = yaml.full_load(key_file)

google_key = keys['google']['key']
udemy_key = keys['udemy']['key']
