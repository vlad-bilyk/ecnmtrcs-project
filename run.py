import json

id_list = []

with open('data/yasp_sample.json', 'r') as f:
    json_data = json.load(f)
    print(json_data)
    # for i in json_data:
    #     id_list.append(i['match_id'])

print(id_list)
