import pygame as pg
import sys, os
from constants import SCREEN_SIZE

playerImage = os.path.join(sys.path[0], './assets/sun.png')
background = os.path.join(sys.path[0], './assets/background.png')

def main():
    pg.init()

    gameDisplay = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption('Test');
    player = pg.transform.rotozoom(pg.image.load(playerImage), 0, 0.5);
    backgroundImage = pg.transform.scale(pg.image.load(background), (800,600));

    running = True
    position = (50, 50)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    position = (position[0] - 1, position[1])

        # TODO: Enforce framerate
        gameDisplay.blit(backgroundImage, (0,0))
        gameDisplay.blit(player, position)
        pg.display.update()
                
main();