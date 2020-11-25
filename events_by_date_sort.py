import urllib.request
import json


def hae_tapahtumat():
    with urllib.request.urlopen('http://open-api.myhelsinki.fi/v1/events/') as response:
        return json.loads(response.read())


tapahtumat = hae_tapahtumat()
lista = tapahtumat["data"]

n = len(lista)
print("tapahtumia yhteensä eli n:n arvo on ", n)

arr = []

for tapahtuma in lista:
    aika = tapahtuma['event_dates']['starting_day']
    if aika is not None:
        arr.append(aika)

arr.sort()
for i in range(len(arr)):
    print(arr[i])

print("Listalla on", len(arr), "tapahtuman aloitusaikaa.")
