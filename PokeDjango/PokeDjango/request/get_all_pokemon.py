import asyncio
import re
import aiohttp

from PokeDjango.request.get_names_pokemon import get_names_pokemons

url = "https://pokeapi.co/api/v2/pokemon"


async def get_all_pokemon():
    allpokes = get_names_pokemons()

    datapkmn = []
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}?offset={0}&limit={898}") as r:
            test = await r.json()
            for poke in test['results']:
                pokemon = {
                    "name": allpokes[int(re.search(r'/([0-9]+)/$', poke['url']).group(1)) - 1],
                    "id": re.search(r'/([0-9]+)/$', poke['url']).group(1),
                }
                datapkmn.append(pokemon)

    return datapkmn


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())