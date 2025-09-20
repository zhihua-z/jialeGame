import datetime
import pygame
import tkinter as tk
from Systems.ResourceSystem import ResourceSystem
from Systems.RenderSystem import RenderSystem

class Game:
	def __init__(self):
		pygame.init()
		self.var主窗口 = pygame.display.set_mode((600,400))
		self.time = 0
		#命名标题，caption:标题
		pygame.display.set_caption('泰拉瑞亚')
		self.rs = ResourceSystem()
		self.renderSystem = RenderSystem(self, self.var主窗口)
		self.score = 0	
		


	def load(self):
		#加载资源
		self.rs.load()

		pygame.mixer.music.load('Resources/sound/背景音乐.mp3')  # 加载背景音乐文件
		pygame.mixer.music.set_volume(0.05)  # 设置音量，范围是0.0到1.0
		pygame.mixer.music.play(-1)  # 循环播放背景音乐



	def handle_keydown(event, surface):
		if event.key == pygame.K_x:
			print("按下了x键,开始自言自语")
			root = tk.Tk()
			root.title("自言自语")
			entry = tk.Entry(root)
			root.geometry("300x100")  # 设置窗口大小
			entry.pack()
			root.mainloop()	# 让Tk窗口保持显示	
        

	def run(self):
		# 游戏主循环，保持窗口打开
		running = True

		# 主循环的目标就是每一帧都要做的事情
		# 1. 处理事件 通过event获取
		# 2. 更新游戏物理状态 通过物理系统  ScriptSystem
		# 3. 画出游戏内容 通过渲染系统
		# 5. 统计信息 分数 ScriptSystem
		# 6. 控制帧率 算时间，fps
		while running:
			t1 = datetime.datetime.now()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN:
					self.handle_keydown(event, self.var主窗口)
					# 处理键盘按下事件
				if event.type == pygame.KEYUP:
				# 处理键盘松开事件
					quit
				if event.type == pygame.MOUSEBUTTONDOWN:
					# 处理鼠标按下事件
					quit
				if event.type == pygame.MOUSEMOTION:
					# 处理鼠标移动事件
					quit

			self.renderSystem.draw()
			# var人物行走 =self.rs.getSprite('人物行走')  # 获取资源
			
			# #画出游戏内容
			# self.var主窗口.fill((0,0,0))
			# rect = var人物行走.get_rect()
			# rect.center = (300,200)
			# self.var主窗口.blit(var人物行走, rect)# 将图片绘制到窗口上
			
			# rect .center = (400, 200)  # 设置图片中心位置
			# self.var主窗口.blit(var人物行走, rect)  # 将图片绘制到窗口上

			# # 在左上角显示分数
			# font = self.rs.getFont('爱点乾峰行书-2')
			# self.score = int(self.time // 10)
			# text_surface = font.render(f'Score: {self.score}', True, (255, 255,255))  # 白色文字
			# self.var主窗口.blit(text_surface, (10, 10))  # 在窗口左上角绘制文字
			
			#更新屏幕内容   两个渲染画板：展示A，画反面B，如果，否则就有撕裂效果。
			pygame.display.flip()
			t2 = datetime.datetime.now()
			self.time += (t2-t1).microseconds/1000
			# 统计信息
			print(f'这一帧花了 {self.time} 毫秒')

	def quit(self):
		#卸载所有模块
		pygame.quit()