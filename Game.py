import datetime
import pygame
import tkinter as tk
from Systems.ResourceSystem import ResourceSystem
from Systems.RenderSystem import RenderSystem
from Systems.EntitySystem import EntitySystem
from Systems.ScriptSystem import ScriptSystem
from Component.renderer import SpriteRenderer, AnimationRenderer, TextRenderer
from Systems.InputSystem import InputSystem
class Game:
	def __init__(self):
		pygame.init()
		self.var主窗口 = pygame.display.set_mode((400,800))
		self.time = 0
		self.dt = 0
		#命名标题，caption:标题
		pygame.display.set_caption('雷电大战-简易版 by jiale')
		self.rs = ResourceSystem(self)
		self.renderSystem = RenderSystem(self, self.var主窗口)
		self.entitysystem = EntitySystem(self)
		self.inputSystem = InputSystem()
		self.scriptSystem = ScriptSystem(self, self.var主窗口)
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
					worldPos = self.renderSystem.changeScreenToWorldPosition(pygame.mouse.get_pos())
					self.entitysystem.create蓝色子弹(worldPos)

				if event.type == pygame.MOUSEMOTION:
					# 处理鼠标移动事件
					pass

			# 2. 更新游戏物理状态
			player = self.entitysystem.gameObjects.get('Player')
			camera = self.entitysystem.gameObjects.get('Camera')
			if player is not None:
				# 使用 pygame.key.get_pressed() 以确保连续按键响应
				keys = pygame.key.get_pressed()
				speed = 400 * self.dt  # 根据帧时间调整速度 100————>400更快了
				if keys[pygame.K_w] or keys[pygame.K_UP]:
					player.pos[1] += speed
				if keys[pygame.K_s] or keys[pygame.K_DOWN]:
					player.pos[1] -= speed
				if keys[pygame.K_a] or keys[pygame.K_LEFT]:
					player.pos[0] -= speed
				if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
					player.pos[0] += speed



			# 3. 更新游戏逻辑
			self.scriptSystem.update(self.time)

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
					x.pos[1] += 800 * self.dt  # 子弹速度：随帧率变化而变化#从加到减说明屏幕坐标和世界坐标y轴方向相反了

				if x.name.startswith('Enemy'):
					x.pos[1] -= 100 * self.dt  # 敌人速度：随帧率变化而变化

				
			
			'''
			代码效率：
			如果我有5个物体 A.1 	B.2 	C.3 	D.4 	E.5
			碰撞检测:A-B A-C A-D A-E B-A B-C B-D B-E C-A C-B C-D C-E D-A D-B D-C D-E E-A E-B E-C E-D

			如果我有100个物体,碰撞检测就是 99*99 ~ 10000次,效率很低。

			优化计划：
			1. 最简单的优化：只检测玩家子弹和敌人之间的碰撞，其他不检测了。
			
			'''

			# 超出屏幕范围检测


			# for obj in self.entitysystem.gameObjects.values():
			# 	[x_min, y_min, x_max, y_max]
			# 	evaluator: 计算器，计算字符串表达式的值
			# 	if obj.pos[0] < self.map_area[0] or obj.pos[0] > self.map_area[2] or obj.pos[1] < self.map_area[1] or obj.pos[1] > self.map_area[3]:
			# 		to_remove.append(obj.id)
			# 	if obj.name.startswith('Enemy') and obj.pos[1] < 0:  # 如果敌人飞出屏幕下方也删除
			# 		to_remove.append(obj.id)
			# 		print(
			# 			f"敌人 {obj.name} 飞出屏幕，已删除"
			# 		)





			for obj in self.entitysystem.gameObjects.values():
				if "BoxCollider" in obj.components:
					collider1 = obj.components["BoxCollider"]
					for other_obj in self.entitysystem.gameObjects.values():
						if obj.id == other_obj.id:#考虑大于的情况 #之后又不考虑了
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
								# if obj.name.startswith('蓝色子弹') and other_obj.name.startswith('Enemy') or obj.name.startswith('Enemy') and other_obj.name.startswith('蓝色子弹'):
								# 		to_remove.append(obj.id)  # 子弹和敌人都要删除
								# 		to_remove.append(other_obj.id)

#					if not getattr(self, "_input_warn_printed", False):
#						print("InputSystem 调用异常：", e)
#						self._input_warn_printed = True
			# 3. 统计信息 分数 ScriptSystem
			# # 在左上角显示分数,对自己的分数进行定义

			self.entitysystem.processRemovals()  # 统一处理删除请求

			self.score = int(self.time // 10)



			#通过渲染系统画出游戏内容
			self.var主窗口.fill((0, 0, 0))
			self.renderSystem.draw()

			

			

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