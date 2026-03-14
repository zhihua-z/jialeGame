from Component.script import Script

class 玩家子弹击杀(Script):

    def __init__(self, game, gameObject, name):
        super().__init__(game, gameObject, name)

    def update(self, time):
        pos = self.gameObject.pos # 获取子弹当前的位置
        
        # 获取当前子弹是否有碰撞
        # 如果有碰撞，并且是敌人，就删除子弹，敌人掉血
        
        # 如果我有BoxCollider, 并且BoxCollider有碰撞
        # 如果碰撞的对象是敌人，就调用敌人的take_damage方法，传入伤害值
        
        if self.gameObject.components and "BoxCollider" in self.gameObject.components:
            collider = self.gameObject.components["BoxCollider"]
            
            if collider.collision:
                other_obj = collider.collision  # 获取碰撞的对象
                
                if other_obj.name.startswith('Enemy'):
                    # 如果碰撞对象是敌人，调用敌人的take_damage方法
                    if "EnemyScript" in other_obj.components:
                        enemy_script = other_obj.components["EnemyScript"]
                        enemy_script.take_damage(10)  # 传入伤害值，例如1
                        
                    # 删除子弹对象
                    self.game.entitysystem.remove(self.gameObject.id)