import math

import pygame as pg
from settings import *
from helpers import *



class Dice(pg.sprite.Sprite):
    def __init__(self, pos,  group,collideSprites, playerSprite):
        super().__init__(group)
        self.image = pg.Surface((DICE_SIZE,DICE_SIZE))
        self.image.fill((150,100,0))
        self.rect = self.image.get_rect(center = pos)
        self.z_layers = LAYERS['weapons'] #kurwa pacz na to cymbale
        self.direction = pg.math.Vector2(pg.mouse.get_pos()[0] - WINDOW_WIDTH/2, \
                                         pg.mouse.get_pos()[1] - WINDOW_HEIGHT/2)

        self.collide_sprites = collideSprites
        self.player_sprite = playerSprite


        self.mov_vec = self.direction.normalize()
        self.mov_vec.x = self.mov_vec.x * DICE_SPEED
        self.mov_vec.y = self.mov_vec.y * DICE_SPEED

    def movement(self,dt):
        # x axis
        self.rect.x += self.mov_vec.x * dt
        self.collision("horizontal")

        # y axis
        self.mov_vec.y += 15
        self.rect.y += self.mov_vec.y * dt
        self.collision("vertical")

    def knockback(self,direction,dt):
        self.mov_vec += direction * 200 * dt

    def destroy(self):
        #calkowicie inaczej
        if self.mov_vec.length() <= DICE_DESTROY:
            if self.rect.colliderect(self.player_sprite.rect):
                self.kill()

    def collision(self,direction):
        for sprite in self.collide_sprites.sprites():
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.rect):
                    if direction == "horizontal":
                        if self.mov_vec.x > 0: #prawa
                            self.rect.right = sprite.hitbox.left
                            self.mov_vec.x = -self.mov_vec.x / 2
                        elif self.mov_vec.x <0: #lewa
                            self.rect.left = sprite.hitbox.right
                            self.mov_vec.x = -self.mov_vec.x / 2

                    if direction == "vertical":
                        if self.mov_vec.y > 0: #dol
                            self.rect.bottom = sprite.hitbox.top
                            self.mov_vec.y = -self.mov_vec.y / 3
                            self.mov_vec.x = self.mov_vec.x / 3 * 2 #fraction with floor
                            if self.mov_vec.y < DICE_SPEED/10 and self.mov_vec.y > -DICE_SPEED/10:
                                self.mov_vec.y = 0 #not jumping constantly
                        elif self.mov_vec.y <0: #gora
                            self.rect.top = sprite.hitbox.bottom
                            self.mov_vec.y = -self.mov_vec.y

    def update(self,dt):
        self.movement(dt)
        self.destroy()


#wyjebuje duzo grup, juz nie lol
class Bullet(pg.sprite.Sprite):
    def __init__(self,start_pos,groups):
        super().__init__(groups)
        self.image = pg.Surface((10,10))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect(center = start_pos)
        self.z_layers = LAYERS['bullet']
        self.group = groups

        self.direction = pg.math.Vector2()
        self.mov_vec = pg.math.Vector2()


        self.dice_sprite = []
        self.block_sprites = []
        self.all_sprites = []

        self.setup()


    def setup(self):
        self.direction = pg.math.Vector2(pg.mouse.get_pos()[0] - WINDOW_WIDTH / 2, \
                                         pg.mouse.get_pos()[1] - WINDOW_HEIGHT / 2)
        self.mov_vec = self.direction.normalize()
        self.mov_vec.x = self.mov_vec.x * BULLET_SPEED
        self.mov_vec.y = self.mov_vec.y * BULLET_SPEED

        for sprite in self.group:
            if split_sprite_name(sprite) == "Block Sprite":
                self.block_sprites.append(sprite)
                self.all_sprites.append(sprite)
            elif split_sprite_name(sprite) == "Dice Sprite":
                self.dice_sprite.append(sprite)
                self.all_sprites.append(sprite)
        #print(self.all_sprites)

    def movement(self,dt):
        self.rect.x += self.mov_vec.x * dt
        self.rect.y += self.mov_vec.y * dt
        self.collide(dt)

    def collide(self,dt):
        for sprites in self.all_sprites:
            if self.rect.colliderect(sprites):
                if sprites in self.block_sprites: #kolizja z blokami
                    self.kill()
                elif sprites in self.dice_sprite: #kolizja z kostka kurwa dziala
                    sprites.knockback(self.direction,dt)
                    self.kill()

    def update(self,dt):
        self.movement(dt)