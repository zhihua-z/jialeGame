import pygame


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
        # 处理物理更新，例如碰撞检测、位置更新等
        
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


                    # O(n^2) -> O(n) 通过只检测玩家子弹和敌人之间的碰撞，其他不检测了。
                    if obj.name.startswith('蓝色子弹') and other_obj.name.startswith('蓝色子弹'):
                        continue  # 子弹之间不检测碰撞

                    # O(n) -> O(n)
                    if obj.name.startswith('蓝色子弹') and other_obj.name.startswith('Player'):
                        continue  # 子弹只检测与敌人的碰撞
                    if obj.name.startswith('Player') and other_obj.name.startswith('蓝色子弹'):
                        continue  # 玩家只检测与子弹的碰撞


                    if "BoxCollider" in other_obj.components:
                        collider2 = other_obj.components["BoxCollider"]

                        # 目标：在这个真正的检测开始之前，尽可能地排除掉不可能碰撞的情况，减少checkCollision的调用次数。
                        if collider1.checkCollision(collider2):
                            collider1.collision = other_obj
                            collider2.collision = obj

                            
                            # if obj.name.startswith('蓝色子弹') and other_obj.name.startswith('Enemy'):
                            #     self.game.entitysystem.remove(obj.id)  # 子弹要删除
                            	
                            
                            # if obj.name.startswith('Enemy') and other_obj.name.startswith('蓝色子弹'):
                            #     self.game.entitysystem.remove(other_obj.id)  # 子弹要删除
                            	
            
