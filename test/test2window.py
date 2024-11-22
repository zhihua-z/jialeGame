import tkinter as tk
import pygame
import multiprocessing
import time
import sys

# pygame 的进程函数
def run_pygame():
    pygame.init()

    # 创建 pygame 窗口
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Pygame 窗口")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 填充颜色（示例）
        screen.fill((100, 150, 200))
        pygame.display.flip()
        
        # 防止 CPU 占用过高
        time.sleep(0.01)

    pygame.quit()
    sys.exit()

# 创建 tkinter 主窗口
root = tk.Tk()
root.title("Tkinter 窗口")

# 启动 pygame 进程的按钮
start_button = tk.Button(root, text="启动 Pygame 窗口", command=lambda: multiprocessing.Process(target=run_pygame).start())
start_button.pack()

# 启动 tkinter 主循环
root.mainloop()
