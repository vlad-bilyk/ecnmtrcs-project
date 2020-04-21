data = {'matchups': []}
data['matchups'].append(1)
data['b'] = 3
import json

with open('lol.json', 'w') as outfile:
    json.dump(data, outfile)