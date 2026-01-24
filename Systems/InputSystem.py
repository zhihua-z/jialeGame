import pygame

class InputSystem:
	def __init__(self):
		# 使用字典以支持任意键码（例如方向键），避免索引越界
		self.keys = {}
		self.previousKeys = {}

	def preUpdate(self):
		# 保存上一帧状态的浅拷贝
		self.previousKeys = self.keys.copy()

	def update(self, event):
		if event.type == pygame.KEYDOWN:
			self.keys[event.key] = 1
			print(f"InputSystem: KEYDOWN {event.key}")
		elif event.type == pygame.KEYUP:
			self.keys[event.key] = 0
			print(f"InputSystem: KEYUP {event.key}")

	def getkeyDown(self, key):
		return self.keys.get(key, 0) == 1

	def getkeyUp(self, key):
		return self.keys.get(key, 0) == 0

	def getKeyRelease(self, key):
		# 上一帧按下，这一帧弹起
		return self.previousKeys.get(key, 0) == 1 and self.keys.get(key, 0) == 0

	def getKeyPress(self, key):
		# 上一帧弹起，这一帧按下
		return self.previousKeys.get(key, 0) == 0 and self.keys.get(key, 0) == 1