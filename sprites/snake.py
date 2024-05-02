import pygame,sys,os,random,math
sys.path.append("..")
import common

class Square(pygame.sprite.Sprite):
    def __init__(self,x,y,di="up",head=False,nxt=None,prv=None):
        pygame.sprite.Sprite.__init__(self)
        self.x,self.y = x,y
        self.ishead = head
        self.next = nxt
        self.prev = prv
        self.rect = pygame.FRect(0,0,19*common.ratio,19*common.ratio)
        self.rect.center = (self.x,self.y)
        self.image = pygame.Surface((19*common.ratio,19*common.ratio))
        self.image.fill([random.randint(1,255) for i in range(3)])
        self.dir = di 
        if self.ishead:
            self.ison = [0,0]
            self.dmov = [0,0]
            self.dpos = [0,0]

    def closeto(self):
        v1 = pygame.math.Vector2(abs(self.prev.x - self.x), abs(self.prev.y - self.y))
        v2 = pygame.math.Vector2(abs(self.prev.x - common.valx), 0)
        v3 = pygame.math.Vector2(0, abs(self.prev.y - common.valy))

        # for some fucking reason this works :')
        if ((self.dir in ["up","left"] and self.prev.dir in ["up","left"]) or (self.dir in ["down","right"] and self.prev.dir in ["down","right"])) and v1.dot(v3)/v1.magnitude()/v3.magnitude() < 0.48:
            return True
        elif ((self.dir in ["up","right"] and self.prev.dir in ["up","right"]) or (self.dir in ["down","left"] and self.prev.dir in ["down","left"])) and v1.dot(v2)/v1.magnitude()/v2.magnitude() < 0.85:
            return True

        return False

    def update(self,hdx=0,hdy=0):

        dx,dy = 0,0

#        1.25,0.665

        if self.dir == "right":
            dx += 1.54 * common.ratio * common.dt
            dy += 0.872 * common.ratio * common.dt 
            if self.ishead: self.ison[1] += dy/common.valy
        elif self.dir == "up":
            dx += 1.54 * common.ratio * common.dt
            dy -= 0.872 * common.ratio * common.dt
            if self.ishead: self.ison[0] += dy/common.valy
        elif self.dir == "left":
            dx -= 1.54 * common.ratio * common.dt
            dy -= 0.872 * common.ratio * common.dt
            if self.ishead: self.ison[1] += dy/common.valy
        elif self.dir == "down":
            dx -= 1.54 * common.ratio * common.dt
            dy += 0.872 * common.ratio * common.dt
            if self.ishead: self.ison[0] += dy/common.valy

        if self.ishead:
            self.dpos[0] -= dx
            self.dpos[1] -= dy
            self.dmov = [dx,dy]
        elif self.prev.dir != self.dir and self.closeto():
            self.x = self.prev.x + common.valx if self.prev.dir in ["down","left"] else self.prev.x - common.valx
            self.y = self.prev.y + common.valy if self.prev.dir in ["up","left"] else self.prev.y - common.valy
            self.rect.centerx,self.rect.centery = self.x,self.y
            self.dir = self.prev.dir
        else:
            self.x += dx - hdx
            self.y += dy - hdy
            self.rect.centerx,self.rect.centery = self.x,self.y

class Snake():
    def __init__(self):
        self.leng = 2
        self.ismove = False
        self.mapchng = False
        self.head = Square(common.displaymid[0],common.displaymid[1],head=True)
        self.tail = Square(self.head.rect.centerx-common.valx,self.head.rect.centery+common.valy)
        self.head.update() # so that the distance is maintained
        self.tail.prev = self.head
        self.head.next = self.tail
        self.timer = pygame.time.get_ticks()

    def add(self):
        self.leng +=1
        if self.tail.prev.dir == "up":
            self.tail.prev.next = Square(self.tail.prev.x-common.valx,self.tail.prev.y+common.valy,di="up",nxt=self.tail,prv=self.tail.prev)
            self.tail.prev = self.tail.prev.next
            self.tail.x -= common.valx
            self.tail.y += common.valy
        elif self.tail.prev.dir == "down":
            self.tail.prev.next = Square(self.tail.prev.x+common.valx,self.tail.prev.y-common.valy-0.2,di="down",nxt=self.tail,prv=self.tail.prev)
            self.tail.prev = self.tail.prev.next
            self.tail.x += common.valx
            self.tail.y -= common.valy
        elif self.tail.prev.dir == "right":
            self.tail.prev.next = Square(self.tail.prev.x-common.valx,self.tail.prev.y-common.valy,di="right",nxt=self.tail,prv=self.tail.prev)
            self.tail.prev = self.tail.prev.next
            self.tail.x -= common.valx
            self.tail.y -= common.valy
        elif self.tail.prev.dir == "left":
            self.tail.prev.next =Square(self.tail.prev.x+common.valx,self.tail.prev.y+common.valy,di="left",nxt=self.tail,prv=self.tail.prev) 
            self.tail.prev = self.tail.prev.next
            self.tail.x += common.valx
            self.tail.y += common.valy
