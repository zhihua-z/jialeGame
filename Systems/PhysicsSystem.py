import pygame

# 物理系统，负责处理物理相关的逻辑，例如碰撞检测、位置更新等
# 9.5 22:06 ：我开始做physics system
# 物理系统的职责：
# 1. 碰撞检测：检测游戏物体之间的碰撞，并触发相应的事件或反应。
# 2. 位置更新：根据物体的速度和加速度更新物体的位置。
# 3. 物理交互：处理物体之间的物理交互，例如弹跳、摩擦等。
# 4. 优化性能：通过空间划分等技术优化碰撞检测的性能，减少不必要的计算。
# 物理系统的实现：
# 1. 碰撞检测：使用简单的碰撞检测算法，例如轴对齐包围盒（AABB）或圆形碰撞检测，根据物体的形状和位置进行检测。
# 2. 位置更新：根据物体的速度和加速度，使用基本的物理公式更新物体的位置。
# 3. 物理交互：根据物体之间的碰撞情况，计算反弹、摩擦等物理效果，并更新物体的速度和位置。
# 4. 优化性能：使用空间划分技术，例如四叉树或网格，将物体分布在不同的区域中，只检测同一区域内的物体之间的碰撞，减少不必要的计算。

class PhysicsSystem:
    def __init__(self,game):
        self.game = game

        '''
        代码效率：
        如果我有5个物体 A.1 	B.2 	C.3 	D.4 	E.5
        碰撞检测:A-B A-C A-D A-E B-A B-C B-D B-E C-A C-B C-D C-E D-A D-B D-C D-E E-A E-B E-C E-D

        如果我有100个物体,碰撞检测就是 99*99 ~ 10000次,效率很低。

        优化计划：
        1. 最简单的优化：只检测玩家子弹和敌人之间的碰撞，其他不检测了。
        
        '''


    def update(self, dt):
        # 处理物理更新，位置更新等
        for obj in self.game.entitysystem.gameObjects.values():
            obj.pos[0] += obj.direction[0] * dt
            obj.pos[1] += obj.direction[1] * dt
        
        # 对全部游戏物体进行碰撞检测
        for obj in self.game.entitysystem.gameObjects.values():
            if "BoxCollider" in obj.components:
                collider1 = obj.components["BoxCollider"]
                for other_obj in self.game.entitysystem.gameObjects.values():
                    if obj.id == other_obj.id:#考虑大于的情况 #之后又不考虑了
                        continue
                    #关于时间复杂度的一些提前学习
                    # 计算复杂度 
                    # O(2^n) : 指数增长  
                    # O(n^2) : 平方增长 100个物体就是10000次检测
                    # O(n log n) : 线性对数增长 100个物体就是100*7次检测
                    # O(n) : 线性增长 100个物体就是100次检测
                    # O(log n) : 对数增长 100个物体就是7次检测
                    # O(1) : 常数时间 100个物体还是1次检测

                    if "BoxCollider" in other_obj.components:
                        collider2 = other_obj.components["BoxCollider"]

                        # 1组之间有碰撞检测
                        # 2组之间没有碰撞检测，但是2组和1组之间有碰撞检测
                        # 3组之间没有碰撞检测，但是3组和1组之间有碰撞检测 (future)
                        if collider1.group == 2 and collider1.group == collider2.group:
                            continue


                        # 目标：在这个真正的检测开始之前，尽可能地排除掉不可能碰撞的情况，减少checkCollision的调用次数。
                        if collider1.checkCollision(collider2):
                            collider1.collision = other_obj
                            collider2.collision = obj

                            
