import yaml
import json

# This file contains all the API keys for
# Google and Udemy
API_KEYS = 'models/apikeys.yaml'

# Loop though the file content and get the dictionary
# representation of the file content
with open(API_KEYS, 'r') as key_file:
    keys = yaml.full_load(key_file)

google_key = keys['google']['key']
udemy_key = keys['udemy']['key']
