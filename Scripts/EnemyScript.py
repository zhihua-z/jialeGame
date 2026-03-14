from Component.script import Script

class EnemyScript(Script):

    def __init__(self, game, gameObject, name, life):
        super().__init__(game, gameObject, name)

        self.life = life 

    def die(self):
        # 敌人死亡，移除对象
        self.game.entitysystem.remove(self.gameObject.id)

        # 可以在这里添加敌人死亡的动画、音效等效果

    def take_damage(self, damage): # 承受伤害
        print('敌人受到了伤害，伤害值：', damage)
        self.life -= damage
        if self.life <= 0:
            self.die()  # 敌人死亡，调用die方法移除对象

    def update(self, time):
        if self.life <= 0:
            self.die()