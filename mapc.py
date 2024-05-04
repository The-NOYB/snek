import pygame,sys,time,json
import common

class Map():
    def __init__(self):
        with open("data/map.json","r") as file:
            data = json.load(file)
            world = data["theworld"]["world"]
            events = data["theworld"]["events"]
            spawn = data["theworld"]["spawn"]

        self.wholeworld = world
        self.spawn = spawn
        self.shift = [0,0]
        self.timer = common.time1
        self.world = self.getworld(self.spawn)
        self.leng = 59 
        self.block = pygame.image.load("data/dekhte hai2.png")
        self.ice_block = pygame.image.load("data/cringe ice.png")
        self.rock_block = pygame.image.load("data/cringe rock.png")

        self.block = pygame.transform.scale(self.block,(74,86))     # [ pygame.transform.scale(self.block,(i*20,i*20)) for i in range(3,7)] # better cluster of blocks 120 x 90
        self.ice_block = pygame.transform.scale(self.ice_block,(74,86))
        self.rock_block = pygame.transform.scale(self.rock_block,(74,86))

    def con_alp(self):
        self.block = self.block.convert_alpha()
        self.ice_block = self.ice_block.convert_alpha()
        self.rock_block = self.rock_block.convert_alpha()

    def getworld(self,spawn):
        warr = []
        for i in range(spawn[0]-29,spawn[0]+30):
            arr = []
            for j in range(spawn[1]-29,spawn[1]+30):
                arr.append(self.wholeworld[i][j])
            warr.append(arr)
            arr = []

        return warr

    def updworld(self,ison):
        warr= self.getworld(ison)
        self.world = warr
                    
    def mapblit(self,valx,valy,dx=0,dy=0):   # work on this and inf
#        valx *= 2
#        valy *= 2
#        valy -= 1

        dx += self.shift[0]*common.valx
        dy += self.shift[1]*common.valy
        midx = common.displaymid[0]
        midy = common.displaymid[1]

        for y,row in enumerate(self.world):
            for x, col in enumerate(row):
                if col == 1:
                    common.vwin.blit(self.block, (midx + (x-1)*valx - y*valx+ dx, midy - (self.leng - y)*valy + x * valy + dy))
                elif col == 2:
                    common.vwin.blit(self.ice_block, (midx + (x-1)*valx - y*valx+ dx, midy - (self.leng - y)*valy + x*valy + dy))
                elif col == 3:
                    common.vwin.blit(self.rock_block, (midx + (x-1)*valx - y*valx+ dx, midy - (self.leng - y)*valy + x*valy + dy))

