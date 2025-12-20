import pygame






class ResourceSystem:
	def __init__(self):
		self.var贴图 = {}
		self.var字体 = {}
		self.var动画 = {}
		self.var声音 = {}

		self.var动画资源 = {}
		
	def load(self):
		import json
		with open('Resources/rs.json', "r", encoding="utf-8") as f:
			data = json.load(f)
			for name, obj_data in data.items():
				if obj_data.get("type") == "Animation":
					self.var动画资源[name] = obj_data
				elif obj_data.get("type") == "Sprite":
					self.var贴图[name] = pygame.image.load(obj_data.get("file_path"))
				elif obj_data.get("type") == "Sound":
					self.var声音[name] = pygame.mixer.Sound(obj_data.get("file_path"))
				elif obj_data.get("type") == "Font":
					self.var字体[name] = pygame.font.Font(obj_data.get("file_path"), obj_data.get("size", 24))
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
	
	def getAnimationFramesByAnimation(self, animation):
		frames = []
		sprite_sheet = self.var贴图.get(animation.get("sprite_sheet"))
		for i in range(animation["frame_count"]):
			frame = sprite_sheet.subsurface((animation["start_x"] + i * animation["frame_width"], animation["start_y"], animation["frame_width"], animation["frame_height"]))
			if animation["flipX"] or animation["flipY"]:
				frame = pygame.transform.flip(frame, animation["flipX"], animation["flipY"])
			frames.append(frame)
		return frames

	def getAnimationFrames(self, name,sprite_sheet, start_x=0, start_y=0, frame_width=64, frame_height=64, frame_count=3, flipX=False, flipY=False):
		frames = []
		for i in range(frame_count):
			frame = sprite_sheet.subsurface((start_x + i * frame_width, start_y, frame_width, frame_height))
			if flipX or flipY:
				frame = pygame.transform.flip(frame, flipX, flipY)
			frames.append(frame)
		return frames