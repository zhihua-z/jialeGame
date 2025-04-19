from Components.ComponentBase import Component



class Collider(Component):

    def __init__(self, game, gameObject,visible, moveWithCamera= False):
        super().__init__(game, "Collider",gameObject)
        self.visible = visible
        self.moveWithCamera = moveWithCamera

class CircleCollider(Collider):
    
    def __init__(self, game, gameObject, name, radius, visible, moveWithCamera= False) :
        super().__init__(game,"CircleCollider",gameObject,visible,moveWithCamera)
        self.radius = radius
        


class RectangleCollider(Collider):
    
    def __init__(self, game, gameObject, name, width , height , color, visible, moveWithCamera = False):
        super().__init__(game,"RectangleCollider",gameObject ,visible,moveWithCamera)
        
        self.width = width
        self.height = height
        self.color = color


class BoxCollider(Collider):

    def __init__(self, game, gameObject,visible, moveWithCamera= False):
        super().__init__(game, "BoxCollider",gameObject),visible,moveWithCamera
        self.visible = visible
        