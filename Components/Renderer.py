from Components.ComponentBase import Component


class RendererComponent(Component):
    
    def __init__(self, game, gameObject, name):
        super().__init__(game, name)
        self.gameObject = gameObject
        

class AnimationRenderer(RendererComponent):
    
    def __init__(self, game, gameObject, name, animationName, visible):
        super().__init__(game, gameObject, name)
        
        self.animation = self.game.getAnimation(animationName)
        self.visible = visible
        
        

class CircleRenderer(RendererComponent):
    
    def __init__(self, game, gameObject, name, radius, visible):
        super().__init__(game, gameObject, name)
        self.radius = radius
        self.visible = visible

class RectangleRenderer(RendererComponent):
    
    def __init__(self, game, gameObject, name, width , height , color, visible):
        super().__init__(game, gameObject, name)
        self.width =  width
        self.height = height
        self.color = color
        self.visible = visible

class TextRenderer(RendererComponent):
    
    def __init__(self, game, gameObject, name, text, font, fontColor, visible):
        super().__init__(game, gameObject, name)
        self.text = text
        self.font = self.game.getFont(font).font
        self.visible = visible
        self.fontColor = fontColor

