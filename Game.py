
#导入所需的模块
import sys
import pygame
import datetime #python里面跟时间相关的函数
import math
import json

from Systems.InputSystem import InputSystem
from Systems.ResourceSystem import ResourceSystem
from Systems.EntitySystem import EntitySystem
from Systems.RenderSystem import RenderSystem
from Systems.ScriptSystem import ScriptSystem
from Systems.PhysicsSystem import PhysicsSystem



class Game:
    
    def __init__(self):
        
        # ┌────────────────────────────────────────────────────────
        # │          初始化游戏系统
        # └────────────────────────────────────────────────────────
        # 使用pygame之前必须初化
        pygame.init()
        # 设置主屏窗口
        self.var主窗口 = pygame.display.set_mode((800,400))
        self.width = 800
        self.height = 400
        
        self.camerapos = [0, 0]
        
        # 设置窗口的标题，即游戏名称
        pygame.display.set_caption('地下城杀手')
        #caption：标题     



        # ┌────────────────────────────────────────────────────────
        # │          初始化游戏变量
        # └────────────────────────────────────────────────────────
        self.time = 0
        self.frametime = 100000000000
        #frametime：渲染一张画面的时间
        self.fps = 0.0
        #fps framepersecond：帧率，一秒能花多少张画面
        self.counter = 0

        # # 设置小窗口
        # self.var小窗口 = pygame.display.set_mode((200,200))
        # self.width小 = 200
        # self.height小 = 200
        # pygame.display.set_caption('资源管理器')
        
        # ┌────────────────────────────────────────────────────────
        # │          初始化各大系统
        # └────────────────────────────────────────────────────────
        self.inputSystem = InputSystem()
        self.entity = EntitySystem(self)
        self.renderSystem = RenderSystem(self, self.var主窗口)
        self.rs = ResourceSystem(self)
        self.scriptSystem = ScriptSystem(self)
        self.physics = PhysicsSystem(self)
        
        
        # ┌────────────────────────────────────────────────────────
        # │          加载资源
        # └────────────────────────────────────────────────────────
        self.fn加载()




    def serialize(self, obj):
        result = obj.Serialize()
        s = json.dumps(result, ensure_ascii=False, indent=4)
        f = open(f'out/{obj.name}.txt', 'w')
        f.write(s)
        f.close()
    
    def saveObject(self):
        self.entity.saveObject()


    def getFont(self, fontName):
        return self.rs.getFont(fontName)
    
    
    def getAnimation(self, animationName):
        return self.rs.getAnimation(animationName)
    
    def getSprite(self, spriteName):
        return self.rs.getSprite(spriteName)
    
    # 把渲染器添加到渲染系统里，所以等会儿可以画出来
    def addRenderer(self, renderer):
        self.renderSystem.addRenderer(renderer)
        
    def addCollider(self, collider):
        self.physics.addCollider(collider)
    
    def createObject(self, item):
        self.entity.CreateObject(item)
        
    def fn加载(self):
        
        self.rs.load()
        

        # # 一堵墙
        # self.wall1 = Wallobject(self,self.var主窗口,'wall 1',None,[500,300],200, 50)
        # self.wall1.direction = [0, 0]
        # #self.var碰撞物体.append({'object': self.wall1, 'checked': []})

    def run(self):
        while True:
            t1 = datetime.datetime.now()
            #帧数计数器：t1
            
            # ┌────────────────────────────────────────────────────────
            # │          在这里处理游戏事件
            # └────────────────────────────────────────────────────────
            # 循环获取事件，监听所有事件状态
            self.inputSystem.preUpdate()
            for event in pygame.event.get():
                # 判断用户是否点了"X"关闭按钮,并执行if代码段
                if event.type == pygame.QUIT:
                    #卸载所有模块
                    pygame.quit()
                    #终止程序，确保退出程序
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    self.inputSystem.update(event)
                if event.type == pygame.KEYUP:
                    self.inputSystem.update(event)
            
                    
            
            # ┌────────────────────────────────────────────────────────
            # │          游戏逻辑都在这里
            # └────────────────────────────────────────────────────────
            self.scriptSystem.update()
            
            self.physics.update(self.time)
            
            # ┌────────────────────────────────────────────────────────
            # │          画出游戏画面
            # └────────────────────────────────────────────────────────
            # 画出游戏内容
            # fill: 填充
            self.var主窗口.fill((0, 0, 0))
            # self.var小窗口.fill((0, 0, 0))
        
            self.renderSystem.draw()
            
            pygame.display.flip() #更新屏幕内容
            #两个渲染画板：展示A，画反面B，如果，否则就有撕裂效果。
            
            
            
            # ┌────────────────────────────────────────────────────────
            # │          统计游戏信息
            # └────────────────────────────────────────────────────────
            t2 = datetime.datetime.now()
            
            # 统计信息
            tt = t2 - t1
            #print(f'这一帧花了 {tt.microseconds} 微秒')
            self.time += tt.microseconds
            self.frametime = tt.microseconds
