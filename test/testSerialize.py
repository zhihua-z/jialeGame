import json

result = {
    'name': '莉莉',
    'age': 16,
    'attack': 27,
    '防御': 30,
    'magic': 15          
}

s = json.dumps(result, ensure_ascii=False, indent=4)
f = open(f'test.json', 'w')
f.write(s)
f.close()

