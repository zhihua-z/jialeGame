import datetime
import pygame
import tkinter as tk
from Systems.ResourceSystem import ResourceSystem
from Systems.RenderSystem import RenderSystem
from Systems.EntitySystem import EntitySystem
from Systems.RenderSystem import SpriteRenderer, AnimationRenderer, TextRenderer
from Systems.InputSystem import InputSystem
class Game:
	def __init__(self):
		pygame.init()
		self.var主窗口 = pygame.display.set_mode((400,800))
		self.time = 0
		self.dt = 0
		#命名标题，caption:标题
		pygame.display.set_caption('雷电大战-简易版 by jiale')
		self.rs = ResourceSystem()
		self.renderSystem = RenderSystem(self, self.var主窗口)
		self.entitysystem = EntitySystem(self)
		self.inputSystem = InputSystem()
		self.camerapos = [0, 0]
		#进行地图区域的设置
		self.map_area = [-1000, -400, 1000, 3000]  # 地图区域，格式为 [x_min, y_min, x_max, y_max]
		self.showDebugInfo = True
		#展示调试信息
		self.score = 0	
		
		# 增添初始化声音系统
		pygame.mixer.init()
		pygame.mixer.set_num_channels(32)  # 设置同时播放的声音数量


	def load(self):
		#加载资源
		print("Game.load() 被调用")
		self.rs.load()
		#获取代码
		self.entitysystem.loadObjectsFromJson('Resources/level/level1.json')
		for obj in self.entitysystem.gameObjects.values():
			print("对象名：", obj.name, "组件：", obj.components_data)
			if obj is  None:
				continue
			for comp_name, comp_data in obj.components_data.items():
				print("遍历到组件：", comp_name, comp_data)
				if comp_name == "SpriteRenderer":
					from Systems.RenderSystem import SpriteRenderer
					sprite = self.rs.getSprite(comp_data["spriteName"])
					print("SpriteRenderer资源:", sprite)
					renderer = SpriteRenderer(sprite, obj, moveWithCamera=obj.moveWithCamera)
					self.renderSystem.addRenderer(renderer)
					obj.addComponent(renderer)
				elif comp_name == "AnimationRenderer":
					from Systems.RenderSystem import AnimationRenderer
					getAnimationname = comp_data["AnimationName"]
					if getAnimationname in self.rs.var动画资源:
						animation = self.rs.var动画资源[getAnimationname]
						start_x = animation.get("start_x", 0)
						start_y = animation.get("start_y", 0)
						sprite_sheet = self.rs.var贴图.get(animation.get("sprite_sheet"))
						frame_width = animation.get("frame_width", 64)
						frame_height = animation.get("frame_height", 64)
						frame_count = animation.get("frame_count", 3)
						fps = animation.get("fps", 4)
						flipX = animation.get("flipX", False)
						flipY = animation.get("flipY", False)
						
					#获取动画帧

					photos = self.rs.getAnimationFrames(comp_data["AnimationName"],sprite_sheet, start_x, start_y, frame_width, frame_height, frame_count, flipX, flipY)
					print("AnimationRenderer帧数:", len(photos))
					renderer = AnimationRenderer(photos, obj, moveWithCamera=obj.moveWithCamera, fps=fps)
					self.renderSystem.addRenderer(renderer)
					obj.addComponent(renderer)
				elif comp_name == "TextRenderer":
					from Systems.RenderSystem import TextRenderer
					font = self.rs.getFont(comp_data["font"])
					text = comp_data.get("text")
					color = comp_data.get("fontColor", (255, 255, 255))
					renderer = TextRenderer(font, text, color, obj, moveWithCamera=obj.moveWithCamera)
					self.renderSystem.addRenderer(renderer)
					obj.addComponent(renderer)
				
				elif comp_name == "BoxCollider":
					from Systems.collider import BoxCollider
					collider = BoxCollider(self, obj, comp_data.get("visible", False),comp_data.get("width",False),comp_data.get("height",False), moveWithCamera=obj.moveWithCamera)
					obj.addComponent(collider)
		

		##原来的声音加载
		# pygame.mixer.music.load('Resources/sound/背景音乐.mp3')  # 加载背景音乐文件
		#pygame.mixer.music.set_volume(0.05)  # 设置音量，范围是0.0到1.0
		#pygame.mixer.music.play(-1)  # 循环播放背景音乐
		##现在的声音加载，优化了声音系统
		背景音效 = self.rs.getSound("背景音乐")
		if 背景音效:
			背景音效.set_volume(0.05)  # 设置音量，范围是0.0到1.0
			背景音效.play()




        

	def run(self):
		# 游戏主循环，保持窗口打开
		running = True

		# 主循环的目标就是每一帧都要做的事情
		# 1. 处理事件 通过event获取
		# 2. 更新游戏物理状态 通过物理系统  ScriptSystem
		# 3. 画出游戏内容 通过渲染系统 	————>	# 3. 统计信息 分数 ScriptSystem
		# 5. 统计信息 分数 ScriptSystem# ---->4. 画出游戏内容 通过渲染系统
		# 6. 控制帧率 算时间，fps# ----->5. 控制帧率 算时间，fps
		while running:
			#运行preupdate
			t1 = datetime.datetime.now()
			self.inputSystem.preUpdate()


			# 1. 处理事件
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN:
					self.inputSystem.update(event)
					# 处理键盘按下事件
				if event.type == pygame.KEYUP:
				# 处理键盘松开事件,用inputsystem.update(event)更好
					self.inputSystem.update(event)
					pass
				if event.type == pygame.MOUSEBUTTONDOWN:
					# 处理鼠标按下事件
					pass
				if event.type == pygame.MOUSEMOTION:
					# 处理鼠标移动事件
					pass

			# 2. 更新游戏物理状态
			player = self.entitysystem.gameObjects.get('Player')
			if player is not None:
				# 使用 pygame.key.get_pressed() 以确保连续按键响应
				keys = pygame.key.get_pressed()
				speed = 400 * self.dt  # 根据帧时间调整速度 100————>400更快了
				if keys[pygame.K_w] or keys[pygame.K_UP]:
					player.pos[1] -= speed
				if keys[pygame.K_s] or keys[pygame.K_DOWN]:
					player.pos[1] += speed
				if keys[pygame.K_a] or keys[pygame.K_LEFT]:
					player.pos[0] -= speed
				if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
					player.pos[0] += speed
			if self.inputSystem.getKeyPress(pygame.K_j) :
				# 生成蓝色子弹
				bullet = self.entitysystem.create蓝色子弹([player.pos[0], player.pos[1]-20])
				#在生成子弹的时候播放射击音效
				射击音效 = self.rs.getSound("射击")
				if 射击音效:
					射击音效.set_volume(0.1)  # 设置音量，范围是0.0到1.0
					射击音效.play()
			if self.inputSystem.getKeyPress(pygame.K_F3) :
				self.showDebugInfo = not self.showDebugInfo
				
			for x in self.entitysystem.gameObjects.values():
				if x.name.startswith('蓝色子弹'):
					x.pos[1] -= 800 * self.dt  # 子弹速度：随帧率变化而变化

				
			
			'''
			代码效率：
			如果我有5个物体 A.1 	B.2 	C.3 	D.4 	E.5
			碰撞检测:A-B A-C A-D A-E B-A B-C B-D B-E C-A C-B C-D C-E D-A D-B D-C D-E E-A E-B E-C E-D

			如果我有100个物体,碰撞检测就是 99*99 ~ 10000次,效率很低。

			优化计划：
			1. 最简单的优化：只检测玩家子弹和敌人之间的碰撞，其他不检测了。
			
			'''

			# 超出屏幕范围检测
			# post delete 延后删除: 先把所有要删除的对象ID记录下来，等遍历结束后再统一删除，避免在遍历过程中修改字典导致的错误。

			to_remove = []

			for obj in self.entitysystem.gameObjects.values():
				# [x_min, y_min, x_max, y_max]
				# evaluator: 计算器，计算字符串表达式的值
				if obj.pos[0] < self.map_area[0] or obj.pos[0] > self.map_area[2] or obj.pos[1] < self.map_area[1] or obj.pos[1] > self.map_area[3]:
					to_remove.append(obj.id)

			# 执行删除操作
			for obj_id in to_remove:
				self.entitysystem.removeObject(obj_id)	





			for obj in self.entitysystem.gameObjects.values():
				if "BoxCollider" in obj.components:
					collider1 = obj.components["BoxCollider"]
					for other_obj in self.entitysystem.gameObjects.values():
						if obj.id >= other_obj.id:#考虑大于的情况
							continue
						#关于时间复杂度的一些提前学习
						# 计算复杂度 
						# O(2^n) : 指数增长  
						# O(n^2) : 平方增长 100个物体就是10000次检测
						# O(n log n) : 线性对数增长 100个物体就是100*7次检测
						# O(n) : 线性增长 100个物体就是100次检测
						# O(log n) : 对数增长 100个物体就是7次检测
						# O(1) : 常数时间 100个物体还是1次检测


						# O(n^2) -> O(n) 通过只检测玩家子弹和敌人之间的碰撞，其他不检测了。
						if obj.name.startswith('蓝色子弹') and other_obj.name.startswith('蓝色子弹'):
							continue  # 子弹之间不检测碰撞

						# O(n) -> O(n)
						if obj.name.startswith('蓝色子弹') and other_obj.name.startswith('Player'):
							continue  # 子弹只检测与敌人的碰撞
						if obj.name.startswith('Player') and other_obj.name.startswith('蓝色子弹'):
							continue  # 玩家只检测与子弹的碰撞


						if "BoxCollider" in other_obj.components:
							collider2 = other_obj.components["BoxCollider"]



							# 目标：在这个真正的检测开始之前，尽可能地排除掉不可能碰撞的情况，减少checkCollision的调用次数。
							if collider1.checkCollision(collider2):
								print(f"碰撞检测：{obj.name} 碰到了 {other_obj.name}")

#					if not getattr(self, "_input_warn_printed", False):
#						print("InputSystem 调用异常：", e)
#						self._input_warn_printed = True
			# 3. 统计信息 分数 ScriptSystem
			# # 在左上角显示分数,对自己的分数进行定义
			self.score = int(self.time // 10)
				


			#通过渲染系统画出游戏内容
			self.var主窗口.fill((0, 0, 0))
			self.renderSystem.draw()
			
			# 4.1 画出（Debug）测出来的调试信息
			if self.showDebugInfo:
				# 
				player = self.entitysystem.gameObjects.get('Player')
				##玩家
				#if player is not None:
				#	player_box = player.components.get("BoxCollider")
				#	if player_box and player_box.visible:
				#		pygame.draw.rect(self.var主窗口, (255, 0, 0), 
				#	   (player.pos[0]-player_box.width/2 - self.camerapos[0], player.pos[1]-player_box.height/2 - self.camerapos[1], 
		 		#		player_box.width, player_box.height), 1)
			
				##敌人
				#enemy = self.entitysystem.gameObjects.get('Enemy')
				#if enemy is not None:
				#	enemy_box = enemy.components.get("BoxCollider")
				#	if enemy_box and enemy_box.visible:
				#		pygame.draw.rect(self.var主窗口, (255, 0, 0), 
				#	   (enemy.pos[0]-enemy_box.width/2 - self.camerapos[0], enemy.pos[1]-enemy_box.height/2 - self.camerapos[1], 
		 		#		enemy_box.width, enemy_box.height), 1)
				 
				for obj in self.entitysystem.gameObjects.values():
					if "BoxCollider" in obj.components:
						collider = obj.components["BoxCollider"]
						if collider.visible:
							pygame.draw.rect(self.var主窗口, (255, 0, 0), 
											(obj.pos[0]-collider.width/2 - self.camerapos[0], obj.pos[1]-collider.height/2 - self.camerapos[1], 
												collider.width, collider.height), 1)
							
				# 显示FPS
				font = self.rs.getFont("爱点乾峰行书-2")
				fps_text = font.render(f"FPS: {int(1/self.dt) if self.dt > 0 else 'inf'}", True, (255, 255, 255))
				self.var主窗口.blit(fps_text, (10, 10))


			

			#更新屏幕内容   两个渲染画板：展示A，画反面B，如果，否则就有撕裂效果。
			pygame.display.flip()

			#对所画帧进行时间控制

			t2 = datetime.datetime.now()
			self.time += (t2-t1).microseconds/1000
			self.dt = (t2 - t1).microseconds / 1000000.0
			# 统计信息

	def quit(self):
		#卸载所有模块
		pygame.quit()