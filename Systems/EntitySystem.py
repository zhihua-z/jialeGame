import json

from Components.GameObject import GameObject, CircleObject, Wallobject, TextObject
'''
Entity: 实体，一个物体 


'''
class EntitySystem:
    #由定义出来的classes生成的实例
    def __init__(self, game ):
        self.game = game
        self.gameObjects = {}
    
    
# for item in gameobjects:
#     dict1[item.name] = {
#         'name': item.name,
#         'type': item.type,
#         'pos':   item.pos,
#         'components' : item.components
#     }
    def saveObject(self):
        dict1 = {}

        for item in self.gameObjects:
            dict1[item] = self.gameObjects[item].serialize()
            
        towrite = json.dumps(dict1,indent=4,ensure_ascii=False)
        a = open('output.json',"w")
        a.write(towrite)
        a.close()



    def findObject(self, name):
        if name in self.gameObjects:
            return self.gameObjects[name]
        
        
        
        return None
    
    def CreateObject(self, item):
        obj = None
        if item['type'] == 'GameObject':
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
                    item['components']['AnimationRenderer']['visible'],
                    item['components']['AnimationRenderer']['moveWithCamera']
                )

            # ┌───────────────────────────────┐
            # │       Sprite Renderer         │
            # └───────────────────────────────┘
            if componentName == 'SpriteRenderer':
                obj.addComponent(
                    'SpriteRenderer', 
                    item['components']['SpriteRenderer']['SpriteName'],
                    item['components']['SpriteRenderer']['visible'],
                    item['components']['SpriteRenderer']['moveWithCamera']
                )
                
            # ┌───────────────────────────────┐
            # │         Circle Renderer       │
            # └───────────────────────────────┘
            elif componentName == "CircleRenderer":
                obj.addComponent(
                    'CircleRenderer',
                    item['components']['CircleRenderer']["radius"],
                    item['components']['CircleRenderer']['visible'],
                    item['components']['CircleRenderer']['moveWithCamera']
                )


            # ┌───────────────────────────────┐
            # │      Rectangle Renderer       │
            # └───────────────────────────────┘

            elif componentName == "RectangleRenderer":
                obj.addComponent(
                    'RectangleRenderer',
                    item['components']['RectangleRenderer']["width"],
                    item['components']['RectangleRenderer']["height"],
                    item['components']['RectangleRenderer']['color'],
                    item['components']['RectangleRenderer']['visible'],
                    item['components']['RectangleRenderer']['moveWithCamera']
                )
                
            # ┌───────────────────────────────┐
            # │         Text Renderer         │
            # └───────────────────────────────┘
            elif componentName == 'TextRenderer':
                obj.addComponent(
                    'TextRenderer',
                    item['components']['TextRenderer']['text'],
                    item['components']['TextRenderer']['font'],
                    item['components']['TextRenderer']['fontColor'],
                    item['components']['TextRenderer']['visible'],
                    item['components']['TextRenderer']['moveWithCamera']
                )
            elif componentName == 'BoxCollider':
                obj.addComponent(
                    'BoxCollider',
                    item['components']['BoxCollider']['visible']
                )
        
        return obj
    
    def CreateNewObject(self, name, pos = [0, 0]):
        obj = GameObject(
            game = self.game, 
            screen = self.game.var主窗口, 
            name = name,
            pos = pos
        )
    
        if obj is not None:
            self.gameObjects[obj.name] = obj
        
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