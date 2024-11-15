import pygame

# 游戏物体
class GameObject:
    
    def __init__(self, game, screen, name, sprite, pos):
        self.game = game
        self.screen = screen
        self.name = name
        self.spriteAnimation = sprite
        self.pos = pos
        self.visible = True
        
        self.type = 'None'
        self.direction = [0, 0]
        
        
    def update(self):
        
        direction = [0, 0]
        direction[0] = self.direction[0] * (self.game.frametime / 1000000)
        direction[1] = self.direction[1] * (self.game.frametime / 1000000)
        
        
        # 更新 x y 位置
        self.pos[0] += direction[0]
        self.pos[1] += direction[1]
        
        # x方向的物理计算
        if self.pos[0] + 20 > self.game.width: #x方向撞了右边
            self.direction[0] = -self.direction[0]
            self.pos[0] = self.game.width - 20
        if self.pos[0] - 20 < 0: #x方向撞了左边
            self.direction[0] = -self.direction[0]
            self.pos[0] = 20
        
        # y方向的物理计算
        if self.pos[1] + 20 > self.game.height: #y方向撞了右边
            self.direction[1] = -self.direction[1]
            self.pos[1] = self.game.height - 20
        if self.pos[1] - 20 < 0: #y方向撞了左边
            self.direction[1] = -self.direction[1]
            self.pos[1] = 20
        
    def draw(self):
        if self.spriteAnimation is not None:
            
            sp = self.spriteAnimation.get_sprite(self.game.time // 1000)
            rect = sp.get_rect()
            rect.center = (self.pos[0], self.pos[1])
            self.screen.blit(sp, rect)
    
    def Serialize(self):
        result = {
            'name': self.name,
            'animation': self.spriteAnimation.animation_name if self.spriteAnimation is not None else '',
            'pos': self.pos
        }
        
        return result
    
    def Deserialize(self):
        pass

class CircleObject(GameObject):
    
    def __init__(self, game, screen, name, sprite, pos, radius):
        super().__init__(game, screen, name, sprite, pos)
        # 半径
        self.radius = radius
        self.type = 'Circle'
    
    def draw(self):
        # 如果没有精灵动画，则绘制一个白色的圆形
        if self.spriteAnimation == None: 
            pygame.draw.circle(self.screen, (255, 255, 255), self.pos, self.radius)
        else:
            # 如果有精灵动画，则获取当前时间对应的精灵帧
            sp = self.spriteAnimation.get_sprite(self.game.time // 1000)
            # 获取精灵帧的矩形区域
            rect = sp.get_rect()
            # 设置矩形区域的中心位置为对象的位置
            rect.center = (self.pos[0], self.pos[1])
            # 将精灵帧绘制到屏幕上
            self.screen.blit(sp, rect)
            
    def Serialize(self):
        result = super().Serialize()
        result['radius'] = self.radius
        
        return result
        
    
    def Deserialize(self):
        pass

class Wallobject(GameObject):

    def __init__(self, game, screen, name, sprite, pos, width, height):
        super().__init__(game,screen,name,sprite,pos)
        #定义长和宽
        self.width = width
        self.height = height
        
        self.type = 'Rectangle'

    def draw(self):
        pygame.draw.rect(self.screen,(255,255,255), (self.pos[0], self.pos[1], self.width, self.height))
    
    def Serialize(self):
        result = super().Serialize()
        result['width'] = self.width
        result['height'] = self.height
        
        return result
        
    
    def Deserialize(self):
        pass
    
class TextObject(GameObject):
    
    def __init__(self, game, screen, name, sprite, pos, font, text, color = (255, 255, 255)):
        super().__init__(game,screen,name,sprite,pos)
        #定义长和宽
        
        self.fontName = font.name
        self.font = font.font
        self.text = text
        self.color = color
    
    def update(self, text):
        self.text = text
        
    def draw(self):
        text = self.font.render(self.text,True,self.color,(0,0,0))
        #获得显示对象的rect区域坐标
        textRect =text.get_rect()
        # 设置显示对象居中
        textRect.center = (self.pos[0], self.pos[1])
        # 将准备好的文本信息，绘制到主屏幕 Screen 上。
        self.screen.blit(text,textRect)
    
    def Serialize(self):
        result = super().Serialize()
        
        result['font'] = self.fontName
        result['text'] = self.text
        result['color'] = self.color
        
        return result
        
    
    def Deserialize(self):
        pass