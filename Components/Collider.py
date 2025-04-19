<<<<<<< HEAD
from Components.ComponentBase import Component



class Collider(Component):

    def __init__(self, game, gameObject,visible, moveWithCamera= False):
        super().__init__(game, "Collider",gameObject)
        self.visible = visible
        self.moveWithCamera = moveWithCamera

class CircleCollider(Collider):
    
    def __init__(self, game, gameObject, name, radius, visible, moveWithCamera= False) :
        super().__init__(game,"CircleCollider",gameObject,visible,moveWithCamera)
        self.radius = radius
        


class RectangleCollider(Collider):
    
    def __init__(self, game, gameObject, name, width , height , color, visible, moveWithCamera = False):
        super().__init__(game,"RectangleCollider",gameObject ,visible,moveWithCamera)
        
        self.width = width
        self.height = height
        self.color = color


class BoxCollider(Collider):

    def __init__(self, game, gameObject,visible, moveWithCamera= False):
        super().__init__(game, "BoxCollider",gameObject),visible,moveWithCamera
        self.visible = visible
        
=======
from ComponentBase import Component

'''
圆形碰撞器（半径和距离检测）
方形碰撞器（AABB碰撞 口 口）
矩形碰撞器（设计碰撞器文件格式）（线性代数）（矢量）（点积）
'''

'''
任何拥有碰撞器的物体，如果这个物体碰撞器可见的话，就在游戏里在这个物体的外面画一个正方形·

'''
class BoxCollider(Component):
    
    def __init__(self, game, gameObject, visible):
        super().__init__(game, "BoxCollider", gameObject)
        self.visible = visible
>>>>>>> acfbf1398e9266b0e7f6692881aefd5adccd8c2e
