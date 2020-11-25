import json

import urllib.request

with urllib.request.urlopen('http://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as url:

    data = json.loads(url.read().decode())

etsittava = input('Kirjoita postinumero:')

print(data[etsittava])
