import pygame

class InputSystem:
    
    def __init__(self):
    
        self.keyA = False
        self.keyD = False
        self.keyW = False
        self.keyS = False
        
    # 更新一个按键的状态
    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.keyA = True
            elif event.key == pygame.K_d:
                self.keyD = True
            elif event.key == pygame.K_w:
                self.keyW = True
            elif event.key == pygame.K_s:
                self.keyS = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.keyA = False
            if event.key == pygame.K_d:
                self.keyD = False
            if event.key == pygame.K_w:
                self.keyW = False
            if event.key == pygame.K_s:
                self.keyS = False
    
    # 获取一个按键的状态
    def getKey(self, key):
        if key == 'A':
            return self.keyA
        elif key == 'D':
            return self.keyD
        elif key == 'W':
            return self.keyW
        elif key == 'S':
            return self.keyS