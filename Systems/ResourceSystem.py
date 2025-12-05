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
		self.var动画资源['Grass'] = pygame.image.load('Resources/img/GRASS+.png')
		#加载字体
		self.var字体['爱点乾峰行书-2'] =  pygame.font.Font('Resources/font/AiDianGanFengXingShuttf-2.ttf',50)
		#加载声音
		self.var声音['背景音乐'] = pygame.mixer.Sound('Resources/sound/背景音乐.mp3')
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
	def getAnimationFrames(self, name):
		if name in self.var动画资源:
			sprite_sheet = self.var动画资源[name]
			frame_width = sprite_sheet.get_width() // 25  # 假设每行有25帧
			frame_height = sprite_sheet.get_height() // 14
			frames = []
			for i in range(25):
				frame = sprite_sheet.subsurface((i * frame_width, 0, frame_width, frame_height))
				frames.append(frame)
			return frames
		else:
			print(f"动画资源 {name} 未找到")
			return []