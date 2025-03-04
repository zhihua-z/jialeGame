'''
资源系统：包含字体，图像，动画

'''

import pygame
from Components.SpriteAnimation import AnimatedSprite
from Components.Font import Font
import json




class ResourceSystem:
    
    def __init__(self, game):
        self.game = game
        
        # 我们会有一些列表来储存不同的资源
        # 游戏要获取一个资源的话，只要呼叫getFont(), getSprite(), getAnimation()
        self.var字体 = {}
        self.var贴图 = {}
        self.var动画 = {}
        
        # 内部变量，不给外面使用
        self.var动画资源 = {}
        
    def load(self):
        
        # 引入字体类型
        self.var字体['三极榜楷'] = Font('三极榜楷', pygame.font.Font('Resources/font/SanJiBangKaiJianTi-2.ttf',50))
        self.var字体['三极榜楷_24'] = Font('三极榜楷', pygame.font.Font('Resources/font/SanJiBangKaiJianTi-2.ttf', 24))
        self.var字体['爱点乾峰行书-2'] = Font('爱点乾峰行书-2', pygame.font.Font('Resources/font/AiDianGanFengXingShuttf-2.ttf',50))
        self.var字体['龙楷24'] = Font('龙楷24', pygame.font.Font('Resources/font/longkai.ttf',24))
        
        # 加载贴图
        self.var动画资源['人物行走'] = pygame.image.load('Resources/img/walk.png')
        self.var动画资源['史莱姆大'] = pygame.image.load('Resources/img/shilaimu_da.png')
        self.var动画资源['史莱姆中'] = pygame.image.load('Resources/img/shilaimu_zhong.png')
        self.var动画资源['史莱姆小'] = pygame.image.load('Resources/img/shilaimu_xiao.png')
        self.var动画资源['游戏贴图'] = pygame.image.load('Resources/img/GRASS+.png')
        self.var动画资源['游戏贴图1'] = pygame.image.load('Resources/img/minecraft.png')
        
        
        # 加载游戏资源贴图
        self.var动画['草地1'] = AnimatedSprite(self.var动画资源['游戏贴图'], 0, 0, 1, 64, 64, '草地1')
        self.var动画['草地2'] = AnimatedSprite(self.var动画资源['游戏贴图'], 64, 0, 1, 64, 64, '草地2')
        self.var动画['棕色的草'] = AnimatedSprite(self.var动画资源['游戏贴图'], 640, 0, 3, 64, 64, '棕色的草')
        self.var动画['草原'] = AnimatedSprite(self.var动画资源['游戏贴图'], 640, 0, 3, 64, 640, '草原')
        self.var动画['圆石'] = AnimatedSprite(self.var动画资源['游戏贴图1'], 448, 0, 1, 64,64, '圆石')


        
        # 转化成一个精灵动画
        #分割 0 0 4 52 52 ；0 0是起始点；4是帧数；52 52是帧的大小
        self.var动画['人物走路_前'] = AnimatedSprite(self.var动画资源['人物行走'], 0, 0, 4, 52, 52, '人物走路_前')
        self.var动画['人物走路_后'] = AnimatedSprite(self.var动画资源['人物行走'], 0, 156, 4, 52, 52, '人物走路_后')
        self.var动画['人物走路_左'] = AnimatedSprite(self.var动画资源['人物行走'], 0, 52, 4, 52, 52, '人物走路_左')
        self.var动画['人物走路_右'] = AnimatedSprite(self.var动画资源['人物行走'], 0, 104, 4, 52, 52, '人物走路_右')
        self.var动画['史莱姆运动1']  = AnimatedSprite(self.var动画资源['史莱姆大'], 0, 0, 6, 210, 64, '史莱姆运动大') 
        self.var动画['史莱姆运动2']  = AnimatedSprite(self.var动画资源['史莱姆中'], 0, 0, 6, 105, 32, '史莱姆运动中') 
        self.var动画['史莱姆运动3']  = AnimatedSprite(self.var动画资源['史莱姆小'], 0, 0, 6, 52, 16, '史莱姆运动小')
        
        
        # 加载游戏关卡
        data = open('level1.json', 'r').read()
        self.level1 = json.loads(data)
        
        # 从读到的文件里创建出来这些游戏物体
        for item in self.level1:
            self.game.createObject(item)
        
        
    def getFont(self, fontName):
        if fontName in self.var字体:
            return self.var字体[fontName]
        else:
            return None
    
    def getSprite(self, spriteName):
        if spriteName in self.var贴图:
            return self.var贴图[spriteName]
        else:
            return None
    
    def getAnimation(self, animationName):
        if animationName in self.var动画:
            return self.var动画[animationName]
        else:
            return None
        #***