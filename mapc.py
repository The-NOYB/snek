import pygame,sys,time,json
import common

class Map():
    def __init__(self):
        with open("data/map.json","r") as file:
            data = json.load(file)
            world = data["theworld"]["world"]
            events = data["theworld"]["events"]
            start = data["theworld"]["spawn"]

        self.wholeworld = world
        self.start = start
        self.middle = [ x + 29 for x in start]
        print(self.start,self.middle)
        self.timer = common.time1
        self.world = self.getworld(self.start)
        self.leng = 59 
        self.block = pygame.image.load("data/newcube.png")
        self.ice_block = pygame.image.load("data/cringe ice.png")
        self.rock_block = pygame.image.load("data/cringe rock.png")

        self.block = pygame.transform.scale(self.block,(74,86))     # [ pygame.transform.scale(self.block,(i*20,i*20)) for i in range(3,7)] # better cluster of blocks 120 x 90
        self.ice_block = pygame.transform.scale(self.ice_block,(74,86))
        self.rock_block = pygame.transform.scale(self.rock_block,(74,86))
        pygame.draw.rect(self.block,(255,255,255),pygame.Rect(35,19,4,4))
        pygame.draw.rect(self.ice_block,(255,255,255),pygame.Rect(35,19,4,4))
        pygame.draw.rect(self.rock_block,(255,255,255),pygame.Rect(35,19,4,4))

    def con_alp(self):
        self.block = self.block.convert_alpha()
        self.ice_block = self.ice_block.convert_alpha()
        self.rock_block = self.rock_block.convert_alpha()

    def getworld(self,start):
        warr = []
        for i in range(start[0],start[0]+59):
            arr = self.wholeworld[i][start[1] : start[1]+59]
            warr.append(arr)

        return warr

    def updworld(self,ison):
        newstart = [ ison[x] + self.start[x] for x in range(2)]
        newison = [ ison[x] + self.middle[x] for x in range(2)]
        print(newstart,newison)
        warr = self.getworld(newstart)
        self.world = warr
                    
    def mapblit(self,valx,valy,dx=0,dy=0):   # work on this and inf
#        valx *= 2
#        valy *= 2
#        valy -= 1

        midx = common.displaymid[0]
        midy = common.displaymid[1]

        for y,row in enumerate(self.world):
            for x, col in enumerate(row):
                if x==y and x==29:
                    common.vwin.blit(pygame.transform.invert(self.block), (midx + (x-1)*valx - y*valx+ dx, midy - (self.leng - y)*valy + x * valy + dy))
                elif col == 1:
                    common.vwin.blit(self.block, (midx + (x-1)*valx - y*valx+ dx, midy - (self.leng - y)*valy + x * valy + dy))
                elif col == 2:
                    common.vwin.blit(self.ice_block, (midx + (x-1)*valx - y*valx+ dx, midy - (self.leng - y)*valy + x*valy + dy))
                elif col == 3:
                    common.vwin.blit(self.rock_block, (midx + (x-1)*valx - y*valx+ dx, midy - (self.leng - y)*valy + x*valy + dy))

