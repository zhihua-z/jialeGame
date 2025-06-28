import pygame

from Components.GameObject import GameObject, CircleObject, Wallobject, TextObject


class ScriptSystem():
    def __init__(self, game):
        self.game = game
        self.jifen = 0
        self.running = True
        
    def addAnimationGameObject(self, name, animationName, visible, moveWithCamera, pos):
        newpos = [pos[0] // 64 *  64+32,pos[1] // 64 *  64+32]
    

        obj = self.game.entity.CreateNewObject(name,newpos)
        self.game.counter += 1

        obj.addComponent(
            'AnimationRenderer', 
            animationName,
            visible
        )
        obj.addComponent(
            'BoxCollider', 
            visible
        )
        return obj
        
    def update(self):
        jifen = self.game.entity.findObject('积分')
        camera = self.game.entity.findObject('Camera')
        player = self.game.entity.findObject('Player')
        jifen.components['TextRenderer'].text = f'积分: {self.jifen}'
        
        camera.direction = [0, 0]
        if self.running:
            playerfacingdirection = [0,-600]
            if self.game.inputSystem.getKeyDown(pygame.K_a) == True:
                camera.direction[0] = -200
                playerfacingdirection[0] = -600
                playerfacingdirection[1] = 0
                player.components['AnimationRenderer'].animation = self.game.rs.getAnimation('人物走路_左')
            if self.game.inputSystem.getKeyDown(pygame.K_d) == True:
                camera.direction[0] = 200
                playerfacingdirection[0] = 600
                playerfacingdirection[1] = 0
                player.components['AnimationRenderer'].animation = self.game.rs.getAnimation('人物走路_右')
            if self.game.inputSystem.getKeyDown(pygame.K_w) == True:
                camera.direction[1] = -200
                playerfacingdirection[1] = -600
                playerfacingdirection[0] = 0
                player.components['AnimationRenderer'].animation = self.game.rs.getAnimation('人物走路_后')
            if self.game.inputSystem.getKeyDown(pygame.K_s) == True:
                camera.direction[1] = 200
                playerfacingdirection[1] = 600
                playerfacingdirection[0] = 0
                player.components['AnimationRenderer'].animation = self.game.rs.getAnimation('人物走路_前')
            if self.game.inputSystem.getKeyPress(pygame.K_f):
                self.addAnimationGameObject(f'obj{self.game.counter}', '史莱姆运动2', True, False, player.getWorldPosition())
                self.game.counter = self.game.counter + 1
            if self.game.inputSystem.getKeyPress(pygame.K_q):
                self.addAnimationGameObject(f'obj{self.game.counter}', '草地1', True, False, player.getWorldPosition())
   
                self.game.counter = self.game.counter + 1
            if self.game.inputSystem.getKeyPress(pygame.K_e):
                self.addAnimationGameObject(f'obj{self.game.counter}', '草地2', True, False, player.getWorldPosition())

                self.game.counter = self.game.counter + 1
            if self.game.inputSystem.getKeyPress(pygame.K_x):
                self.addAnimationGameObject(f'obj{self.game.counter}', '棕色的草', True, False, player.getWorldPosition())

                self.game.counter = self.game.counter + 1

            if self.game.inputSystem.getKeyPress(pygame.K_g):
                self.game.saveObject()

            if self.game.inputSystem.getKeyPress(pygame.K_r):
                
                r = self.addAnimationGameObject(f'obj{self.game.counter}','子弹',True,False,player.getWorldPosition())
                r.direction = playerfacingdirection.copy()
        # 我们想要获得这个人物在这一帧可以走多远（路程）
        # 我的目标速度是每秒200单位（速度）
        # 我当前这一帧的时间是(self.game.frametime/1000000)秒（时间）
    
        # 计算游戏内容
        self.jifen += 1
            
        self.game.camerapos[0] = camera.pos[0]
        self.game.camerapos[1] = camera.pos[1]
        
        
            
            
        
        
        
        if self.running ==False:
            self.game.entity.findObject('游戏结束').visible = True