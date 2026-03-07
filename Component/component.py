class Component:

    def __init__(self, game, gameObject, name):
        self.game = game
        self.gameObject = gameObject
        self.name = name

    def cleanup(self):
        pass