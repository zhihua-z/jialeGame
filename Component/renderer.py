from Component.component import Component

class Renderer(Component):
	def __init__(self, game, gameObject, name):
		super().__init__(game, gameObject, name)
		
	def cleanup(self):
		if self in self.game.renderSystem.renders:
			self.game.renderSystem.renders.remove(self)

class SpriteRenderer(Renderer):
		def __init__(self, sprite, gameObject, moveWithCamera=False):
			super().__init__(gameObject.game, gameObject, "SpriteRenderer")
			self.sprite = sprite
			self.gameObject = gameObject
			self.moveWithCamera = moveWithCamera
			self.visible = True

class AnimationRenderer(Renderer):
		def __init__(self, photos, gameObject, moveWithCamera=False,fps = 4):
			super().__init__(gameObject.game, gameObject, "AnimationRenderer")
			self.photos = photos  # 动画帧列表
			self.gameObject = gameObject
			self.moveWithCamera = moveWithCamera
			self.visible = True
			self.fps = fps

		def get_current_frame(self, time):
			if not self.photos:
				return None
			frame_time_ms = 1000 / max(self.fps, 1)
			frame_index = int(time // frame_time_ms) % len(self.photos)
			return self.photos[frame_index]
		
class TextRenderer(Renderer):
		def __init__(self, font, text, fontColor, gameObject, moveWithCamera=False):
			super().__init__(gameObject.game, gameObject, "TextRenderer")
			self.font = font  # 字体对象
			self.text = text  # 要渲染的文本
			self.fontColor = fontColor  # 字体颜色
			self.gameObject = gameObject
			self.moveWithCamera = moveWithCamera
			self.visible = True