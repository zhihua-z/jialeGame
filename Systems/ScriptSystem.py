import pygame

from Components.GameObject import GameObject, CircleObject, Wallobject, TextObject


class ScriptSystem():
    def __init__(self, game):
        self.game = game
        self.jifen = 0
        self.running = True
        
    def addAnimationGameObject(self, name, animationName, visible, moveWithCamera, pos):
        obj = self.game.entity.CreateNewObject(name)
        obj.addComponent(
            'AnimationRenderer', 
            animationName,
            visible,
            moveWithCamera
        )
        obj.pos = pos
        
        return obj
        
    def update(self):
        jifen = self.game.entity.findObject('积分')
        camera = self.game.entity.findObject('Camera')
        player = self.game.entity.findObject('Player')
        jifen.components['TextRenderer'].text = f'积分: {self.jifen}'
        
        camera.direction = [0, 0]
        if self.running:
            if self.game.inputSystem.getKeyDown(pygame.K_a) == True:
                camera.direction[0] = -200
                player.components['AnimationRenderer'].animation = self.game.rs.getAnimation('人物走路_左')
            if self.game.inputSystem.getKeyDown(pygame.K_d) == True:
                camera.direction[0] = 200
                player.components['AnimationRenderer'].animation = self.game.rs.getAnimation('人物走路_右')
            if self.game.inputSystem.getKeyDown(pygame.K_w) == True:
                camera.direction[1] = -200
                player.components['AnimationRenderer'].animation = self.game.rs.getAnimation('人物走路_后')
            if self.game.inputSystem.getKeyDown(pygame.K_s) == True:
                camera.direction[1] = 200
                player.components['AnimationRenderer'].animation = self.game.rs.getAnimation('人物走路_前')
            if self.game.inputSystem.getKeyPress(pygame.K_f):
                newobj = self.addAnimationGameObject('obj1', '史莱姆运动2', True, False, player.getWorldPosition())
                newobj.direction = [500, 0]
            if self.game.inputSystem.getKeyPress(pygame.K_q):
                newobj = self.addAnimationGameObject('obj1', '草地1', True, False, player.getWorldPosition())
                newobj.direction = [0, 0]
        # 我们想要获得这个人物在这一帧可以走多远（路程）
        # 我的目标速度是每秒200单位（速度）
        # 我当前这一帧的时间是(self.game.frametime/1000000)秒（时间）
    
        # 计算游戏内容
        self.jifen += 1
        
        # 自动更新所有物体的位置
        for name in self.game.entity.gameObjects:
            obj = self.game.entity.gameObjects[name]
            obj.update()
            
        self.game.camerapos[0] = camera.pos[0]
        self.game.camerapos[1] = camera.pos[1]
        
        
            
            
        
        
        
        if self.running ==False:
            self.game.entity.findObject('游戏结束').visible = True