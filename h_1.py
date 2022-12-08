import requests

url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)

heroes = [ 'Hulk', 'Captain America', 'Thanos', 'A-Bomb']
information_about_heroes = []
intelligence = 0

for element in resp.json():
	for header,meaning in element.items():
		for hero in heroes:
			if header == 'name' and meaning == hero:
				information_about_heroes.append(element)
				for characteristic in information_about_heroes:
					for key, value in characteristic.items():
						if key == 'powerstats':
							for key_, value_ in value.items():
								if key_ == 'intelligence':
									if intelligence < value_:
										win = hero
										intelligence = value_

print(f'Самый умный супергерой {win} c интеллектом {intelligence}')

print('\nP.S.\nТанос не супергерой <(-_-)> \n')