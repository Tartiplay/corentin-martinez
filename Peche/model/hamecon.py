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

    def __init__(self, world, bobberX, bobberY):
        self.x = bobberX
        self.base_player_y = world.player_grid_y * TILE_SIZE + TILE_SIZE*2
        self.y = bobberY
        self.world = world
        self.en_peche = 0
        self.range_canne = 60
        self.vitesse_hamecon = 2
        self.cible_x = 0
        self.cible_y = 0

    def update(self, bobberX, bobberY):
        self.x = bobberX
        self.dep_hamecon(bobberY)
    
    def move_left(self):
        self.x -= self.DX
    
    def move_right(self):
        self.x += self.DX

         

    def dep_hamecon(self, bobberY):
         #Déplacement du hamecon
         #Descente du hamecon
         if self.y >= bobberY :
            if pyxel.btn(pyxel.KEY_DOWN):
                self.y += self.vitesse_hamecon
         #Remontée du hamecon limité à la hauteur du bouchon       
         if self.y > bobberY :
             if pyxel.btn(pyxel.KEY_UP):
                 self.y -= self.vitesse_hamecon

