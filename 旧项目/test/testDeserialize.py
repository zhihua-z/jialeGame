import json

f = open('test.json', 'r')

data = f.read()

obj = json.loads(data)

print(obj['name'])
print(obj['age'])
print(obj['attack'])
print(obj['defence'])
print(obj['magic'])