import json


path = './data/raw/endsong_0.json'

with open(path) as file:
  data = json.load(file)


print(data)