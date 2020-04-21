import json
import requests

# matchups = {}
#
# with open('data/heroes.json', 'r') as f:
#     json_data = json.load(f)
# for hero in json_data['result']['heroes']:
#     id = hero['id']
#     if id < 68:
#         continue
#     matchups[id] = requests.get("https://api.opendota.com/api/heroes/{}/matchups".format(id)).json()
#
# print(matchups)
#
# with open('hero_matchups1.json', 'w') as outfile:
#     json.dump(matchups, outfile)

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