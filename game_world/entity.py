class Entity:
    def __init__(self, x, y, sprite, name, blocks=False):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.sprite = sprite
        self.name = name
        self.blocks = blocks
