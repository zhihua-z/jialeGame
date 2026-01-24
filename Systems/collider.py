import pygame
#from GameObject import Component
from GameObject import GameObject


class Collider:

    def __init__(self, game, gameObject, name, visible, moveWithCamera=False):
        self.game = game
        self.gameObject = gameObject
        self.name = name
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

    def __init__(self, game, gameObject, visible, moveWithCamera=False):
        super().__init__(game, gameObject, "BoxCollider", visible, moveWithCamera)
        self.visible = visible

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



    def checkBoxColliderWithBoxCollider(self, a, b):
        hit = False
        dist = 1

        apos = a.gameObject.getWorldPosition()
        
        ax0 = apos[0] - 32
        ay0 = apos[1] - 32
        ax1 = apos[0] + 32
        ay1 = apos[1] + 32
        
        
        bx0 = b.gameObject.pos[0] - 32
        by0 = b.gameObject.pos[1] - 32
        bx1 = b.gameObject.pos[0] + 32
        by1 = b.gameObject.pos[1] + 32
        
        if self.checkPointInBoxCollider((ax0, ay0), b):
            hit = True
        if self.checkPointInBoxCollider((ax0, ay1), b):
            hit = True
        if self.checkPointInBoxCollider((ax1, ay0), b):
            hit = True
        if self.checkPointInBoxCollider((ax1, ay1), b):
            hit = True
        if self.checkPointInBoxCollider((bx0, by0), a):
            hit = True
        if self.checkPointInBoxCollider((bx0, by1), a):
            hit = True
        if self.checkPointInBoxCollider((bx1, by0), a):
            hit = True
        if self.checkPointInBoxCollider((bx1, by1), a):
            hit = True
            
        return (hit, dist)
        

    #   1   2   3
    #   4   5   6
    #   7   8   9
        

