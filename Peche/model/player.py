from model.world import TILE_SIZE,WorldItem

class Player:
    IMG = 0
    U = 0
    V = 0
    WIDTH = 16
    HEIGHT = 16
    DX = 1

    def __init__(self, world):
        self.x = world.player_grid_x * TILE_SIZE
        self.y = world.player_grid_y * TILE_SIZE
        self.world = world

    def move_left(self):
        self.x -= self.DX
    
    def move_right(self):
        self.x += self.DX