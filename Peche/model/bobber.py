import pyxel
from model.world import TILE_SIZE,WorldItem
from model.player import Player

class Bobber:
    IMG = 0
    U = 32
    V = 0
    WIDTH = 8
    HEIGHT = 8
    DX = 1
    lancer = 0

    def __init__(self, world):
        self.x = world.player_grid_x * TILE_SIZE
        self.base_player_y = world.player_grid_y * TILE_SIZE + TILE_SIZE*2
        self.y = world.player_grid_y * TILE_SIZE + Player.HEIGHT
        self.world = world
        self.active = 0



    def update(self,hameconY):
        if hameconY==self.y :             
            if pyxel.btn(pyxel.KEY_LEFT):
                self.move_left()
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.move_right()


    
    def move_left(self):
        if self.active == 0 :
            self.x -= self.DX
    
    def move_right(self):
        if self.active == 0 :
            self.x += self.DX

