import pygame
import json
from GameObject import GameObject
class EntitySystem:#9.5 22：06 ：我开始做entity system
	#由定义出来的classes生成的实例
	def __init__(self, game ):
		self.game = game
		self.gameObjects = {}

	import json
#读取json文件
	def loadObjectsFromJson(self, filename):
		import json
		with open(filename, "r", encoding="utf-8") as f:
			data = json.load(f)
			for name, obj_data in data.items():
				obj = self.CreateGameObject(obj_data)
				if obj is not None:
					self.gameObjects[name] = obj


	def saveObject(self):
		dict_saveObject = {}#设个列表用来存储object

		for item in self.gameObjects:
			dict_saveObject[item] = self.gameObjects[item].serialize()
		#把物体的名字作为键，物体的属性作为值

		towrite = json.dumps(dict_saveObject,indent=4,ensure_ascii=False)
		a = open('output.json',"w")
		a.write(towrite)
		a.close()


	def findObject(self, name):#寻找物体
		if name in self.gameObjects:
			return self.gameObjects[name]
		
		
		
		return None

		

	def CreateGameObject(self, item):	#应用实例，呼应上文
		obj = GameObject(
        	game=self.game,
        	screen=self.game.var主窗口,
        	name=item['name'],
       		pos=item['pos'],
        	components={},
        	moveWithCamera=item.get('moveWithCamera', False)
            #导入了我的gameobject
        )
		obj.components_data = item.get('components', {})  #
		return obj  #
	
	
