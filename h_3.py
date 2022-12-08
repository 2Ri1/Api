import requests

url = "https://api.stackexchange.com/2.3/questions?order=desc&min=1670284800&max=1670457600&sort=activity&tagged=%27Python%27&site=stackoverflow"
resp = requests.get(url)
element = resp.json()

for key, value in element.items():
	if key == 'items':
		for el in value:
			for key_2, value_2 in el.items():
				if key_2 == 'link':
					print(f'{el["title"]}:\n {value_2}\n')