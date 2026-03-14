from GameObject import GameObject
from Component.component import Component

class Script(Component):

    def __init__(self, game, gameObject, name):
        self.game = game
        self.gameObject = gameObject
        self.name = name
        super().__init__(game, gameObject, name)

    def cleanup(self):
        return self.game.scriptSystem.removeScript(self)

    def update(self, time):
        pass