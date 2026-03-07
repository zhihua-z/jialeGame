import pygame

class RenderSystem:
	#渲染应该有屏幕
	def __init__(self,game,screen):
		self.game = game
		self.screen = screen
		self.renders = []
		
		#self.numbers = []
		###完成


	def get_current_frame(self, time):
			if not self.photos:
				return None
			frame_index = int(time // 100) % len(self.photos)
			return self.photos[frame_index]

	#针对游戏物体添加不同的渲染系统
	def addRenderer(self,renderer):
		self.renders.append(renderer)

	#渲染坐标转换,世界坐标转屏幕坐标,如人物实现视角跟随
	def changeWorldToScreenPosition(self, pos):
		return [pos[0], -pos[1] + 800]
	
	#屏幕坐标转世界坐标，静态景物
	def changeScreenToWorldPosition(self, pos):
		return [pos[0], 800 - pos[1]]
	#画出来
	def draw(self):
		#将渲染对象进行不同的操作
		for r_对象 in self.renders:
			#跳过不可见的
			if not r_对象.visible:
				continue
			
			# 从世界坐标转换为屏幕坐标
			if r_对象.gameObject.moveWithCamera == True:
				pos = r_对象.gameObject.pos
			else:
				pos = self.changeWorldToScreenPosition(r_对象.gameObject.pos)
			
			#创建雪碧渲染器
			if r_对象.name == 'SpriteRenderer':
				if r_对象.sprite is not None:
					rect = r_对象.sprite.get_rect()
					rect.center = (pos[0], pos[1])
					self.screen.blit(r_对象.sprite, rect)

			#创建动画渲染器
			elif r_对象.name == 'AnimationRenderer':	
				frame = r_对象.get_current_frame(self.game.time)
				if frame is not None:
					
					rect = frame.get_rect()
					rect.center = (pos[0], pos[1]) # 设置锚点
					self.screen.blit(frame, rect)

			#创建字体渲染器
			elif r_对象.name == 'TextRenderer':
				if r_对象.font is not None:
					font = r_对象.font
					text_surface = font.render(r_对象.text+str(self.game.score), True, r_对象.fontColor)
					text_rect = text_surface.get_rect()
					text_rect.center = (pos[0], pos[1])
					self.screen.blit(text_surface, text_rect)
		
		
		# 4.1 画出（Debug）测出来的调试信息
		if self.game.showDebugInfo:
			for obj in self.game.entitysystem.gameObjects.values():
				if "BoxCollider" in obj.components:
					collider = obj.components["BoxCollider"]
					if collider.visible:
						screenPos = self.changeWorldToScreenPosition(obj.pos)
						pygame.draw.rect(self.screen, (255, 0, 0), 
						(screenPos[0] - collider.width/2, screenPos[1] - collider.height/2, collider.width, collider.height), 1)
						
			# 显示FPS
			font = self.game.rs.getFont("爱点乾峰行书-2")
			fps_text = font.render(f"FPS: {int(1/self.game.dt) if self.game.dt > 0 else 'inf'}", True, (255, 255, 255))
			self.screen.blit(fps_text, (10, 10))

		