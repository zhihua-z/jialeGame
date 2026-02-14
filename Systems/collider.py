import pygame
#from GameObject import Component
from GameObject import GameObject
from component import Component


class Collider(Component):

    def __init__(self, game, gameObject, name, visible, moveWithCamera=False):
        super().__init__(game, gameObject, name)
        self.visible = visible
        self.moveWithCamera = moveWithCamera

class CircleCollider(Collider):
    
    def __init__(self, game, gameObject, name, radius, visible, moveWithCamera=False):
        super().__init__(game, gameObject, name, visible, moveWithCamera)
        self.radius = radius
        


class RectangleCollider(Collider):
    
    def __init__(self, game, gameObject, name, width, height, color, visible, moveWithCamera=False):
        super().__init__(game, gameObject, name, visible, moveWithCamera)

        self.width = width
        self.height = height
        self.color = color


class BoxCollider(Collider):

    def __init__(self, game, gameObject, visible, width, height, moveWithCamera=False):
        super().__init__(game, gameObject, "BoxCollider", visible, moveWithCamera)
        self.width = width
        self.height = height

    def serialize (self):
        dict1 = {}
        dict1['name'] = "BoxCollider"
        dict1['visible'] = self.visible
        return dict1
    

    def checkPointInBoxCollider(self, pos, collider):
        # 默认宽度64
        cx0 = collider.gameObject.pos[0] - 32
        cy0 = collider.gameObject.pos[1] - 32
        cx1 = collider.gameObject.pos[0] + 32
        cy1 = collider.gameObject.pos[1] + 32
        
        return cx0 < pos[0] and cx1 > pos[0] and cy0 < pos[1] and cy1 > pos[1]


        #'''
        #a0 ------- a1   -
        #|          |   |
        #|           |   ah
        #|           |   |
        #a3 ------- a2   -

                #|----aw-----|

         #       b0 ------- b1   -
          #      |           |   |
           #     |           |   bh
            #    |           |   |
             #   b3 ------- b2   -
              #  
               # |----bw-----|

    def checkCollision(self, other):
        # 检测与另一个BoxCollider的碰撞
        ax,ay = self.gameObject.pos
        aw = self.width
        ah = self.height
        bx,by = other.gameObject.pos
        bw = other.width
        bh = other.height
        a0 = [ax - aw / 2, ay + ah / 2]
        a1 = [ax + aw / 2, ay + ah / 2]
        a2 = [ax + aw / 2, ay - ah / 2]
        a3 = [ax - aw / 2, ay - ah / 2]
        b0 = [bx - bw / 2, by + bh / 2]
        b2 = [bx + bw / 2, by - bh / 2]
        if (a0[0] >= b0[0] and a0[1] <= b0[1] 
                           and 
            a0[0] <= b2[0] and a0[1] >= b2[1] 
                           and 
            a2[0] >= b0[0] and a2[1] <= b0[1] 
                           and 
            a2[0] <= b2[0] and a2[1] >= b2[1]):
            return True
        if (a0[0] >= b0[0] and a0[1] <= b0[1] and
            a0[0] <= b2[0] and a0[1] >= b2[1]):
            return True
        if (a2[0] >= b0[0] and a2[1] <= b0[1] and
            a2[0] <= b2[0] and a2[1] >= b2[1]):
            return True
        if (a1[0] >= b0[0] and a1[1] <= b0[1] and
            a1[0] <= b2[0] and a1[1] >= b2[1]):
            return True
        if (a3[0] >= b0[0] and a3[1] <= b0[1] and
            a3[0] <= b2[0] and a3[1] >= b2[1]):
            return True
        
        return False
        
        
        
        

