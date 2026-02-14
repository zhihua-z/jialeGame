import pygame
import json
from GameObject import GameObject
class EntitySystem:#9.5 22：06 ：我开始做entity system
	#由定义出来的classes生成的实例
	def __init__(self, game ):
		self.game = game
		self.gameObjects = {}
		self.counter = 0


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

	# 每呼叫一次，计数器+1
	def GenID(self):
		self.counter += 1
		return self.counter

	def saveObject(self):
		dict_saveObject = {}#设个列表用来存储object

		for item in self.gameObjects:
			dict_saveObject[item] = self.gameObjects[item].serialize()
		#把物体的名字作为键，物体的属性作为值

		towrite = json.dumps(dict_saveObject,indent=4,ensure_ascii=False)
		a = open('output.json',"w")
		a.write(towrite)
		a.close()

	# 传入一个对象ID，删除这个对象
	def removeObject(self, obj_id):
		for name, obj in list(self.gameObjects.items()):
			if obj.id == obj_id:
				# delete ： 删除

				# 先清除全部的组件
				for component in obj.components.values():
					component.cleanup()  # 调用组件的清理方法，释放资源等

				# 再删除这个对象
				del self.gameObjects[name]
				print(f"对象 {name} 已被移除")
				return
		print(f"对象 ID {obj_id} 未找到，无法移除")

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
	
	# 游戏对象生成都在这里
	def create蓝色子弹(self, pos):
		import uuid
		
		bulletname = '蓝色子弹' + str(uuid.uuid4())
		bullet = GameObject(
			game=self.game,
			screen=self.game.var主窗口,
			name=bulletname,
	   		pos=pos,
			components={},
			moveWithCamera=False
		)
		#添加组件
		from Systems.RenderSystem import AnimationRenderer
		
		# 添加动画渲染组件
		animation = self.game.rs.var动画资源.get("蓝色子弹")
		frames = self.game.rs.getAnimationFramesByAnimation(animation)
		renderer = AnimationRenderer(frames, bullet, moveWithCamera=False)
		self.game.renderSystem.addRenderer(renderer)
		self.gameObjects[bulletname] = bullet
		bullet.addComponent(renderer)

		# 添加box collider
		from Systems.collider import BoxCollider
		collider = BoxCollider(self.game, bullet, visible=False, width=16, height=20, moveWithCamera=False)
		bullet.addComponent(collider)

		return bullet
	
