import pygame

class InputSystem:
	def __init__(self):	
		self.keys = []#做一个空列表
		self.previousKeys = []#也是个空列表，保存上一帧的状态		
	
		for i in range(32):
			self.keys.append(0)#先往里填32个0，一会儿好对应按键值
		for i in range(pygame.K_SPACE, pygame.K_DELETE + 1):
			self.keys.append(0)#这个实在从space到delete的按键值范围内，全部初始化为0
		self.previousKeys = self.keys.copy()#复制一份过去的状态，以便比较每帧时的按钮状态

	def preUpdate(self):
		self.previousKeys = self.keys.copy()

	def update(self, event):
		if event.type == pygame.KEYDOWN:
			self.keys[event.key] = 1
		elif event.type == pygame.KEYUP:
			self.keys[event.key] = 0

	def getkeyDown(self, key):
		return self.keys[key] == 1	
	def getkeyUp(self, key):
		return self.keys[key] == 0