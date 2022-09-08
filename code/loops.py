import pygame as pg
from characters import *
from dev import dev_room
from world import *




class Loops:
    def __init__(self):
        self.screen = pg.display.get_surface()

        #sprites groups
        self.all_sprites = DrawOnScreen()
        self.coll_sprites = pg.sprite.Group()

        self.set_level()

    def set_level(self):

        for row_index, row in enumerate(dev_room):
            for coll_index, coll in enumerate(row):
                if coll == 'x':
                    x_pos = coll_index * BLOCK_SIZE
                    y_pos = row_index * BLOCK_SIZE
                    Block((x_pos,y_pos), [self.all_sprites, self.coll_sprites])

        self.player = Player((200, 450), self.all_sprites, self.coll_sprites)


    def run(self,dt):
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)




class DrawOnScreen(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.offset = pg.math.Vector2()

    def custom_draw(self, target):
        self.offset.x = target.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = target.rect.centery - WINDOW_HEIGHT / 2

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z_layers == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)












