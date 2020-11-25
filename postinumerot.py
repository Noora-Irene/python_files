import json
import urllib.request

with urllib.request.urlopen('http://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as url:
    data = json.loads(url.read().decode())

etsittava = input('Kirjoita postitoimipaikka:').upper()

postinumerot = []

if etsittava in data.values():
    for postinumero, postitoimipaikka in data.items():
        if postitoimipaikka == etsittava:
            postinumerot.append(postinumero)
    print(postinumerot)
else:
    print('Postitoimipaikka ei löytynyt listalta')
