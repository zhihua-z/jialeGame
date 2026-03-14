from Component.script import Script

class Bullet自杀Script(Script):

    def __init__(self, game, gameObject, name):
        super().__init__(game, gameObject, name)

    def update(self, time):
        pos = self.gameObject.pos # 获取子弹当前的位置
        map_area = self.game.map_area # 获取地图范围，格式为 [x_min, y_min, x_max, y_max]
        # [x_min, y_min, x_max, y_max]

        # 超出屏幕范围检测
        if pos[0] < map_area[0] or pos[0] > map_area[2] or pos[1] < map_area[1] or pos[1] > map_area[3]:
            # 直接调用EntitySystem的removeObject方法删除这个对象
            self.game.entitysystem.removeObject(self.gameObject.id)