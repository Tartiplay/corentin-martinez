import pyxel
from model.player import Player
from model.hamecon import Hamecon
from model.bobber import Bobber
from model.world import World ,world_item_draw, TILE_SIZE
from model.fish import Fish
speed = 0.5
en_peche = 0
class App:
    def __init__(self):
        pyxel.init(160, 120, title="Hello world")
        pyxel.load("ressources.pyxres")
        pyxel.mouse(True) 

        self.world = World(pyxel.tilemap(0))
        
        self.player = Player(self.world)
        self.bobber = Bobber(self.world)
        self.hamecon = Hamecon(self.world,self.bobber.x,self.bobber.y)
        self.fish = Fish(self.world)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            self.player.move_left()
            self.hamecon.move_left()
        if pyxel.btn(pyxel.KEY_D):
            self.player.move_right()
            self.hamecon.move_right()

        self.bobber.update(self.hamecon.y)
        self.hamecon.update(self.bobber.x,self.bobber.y)
        self.fish.update()
        ## capture et Remontee du poisson
        if (self.fish.x <=(self.hamecon.x + self.hamecon.WIDTH/2) <= self.fish.x + abs(self.fish.WIDTH)) and (self.fish.y <=(self.hamecon.y + self.hamecon.HEIGHT) <= self.fish.y + self.fish.HEIGHT):
            self.fish.attrape = 1
        if self.fish.attrape == 1:
            self.fish.rotate = 90
            self.fish.x = self.hamecon.x
            self.fish.y = self.hamecon.y


        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0,0, 0, 0, 0, 8, 8)

        pyxel.blt(self.player.x,
                  self.player.y,
                  self.player.IMG,
                  self.player.U,
                  self.player.V,
                  self.player.WIDTH,
                  self.player.HEIGHT)
        pyxel.circ(self.bobber.x,
                   self.bobber.y,
                    3,
                    7)
        pyxel.blt(self.hamecon.x,
                  self.hamecon.y,
                  self.hamecon.IMG,
                  self.hamecon.U,
                  self.hamecon.V,
                  self.hamecon.WIDTH,
                  self.hamecon.HEIGHT)
        pyxel.blt(self.fish.x,
                  self.fish.y,
                  self.fish.IMG,
                  self.fish.U,
                  self.fish.V,
                  self.fish.WIDTH,
                  self.fish.HEIGHT,
                  rotate=self.fish.rotate,
                  colkey=0)
        pyxel.line(self.player.x,
                   self.player.y+5,
                   self.bobber.x,
                   self.bobber.y,
                   7)
        pyxel.line(self.bobber.x,
                   self.bobber.y+5,
                   self.hamecon.x,
                   self.hamecon.y,
                   7
                   )
App()
