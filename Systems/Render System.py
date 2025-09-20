import pygame

class RenderSystem:
	#渲染应该有屏幕
	def init__(self,game,screen):
		self.game = game
		self.screen = screen
		self.renders = []
		###完成

	#针对游戏物体添加不同的渲染系统
	def addRenderer(self,renderer):
		self.renders.append(renderer)

	#渲染坐标转换,世界坐标转屏幕坐标,如人物实现视角跟随
	def changeWorldToScreenPosition(self, pos):
		return [pos[0] - self.game.camerapos[0], pos[1] - self.game.camerapos[1]]
	
	#屏幕坐标转世界坐标，静态景物
	def changeScreenToWorldPosition(self, pos):
		return [pos[0] + self.game.camerapos[0], pos[1] + self.game.camerapos[1]]
	
	#画出来
	def draw(self):
		
		#将渲染对象进行不同的操作
		for r_对象 in self.renders:
			
			#跳过不可见的
			if not r_对象.visible:
				continue
			
			if r_对象.gameObject.moveWithCamera == True:
				pos = r_对象.gameObject.pos
			else:
				pos = self.changeWorldToScreenPosition(r_对象.gameObject.pos)
			
			#创建雪碧渲染器
			if r_对象.name == 'SpriteRenderer':
				if r_对象.sprite is not None:
					pic = r_对象.sprite.get_sprite(self.game.time // 1000)
					rect = pic.get_rect()
					rect.center = (pos[0], pos[1])
					self.screen.blit(pic, rect)

			#创建字体渲染器
			elif r_对象.name == 'FontRenderer':
				if r_对象.font is not None:
					font = pygame.font.Font(r_对象.font, r_对象.fontSize)
					text_surface = font.render(r_对象.text, True, r_对象.fontColor)
					text_rect = text_surface.get_rect()
					text_rect.center = (pos[0], pos[1])
					self.screen.blit(text_surface, text_rect)
			