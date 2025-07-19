from Components.ComponentBase import Component


class RendererComponent(Component):
    
    def __init__(self, game, gameObject, name, visible):
        super().__init__(game, name, gameObject)
        self.visible = visible
       
        
        

class AnimationRenderer(RendererComponent):
    
    def __init__(self, game, gameObject, name, animationName, visible):
        super().__init__(game, gameObject, name, visible)
        
        self.animation = self.game.getAnimation(animationName)
    

# for item in gameobjects:
#     dict1[item.name] = {
#         'name': item.name,
#         'type': item.type,
#         'pos':   item.pos,
#         'components' : item.components
#     }

    def serialize (self):
        dict1 = {}
        
        dict1['visible'] = self.visible
        dict1['AnimationName'] = self.animation.animation_name

        return dict1
class SpriteRenderer(RendererComponent):
    
    def __init__(self, game, gameObject, name, spriteName, visible):
        super().__init__(game, gameObject, name, visible)
        
        self.sprite = self.game.getSprite(spriteName)        


    def serialize (self):
        dict1 = {}
        dict1['name'] = self.name
        dict1['visible'] = self.visible
        dict1['sprite'] = self.sprite.name

        return dict1
class CircleRenderer(RendererComponent):
    
    def __init__(self, game, gameObject, name, radius, visible):
        super().__init__(game, gameObject, name, visible)
        self.radius = radius


    def serialize (self):
        dict1 = {}
        dict1['name'] = self.name
        dict1['visible'] = self.visible
        dict1['radius'] = self.radius

        return dict1

class RectangleRenderer(RendererComponent):
    
    def __init__(self, game, gameObject, name, width , height , color, visible):
        super().__init__(game, gameObject, name, visible)
        self.width =  width
        self.height = height
        self.color = color

    def serialize (self):
        dict1 = {}
        dict1['name'] = self.name
        dict1['visible'] = self.visible
        dict1['width'] = self.width
        dict1['height'] = self.height
        dict1['color'] = self.color

        return dict1

class TextRenderer(RendererComponent):
    
    def __init__(self, game, gameObject, name, text, font, fontColor, visible):
        super().__init__(game, gameObject, name, visible)
        self.text = text
        self.fontname = font
        self.font = self.game.getFont(self.fontname).font
        self.fontColor = fontColor


    def serialize (self):
        dict1 = {}
        dict1['name'] = self.name
        dict1['visible'] = self.visible
        dict1['text'] = self.text
        dict1['font'] = self.fontname
        dict1['fontColor'] = self.fontColor

        return dict1


