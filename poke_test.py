import requests

pokemon_list = requests.get("https://pokeapi.co/api/v2/pokemon?limit=60").json()
print(pokemon_list,)
poke_guy_test = pokemon_list['results'][0]['name']
list_size = pokemon_list['results']
print(len(list_size))
print(pokemon_list['results'][0]['name'])


pokemon_get_guy = "https://pokeapi.co/api/v2/pokemon/"

poke_guy_test = pokemon_list['results'][0]['name']
print(poke_guy_test)

print(requests.get(pokemon_get_guy).json())



