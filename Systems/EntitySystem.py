import pygame
import json

from Component.renderer import SpriteRenderer, AnimationRenderer, TextRenderer
from Component.collider import BoxCollider

from Scripts.EnemyScript import EnemyScript
from Scripts.bullet自杀 import Bullet自杀Script


from GameObject import GameObject
from Scripts.玩家子弹击杀 import 玩家子弹击杀
class EntitySystem:#9.5 22：06 ：我开始做entity system
	#由定义出来的classes生成的实例
	def __init__(self, game ):
		self.game = game
		self.gameObjects = {}
		self.to_remove = []
		self.counter = 0#初始化计数器
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

				print("对象名：", obj.name, "组件：", obj.components_data)
				if obj is  None:
					continue
				for comp_name, comp_data in obj.components_data.items():
					print("遍历到组件：", comp_name, comp_data)
					if comp_name == "SpriteRenderer":
						sprite = self.game.rs.getSprite(comp_data["spriteName"])
						print("SpriteRenderer资源:", sprite)
						renderer = SpriteRenderer(sprite, obj, moveWithCamera=obj.moveWithCamera)
						self.game.renderSystem.addRenderer(renderer)
						obj.addComponent(renderer)
					elif comp_name == "AnimationRenderer":
						getAnimationname = comp_data["AnimationName"]
						if getAnimationname in self.game.rs.var动画资源:
							animation = self.game.rs.var动画资源[getAnimationname]
							start_x = animation.get("start_x", 0)
							start_y = animation.get("start_y", 0)
							sprite_sheet = self.game.rs.var贴图.get(animation.get("sprite_sheet"))
							frame_width = animation.get("frame_width", 64)
							frame_height = animation.get("frame_height", 64)
							frame_count = animation.get("frame_count", 3)
							fps = animation.get("fps", 4)
							flipX = animation.get("flipX", False)
							flipY = animation.get("flipY", False)
							
						#获取动画帧

						photos = self.game.rs.getAnimationFrames(comp_data["AnimationName"],sprite_sheet, start_x, start_y, frame_width, frame_height, frame_count, flipX, flipY)
						print("AnimationRenderer帧数:", len(photos))
						renderer = AnimationRenderer(photos, obj, moveWithCamera=obj.moveWithCamera, fps=fps)
						self.game.renderSystem.addRenderer(renderer)
						obj.addComponent(renderer)
					elif comp_name == "TextRenderer":
						font = self.game.rs.getFont(comp_data["font"])
						text = comp_data.get("text")
						color = comp_data.get("fontColor", (255, 255, 255))
						renderer = TextRenderer(font, text, color, obj, moveWithCamera=obj.moveWithCamera)
						self.game.renderSystem.addRenderer(renderer)
						obj.addComponent(renderer)
					
					elif comp_name == "BoxCollider":
						collider = BoxCollider(self.game, obj, comp_data.get("visible", False),comp_data.get("width",False),comp_data.get("height",False), moveWithCamera=obj.moveWithCamera)
						obj.addComponent(collider)
					elif comp_name == "EnemyScript":
						life = comp_data.get("life", 20)
						enemy_script = EnemyScript(self.game, obj, "EnemyScript", life)
						self.game.scriptSystem.addScript(enemy_script)
						obj.addComponent(enemy_script)
					elif comp_name == "Bullet自杀Script":
						bullet_script = Bullet自杀Script(self.game, obj, "Bullet自杀Script")
						self.game.scriptSystem.addScript(bullet_script)
						obj.addComponent(bullet_script)
					elif comp_name == "玩家子弹击杀":
						玩家子弹击杀_script = 玩家子弹击杀(self.game, obj, "玩家子弹击杀")
						self.game.scriptSystem.addScript(玩家子弹击杀_script)
						obj.addComponent(玩家子弹击杀_script)

					# 方式1：直接在这里根据组件名称创建对应的组件实例，并添加到对象上。
					# 方式2(业界最常用)：factory模式：创建一个组件工厂，根据组件名称动态创建组件实例，这样就不需要在这里写死每种组件的创建逻辑了，后续添加新组件也更方便。
					# 方式3（第二常用）：反射（Reflection）：如果使用的编程语言支持反射，可以直接根据组件名称动态找到对应的组件类并创建实例，这样就完全不需要在这里写死每种组件的创建逻辑了，后续添加新组件也更方便。
	def GenID(self):
		self.counter += 1
		return self.counter


	def saveObject(self):
		dict_saveObject = {}#设个列表用来存储object
			# 每呼叫一次，计数器+1

		for item in self.gameObjects:
			dict_saveObject[item] = self.gameObjects[item].serialize()
		#把物体的名字作为键，物体的属性作为值

		towrite = json.dumps(dict_saveObject,indent=4,ensure_ascii=False)
		a = open('output.json',"w")
		a.write(towrite)
		a.close()

	# 传入一个对象ID，删除这个对象
	# 注意：在遍历gameObjects时，不要直接删除对象，而是把要删除的对象ID记录下来，等遍历结束后再统一删除，避免在遍历过程中修改字典导致的错误。
	def remove(self, obj_id):
		self.to_remove.append(obj_id)
	
	# 处理删除请求，在合适的时机调用这个方法来统一删除对象，避免在遍历过程中修改字典导致的错误。
	def processRemovals(self):
		for obj_id in self.to_remove:
			self.removeObject(obj_id)
		self.to_remove.clear()

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
		
		# 添加动画渲染组件
		animation = self.game.rs.var动画资源.get("蓝色子弹")
		frames = self.game.rs.getAnimationFramesByAnimation(animation)
		renderer = AnimationRenderer(frames, bullet, moveWithCamera=False)
		self.game.renderSystem.addRenderer(renderer)
		self.gameObjects[bulletname] = bullet
		bullet.addComponent(renderer)
		
		# 添加box collider
		from Component.collider import BoxCollider
		collider = BoxCollider(self.game, bullet, visible=True, width=16, height=26, moveWithCamera=False)
		bullet.addComponent(collider)
		
	
		# 添加脚本
		bullet_script = Bullet自杀Script(self.game, bullet, "Bullet自杀Script")
		self.game.scriptSystem.addScript(bullet_script)
		bullet.addComponent(bullet_script)

		玩家子弹击杀_script = 玩家子弹击杀(self.game, bullet, "玩家子弹击杀")
		self.game.scriptSystem.addScript(玩家子弹击杀_script)
		bullet.addComponent(玩家子弹击杀_script)

		return bullet
