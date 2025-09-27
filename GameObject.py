import pygame 
class GameObject:#我需要一个空的箱子让我放东西或有东西的箱子拿东西
	#由定义出来的classes生成的实例
	def __init__(self, game, screen, name, pos,components, moveWithCamera):
		self.game = game
		self.screen = screen
		self.name = name
		self.pos = pos
		self.components = components
		self.moveWithCamera = moveWithCamera

	#上为物体的属性，下位添加组件
	def addComponent(self, component):
		self.components.append(component)