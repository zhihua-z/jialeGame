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
		self.var主窗口 = pygame.display.set_mode((600,400))
		self.time = 0
		#命名标题，caption:标题
		pygame.display.set_caption('泰拉瑞亚')
		self.rs = ResourceSystem()
		self.renderSystem = RenderSystem(self, self.var主窗口)
		self.entitysystem = EntitySystem(self)
		self.inputSystem = InputSystem()
		self.camerapos = [0, 0]
		

		self.score = 0	
		


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
					photos = self.rs.getAnimationFrames(comp_data["AnimationName"])
					print("AnimationRenderer帧数:", len(photos))
					renderer = AnimationRenderer(photos, obj, moveWithCamera=obj.moveWithCamera)
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
		

		#加载背景音乐
		pygame.mixer.music.load('Resources/sound/背景音乐.mp3')  # 加载背景音乐文件
		pygame.mixer.music.set_volume(0.05)  # 设置音量，范围是0.0到1.0
		pygame.mixer.music.play(-1)  # 循环播放背景音乐




        

	def run(self):
		# 游戏主循环，保持窗口打开
		running = True

		# 主循环的目标就是每一帧都要做的事情
		# 1. 处理事件 通过event获取
		# 2. 更新游戏物理状态 通过物理系统  ScriptSystem
		# 3. 画出游戏内容 通过渲染系统
		# 5. 统计信息 分数 ScriptSystem
		# 6. 控制帧率 算时间，fps
		while running:
			#运行preupdate
			t1 = datetime.datetime.now()
			self.inputSystem.preUpdate()

			for event in pygame.event.get():
				
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN:
					self.inputSystem.update(event)
					# 处理键盘按下事件
				if event.type == pygame.KEYUP:
				# 处理键盘松开事件,用inputsystem.update(event)更好
					quit
				if event.type == pygame.MOUSEBUTTONDOWN:
					# 处理鼠标按下事件
					quit
				if event.type == pygame.MOUSEMOTION:
					# 处理鼠标移动事件
					quit
				player = self.entitysystem.gameObjects.get('Player')
				if self.inputSystem.getkeyDown(pygame.K_w) :
					player.pos[1] -= 5
				if self.inputSystem.getkeyDown(pygame.K_s) :
					player.pos[1] += 5
				if self.inputSystem.getkeyDown(pygame.K_a) :
					player.pos[0] -= 5
				if self.inputSystem.getkeyDown(pygame.K_d) :
					player.pos[0] += 5


				
#					if not getattr(self, "_input_warn_printed", False):
#						print("InputSystem 调用异常：", e)
#						self._input_warn_printed = True
				
			self.var主窗口.fill((0, 0, 0))
			self.renderSystem.draw()
			# var人物行走 =self.rs.getSprite('人物行走')  # 获取资源
			
			# #画出游戏内容
			# self.var主窗口.fill((0,0,0))
			# rect = var人物行走.get_rect()
			# rect.center = (300,200)
			# self.var主窗口.blit(var人物行走, rect)# 将图片绘制到窗口上
			
			# rect .center = (400, 200)  # 设置图片中心位置
			# self.var主窗口.blit(var人物行走, rect)  # 将图片绘制到窗口上

			# # 在左上角显示分数
			
			self.score = int(self.time // 10)
			
			# self.var主窗口.blit(text_surface, (10, 10))  # 在窗口左上角绘制文字
			

			#如果inputsystem有变化，就更新,"w""a""s""d"控制移动,以此来进行x,y坐标的变化



			

			#更新屏幕内容   两个渲染画板：展示A，画反面B，如果，否则就有撕裂效果。
			pygame.display.flip()
			t2 = datetime.datetime.now()
			self.time += (t2-t1).microseconds/1000
			# 统计信息
			print(f'这一帧花了 {self.time} 毫秒')

	def quit(self):
		#卸载所有模块
		pygame.quit()