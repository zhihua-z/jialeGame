import pygame

class InputSystem:
    
    def __init__(self):
        self.keys = []
        self.previousKeys = []
        
        # [0,0,0,0,0,0...0, SPACE ! " # ....] 在前面塞32个空物体，所以K_SPACE将从第32号开始。就不需要做键值转换了
        for i in range(32):
            self.keys.append([])
        
        # 32: SPACE ~ 127 DELETE
        # 0: down, 1: up
        for i in range(pygame.K_SPACE, pygame.K_DELETE):
            self.keys.append(0)
        self.previousKeys = self.keys.copy()
    
    def preUpdate(self):
        self.previousKeys = self.keys.copy()
    
    # 更新一个按键的状态
    def update(self, event):
        if event.type == pygame.KEYDOWN:
            self.keys[event.key] = 1
        elif event.type == pygame.KEYUP:
            self.keys[event.key] = 0
    
    # 后面的 post 
    def postUpdate(self):
        pass
    
    # 获取一个按键的状态
    def getKeyDown(self, key):
        return self.keys[key] == 1
    
    def getKeyUp(self, key):
        return self.keys[key] == 0

    def getKeyRelease(self, key):
        return self.previousKeys[key] == 1 and self.keys[key] == 0
    
    def getKeyPress(self, key):
        return self.previousKeys[key] == 0 and self.keys[key] == 1
    
    