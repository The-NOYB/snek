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
        self.state = "menu"
        world.con_alp()

    def gmloop(self):
        dx,dy = player.head.dpos
        world.mapblit(common.valx,common.valy,dx,dy,player.head.ison[0],player.head.ison[1])

        for event in pygame.event.get(): # for loop for events
            if event.type == pygame.QUIT: # quitting 
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player.add()
                    snakebod.add(player.tail.prev)

                if event.key == pygame.K_SPACE and not player.ismove:
                    player.ismove = True
                elif event.key == pygame.K_SPACE and player.ismove:
                    player.ismove = False

                if player.ismove and event.key == pygame.K_d and (player.head.dir=="up" or player.head.dir == "down") and common.time1 - player.timer > 0.5:
                    player.timer = common.time1
                    player.head.dir = "right"
                elif player.ismove and event.key == pygame.K_a and (player.head.dir=="up" or player.head.dir == "down")and common.time1 - player.timer > 0.5:
                    player.timer = common.time1
                    player.head.dir = "left"
                elif player.ismove and event.key == pygame.K_w and (player.head.dir=="left" or player.head.dir == "right")and common.time1 - player.timer > 0.5:
                    player.timer = common.time1
                    player.head.dir = "up"
                elif player.ismove and event.key == pygame.K_s and (player.head.dir=="left" or player.head.dir == "right")and common.time1 - player.timer > 0.5:
                    player.timer = common.time1
                    player.head.dir = "down"

        if player.ismove:
            snakebod.update(player.head.dmov[0],player.head.dmov[1])
        snakebod.draw(common.vwin)

    def menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quitting
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.state = "gmloop"
                    
    def selector(self): 
        if self.state == "gmloop":
            self.gmloop()
        elif self.state == "menu":
            self.menu()

