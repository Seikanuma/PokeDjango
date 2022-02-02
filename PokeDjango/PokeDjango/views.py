from django.shortcuts import render

from PokeDjango.function.type_weakness import get_weakness
from PokeDjango.request.get_all_pokemon import get_all_pokemon
from PokeDjango.request.get_pokemon_infos import get_pokemon

async def index(request):
	data = await get_all_pokemon()
	contextvalue = {"values": data}

	return render(request, 'index.html', contextvalue)


async def pokemon(request, number):
	data = await get_pokemon(number)

	types = []
	weakness = set()

	for t in data["types"]:
		types.append(t["type"]["name"])

	for type in types:
		print(type)

		weaks = get_weakness(type)
		print(weaks)
		for w in weaks:
			print(w)
			weakness.add(w)
	weakness = list(weakness)[:6]

	return render(request, 'pokemon.html', {"pokemon": data, "number": number, "weakness": weakness})