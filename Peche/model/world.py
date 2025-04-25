class WorldItem :
    WALL = (2, 0)
    CORRIDOR = (4, 0)
    PLAYER = (0, 0)

TILE_SIZE=8
SPRITE_BANK = 0

class World:
    HEIGHT = 16
    WIDTH = 16
    def __init__(self, tilemap):
        self.tilemap = tilemap
        self.world_map = []
        self.player_grid_x = 0
        self.player_grid_y = 0
        for y in range(self.HEIGHT):
            self.world_map.append([])
            for x in range(self.WIDTH):
                if self.tilemap.pget(x,y) == WorldItem.WALL:
                    self.world_map[y].append(WorldItem.WALL)
                elif self.tilemap.pget(x,y) == WorldItem.PLAYER:
                    self.world_map[y].append(WorldItem.CORRIDOR)
                    self.player_grid_x = x
                    self.player_grid_y = y
                else:
                    self.world_map[y].append(WorldItem.CORRIDOR)

def world_item_draw(pyxel, x, y, world_item):
    pyxel.blt(
        x * TILE_SIZE,
        y * TILE_SIZE,
        0,
        world_item[0] * TILE_SIZE,
        world_item[1] * TILE_SIZE,
        16,
        16
    )               