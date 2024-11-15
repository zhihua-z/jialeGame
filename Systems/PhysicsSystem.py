# Physics: 物理
import math

class PhysicsSystem:
    
    def __init__(self):
        pass
    
    
    def distance(self, pos1, pos2):
        a=pos1[0] - pos2[0]
        b=pos1[1] - pos2[1]
        
        return math.sqrt(a*a + b*b)
    
    
    def update(self, time):

        # #计算物理碰撞
        for item in self.var碰撞物体:
            for other in self.var碰撞物体:
                if item == other:
                    continue
                
                # 只想计算玩家和其他物体之间的碰撞
                if item['object'].name != 'Player' or item['object'].name != 'shilaimu':
                    continue
                
                item1 = item['object']
                item2 = other['object']
                
                if item1.type == 'Circle' and item2.type == 'Circle':
                    # 检测item1和item2是否碰撞
                    juli = self.distance(item1.pos, item2.pos)
                    
                    if juli <= item1.radius + item2.radius:
                        print(f'你被撞了！') 
                        self.running = False
                
                if item1.type == 'Circle' and item2.type == 'Rectangle':
                    circleRectanglePos = self.checkCircleRectanglePos(item1, item2)
                    hit, dist = self.checkCircleRectangleHit(item1, item2, circleRectanglePos)
                    
                    if hit:
                        print('撞到啦')
                        self.player.pos = self.setCircleRectangleHitDistance(item1, item2, circleRectanglePos,item1.direction)
                        self.player.direction[0] = 0
                        self.player.direction[1] = 0
                    else:
                        pass

    #   1   2   3
    #   4   5   6
    #   7   8   9
    def checkCircleRectanglePos(self, circle, rectangle) -> int:
        cx = circle.pos[0]
        cy = circle.pos[1]
        r1x = rectangle.pos[0]
        r1y = rectangle.pos[1]
        r2x = rectangle.pos[0] + rectangle.width
        r2y = rectangle.pos[1] + rectangle.height
        
        if cx < r1x and cy < r1y:
            return 1
        elif cx > r2x and cy > r2y: 
            return 9
        elif cx < r1x and cy > r2y:
            return 7
        elif cx > r2x and cy < r1y:
            return 3
        elif cy < r1y:
            return 2
        elif cx < r1x:
            return 4
        elif cx > r2x:
            return 6
        elif cy > r2y:
            return 8
        else:
            return 5 # 中间
    
    def checkCircleRectangleHit(self, circle, rectangle, 方向):
        cx = circle.pos[0]
        cy = circle.pos[1]
        r1x = rectangle.pos[0]
        r1y = rectangle.pos[1]
        r2x = rectangle.pos[0] + rectangle.width
        r2y = rectangle.pos[1] + rectangle.height
        
        dist = 0
        
        if 方向 == 1:
            dist = self.distance(circle.pos, (r1x, r1y))
        elif 方向 == 2:
            dist = abs(r1y - cy)
        elif 方向 == 3:
            dist = self.distance(circle.pos, (r2x, r1y))
        elif 方向 == 4:
            dist = abs(r1x - cx)
        elif 方向 == 5:
            return -1
        elif 方向 == 6:
            dist = abs(r2x - cx)
        elif 方向 == 7:
            dist = self.distance(circle.pos, (r1x, r2y))
        elif 方向 == 8:
            dist = abs(r2y - cy)
        else: # 9
            dist = self.distance(circle.pos, (r2x, r2y))
            
        return (dist < circle.radius, dist)
        
    def setCircleRectangleHitDistance(self, circle, rectangle, 方向, direction):
        yidiandian = 0.05
        
        radius = circle.radius
        direction[0] = circle.direction[0]
        direction[1] = circle.direction[1]
        cx = circle.pos[0]
        cy = circle.pos[1]
        
        r1x = rectangle.pos[0]
        r1y = rectangle.pos[1]
        r2x = rectangle.pos[0] + rectangle.width
        r2y = rectangle.pos[1] + rectangle.height
        
        if 方向 == 1:
            return [cx - yidiandian, cy - yidiandian]
        elif 方向 == 2:
            return [cx, r1y - radius - yidiandian]
        elif 方向 == 3:
            return [cx + yidiandian, cy - yidiandian]
        elif 方向 == 4:
            return [r1x - radius - yidiandian, cy]
        elif 方向 == 5:
            return [cx + yidiandian, cy + yidiandian]
        elif 方向 == 6:
            return [r2x + radius + yidiandian, cy]
        elif 方向 == 7:
            return [cx - yidiandian, cy + yidiandian]
        elif 方向 == 8:
            return [cx, r2y + radius + yidiandian]
        else: # 9
            return [cx + yidiandian, cy + yidiandian]
