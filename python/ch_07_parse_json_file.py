import json

file_name = 'ch_07_example_file.json'

json_file = open(file_name)
j = json.load(json_file)
json_file.close()

print(j['books'][1]['title'])
