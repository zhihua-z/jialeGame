import pygame
from Components.Renderer import AnimationRenderer,SpriteRenderer, CircleRenderer, TextRenderer , RectangleRenderer

# 游戏物体
class GameObject:
    

    def __init__(self):
        self.name = ''
        self.type = 'GameObject'
        self.pos = [1, 1]
        
        self.components = {}
#serialize：序列化：把物体编码成一段可读的文字和数字
    def serialize(self):
        dict1 = {}
        dict1['name'] =  self.name
        dict1['type'] =  self.type
        dict1['pos'] =  self.pos
        
        for item in self.components:
            dict1[item] = self.components[item].serialize()


        return dict1
           



# for item in gameobjects:
#     dict1[item.name] = {
#         'name': item.name,
#         'type': item.type,
#         'pos':   item.pos,
#         'components' : item.components
#     }



    def __init__(self, game, screen, name, pos):
        self.game = game
        self.screen = screen
        self.name = name
        self.pos = pos
        self.visible = True
        
        self.type = 'None'
        self.direction = [0, 0]
        
        self.components = {
            # 保存这个游戏物体拥有的所有的组件
        }
    
    def getWorldPosition(self):
        return [self.pos[0] + self.game.camerapos[0], self.pos[1] + self.game.camerapos[1]]
        
    
    # 添加组件除了组件的名字之外，我们还会传一堆数据过来。
    # 如果是AnimationRenderer, param1会是我的动画名字
    def addComponent(self, componentName, param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, param6 = None):
        if componentName == 'AnimationRenderer':
            # param1: animation name, param2 visible, param3 moveWithCamera
            self.components['AnimationRenderer'] = AnimationRenderer(self.game, self, 'AnimationRenderer', param1, param2, param3)   
            self.game.addRenderer(self.components['AnimationRenderer'])
            #param:参数

        elif componentName == 'SpriteRenderer':
            # param1: animation name, param2 visible, param3 moveWithCamera
            self.components['SpriteRenderer'] = SpriteRenderer(self.game, self, 'SpriteRenderer', param1, param2, param3)   
            self.game.addRenderer(self.components['SpriteRenderer'])
            #param:参数

        elif componentName == 'CircleRenderer':
            # param1: radius, param2 visible, param3 moveWithCamera
            self.components['CircleRenderer'] = CircleRenderer(self.game, self, "CircleRenderer",param1, param2, param3)
            self.game.addRenderer(self.components['CircleRenderer'])
        elif componentName == 'RectangleRenderer':
             # param1: width, param2 height, param3 color, param4 visible, param5 moveWithCamera
            self.components['RectangleRenderer'] = RectangleRenderer(self.game, self, "RectangleRenderer",param1, param2, param3, param4, param5)
            self.game.addRenderer(self.components['RectangleRenderer'])
            
        elif componentName == 'TextRenderer':
            # param1: text, param2 font, param3 color, param4 visible, param5 moveWithCamera
            self.components['TextRenderer'] = TextRenderer(self.game, self, "TextRenderer", param1, param2, param3, param4, param5)
            self.game.addRenderer(self.components['TextRenderer'])
    
    def update(self):
        
        direction = [0, 0]
        direction[0] = self.direction[0] * (self.game.frametime / 1000000)
        direction[1] = self.direction[1] * (self.game.frametime / 1000000)
        
        
        # 更新 x y 位置
        if (direction[0] != 0 and direction[1] != 0):
            self.pos[0] += direction[0] / 1.414213562
            self.pos[1] += direction[1] / 1.414213562
        else:
            self.pos[0] += direction[0]
            self.pos[1] += direction[1]
        
        # # x方向的物理计算
        # if self.pos[0] + 20 > self.game.width: #x方向撞了右边
        #     self.direction[0] = -self.direction[0]
        #     self.pos[0] = self.game.width - 20
        # if self.pos[0] - 20 < 0: #x方向撞了左边
        #     self.direction[0] = -self.direction[0]
        #     self.pos[0] = 20
        
        # # y方向的物理计算
        # if self.pos[1] + 20 > self.game.height: #y方向撞了右边
        #     self.direction[1] = -self.direction[1]
        #     self.pos[1] = self.game.height - 20
        # if self.pos[1] - 20 < 0: #y方向撞了左边
        #     self.direction[1] = -self.direction[1]
        #     self.pos[1] = 20
        
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
    
    def __init__(self, game, screen, name, pos, radius):
        super().__init__(game, screen, name,  pos)
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