import pygame as pg

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FLAGS = pg.SCALED | pg.FULLSCREEN


#z layers
LAYERS = {
    'background' : 0,
    'player' : 1,
    'weapons' : 2,
    'bullet' : 3
}

PLAYER_SIZE = (64,128)
PLAYER_MAX_SPEED = 600
PLAYER_ACCELERATION = 30
PLAYER_JUMP = 20000
PLAYER_FALL_MAX = 800
PLAYER_FALL_ACC = 70


BLOCK_SIZE = 64

DICE_SIZE = 16
DICE_SPEED = 800
DICE_DESTROY = 120


BULLET_SPEED = 1700