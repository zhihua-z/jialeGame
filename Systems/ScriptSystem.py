import pygame

from Components.GameObject import GameObject, CircleObject, Wallobject, TextObject


class ScriptSystem():
        def __init__(self, game):
            self.game = game
            self.jifen = 0
            self.running = True
            
        def update(self):
            jifen = self.game.entity.findObject('积分')
            player = self.game.entity.findObject('Player')
            jifen.components['TextRenderer'].text = f'积分: {self.jifen}'
            
            player.direction = [0, 0]
            if self.running:
                if self.game.inputSystem.getKey('A') == True:
                        player.direction[0] = -200
                        player.components['AnimationRenderer'].animation = self.game.rs.getAnimation('人物走路_左')
                if self.game.inputSystem.getKey('D') == True:
                        player.direction[0] = 200
                        player.components['AnimationRenderer'].animation = self.game.rs.getAnimation('人物走路_右')
                if self.game.inputSystem.getKey('W') == True:
                        player.direction[1] = -200
                        player.components['AnimationRenderer'].animation = self.game.rs.getAnimation('人物走路_后')
                if self.game.inputSystem.getKey('S') == True:
                        player.direction[1] = 200
                        player.components['AnimationRenderer'].animation = self.game.rs.getAnimation('人物走路_前')
       
        
            # 我们想要获得这个人物在这一帧可以走多远（路程）
            # 我的目标速度是每秒200单位（速度）
            # 我当前这一帧的时间是(self.game.frametime/1000000)秒（时间）
        
            # 计算游戏内容
            self.jifen += 1
            self.game.entity.findObject('Player').update()
            
            
            if self.running ==False:
                self.game.entity.findObject('游戏结束').visible = True