import pyxel
from model.world import TILE_SIZE,WorldItem
from model.player import Player

class Hamecon:
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
        self.y = world.player_grid_y * TILE_SIZE + TILE_SIZE*2
        self.world = world
        self.en_peche = 0
        self.range_canne = 60
        self.vitesse_hamecon = 2
        self.cible_x = 0
        self.cible_y = 0

    def update(self):
        self.lancer()
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            if self.en_peche == 0 and (pyxel.mouse_y-self.y) > 0:
                self.cible_x = pyxel.mouse_x
                self.cible_y = pyxel.mouse_y
                self.ratio_cible = (self.cible_x-self.x)/(self.cible_y-self.y)
                self.depart_x = self.x
                self.depart_y = self.y
                self.en_peche = 1
    
    def move_left(self):
        self.x -= self.DX
    
    def move_right(self):
        self.x += self.DX


    def lancer(self):
            if self.en_peche == 1:
                if (self.depart_y-self.y)**2 + (self.depart_x-self.x)**2 < self.range_canne**2 :
                    self.y += self.vitesse_hamecon 
                    self.x += self.vitesse_hamecon * (self.cible_x-self.depart_x)/(self.cible_y-self.depart_y)
                else :
                    self.en_peche = 2
            if self.en_peche == 2:
                if self.y > self.base_player_y:
                      self.y -= self.vitesse_hamecon 
                      self.x -= self.vitesse_hamecon * (self.cible_x-self.depart_x)/(self.cible_y-self.depart_y)
                else :
                     self.en_peche = 0
