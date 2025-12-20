import pygame






class ResourceSystem:
	def __init__(self):
		self.var贴图 = {}
		self.var字体 = {}
		self.var动画 = {}
		self.var声音 = {}

		self.var动画资源 = {}
		
	def load(self):
		# 加载贴图
		self.var贴图['人物行走'] = pygame.image.load('Resources/img/人物行走.png')
		self.var贴图['Grass'] = pygame.image.load('Resources/img/GRASS+.png')
		#加载字体
		self.var字体['爱点乾峰行书-2'] =  pygame.font.Font('Resources/font/AiDianGanFengXingShuttf-2.ttf',50)
		#加载声音
		self.var声音['背景音乐'] = pygame.mixer.Sound('Resources/sound/背景音乐.mp3')
		#加载动画资源
		import json
		with open('Resources/rs.json', "r", encoding="utf-8") as f:
			data = json.load(f)
			for name, obj_data in data.items():
				self.var动画资源[name] = obj_data
		print("资源加载完成")


		



	def getSprite(self, name):
		if name in self.var贴图:
			return self.var贴图[name]
		else:
			print(f"资源 {name} 未找到")
			return None
	#获取字体	
	def getFont(self, name):
		if name in self.var字体:
			return self.var字体[name]
		else:
			print(f"资源 {name} 未找到")
			return None
	#获取声音
	def getSound(self, name):
		if name in self.var声音:
			return self.var声音[name]
		else:
			print(f"资源 {name} 未找到")
			return None
	def getAnimationFrames(self, name,sprite_sheet, start_x=0, start_y=0, frame_width=64, frame_height=64, frame_count=3):
		if sprite_sheet in self.var贴图:
			sprite_sheet = self.var贴图[sprite_sheet]
			frames = []
			for i in range(frame_count):
				frame = sprite_sheet.subsurface((start_x + i * frame_width, start_y, frame_width, frame_height))
				frames.append(frame)
			return frames
		else:
			print(f"动画资源 {name} 未找到")
			return []