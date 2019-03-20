import json

s = '{"books" : [{"title" : "Programnming Arduino", "price" : 10.95}, {"title" : "Pi Cookbook", "price" : 19.95}]}''
j = json.loads(s)
print(j['books'][1]['title'])
