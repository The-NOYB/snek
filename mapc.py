import pygame,sys,time,json
import common

class Map():
    def __init__(self):
        with open("data/map.json","r") as file:
            data = json.load(file)
            world = data["theworld"]["world"]
            events = data["theworld"]["events"]
            leng = len(world)

        self.world = world
        self.leng = leng 
        self.block = pygame.image.load("data/dekhte hai.png")
        self.ice_block = pygame.image.load("data/cringe ice.png")
        self.rock_block = pygame.image.load("data/cringe rock.png")
        self.block = pygame.transform.scale(self.block,(74,86))     # [ pygame.transform.scale(self.block,(i*20,i*20)) for i in range(3,7)] # better cluster of blocks 120 x 90
        self.ice_block = pygame.transform.scale(self.ice_block,(74,86))
        self.rock_block = pygame.transform.scale(self.rock_block,(74,86))

    def con_alp(self):
#        for various blocks
#        for i in range(len(self.blkls)):
#            self.blkls[i] = self.blkls[i].convert_alpha()
        self.block = self.block.convert_alpha()
        self.ice_block = self.ice_block.convert_alpha()
        self.rock_block = self.rock_block.convert_alpha()
#        curworld = world[playerpos[0]:61]

    def nextwo(self):
        pass

    def mapblit(self,valx,valy,dx=0,dy=0,posx=0,posy=0):   # work on this and inf
#        valx *= 2
#        valy *= 2
#        valy -= 1

        midx = common.displaymid[0]
        midy = common.displaymid[1]

        for y,row in enumerate(self.world):
            for x, col in enumerate(row):

                if x==round(posx) and y==round(posy):
                    common.vwin.blit(pygame.transform.invert(self.block), (midx + (x-1)*valx - y*valx+ dx, midy - (self.leng - y)*valy + x*valy + dy))
                elif col == 1:
                    common.vwin.blit(self.block, (midx + (x-1)*valx - y*valx+ dx, midy - (self.leng - y)*valy + x*valy + dy))
                elif col == 2:
                    common.vwin.blit(self.ice_block, (midx + (x-1)*valx - y*valx+ dx, midy - (self.leng - y)*valy + x*valy + dy))
                elif col == 3:
                    common.vwin.blit(self.rock_block, (midx + (x-1)*valx - y*valx+ dx, midy - (self.leng - y)*valy + x*valy + dy))
