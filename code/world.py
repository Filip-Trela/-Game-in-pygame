import pygame as pg
from settings import *


class Block(pg.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pg.Surface((BLOCK_SIZE,BLOCK_SIZE))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect(topleft = pos)
        self.z_layers = LAYERS["background"]
        self.hitbox = self.rect.copy()
