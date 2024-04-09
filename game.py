import pygame,sys,time
import common
from mapc import Map
from sprites.snake import Snake,Square

world = Map()
snakebod = pygame.sprite.Group()
player = Snake()
snakebod.add(player.head)
snakebod.add(player.tail)

class Game():
    def __init__(self):
        self.state = "gmloop"
        world.con_alp()

    def gmloop(self):
        dx,dy = player.head.dpos
        world.mapblit(common.valx,common.valy,dx,dy)

        for event in pygame.event.get(): # for loop for events
            if event.type == pygame.QUIT: # quitting 
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player.add()
                    snakebod.add(player.bod[-1])
    
                if event.key == pygame.K_RIGHT and (player.head.dir=="up" or player.head.dir == "down") and common.time1 - player.timer > 0.5:
                    player.timer = common.time1
                    player.head.dir = "right"
                elif event.key == pygame.K_LEFT and (player.head.dir=="up" or player.head.dir == "down")and common.time1 - player.timer > 0.5:
                    player.timer = common.time1
                    player.head.dir = "left"
                elif event.key == pygame.K_UP and (player.head.dir=="left" or player.head.dir == "right")and common.time1 - player.timer > 0.5:
                    player.timer = common.time1
                    player.head.dir = "up"
                elif event.key == pygame.K_DOWN and (player.head.dir=="left" or player.head.dir == "right")and common.time1 - player.timer > 0.5:
                    player.timer = common.time1
                    player.head.dir = "down"

        player.changedir(player.newd)
        player.updaterel()
        snakebod.update()
        snakebod.draw(common.vwin)

    def menu(self):
        pass

    def selector(self): 
        if self.state == "gmloop":
            self.gmloop()
        elif self.state == "menu":
            self.menu()
