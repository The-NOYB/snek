import pygame,sys,time,csv
import common

class Map():
    def __init__(self):
        with open("data/map","r") as f:
            world = []
            rfile = csv.reader(f,delimiter="-")
            for i in rfile:
                world.append(i)
        self.world = world
        self.block = pygame.image.load("data/newcubes.png")
        self.blkls = [ pygame.transform.scale(self.block,(119/(60)*i*20,91/60*i*20)) for i in range(3,7)] # better cluster of blocks 120 x 90

    def con_alp(self):
        for i in range(len(self.blkls)):
            self.blkls[i] = self.blkls[i].convert_alpha()

    def mapblit(self,valx,valy,dx=0,dy=0):   # work on this and inf
        valx *= 2
        valy *= 2
    #    valy -= 1
        midx = common.displaymid[common.screen][0]
        midy = common.displaymid[common.screen][1]
        for y,row in enumerate(self.world):
            for x, col in enumerate(row):
                if col == "1":
                    common.vwin.blit(self.blkls[common.screen],(midx+valx*(x-1)-y*valx,midy-(len(self.world)-y)*valy+x*valy))
   
    def C(self):
        pass
