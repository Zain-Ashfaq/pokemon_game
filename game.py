import random

import requests
# https://pokeapi.co/api/v2/pokemon/ditto
from random import randint


# pokemon_list = [
#     {"name": "Sorcerer", "health": 100, "damage": [10, 25]},
#     {"name": "Barbarian", "health": 150, "damage": [5, 15]},
#     {"name": "Rogue", "health": 80, "damage": [15, 20]},
#     {"name": "Necromancer", "health": 120, "damage": [10, 20]},
#     {"name": "Druid", "health": 90, "damage": [15, 25]}
# ]

pokemon_list = requests.get("https://pokeapi.co/api/v2/pokemon?limit=60").json()


# poke_guy_test = pokemon_list['results'][0]['name']
# poke_list_test = pokemon_list['results']
# print(poke_list_test[0])
# print(len(pokemon_list))
# print("this is pokemon list", pokemon_list)

def get_one_pokemon(pokename):
    return requests.get("https://pokeapi.co/api/v2/pokemon/"+pokename).json()
def select_character(player_num):
    # Let the player select a character
    if player_num == 1:
        player_name = input("Player 1, enter your name: ")
        print(f"{player_name}, select your character:")
    elif player_num == 2:

        player_name = input("Player 2, enter your name: ")
        print(f"{player_name}, select your character:")
    else:
        player_name = 'CPU'
    choice = None
    while not choice:
        for i in range(len(pokemon_list['results'])):





            print(f"{i + 1}. {pokemon_list['results'][i]['name']}")
        if player_num == 3:
            choice = random.randrange(1, len(pokemon_list['results']))
        else:

            choice = int(input("Enter the number of your choice: "))

        if 1 <= choice <= len(pokemon_list['results']):
            return {"player_name": player_name, "character": pokemon_list['results'][choice - 1]}
        else:
            print("Invalid choice. Please try again.")
            choice = None


def fight(player1, player2):
    print(player1," SIUUUU")

    print(
        f"{player1['player_name']} ({player1['character']['name']}) and {player2['player_name']} ({player2['character']['name']}) are fighting!")

    # get the health and damage values for each player
    player_1_pokemon=get_one_pokemon(player1['character']['name'])
    player_2_pokemon = get_one_pokemon(player2['character']['name'])
    # print(player_1_pokemon)
    # print(player_2_pokemon)
    print("this is player 1 health",player_1_pokemon['stats'][0]['base_stat'])
    print("this is player 1 damage",player_1_pokemon['stats'][1]['base_stat'])
    print("this is player 1 rand", player_1_pokemon['stats'][2]['base_stat'])
#
    player1_health = int(player_1_pokemon['stats'][0]['base_stat']) * random.randrange(1,4)
    print("this is health",player1_health)
    player1_damage = int(player_1_pokemon['stats'][1]['base_stat'])
    print("this is damage", player1_health)
    player2_health = int(player_2_pokemon['stats'][0]['base_stat']) * random.randrange(1,4)
    print("this is health", player2_health)
    player2_damage = int(player_2_pokemon['stats'][1]['base_stat'])
    print("this is damage", player2_health)
#

    while player1_health > 0 and player2_health > 0:


        input("Press any key to continue...")

        player2_health -= player1_damage * random.randrange(1,2)
        print(
            f"{player1['player_name']} ({player1['character']['name']}) attacks {player2['player_name']} ({player2['character']['name']}) for {player1_damage} damage. {player2['player_name']}'s health: {player2_health}")

        # check if player 2 is dead
        if player2_health <= 0:
            print(f"{player2['player_name']} ({player2['character']['name']}) is dead")
            break


        input("Press any key to continue")

        player1_health -= player2_damage * random.randrange(1,2)
        print(
            f"{player2['player_name']} ({player2['character']['name']}) attacks {player1['player_name']} ({player1['character']['name']}) for {player1_damage} damage. {player1['player_name']}'s health: {player1_health}")


        if player1_health <= 0:
            print(f"{player1['player_name']} ({player1['character']['name']}) is dead")

    if player1_health < 0:
        player1_health = 0
    if player2_health < 0:
        player2_health = 0
    # determine who won
    if player1_health > player2_health:
        print(f"The winner is {player1['player_name']} ({player1['character']['name']})")
    else:
        print(f"The winner is {player2['player_name']} ({player2['character']['name']})")

def play_game(istwoplayer=True):
    while True:
        print("Choose your fighters")
        player1 = select_character(1)
        if istwoplayer:

            player2 = select_character(2)
        else:
            player2 = select_character(3)



        print("this is player 1", player1)
        fight(player1, player2)

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break
# main game loop
def main():
    isTwoPlayer = True
    if input("Do you want to play against a human?: (y/n)") == 'n':
        isTwoPlayer = False

    if isTwoPlayer:

        play_game()
    else:
        play_game(False)

main()


