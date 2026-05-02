from Component.script import Script
import pygame


class 生成敌人脚本(Script):
    def __init__(self, game, gameObject, name, speed=400):
        super().__init__(game, gameObject, name)
        self.enemy_count = 0

        # interval 区间
        self.enemy_spawn_interval = 2.0  # 每2秒生成一个敌人

    def update(self, time):
        if self.enemy_count < 10:  # 最多生成10个敌人
            self.enemy_spawn_interval -= time
        
        if self.enemy_spawn_interval <= 0:
            self.enemy_spawn_interval = 2.0  # 重置生成间隔
            self.enemy_count += 1
            
            # 在玩家上方随机位置生成敌人
            player_pos = self.game.entitysystem.getPlayer().pos
            spawn_x = player_pos[0] + (pygame.rand.randint(-100, 100))  # 在玩家左右100像素范围内生成
            spawn_y = player_pos[1] - 200  # 在玩家上方200像素处生成
            pos = [spawn_x, spawn_y]
            
            try:
                enemy = self.game.entitysystem.create敌人(pos)
            except Exception:
                enemy = None