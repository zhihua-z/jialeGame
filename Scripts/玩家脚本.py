from Component.script import Script
import pygame


class 玩家脚本(Script):
    def __init__(self, game, gameObject, name, speed=400):
        super().__init__(game, gameObject, name)
        self.speed = speed

    def update(self, time):
        # 使用 InputSystem 读取按键状态
        ks = self.game.inputSystem
        dt = getattr(self.game, 'dt', 0)
        move = self.speed * dt

        # WASD 控制（与 Game.run 中的方向一致）
        if ks.getkeyDown(pygame.K_w):
            self.gameObject.pos[1] += move
        if ks.getkeyDown(pygame.K_s):
            self.gameObject.pos[1] -= move
        if ks.getkeyDown(pygame.K_a):
            self.gameObject.pos[0] -= move
        if ks.getkeyDown(pygame.K_d):
            self.gameObject.pos[0] += move

        # J 键单次按下触发射击（使用 InputSystem.getKeyPress）
        if ks.getKeyPress(pygame.K_j):
            # 在玩家当前位置上方生成蓝色子弹
            pos = [self.gameObject.pos[0], self.gameObject.pos[1] - 20]
            try:
                bullet = self.game.entitysystem.create蓝色子弹(pos)
            except Exception:
                bullet = None

            # 播放射击音效（若存在）
            射击音效 = None
            try:
                射击音效 = self.game.rs.getSound("射击")
            except Exception:
                射击音效 = None

            if 射击音效:
                射击音效.set_volume(0.1)
                射击音效.play()
