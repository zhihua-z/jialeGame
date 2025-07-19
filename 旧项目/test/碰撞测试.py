import math
'''
1. 都是边缘和坐标轴平行 AABB (axis aligned bounding box)
2. 一个物体动，一个物体不动

'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rect:
    def __init__(self, pos, width, height):
        self.pos = pos
        self.width = width
        self.height = height
        self.topleft = Point(pos.x - width * 0.5, pos.y + height * 0.5)
        self.bottomright = Point(pos.x + width * 0.5, pos.y - height * 0.5)
        
        self.direction = Vector(0, 0)
    
    def getCenter(self):
        centerx = self.topleft.x * 0.5 + self.bottomright.x * 0.5
        centery = self.topleft.y * 0.5 + self.bottomright.y * 0.5
        
        return Point(centerx, centery)
    
    def getTopLeft(self):
        return self.topleft
    
    def getTopRight(self):
        return Point(self.bottomright.x, self.topleft.y)
    
    def getBottomLeft(self):
        return Point(self.topleft.x, self.bottomright.y)
    
    def getBottomRight(self):
        return self.bottomright
        
        
def checkPointInBoxCollider(point: Point, rectangle: Rect):
    return point.x >= rectangle.topleft.x and point.x <= rectangle.bottomright.x and point.y >= rectangle.bottomright.y and point.y <= rectangle.topleft.y

def calculateHitDistancePointBox(point: Point, rectangle: Rect, rectangleB: Rect, direction: Vector):
    弹出点 = Point(0, 0)
    centerA = rectangle.getCenter() 
    centerB = rectangleB.getCenter()
    if centerB.x > centerA.x:
        if centerB.y > centerA.y:
            弹出点 = rectangle.getTopRight()
        else:
            弹出点 = rectangle.getBottomRight()
    else:
        if centerB.y > centerA.y:
            弹出点 = rectangle.getTopLeft()
        else:
            弹出点 = rectangle.getBottomLeft()
            
    bounce_x = point.x - 弹出点.x
    bounce_y = point.y - 弹出点.y
    
    if direction.x == 0:
        bounce_x = 0
    if direction.y == 0:
        bounce_y = 0
            
    dist = math.sqrt(bounce_x ** 2 + bounce_y ** 2)
    
    return dist
     

a = Rect(Point(0.5, 0.5), 1, 1)
b = Rect(Point(-0.4, -0.4), 1, 1)

b.direction = Vector(0, 1)

# 1. 计算方向和我应该使用哪个点
ca = a.getCenter()
cb = b.getCenter()
b_collide_point = []

# 1234象限
if cb.x > ca.x:
    if cb.y > ca.y:
        b_collide_point = b.getBottomLeft()
    else:
        b_collide_point = b.getTopLeft()
else:
    if cb.y > ca.y:
        b_collide_point = b.getBottomRight()
    else:
        b_collide_point = b.getTopRight()
        
hit = checkPointInBoxCollider(b_collide_point, a)
dist = calculateHitDistancePointBox(b_collide_point, a, b, b.direction)

print(hit)
print(dist)






