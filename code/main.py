import pygame as pg
import sys
from settings import *
from loops import Loops
import time



class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), FLAGS)
        pg.display.set_caption("nazwa robocza")
        self.clock = pg.time.Clock()
        self.loops = Loops()

    def run(self):
        last_time = time.time()
        while True:
            self.screen.fill((255,255,255))

            dt = time.time() - last_time
            last_time = time.time()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()

            self.clock.tick(60)
            self.loops.run(dt)
            pg.display.update()




if __name__ == "__main__":
    Game().run()
