import json

'''
json: dumps, loads 

dumps() -> 把一个物体丢到一个json string里

loads() -> 从一个json string里加载一个物体

'''

class GameObject:
    def __init__(self):
        self.name = ''
        self.type = 'GameObject'
        self.pos = [1, 1]
        
        self.components = []



gameobjects = []

g1 = GameObject()
g1.name = 'Player'
g1.pos = [400, 200]
g1.components.append('AnimationRenderer')
gameobjects.append(g1)

g2 = GameObject()
g2.name = 'Camera'
g2.pos = [0, 0]
gameobjects.append(g2)

g3 = GameObject()
g3.name = 'obj1'
g3.pos = [64, 64]
g1.components.append('SpriteRenderer')
gameobjects.append(g3)

g4 = GameObject()
g4.name = 'obj2'
g4.pos = [128, 64]
g1.components.append('SpriteRenderer')
gameobjects.append(g4)

# 把这个游戏物体的列表转成一个全是string的dictionary字典，然后让json去保存字典
dict1 = {}

for item in gameobjects:
    dict1[item.name] = {
        'name': item.name,
        'type': item.type,
        'pos':   item.pos,
        'components' : item.components
    }

# 1. 把这个物体换成一个Json的string
towrite = json.dumps(dict1, indent=4)
print(towrite)


# 2. 打开一个文件，把这个string保存在里面
f = open('output.json', 'w')
f.write(towrite)
f.close()



# 作业1 把这个gameobjects这个逻辑写完，保存在output.json里面
# 作业2 把这个保存的逻辑应用在你的游戏物体上
#    一键保存游戏地图 （O）