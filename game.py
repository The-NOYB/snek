import pygame,sys,time
import common
from sprites.snake import Snake,Square

class Game():
    def __init__(self,player,snb):
        self.state = "gmloop"
        self.player = player
        self.snb = snb

    def gmloop(self):

        for event in pygame.event.get(): # for loop for events
            if event.type == pygame.QUIT: # quitting 
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4: # for resizing window
                    common.punit = common.displayunit[common.screen] 
                    common.vwin,common.screen,common.ratio = common.changewin(window,common.vwin,common.screen,common.ratio)
                    common.valy = round(38/72*common.displayunit[common.screen]/2)
                    common.valx = common.displayunit[common.screen]//2
    
                if event.key == pygame.K_RETURN:
                    self.player.add()
                    self.snb.add(self.player.bod[-1])
    
                if event.key == pygame.K_RIGHT and (self.player.head.dir=="up" or self.player.head.dir == "down") and common.time1 - self.player.timer > 0.5:
                    self.player.timer = common.time1
                    self.player.head.pos = ([self.player.head.x,self.player.head.y,"right"])
                    self.player.head.dir = "right"
                elif event.key == pygame.K_LEFT and (self.player.head.dir=="up" or self.player.head.dir == "down")and common.time1 - self.player.timer > 0.5:
                    self.player.timer = common.time1
                    self.player.head.pos = ([self.player.head.x,self.player.head.y,"left"])
                    self.player.head.dir = "left"
                elif event.key == pygame.K_UP and (self.player.head.dir=="left" or self.player.head.dir == "right")and common.time1 - self.player.timer > 0.5:
                    self.player.timer = common.time1
                    self.player.head.pos = ([self.player.head.x,self.player.head.y,"up"])
                    self.player.head.dir = "up"
                elif event.key == pygame.K_DOWN and (self.player.head.dir=="left" or self.player.head.dir == "right")and common.time1 - self.player.timer > 0.5:
                    self.player.timer = common.time1
                    self.player.head.pos = ([self.player.head.x,self.player.head.y,"down"])
                    self.player.head.dir = "down"

        self.player.changedir(self.player.newd)
        self.snb.update()
        self.snb.draw(common.vwin)

    def menu(self):
        pass

    def selector(self): 
        if self.state == "gmloop":
            self.gmloop()
        elif self.state == "menu":
            self.menu()
