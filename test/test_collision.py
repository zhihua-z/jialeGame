def checkCollision(self, other):
     # AABB碰撞检测
        # 如果我的任何一个点在那个个矩形里，就算碰撞
        # 如果我完全包裹在另一个矩形里，也算碰撞
        ax, ay = self
        aw, ah = (30, 30)  # 假设当前物体的宽高为64x64，可以根据实际情况调整
        bx, by = other
        bw, bh = (100, 100)  # 假设另一个物体的宽高为64x64，可以根据实际情况调整
        
        #  检测四个角点
        '''
        a0 ------- a1   -
        |           |   |
        |           |   ah
        |           |   |
        a3 ------- a2   -

        |----aw-----|

                b0 ------- b1   -
                |           |   |
                |           |   bh
                |           |   |
                b3 ------- b2   -
                
                |----bw-----|

        '''
        a0 = [ax - aw / 2, ay + ah / 2]
        a1 = [ax + aw / 2, ay + ah / 2]
        a2 = [ax + aw / 2, ay - ah / 2]
        a3 = [ax - aw / 2, ay - ah / 2]
        b0 = [bx - bw / 2, by + bh / 2]
        b2 = [bx + bw / 2, by - bh / 2]

        # 包裹检测
        if (a0[0] >= b0[0] and a0[1] <= b0[1] and
            a0[0] <= b2[0] and a0[1] >= b2[1] and 
            a2[0] >= b0[0] and a2[1] <= b0[1] and
            a2[0] <= b2[0] and a2[1] >= b2[1]): # 左上包裹在里面
            return True
        


        '''
        a0 ------- a1   -
        |           |   |
        |           |   ah
        |           |   |
        a3 ------- a2   -

        |----aw-----|

                b0 ------- b1   -
                |           |   |
                |           |   bh
                |           |   |
                b3 ------- b2   -
                
                |----bw-----|

        '''
        
        # 检测四个角点

        if (a0[0] >= b0[0] and a0[1] <= b0[1] and
            a0[0] <= b2[0] and a0[1] >= b2[1]):
            return True  # a0 在 b 矩形内

        if (a1[0] >= b0[0] and a1[1] <= b0[1] and
            a1[0] <= b2[0] and a1[1] >= b2[1]):
            return True  # a1 在 b 矩形内

        if (a2[0] >= b0[0] and a2[1] <= b0[1] and
            a2[0] <= b2[0] and a2[1] >= b2[1]):
            return True  # a2 在 b 矩形内

        if (a3[0] >= b0[0] and a3[1] <= b0[1] and
            a3[0] <= b2[0] and a3[1] >= b2[1]):
            return True  # a3 在 b 矩形内
        
        return False
        
print(checkCollision((50, 116), (50, 50)))  # 测试函数调用