import pygame as pg
from settings import *
from helpers import *
from weapons import *



class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, collideSprites):
        super().__init__(groups)
        self.groups = groups

        self.image = pg.Surface(PLAYER_SIZE)
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(topleft = pos)
        self.z_layers = LAYERS['player']

        #states
        self.ammo = 0

        #collision variables
        self.collide_sprites = collideSprites

        #movement variables
        self.input_vec = pg.math.Vector2()
        self.mov_vec = pg.math.Vector2()

    def input(self):
        self.input_vec.x = inputHandler(pg.K_d) - inputHandler(pg.K_a)

        i = 0 #o kurwa to dziala
        for sprite in self.groups.sprites():
            sprite = split_sprite_name(sprite)
            if sprite == 'Dice Sprite':
                i = 1
        if inputHandler(pg.K_SPACE) and i ==0:
            Dice(self.rect.center, self.groups,self.collide_sprites,self)


        if pg.mouse.get_pressed()[0] and self.ammo:
            Bullet(self.rect.center, self.groups)
            self.ammo = 0

        if inputHandler(pg.K_r):
            self.ammo = 1

    def collision(self, direction,dt):
        for sprite in self.collide_sprites.sprites():
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.rect):
                    if direction == "horizontal":
                        if self.mov_vec.x > 0: #prawa
                            self.rect.right = sprite.hitbox.left
                        elif self.mov_vec.x <0: #lewa
                            self.rect.left = sprite.hitbox.right

                        self.mov_vec.x = 0

                    if direction == "vertical":
                        if self.mov_vec.y > 0: #dol
                            self.rect.bottom = sprite.hitbox.top
                            self.mov_vec.y = 0
                            self.jump_handler(dt)
                        elif self.mov_vec.y <0: #gora
                            self.rect.top = sprite.hitbox.bottom
                            self.mov_vec.y = 0

    def movement_x(self,dt):
        self.mov_vec.x = move_towards(self.mov_vec.x,PLAYER_ACCELERATION,PLAYER_MAX_SPEED * self.input_vec.x)
        self.rect.x += self.mov_vec.x * dt
        self.collision('horizontal',dt)

    def jump_handler(self,dt):
        if inputHandler(pg.K_w):
            self.mov_vec.y = -PLAYER_JUMP * dt

    def movement_y(self,dt):
        #falling
        self.mov_vec.y = move_towards(self.mov_vec.y, PLAYER_FALL_ACC,PLAYER_FALL_MAX)
        self.rect.y += self.mov_vec.y * dt
        self.collision('vertical',dt)

    def update(self, dt):
        self.input()
        self.movement_x(dt)
        self.movement_y(dt)

















