import asyncio
import random
import time


async def busca_pokemon_kanto() -> str:
	"""Simula a busca de um Pokemon na regiao de Kanto."""
	pokemons_kanto = ["Pikachu", "Bulbasaur", "Charmander", "Squirtle", "Eevee"]
	tempo_aleatorio = random.uniform(1, 5)
	await asyncio.sleep(tempo_aleatorio)
	return random.choice(pokemons_kanto)


async def busca_pokemon_johto() -> str:
	"""Simula a busca de um Pokemon na regiao de Johto."""
	pokemons_johto = ["Chikorita", "Cyndaquil", "Totodile", "Mareep", "Umbreon"]
	tempo_aleatorio = random.uniform(1, 5)
	await asyncio.sleep(tempo_aleatorio)
	return random.choice(pokemons_johto)


async def busca_pokemon_hoenn() -> str:
	"""Simula a busca de um Pokemon na regiao de Hoenn."""
	pokemons_hoenn = ["Treecko", "Torchic", "Mudkip", "Ralts", "Gardevoir"]
	tempo_aleatorio = random.uniform(1, 5)
	await asyncio.sleep(tempo_aleatorio)
	return random.choice(pokemons_hoenn)


async def main() -> None:
	"""Executa as buscas simultaneas e exibe os resultados."""
	inicio = time.perf_counter()

	resultado_kanto, resultado_johto, resultado_hoenn = await asyncio.gather(
		busca_pokemon_kanto(),
		busca_pokemon_johto(),
		busca_pokemon_hoenn(),
	)

	fim = time.perf_counter()
	tempo_total = fim - inicio

	print("=== Simulador de Captura Pokemon (Asyncio) ===")
	print(f"Encontrado em Kanto: {resultado_kanto}")
	print(f"Encontrado em Johto: {resultado_johto}")
	print(f"Encontrado em Hoenn: {resultado_hoenn}")
	print(f"Tempo total da busca simultanea: {tempo_total:.2f} segundos")


if __name__ == "__main__":
	asyncio.run(main())
