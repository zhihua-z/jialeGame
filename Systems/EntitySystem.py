import json

from GameObject import GameObject, CircleObject, Wallobject, TextObject
'''
Entity: 实体，一个物体 


'''
class EntitySystem:
    #由定义出来的classes生成的实例
    def __init__(self, game ):
        self.game = game
        self.gameObjects = {}
        
    def findObject(self, name):
        if name in self.gameObjects:
            return self.gameObjects[name]
        
        
        
        return None
    
    def CreateObject(self, item):
        obj = None
        if item['type'] == 'CircleObject':
            obj = self.CreateCircleObject(item)
        elif item['type'] == 'TextObject':
            obj = self.CreateTextObject(item)
        elif item['type'] == 'GameObject':
            obj = self.CreateGameObject(item)
        
        if obj is not None:
            self.gameObjects[obj.name] = obj
        
    
    def CreateGameObject(self, item):
        obj = GameObject(
            game = self.game, 
            screen = self.game.var主窗口, 
            name = item['name'],
            pos = item['pos']
            #pos：posisition：位置
        )
        #
        for componentName in item['components']:
            
            # ┌───────────────────────────────┐
            # │       Animation Renderer      │
            # └───────────────────────────────┘
            if componentName == 'AnimationRenderer':
                obj.addComponent(
                    'AnimationRenderer', 
                    item['components']['AnimationRenderer']['AnimationName'],
                    item['components']['AnimationRenderer']['visible']
                )
                self.game.addRenderer(obj.components['AnimationRenderer'])
                
            # ┌───────────────────────────────┐
            # │         Circle Renderer       │
            # └───────────────────────────────┘
            elif componentName == "CircleRenderer":
                obj.addComponent(
                    'CircleRenderer',
                    item['components']['CircleRenderer']["radius"],
                    item['components']['CircleRenderer']['visible']
                )
                self.game.addRenderer(obj.components['CircleRenderer'])


            # ┌───────────────────────────────┐
            # │      Rectangle Renderer       │
            # └───────────────────────────────┘

            elif componentName == "RectangleRenderer":
                obj.addComponent(
                    'RectangleRenderer',
                    item['components']['RectangleRenderer']["width"],
                    item['components']['RectangleRenderer']["height"],
                    item['components']['RectangleRenderer']['color'],
                    item['components']['RectangleRenderer']['visible']
                )
                self.game.addRenderer(obj.components['RectangleRenderer'])
                
            # ┌───────────────────────────────┐
            # │         Text Renderer         │
            # └───────────────────────────────┘
            elif componentName == 'TextRenderer':
                obj.addComponent(
                    'TextRenderer',
                    item['components']['TextRenderer']['text'],
                    item['components']['TextRenderer']['font'],
                    item['components']['TextRenderer']['fontColor'],
                    item['components']['TextRenderer']['visible']
                )
                self.game.addRenderer(obj.components['TextRenderer'])
        
        return obj
    
 
        
    def CreateTextObject(self, item):
        obj = TextObject(
            game = self.game, 
            screen = self.game.var主窗口, 
            name = item['name'], 
            sprite = None, 
            pos = item['pos'], 
            font = self.game.getFont(item['font']),
            text = item['text'],
            color = item['color'])
        obj.visible = item['visible']
        return obj
    
    def DrawObjects(self):
        for objName in self.gameObjects:
            obj = self.gameObjects[objName]
            if obj.visible:
                obj.draw()
    
    def DestroyObject(self):
        pass
    
    # 序列化
    def Serialize(self):
        pass
    
    # 反序列化
    def Deserialize(self):
        pass