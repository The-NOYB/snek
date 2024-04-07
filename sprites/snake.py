import pygame,sys,os,random
sys.path.append("..")
import common

class Square(pygame.sprite.Sprite):
    def __init__(self,x,y,di="up"):
        pygame.sprite.Sprite.__init__(self)
        self.x,self.y = x,y
        self.rect = pygame.Rect(0,0,19*common.ratio,19*common.ratio)
        self.rect.center = (self.x,self.y)
        self.image = pygame.Surface((19*common.ratio,19*common.ratio))
        self.image.fill([random.randint(1,255) for i in range(3)])
        self.dir = di 
        self.ndir = []
        self.pos = []

    def update(self):
        dx,dy = 0,0
        if self.dir == "right":
            dx += 1.25 * common.ratio * common.dt
            dy += 0.665 * common.ratio * common.dt 
        elif self.dir == "up":
            dx += 1.25 * common.ratio * common.dt
            dy -= 0.665 * common.ratio * common.dt
        elif self.dir == "left":
            dx -= 1.25 * common.ratio * common.dt
            dy -= 0.665 * common.ratio * common.dt
        elif self.dir == "down":
            dx -= 1.25 * common.ratio * common.dt
            dy += 0.665 * common.ratio * common.dt

        self.x += dx
        self.y += dy
        self.rect.centerx,self.rect.centery = self.x,self.y
        return dx,dy

class Snake():
    def __init__(self):
        self.leng = 2
        self.newd = None
        self.head = Square(common.displaymid[common.screen][0]+1,common.displaymid[common.screen][1]-common.valy+1)
        self.tail = Square(self.head.rect.centerx-common.valx,self.head.rect.centery+common.valy)
        self.bod = [self.head]
        self.timer = pygame.time.get_ticks()

    def add(self):
        self.leng +=1
        if self.bod[-1].dir == "up":
            self.bod.append(Square(self.bod[-1].x-common.valx,self.bod[-1].y+common.valy,di="up"))
            self.tail.x -= common.valx
            self.tail.y += common.valy
        elif self.bod[-1].dir == "down":
            self.bod.append(Square(self.bod[-1].x+common.valx,self.bod[-1].y-common.valy,di="down"))
            self.tail.x += common.valx
            self.tail.y -= common.valy
        elif self.bod[-1].dir == "right":
            self.bod.append(Square(self.bod[-1].x-common.valx,self.bod[-1].y-common.valy,di="right"))
            self.tail.x -= common.valx
            self.tail.y -= common.valy
        elif self.bod[-1].dir == "left":
            self.bod.append(Square(self.bod[-1].x+common.valx,self.bod[-1].y+common.valy,di="left"))
            self.tail.x += common.valx
            self.tail.y += common.valy

    def changedir(self,di):
        li = self.bod + [self.tail]

        for i in range(1,self.leng):
            if ((li[i-1].x - li[i].x)**2 + (li[i-1].y - li[i].y)**2)//1 > 1200:
                    li[i].x = self.bod[i-1].x + common.valx if li[i-1].dir in ["down","left"] else self.bod[i-1].x - common.valx
                    li[i].y = self.bod[i-1].y + common.valy if li[i-1].dir in ["up","left"] else self.bod[i-1].y - common.valy
                    li[i].dir = li[i-1].dir
