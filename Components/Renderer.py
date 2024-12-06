from Components.ComponentBase import Component


class RendererComponent(Component):
    
    def __init__(self, game, gameObject, name, visible, moveWithCamera):
        super().__init__(game, name)
        self.gameObject = gameObject
        self.visible = visible
        self.moveWithCamera = moveWithCamera
        
        

class AnimationRenderer(RendererComponent):
    
    def __init__(self, game, gameObject, name, animationName, visible, moveWithCamera):
        super().__init__(game, gameObject, name, visible, moveWithCamera)
        
        self.animation = self.game.getAnimation(animationName)
        
        

class CircleRenderer(RendererComponent):
    
    def __init__(self, game, gameObject, name, radius, visible, moveWithCamera):
        super().__init__(game, gameObject, name, visible, moveWithCamera)
        self.radius = radius

class RectangleRenderer(RendererComponent):
    
    def __init__(self, game, gameObject, name, width , height , color, visible, moveWithCamera):
        super().__init__(game, gameObject, name, visible, moveWithCamera)
        self.width =  width
        self.height = height
        self.color = color

class TextRenderer(RendererComponent):
    
    def __init__(self, game, gameObject, name, text, font, fontColor, visible, moveWithCamera):
        super().__init__(game, gameObject, name, visible, moveWithCamera)
        self.text = text
        self.font = self.game.getFont(font).font
        self.fontColor = fontColor

