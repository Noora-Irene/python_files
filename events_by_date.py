import json
import urllib.request


def hae_tapahtumat():
    with urllib.request.urlopen('http://open-api.myhelsinki.fi/v1/events/') as response:
        return json.loads(response.read())


tapahtumat = hae_tapahtumat()
lista = tapahtumat["data"]

ajat = []

for tapahtuma in lista:
    aloitusaika = tapahtuma['event_dates']['starting_day']
    if aloitusaika is not None:
        ajat.append(tapahtuma)

x = len(ajat)
print("Listalla on ", x, "tapahtumaa. Haetaan. . .\n")

for i in range(x-1):
    for aika in range(0, x-i-1):
        if ajat[aika]['event_dates']['starting_day'] > ajat[aika+1]['event_dates']['starting_day']:
            ajat[aika], ajat[aika + 1] = ajat[aika + 1], ajat[aika]

for i in range(len(ajat)):
    print(ajat[i]['event_dates']['starting_day']
          [0:16], "\t", ajat[i]["name"]["fi"])
