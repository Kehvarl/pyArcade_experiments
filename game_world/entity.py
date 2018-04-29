class Entity:
    def __init__(self, x, y, sprite, name, blocks=False):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.name = name
        self.blocks = blocks
