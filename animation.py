import pygame 


#创建一个动画的class
class Animation:
	def __init__(self, sprite, start_x, start_y, num_of_frames, frame_width, frame_height, animation_name):
		self.sprite = sprite
		self.start_x = start_x
		self.start_y = start_y
		self.num_of_frames = num_of_frames
		self.frame_width = frame_width
		self.frame_height = frame_height
		self.animation_name = animation_name
		
		self.frames = []
		
		self.load_frames()
		
		self.current_frame = 0
		self.fps = 4

	def load_frames(self):
		# 加载每一帧的图像
		for frame_count in range(self.num_of_frames):
			frame_x = self.start_x + frame_count * self.frame_width
			frame_y = self.start_y
			
			frame = self.sprite.subsurface(pygame.Rect(
				frame_x,#开始画的点
				frame_y,
				self.frame_width,#大小
				self.frame_height
			))
			self.frames.append(frame)
			frame_count = frame_count + 1