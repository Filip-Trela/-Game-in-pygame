import pygame as pg

def clamp(value, min_value, max_value):
    return max(min_value,min(value,max_value))

def inputHandler(key):
    keys = pg.key.get_pressed()
    if keys[key]:
        return True
    else:
        return False

def move_towards(value, byHowMuch, theEnd):
    if value > theEnd:
        value -= byHowMuch
        if value < theEnd:
            value = theEnd
    elif value < theEnd:
        value += byHowMuch
        if value > theEnd:
            value = theEnd
    return value



#for spliting <Dice Sprite (in 1 group)> into Dice Sprite
def split_sprite_name(name):
    sprite = str(name)
    sprite = sprite.split('(')[0]
    sprite = sprite[1:]
    return sprite