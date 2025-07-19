import json

mydictionary = {
    '苹果': 'apple',
    '香蕉': 'banana',
    '橙子家族': {
        '橘子': 'tangerine',
        '橙子': 'orange',
        '柚子': 'pomegrande',
        '柑橘': 'citrus'
    },
    '列表': ['1', 2, '3', 4, 5, 6, 1.1, 2.2]
}

s = json.dumps(mydictionary, ensure_ascii=False, indent=4)

f = open('level1.txt', 'w')
f.write(s)
f.close()