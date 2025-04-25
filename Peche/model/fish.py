from model.world import TILE_SIZE,WorldItem
from Peche.model.hamecon_souris import Hamecon

class Fish:
    IMG = 0
    U = 48
    V = 0
    WIDTH = 16
    HEIGHT = 8
    speed = 1
    profondeur = 60
    rotate=0

    def __init__(self, world):
        self.x = 30
        self.y = self.profondeur
        self.aller_retour =0
        self.world = world
        self.attrape = 0
        self.hamecon = Hamecon
    
    def update(self):
        if self.attrape == 0:
            if self.x == 20 :
                self.aller_retour =0
            if self.x == 100 :
                self.aller_retour =1
            if self.aller_retour ==0 :
                self.WIDTH = -16
                self.x += self.speed
            if self.aller_retour ==1:
                self.WIDTH = 16
                self.x -= self.speed
