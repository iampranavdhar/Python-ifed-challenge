import requests
import json
def ability(pokeName):
    response=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokeName)
    abilities=response.json()['abilities']
    ability=[]
    for i in abilities:
        j=(i['ability'])
        ability.append(j['name'])
    return ability