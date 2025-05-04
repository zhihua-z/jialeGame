from Components.ComponentBase import Component



class Collider(Component):

    def __init__(self, game, gameObject, name, visible, moveWithCamera= False):
        super().__init__(game, name, gameObject)
        self.visible = visible
        self.moveWithCamera = moveWithCamera

class CircleCollider(Collider):
    
    def __init__(self, game, gameObject, name, radius, visible, moveWithCamera= False) :
        super().__init__(game,gameObject,"CircleCollider",visible,moveWithCamera)
        self.radius = radius
        


class RectangleCollider(Collider):
    
    def __init__(self, game, gameObject, name, width , height , color, visible, moveWithCamera = False):
        super().__init__(game,gameObject,"RectangleCollider",visible,moveWithCamera)
        
        self.width = width
        self.height = height
        self.color = color


class BoxCollider(Collider):

    def __init__(self, game, gameObject,visible, moveWithCamera= False):
        super().__init__(game, gameObject,"BoxCollider",visible,moveWithCamera)
        self.visible = visible

    def serialize (self):
        dict1 = {}
        dict1['name'] = "BoxCollider"
        dict1['visible'] = self.visible
        return dict1