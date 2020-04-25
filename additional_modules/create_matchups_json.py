# this code was used to create data/hero_matchups.json file

import json

newdata = {}

with open('data/hero_matchups.json') as file:
    data = json.load(file)
    print(data)
    for key in data:
        # newdata[key] = {}
        inner_dict = {}
        values = data[key]
        sv = sorted(values, key = lambda x: x['hero_id'])
        for val in sv:
            hero_id = val['hero_id']
            inner_dict[hero_id] = [val['games_played'], val['wins']]
            # print(inner_dict)
            # print(val)
        newdata[key] = inner_dict


with open('data/hero_matchups.json', 'w') as file:
    json.dump(newdata, file)
